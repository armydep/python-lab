"""Exercise 6.6 — atomic file writes.

atomic_write_text(path, text): write to a temp file in the SAME directory
(tempfile.NamedTemporaryFile(dir=path.parent, delete=False)), then
os.replace(tmp, path). A crash mid-write must leave the original file
untouched — readers see either the old or the new content, never a hybrid.

Use encoding="utf-8". Clean up the temp file if the write fails.

Skills practiced:
- Atomic writes: temp file + os.replace
- tempfile
- Crash-safe file replacement
"""


def atomic_write_text(path, text):
    """Write text to path atomically, crash-safe."""
    import os
    import tempfile
    from pathlib import Path

    path = Path(path)
    temp_file = None
    try:
        with tempfile.NamedTemporaryFile(
            mode="w", encoding="utf-8", dir=path.parent, delete=False
        ) as tmp:
            temp_file = tmp.name
            tmp.write(text)
        os.replace(temp_file, path)
    except Exception:
        if temp_file and os.path.exists(temp_file):
            os.remove(temp_file)
        raise
