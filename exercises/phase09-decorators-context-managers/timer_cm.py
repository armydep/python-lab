"""Exercise 9.5 — a Timer context manager, twice.

Class-based Timer: `with Timer() as t: ...` then t.elapsed holds seconds.
Must still record elapsed when the body RAISES (test the exception path).
Then rewrite as @contextmanager in ~6 lines (timer() yielding a mutable
holder or the start time — your call; document it).

Skills practiced:
- Class-based context managers (__enter__/__exit__)
- @contextmanager
- Cleanup on the exception path
"""

from contextlib import contextmanager
import time


class Timer:
    def __enter__(self):
        self._start = time.perf_counter()
        return self

    def __exit__(self, exc_type, exc, tb):
        self.elapsed = time.perf_counter() - self._start
        return False


@contextmanager
def timer():
    """Yield a dictionary populated with elapsed seconds on exit."""
    result = {}
    start = time.perf_counter()
    try:
        yield result
    finally:
        result["elapsed"] = time.perf_counter() - start
