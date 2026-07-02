"""Exercise 07: reading and writing files.

Based on Microsoft More Python for Beginners lesson
"07 - Reading and writing files".

Replace each NotImplementedError with your own code, then run:

    python3 -m unittest tests.test_07_reading_and_writing_files
"""

from pathlib import Path


def read_first_line(path: str | Path) -> str:
    """Open path for reading and return its first line, without the newline."""
    with open(path, "rt") as stream:
        return stream.readline().rstrip("\n")


def read_all_lines(path: str | Path) -> list[str]:
    """Open path for reading and return every line, without newlines."""
    with open(path, "rt") as stream:
        return [line.rstrip("\n") for line in stream]


def write_lines(path: str | Path, lines: list[str]) -> None:
    """Open path for writing and write each line followed by a newline.

    Overwrite any existing content at path.
    """
    with open(path, "wt") as stream:
        for line in lines:
            stream.write(line + "\n")


def append_line(path: str | Path, line: str) -> None:
    """Append line followed by a newline to the end of path."""
    with open(path, "at") as stream:
        stream.write(line + "\n")
