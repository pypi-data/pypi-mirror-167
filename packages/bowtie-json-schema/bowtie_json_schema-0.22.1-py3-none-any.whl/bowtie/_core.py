from __future__ import annotations

from contextlib import asynccontextmanager
import asyncio
import json
import sys

from attrs import define, field
import aiodocker
import structlog

from bowtie import exceptions


@define
class InvalidResponse:
    """
    An implementation sent an invalid response to a command.
    """

    succeeded = False

    exc_info: Exception
    response: dict


@define
class Result:
    """
    The result of running a test case.
    """

    succeeded = True

    implementation: str
    contents: dict
    expected: bool | None

    def report(self, reporter):
        errored = self.contents.pop("errored", None)
        if errored:
            return reporter.errored(self.implementation, self.contents)

        reporter.got_results(
            implementation=self.implementation,
            results=self.contents,
            expected=self.expected,
        )


@define
class Started:

    succeeded = True

    implementation: dict
    ready: bool = False
    version: int = None


@define
class StartedDialect:

    succeeded = True

    ok: bool


StartedDialect.OK = StartedDialect(ok=True)


@define
class BackingOff:
    """
    An implementation has failed too many times.
    """

    succeeded = False

    implementation: str

    def report(self, reporter):
        reporter.backoff(implementation=self.implementation)


@define
class UncaughtError:
    """
    An implementation spewed to its stderr.
    """

    implementation: str
    stderr: bytes

    succeeded = False

    def report(self, reporter):
        reporter.errored_uncaught(
            implementation=self.implementation,
            stderr=self.stderr,
        )


@define
class BadFraming:
    """
    We're confused about line endings.
    """

    data: bytes

    succeeded = False

    def report(self, reporter):
        reporter.errored_uncaught(
            implementation=self.implementation,
            data=self.data,
        )


@define
class Empty:
    """
    We didn't get a response.
    """

    implementation: str

    succeeded = False

    def report(self, reporter):
        reporter.errored_uncaught(
            implementation=self.implementation,
            reason="Empty response.",
        )


@define(hash=True)
class Implementation:
    """
    A running implementation under test.
    """

    name: str

    _docker: aiodocker.Docker = field(repr=False)
    _restarts: int = field(default=20 + 1, repr=False)
    _read_timeout_sec: float = field(default=2.0, repr=False)

    _container: aiodocker.containers.DockerContainer = field(
        default=None, repr=False,
    )
    _stream: aiodocker.stream.Stream = field(default=None, repr=False)

    metadata: dict = {}

    @classmethod
    @asynccontextmanager
    async def start(cls, docker, image_name):
        try:
            self = cls(name=image_name, docker=docker)
            await self._restart_container()
            yield self
            await self._stop()
        finally:
            try:
                await self._container.delete(force=True)
            except aiodocker.exceptions.DockerError:
                pass

    async def _restart_container(self):
        self._restarts -= 1

        if self._container is not None:
            await self._container.delete(force=True)
        self._container = await self._docker.containers.create(
            config=dict(Image=self.name, OpenStdin=True),
        )
        await self._container.start()
        self._stream = self._container.attach(
            stdin=True,
            stdout=True,
            stderr=True,
        )
        self.metadata = await self._start()

    def supports_dialect(self, dialect):
        return dialect in self.metadata.get("dialects", [])

    async def start_speaking(self, dialect):
        return await self._send(
            cmd="dialect",
            dialect=dialect,
            succeed=StartedDialect,
        )

    async def _start(self):
        response = await self._send(cmd="start", version=1, succeed=Started)

        if not response.succeeded:
            raise exceptions.StartupFailure(self, response.stderr)
        elif not response.ready:
            raise exceptions.ImplementationNotReady(self)
        else:
            version = response.version
            if version != 1:
                raise exceptions.VersionMismatch(self, expected=1, got=version)

        return response.implementation

    async def run_case(self, seq, case, expected):
        if self._restarts <= 0:
            return BackingOff(implementation=self.name)
        return await self._send(
            cmd="run",
            seq=seq,
            case=case,
            succeed=lambda **contents: Result(
                implementation=self.name,
                contents=contents,
                expected=expected,
            ),
        )

    async def _stop(self):
        if self._restarts > 0:
            await self._send(cmd="stop", succeed=lambda **data: None)

    async def _send(self, succeed, retry=3, **kwargs):
        cmd = f"{json.dumps(kwargs)}\n"
        try:
            await self._stream.write_in(cmd.encode("utf-8"))
        except AttributeError:
            # FIXME: aiodocker doesn't appear to properly report when its
            # stream is closed
            await self._restart_container()
            await self._stream.write_in(cmd.encode("utf-8"))

        for _ in range(retry):
            try:
                message = await self._read_with_timeout()
                if message is None:
                    continue
            except asyncio.exceptions.TimeoutError:
                continue

            if message.stream == 2:
                data = []
                while message is not None and message.stream == 2:
                    data.append(message.data)
                    try:
                        message = await self._read_with_timeout()
                    except asyncio.exceptions.TimeoutError:
                        break
                return UncaughtError(
                    implementation=self.name,
                    stderr=b"".join(data),
                )

            data = message.data
            assert b"\n" not in message[:-1]
            while not data.endswith(b"\n"):
                try:
                    message = await self._read_with_timeout()
                except asyncio.exceptions.TimeoutError:
                    return BadFraming(
                        implementation=self.name,
                        data=b"".join(data),
                    )
                data += message.data
            try:
                data = json.loads(data)
            except json.JSONDecodeError:
                return BadFraming(
                    implementation=self.name,
                    data=b"".join(data),
                )
            else:
                try:
                    return succeed(**data)
                except Exception as error:
                    return InvalidResponse(exc_info=error, response=data)
        return Empty(implementation=self.name)

    def _read_with_timeout(self):
        return asyncio.wait_for(
            self._stream.read_out(),
            timeout=self._read_timeout_sec,
        )


def writer(file=sys.stdout):
    return lambda **result: file.write(f"{json.dumps(result)}\n")


@define
class Reporter:

    _write = field(default=writer())
    _log: structlog.BoundLogger = field(factory=structlog.get_logger)

    def unsupported_dialect(self, implementation, dialect):
        self._log.warn(
            "Unsupported dialect, skipping implementation.",
            logger_name=implementation.name,
            dialect=dialect,
        )

    def unacknowledged_dialect(self, implementation, dialect, response):
        self._log.warn(
            (
                "Implicit dialect not acknowledged. "
                "Proceeding, but implementation may not have configured "
                "itself to handle schemas without $schema."
            ),
            logger_name=implementation.name,
            dialect=dialect,
            response=response,
        )

    def ready(self, implementations, dialect):
        metadata = {
            implementation.name: dict(
                implementation.metadata, image=implementation.name,
            ) for implementation in implementations
        }
        self._write(implementations=metadata)

    def will_speak(self, dialect):
        self._log.info("Will speak dialect", dialect=dialect)

    def finished(self, count):
        if not count:
            self._log.error("No test cases ran.")
        else:
            self._log.msg("Finished", count=count)

    def case_started(self, seq, case):
        return _CaseReporter.case_started(
            case=case,
            seq=seq,
            write=self._write,
            log=self._log.bind(seq=seq, case=case),
        )


@define
class _CaseReporter:

    _write: callable
    _log: structlog.BoundLogger

    @classmethod
    def case_started(cls, log, write, case, seq):
        self = cls(log=log, write=write)
        self._write(case=case, seq=seq)
        return self

    def got_results(self, implementation, expected, results):
        self._write(
            implementation=implementation,
            expected=expected,
            **results,
        )

    def backoff(self, implementation):
        self._log.warn("backing off", logger_name=implementation)

    def errored(self, implementation, response):
        self._log.error("", logger_name=implementation, **response)

    def errored_uncaught(self, implementation, **response):
        self._log.error("uncaught", logger_name=implementation, **response)


def report_on(input):
    """
    Create a structure suitable for the report template from an input file.
    """

    lines = (json.loads(line) for line in input)
    header = next(lines)
    implementations = header["implementations"]

    combined = {}

    for each in lines:
        if "case" in each:
            combined[each["seq"]] = {
                "case": each["case"],
                "results": [(test, {}) for test in each["case"]["tests"]],
            }
            continue

        implementation = each.pop("implementation")
        case = combined[each["seq"]]

        for result, expected, (_, seen) in zip(
            each["results"],
            each["expected"],
            case["results"],
        ):
            incorrect = expected is not None and result["valid"] != expected
            seen[implementation] = result, incorrect

    return dict(
        implementations=implementations.values(),
        results=[(v, k) for k, v in sorted(combined.items())],
    )
