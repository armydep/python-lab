"""Exercise 9.5 — a Timer context manager, twice.

Class-based Timer: `with Timer() as t: ...` then t.elapsed holds seconds.
Must still record elapsed when the body RAISES (test the exception path).
Then rewrite as @contextmanager in ~6 lines (timer() yielding a mutable
holder or the start time — your call; document it).
"""

from contextlib import contextmanager


class Timer:
    def __enter__(self):
        raise NotImplementedError

    def __exit__(self, exc_type, exc, tb):
        raise NotImplementedError


@contextmanager
def timer():
    raise NotImplementedError
    yield  # keep this a generator; restructure as you implement
