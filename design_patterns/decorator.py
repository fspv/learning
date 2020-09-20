from __future__ import annotations
from typing import Callable
from functools import wraps


# Java way


class File:
    def __init__(self, filename: str) -> None:
        self._filename = filename

    def read(self) -> str:
        with open(self._filename) as descriptor:
            return "".join(descriptor.readlines())


class FileDecorator(File):
    def __init__(self, decorated_obj: File) -> None:
        self._decorated_obj = decorated_obj


class LowercaseFile(FileDecorator):
    def read(self) -> str:
        return self._decorated_obj.read().lower()


class UppercaseFile(FileDecorator):
    def read(self) -> str:
        return self._decorated_obj.read().upper()


lowercase_file = LowercaseFile(File("/etc/passwd"))

print(lowercase_file.read())

uppercase_file = UppercaseFile(File("/etc/passwd"))

print(uppercase_file.read())


# Python way


def upper(func: Callable) -> Callable:
    @wraps(func)
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs).upper()

    return wrapper


class Repeat:
    def __init__(self, repeat: int) -> None:
        self._repeat = repeat

    def __call__(self, func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args, **kwargs) -> str:
            return "".join([func(*args, **kwargs) for _ in range(self._repeat)])

        return wrapper


@Repeat(10)
@upper
def read(filename: str) -> str:
    with open(filename) as descriptor:
        return "".join(descriptor.readlines())


print("Python")
print(read("/etc/passwd"))
print(read)
