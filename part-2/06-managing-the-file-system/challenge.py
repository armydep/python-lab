"""Exercise 06: managing the file system.

Based on Microsoft More Python for Beginners lesson
"06 - Managing the file system".

Replace each NotImplementedError with your own code, then run:

    python3 -m unittest tests.test_06_managing_the_file_system
"""

from pathlib import Path


def join_path(directory: str | Path, name: str) -> Path:
    """Return directory joined with name as a Path."""
    return Path(directory) / name


def path_exists(path: str | Path) -> bool:
    """Return True when path exists on disk."""
    return Path(path).exists()


def is_directory(path: str | Path) -> bool:
    """Return True when path is an existing directory."""
    return Path(path).is_dir()


def file_name_parts(path: str | Path) -> dict[str, str]:
    """Return {"name": ..., "suffix": ..., "parent_name": ...} for path.

    Example: for ".../notes/demo.txt" return
    {"name": "demo.txt", "suffix": ".txt", "parent_name": "notes"}.
    """
    file_path = Path(path)
    return {
        "name": file_path.name,
        "suffix": file_path.suffix,
        "parent_name": file_path.parent.name,
    }


def list_subdirectory_names(directory: str | Path) -> list[str]:
    """Return the sorted names of the immediate subdirectories of directory."""
    return sorted(path.name for path in Path(directory).iterdir() if path.is_dir())
