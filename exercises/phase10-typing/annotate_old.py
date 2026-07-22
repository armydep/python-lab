"""Exercise 10.1 — annotate your own past code (checker exercise, no test).

Copy three of your finished Phase 2/3 solutions here (e.g. describe,
invert_roles, group_anagrams). Fully annotate them. Run:

    mypy --strict exercises/phase10/annotate_old.py

Fix every finding. In comments, classify each: real bug vs annotation gap.

Skills practiced:
- Adding type annotations to existing code
- Running mypy --strict
"""

from collections.abc import Iterable, Mapping


# Annotation gap: the original function did not specify the numeric argument
# type or the three-value tuple it returns.
def describe(*numbers: float) -> tuple[float, float, float]:
    if not numbers:
        raise ValueError("describe() requires at least one number")
    return min(numbers), max(numbers), sum(numbers) / len(numbers)


# Annotation gap: the original function did not describe either the input
# mapping or the dictionary of lists produced by the inversion.
def invert_roles(users: Mapping[str, str]) -> dict[str, list[str]]:
    roles: dict[str, list[str]] = {}
    for user, role in users.items():
        roles.setdefault(role, []).append(user)
    return roles


# Annotation gap: the original function left the element and nested container
# types implicit. No runtime bug was found while adding these annotations.
def group_anagrams(words: Iterable[str]) -> dict[str, list[str]]:
    groups: dict[str, list[str]] = {}
    for word in words:
        key = "".join(sorted(word))
        groups.setdefault(key, []).append(word)
    return groups
