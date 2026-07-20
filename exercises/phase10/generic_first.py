"""Exercise 10.3 — a generic function.

first(xs, default=None) returns the first item of any iterable, or default
when empty. Annotate with a TypeVar so the checker infers first([1, 2]) as
int | None. Verify the inference with reveal_type() under mypy (then remove
it — reveal_type doesn't exist at runtime).
"""

from typing import TypeVar

T = TypeVar("T")


def first(xs, default=None):  # TODO: annotate with T
    raise NotImplementedError
