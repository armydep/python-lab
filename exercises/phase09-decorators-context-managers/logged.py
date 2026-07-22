"""Exercise 9.2 — a parameterized decorator (the three-layer form).

@logged(prefix="CALL") prints f"{prefix}: {func.__name__}{args!r}" before
calling, and passes the return value through untouched. Preserve metadata
with functools.wraps.

Then stack @timed and @logged both ways on one function and explain the
output order in a comment.

Skills practiced:
- Parameterized (three-layer) decorators
- Decorator stacking order
"""
from functools import wraps


def logged(prefix="CALL"):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            print(f"{prefix}: {func.__name__}{args!r}", end=" ")
            result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator
