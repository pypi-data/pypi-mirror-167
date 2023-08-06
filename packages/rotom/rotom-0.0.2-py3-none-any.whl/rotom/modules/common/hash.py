import hashlib
from typing import *
from pathlib import Path
from enum import Enum

from rich.progress import track
from typer import Argument, Option

from .app import app


class InvalidHashAlgoException(Exception):
    def __init__(self, hash_name: str):
        super().__init__(f"{hash_name} is not supported")


class PathNotFoundExecption(Exception):
    def __init__(self, path: Path) -> None:
        super().__init__(f"{path.as_posix()} not found")


class HashAlgo(str, Enum):
    md5: str = "md5"
    sha1: str = "sha1"
    sha224: str = "sha224"
    sha256: str = "sha256"
    sha384: str = "sha384"

    def __call__(self):
        if self == HashAlgo.md5:
            return hashlib.md5()

        if self == HashAlgo.sha1:
            return hashlib.sha1()

        if self == HashAlgo.sha224:
            return hashlib.sha224()

        if self == HashAlgo.sha256:
            return hashlib.sha256()

        if self == HashAlgo.sha384:
            return hashlib.sha384()

        raise InvalidHashAlgoException(self.value)


@app.command(callback=print)
def hash_path(
    path: Path = Argument(..., help="File to hash"),
    pattern: str = Option("*", help="File patern incase path is directory"),
    algo: HashAlgo = Option(HashAlgo.md5.value, help="Hash generator"),
    num_block: int = Option(16, help="Number of block for each step"),
    length: int = Option(-1, help="Output length"),
    verbose: bool = Option(True, help="show more info"),
):
    if not path.exists():
        raise PathNotFoundExecption(path)

    path = path.resolve()
    files = []
    if path.is_file():
        files.append(path)

    if path.is_dir():
        for child in path.rglob(pattern):
            if child.is_dir():
                continue

            files.append(child.resolve())

    def get_hash(file: Path) -> str:
        hash = algo()
        with open(file, "rb") as fin:
            while True:
                buf = fin.read(num_block * hash.block_size)
                if not buf:
                    break
                hash.update(buf)
        hash = hash.hexdigest()
        return hash

    def shorten_hash(hash: str) -> str:
        if length > 0:
            hash = hash.encode()
            hash = hashlib.shake_256(hash).hexdigest(length=length // 2)
        return hash

    hashes = []

    if verbose:
        for file in track(files, description="Hashing..."):
            hashes.append((file.relative_to(path).as_posix(), get_hash(file)))
    else:
        for file in files:
            try:
                hashes.append((file.relative_to(path).as_posix(), get_hash(file)))
            except Exception as e:
                print(e, file)
                raise e

    if path.is_file():
        _, hash = hashes[0]
        return shorten_hash(hash)

    if len(hashes) == 0:
        return ""

    hashes.sort()
    return hash_str(
        "-".join(f"{file}-{hash}" for file, hash in hashes),
        algo,
        length,
    )


@app.command(callback=print)
def hash_str(
    string: str = Argument(..., help="String to hash"),
    algo: HashAlgo = Option(HashAlgo.md5.value, help="Hash generator"),
    length: int = Option(-1, help="Output length"),
):
    hash = algo()
    hash.update(string.encode())
    hash = hash.hexdigest()

    if length > 0:
        hash = hash.encode()
        hash = hashlib.shake_256(hash).hexdigest(length=length // 2)

    return hash
