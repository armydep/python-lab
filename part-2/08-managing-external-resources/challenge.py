"""Exercise 08: managing external resources.

Based on Microsoft More Python for Beginners lesson
"08 - Managing external resources".

Replace each NotImplementedError with your own code, then run:

    python3 -m unittest tests.test_08_managing_external_resources
"""

from pathlib import Path


def write_with_context_manager(path: str | Path, text: str) -> None:
    """Write text to path using a `with` statement, not try/finally.

    Overwrite any existing content at path.
    """
    raise NotImplementedError


def copy_with_context_manager(source: str | Path, destination: str | Path) -> None:
    """Copy the text contents of source to destination.

    Open both files with `with` statements so each is closed automatically,
    even if an error occurs while copying.
    """
    raise NotImplementedError


def safe_read(path: str | Path, default: str = "") -> str:
    """Return the text content of path, or default if path does not exist.

    Use a `with` statement for the read; do not let a missing file raise.
    """
    raise NotImplementedError
