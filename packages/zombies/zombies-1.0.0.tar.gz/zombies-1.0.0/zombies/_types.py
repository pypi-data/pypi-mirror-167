from typing import AnyStr, Protocol


class Readable(Protocol):
    def read(self, size: int) -> AnyStr:
        ...


class Writable(Protocol):
    def write(self, s: AnyStr) -> None:
        ...
