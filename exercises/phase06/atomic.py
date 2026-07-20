"""Exercise 6.6 — atomic file writes.

atomic_write_text(path, text): write to a temp file in the SAME directory
(tempfile.NamedTemporaryFile(dir=path.parent, delete=False)), then
os.replace(tmp, path). A crash mid-write must leave the original file
untouched — readers see either the old or the new content, never a hybrid.

Use encoding="utf-8". Clean up the temp file if the write fails.
"""


def atomic_write_text(path, text):
    raise NotImplementedError
