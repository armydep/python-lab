"""Exercise 18: decorators.

Based on Microsoft Python for Beginners lesson "18 - Decorators".

Replace each NotImplementedError with your own code, then run:

    python3 -m unittest tests.test_18_decorators
"""

import functools


def uppercase_result(func):
    """Decorate func so any string result is returned in uppercase.

    Use functools.wraps() so the decorated function keeps its original name.
    """

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)

        if isinstance(result, str):
            return result.upper()

        return result

    return wrapper


def prefix_result(prefix: str):
    """Return a decorator that prefixes a string result with prefix."""

    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)

            if isinstance(result, str):
                return prefix + result

            return result

        return wrapper

    return decorator


def repeat(times: int):
    """Return a decorator that calls func times times and returns a list of results."""

    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            results = []

            for _ in range(times):
                results.append(func(*args, **kwargs))

            return results

        return wrapper

    return decorator
