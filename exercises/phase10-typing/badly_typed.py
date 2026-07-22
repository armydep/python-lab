"""Exercise 10.6 — when typing exposes bad design (checker exercise).

Write get_names(data, as_string=False) that returns a comma-joined str
when as_string else a list[str]. Try to annotate it honestly
(-> str | list[str]) and watch every CALLER need isinstance checks.

Then refactor into two functions (get_names / get_names_joined) and note
in a comment why the design — not the annotation — was the problem.

Skills practiced:
- Hard-to-type signatures as a signal of poor design
- Refactoring one function into two
"""

from collections.abc import Iterable, Mapping


NameRecord = Mapping[str, str]


def get_names(data: Iterable[NameRecord]) -> list[str]:
    """Return the name from each record."""
    return [record["name"] for record in data]


def get_names_joined(data: Iterable[NameRecord]) -> str:
    """Return the names as a comma-separated string."""
    return ", ".join(get_names(data))


# The old flag-based design returned str | list[str], so every caller had to
# narrow the result before using string- or list-specific operations. The
# problem was the ambiguous API, not the annotation. Separate functions give
# each call one predictable return type.
