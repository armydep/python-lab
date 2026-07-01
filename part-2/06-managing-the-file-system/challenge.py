"""Exercise 06: managing the file system.

Based on Microsoft More Python for Beginners lesson
"06 - Managing the file system".

Replace each NotImplementedError with your own code, then run:

    python3 -m unittest tests.test_06_managing_the_file_system
"""

from pathlib import Path


def join_path(directory: str | Path, name: str) -> Path:
    """Return directory joined with name as a Path."""
    raise NotImplementedError


def path_exists(path: str | Path) -> bool:
    """Return True when path exists on disk."""
    raise NotImplementedError


def is_directory(path: str | Path) -> bool:
    """Return True when path is an existing directory."""
    raise NotImplementedError


def file_name_parts(path: str | Path) -> dict[str, str]:
    """Return {"name": ..., "suffix": ..., "parent_name": ...} for path.

    Example: for ".../notes/demo.txt" return
    {"name": "demo.txt", "suffix": ".txt", "parent_name": "notes"}.
    """
    raise NotImplementedError


def list_subdirectory_names(directory: str | Path) -> list[str]:
    """Return the sorted names of the immediate subdirectories of directory."""
    raise NotImplementedError
