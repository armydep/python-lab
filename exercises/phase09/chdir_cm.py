"""Exercise 9.6 — working_directory context manager.

with working_directory(path): chdir in, ALWAYS chdir back — even when the
body raises (that's the test). Build it with @contextmanager + try/finally.
Compare with contextlib.chdir in a comment.
"""

from contextlib import contextmanager


@contextmanager
def working_directory(path):
    raise NotImplementedError
    yield  # keep this a generator; restructure as you implement
