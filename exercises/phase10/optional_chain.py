"""Exercise 10.2 — Optional forces None-handling (checker exercise).

Model: users = {1: "ada", 2: "bob"}.

find_user(user_id) -> str | None.
shout_name_guarded(user_id) -> the name upper-cased, or "NOBODY" when
absent (narrow with an if).
shout_name_or_raise(user_id) -> name upper-cased, KeyError when absent
(narrow with an early raise).

First write shout_name_guarded WITHOUT the guard, run mypy --strict, and
paste the exact checker error as a comment. Feel the pressure; then fix.
"""

USERS = {1: "ada", 2: "bob"}


def find_user(user_id: int) -> str | None:
    raise NotImplementedError


def shout_name_guarded(user_id: int) -> str:
    raise NotImplementedError


def shout_name_or_raise(user_id: int) -> str:
    raise NotImplementedError
