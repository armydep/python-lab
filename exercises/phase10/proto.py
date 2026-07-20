"""Exercise 10.4 — Protocol (structural typing).

Storable is a Protocol with to_dict(self) -> dict and a classmethod
from_dict(cls, d: dict). save_all(items: Iterable[Storable]) -> list[dict]
calls to_dict on each.

Write a class satisfying Storable WITHOUT importing or inheriting it, and
run mypy to confirm. Then break the protocol (rename a method) and paste
the checker error in a comment.
"""

from typing import Iterable, Protocol


class Storable(Protocol):
    def to_dict(self) -> dict: ...


def save_all(items):  # TODO: annotate
    raise NotImplementedError
