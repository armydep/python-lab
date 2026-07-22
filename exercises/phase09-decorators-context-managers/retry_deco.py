"""Exercise 9.3 — port Phase 5's retry into a decorator.

@retry(attempts=3, on=(OSError,)):
  - retries only on the exceptions in `on`, up to `attempts` total calls
  - re-raises the last error after exhausting attempts
  - other exceptions propagate immediately
  - preserves the function's metadata

Skills practiced:
- Decorators that take arguments
- Selective retry on given exception types
"""
from functools import wraps


def retry(attempts=3, on=(OSError,)):
    if attempts < 1:
        raise ValueError("attempts must be at least 1")

    def decorator(func):
        @wraps(func)
        def call_with_retry(*args, **kwargs):
            for attempt in range(attempts):
                try:
                    return func(*args, **kwargs)
                except on:
                    if attempt == attempts - 1:
                        raise

        return call_with_retry

    return decorator
