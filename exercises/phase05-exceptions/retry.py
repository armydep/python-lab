"""Exercise 5.2 — retry with exception discipline.

call_with_retry(func, attempts=3):
  - calls func(); returns its result on success
  - retries ONLY on OSError, up to `attempts` total calls
  - after exhausting attempts, raises RetryError with the last OSError as
    __cause__ (raise ... from err)
  - any other exception propagates immediately, no retry

Test it yourself with a flaky fake built from a closure counter (Phase 2).

Skills practiced:
- A try/except retry loop
- Exception chaining with 'raise ... from'
- Re-raising after attempts are exhausted
"""


class RetryError(Exception):
    pass


def call_with_retry(func, attempts=3):
    if attempts < 1:
        raise ValueError("attempts must be at least 1")

    for att in range(attempts):
        try:
            return func()
        except OSError as err:
            if att == attempts - 1:
                raise RetryError("All attempts failed") from err
