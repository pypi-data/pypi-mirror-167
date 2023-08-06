import re
import os

from enum import Enum
from pathlib import Path

from typer import Argument, Option
from .app import app


__all__ = ["fpath"]


class PathNotFoundException(Exception):
    def __init__(self, path: Path) -> None:
        super().__init__(f"{path.as_posix()} not found")


class OptionNotImplementedException(Exception):
    def __init__(self, option: "POption") -> None:
        super().__init__(f"`{option.value}` not implemented")


class POption(str, Enum):
    raw: str = "raw"
    dir: str = "dir"
    ext: str = "ext"
    name: str = "name"
    stem: str = "stem"

    def read(
        self, path: Path, relative: bool = True, strict: bool = True, level: int = 1
    ) -> str:
        if strict and not path.exists():
            raise PathNotFoundException(path)

        path = path.resolve()
        if relative:
            call_dir = os.getcwd()
            path = path.relative_to(call_dir)

        if self == POption.raw:
            return path.as_posix()

        if self == POption.dir:
            curr_path = path
            for _ in range(level):
                posix = curr_path.as_posix()
                if re.fullmatch("\.+", posix):
                    curr_path = Path(posix + ".")
                else:
                    curr_path = curr_path.parent
            return curr_path.as_posix()

        if self == POption.ext:
            return path.suffix[1:]

        if self == POption.name:
            return path.name

        if self == POption.stem:
            return path.stem

        raise OptionNotImplementedException(self)


@app.command(callback=print)
def fpath(
    path: Path = Argument(..., help="Path to find path"),
    option: POption = Option(POption.raw.value, "--option", "-o", help="Option"),
    strict: bool = Option(
        True, "--strict/--no-strict", "-s/-S", help="Check file exist or not"
    ),
    level: int = Option(1, "--level", "-l", help="Level incase of directory"),
    relative: bool = Option(
        True, "--relative/--no-relative", "-r/-R", help="Return relative path"
    ),
):
    return option.read(path, strict=strict, level=level, relative=relative)
