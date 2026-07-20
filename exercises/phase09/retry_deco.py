"""Exercise 9.3 — port Phase 5's retry into a decorator.

@retry(attempts=3, on=(OSError,)):
  - retries only on the exceptions in `on`, up to `attempts` total calls
  - re-raises the last error after exhausting attempts
  - other exceptions propagate immediately
  - preserves the function's metadata
"""


def retry(attempts=3, on=(OSError,)):
    raise NotImplementedError
