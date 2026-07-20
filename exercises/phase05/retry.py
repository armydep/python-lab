"""Exercise 5.2 — retry with exception discipline.

call_with_retry(func, attempts=3):
  - calls func(); returns its result on success
  - retries ONLY on OSError, up to `attempts` total calls
  - after exhausting attempts, raises RetryError with the last OSError as
    __cause__ (raise ... from err)
  - any other exception propagates immediately, no retry

Test it yourself with a flaky fake built from a closure counter (Phase 2).
"""


class RetryError(Exception):
    pass


def call_with_retry(func, attempts=3):
    raise NotImplementedError
