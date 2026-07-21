"""Exercise 6.5 — walk a tree with pathlib.

py_files_by_size(root) -> list of (Path, size_bytes), largest first, for
every *.py under root (recursive: Path.glob("**/*.py")). The __main__ demo
prints them plus a total at the bottom.

Skills practiced:
- pathlib.Path and glob('**/*.py')
- Sorting by file size
"""


def py_files_by_size(root):
    """Return a list of (Path, size_bytes) for every *.py under root."""
    from pathlib import Path

    root_path = Path(root)
    py_files = [(p, p.stat().st_size) for p in root_path.glob("**/*.py")]
    return sorted(py_files, key=lambda x: x[1], reverse=True)


if __name__ == "__main__":
    import sys

    root_dir = sys.argv[1] if len(sys.argv) > 1 else "."
    py_files = py_files_by_size(root_dir)
    total_size = sum(size for _, size in py_files)
    for path, size in py_files:
        if size > 0:
            print(f"{size:>10} {path}")
    print(f"Total size: {total_size} bytes")
