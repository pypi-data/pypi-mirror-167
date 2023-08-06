from pathlib import Path
from typing import *

import setuptools

PACKAGE = "rotom"
CURRENT_DIR = Path(__file__).resolve().parent

with open(CURRENT_DIR / "README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()


def read_requirements(path: Union[str, Path]):
    with open(path, "r") as fh:
        return [line.strip() for line in fh.readlines() if not line.startswith("#")]


__VERSION__ = "0.0.2"

requirements = read_requirements(CURRENT_DIR / "requirements.txt")
extras_require = {}


packages = setuptools.find_packages()
sub_packages = []
for sub_requirement in (CURRENT_DIR / PACKAGE / "modules").rglob("requirements.txt"):
    sub_package = sub_requirement.parent.relative_to(CURRENT_DIR)
    extras_require[sub_package.name] = read_requirements(sub_requirement)


extras_require["all"] = list(set(sum((val for val in extras_require.values()), [])))


entry_points = {"console_scripts": (f"{PACKAGE} = {PACKAGE}.__main__:main",)}


setuptools.setup(
    name=PACKAGE,
    packages=packages,
    version=__VERSION__,
    author="nghoangdat",
    author_email="18.hoang.dat.12@gmail.com",
    description="rotom",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=f"https://github.com/NgHoangDat/{PACKAGE}.git",
    download_url=f"https://github.com/NgHoangDat/rotom/archive/v{__VERSION__}.tar.gz",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    entry_points=entry_points,
    install_requires=requirements,
    extras_require=extras_require,
)
