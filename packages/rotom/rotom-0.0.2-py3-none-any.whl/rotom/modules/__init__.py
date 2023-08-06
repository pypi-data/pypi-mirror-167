from importlib import import_module
from pathlib import Path

from mousse import export_instance

from ..app import Command

CURRENT_FILE = Path(__file__).resolve()
CURRENT_DIR = CURRENT_FILE.parent

__all__ = []

for child in CURRENT_DIR.glob("*"):
    if not child.is_dir():
        continue

    if child.name.startswith("_"):
        continue

    try:
        module = import_module(f".{child.name}", package=__name__)
    except ImportError as e:
        pass
    else:
        export_instance(Command, module=module)
        __all__.append(child.name)
