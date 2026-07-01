"""Test helpers for loading challenge files from topic folders."""

import importlib.util
import sys
from pathlib import Path
from types import ModuleType


PROJECT_ROOT = Path(__file__).resolve().parents[1]


def load_challenge(folder: str) -> ModuleType:
    """Load a topic folder's challenge.py file as a module."""
    challenge_path = PROJECT_ROOT / folder / "challenge.py"
    module_name = f"challenge_{folder.replace('-', '_')}"

    folder_path = str(challenge_path.parent)
    if folder_path not in sys.path:
        sys.path.insert(0, folder_path)

    spec = importlib.util.spec_from_file_location(module_name, challenge_path)
    assert spec is not None
    assert spec.loader is not None

    module = importlib.util.module_from_spec(spec)
    sys.modules[module_name] = module
    spec.loader.exec_module(module)
    return module
