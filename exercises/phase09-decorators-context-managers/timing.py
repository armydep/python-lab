"""Exercise 9.1 — a timing decorator.

@timed measures with time.perf_counter, stores the last duration on the
wrapper as func.last_elapsed, and RETURNS the wrapped function's result.
Use functools.wraps — then check help(func) and func.__name__ with and
without it, recording the difference in comments.

Skills practiced:
- Writing a decorator
- functools.wraps
- time.perf_counter
"""

import time
from functools import wraps


def timed(func):
    @wraps(func)
    def wrp(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        end = time.perf_counter()
        wrp.last_elapsed = end - start
        return result

    return wrp
