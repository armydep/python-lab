"""Exercise 9.1 — a timing decorator.

@timed measures with time.perf_counter, stores the last duration on the
wrapper as func.last_elapsed, and RETURNS the wrapped function's result.
Use functools.wraps — then check help(func) and func.__name__ with and
without it, recording the difference in comments.
"""


def timed(func):
    raise NotImplementedError
