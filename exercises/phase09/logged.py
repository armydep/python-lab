"""Exercise 9.2 — a parameterized decorator (the three-layer form).

@logged(prefix="CALL") prints f"{prefix}: {func.__name__}{args!r}" before
calling, and passes the return value through untouched. Preserve metadata
with functools.wraps.

Then stack @timed and @logged both ways on one function and explain the
output order in a comment.
"""


def logged(prefix="CALL"):
    raise NotImplementedError
