"""Exercise 10.4 — Protocol (structural typing).

Storable is a Protocol with to_dict(self) -> dict and a classmethod
from_dict(cls, d: dict). save_all(items: Iterable[Storable]) -> list[dict]
calls to_dict on each.

Write a class satisfying Storable WITHOUT importing or inheriting it, and
run mypy to confirm. Then break the protocol (rename a method) and paste
the checker error in a comment.

Skills practiced:
- typing.Protocol (structural typing)
- Iterable annotations
"""

from collections.abc import Iterable
from typing import Protocol, Self


class Storable(Protocol):
    def to_dict(self) -> dict[str, object]: ...

    @classmethod
    def from_dict(cls, data: dict[str, object]) -> Self: ...


def save_all(items: Iterable[Storable]) -> list[dict[str, object]]:
    return [item.to_dict() for item in items]


class User:
    def __init__(self, name: str) -> None:
        self.name = name

    def to_dict(self) -> dict[str, object]:
        return {"name": self.name}

    @classmethod
    def from_dict(cls, data: dict[str, object]) -> Self:
        return cls(name=str(data["name"]))


# This call makes mypy verify that User structurally satisfies Storable.
# Renaming User.to_dict to serialize produced:
# error: Argument 1 to "save_all" has incompatible type "list[User]";
# expected "Iterable[Storable]"  [arg-type]
EXAMPLE_USERS = [User("Ada"), User("Bob")]
EXAMPLE_DATA = save_all(EXAMPLE_USERS)
