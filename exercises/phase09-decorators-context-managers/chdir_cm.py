"""Exercise 9.6 — working_directory context manager.

with working_directory(path): chdir in, ALWAYS chdir back — even when the
body raises (that's the test). Build it with @contextmanager + try/finally.
Compare with contextlib.chdir in a comment.

Skills practiced:
- @contextmanager with try/finally
- Guaranteed cleanup
"""

from contextlib import contextmanager
import os


@contextmanager
def working_directory(path):
    previous_directory = os.getcwd()
    os.chdir(path)
    try:
        yield
    finally:
        os.chdir(previous_directory)


# Python 3.11+ also provides equivalent behavior via contextlib.chdir.
