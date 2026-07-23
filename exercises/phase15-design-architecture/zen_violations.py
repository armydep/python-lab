"""Exercise 15.1 — the Zen, violated then fixed (script, no test).

Six short snippets, each violating one Zen line (run `import this`):
nested where flat works · implicit magic · silent except · ambiguity ·
clever one-liner nobody can read · two ways to do the same thing in one
codebase. For each: the violation, the fix, and the Zen line as a label.

Skills practiced:
- The Zen of Python applied to real trade-offs
- Flat over nested; explicit over implicit; errors never pass silently
"""

from datetime import date
from typing import Any


# 1. "Flat is better than nested."
def nested_access_check(user: dict[str, Any] | None) -> bool:
    """Violation: several nested conditions obscure the actual rule."""
    if user is not None:
        if user.get("active"):
            if user.get("role") == "admin":
                return True
    return False


def flat_access_check(user: dict[str, Any] | None) -> bool:
    """Fix: guard clauses keep the successful path flat."""
    if user is None:
        return False
    if not user.get("active"):
        return False
    return user.get("role") == "admin"


# 2. "Explicit is better than implicit."
current_user = {"name": "Ada"}


def implicit_greeting() -> str:
    """Violation: behavior secretly depends on a module-level value."""
    return f"Hello, {current_user['name']}"


def explicit_greeting(user_name: str) -> str:
    """Fix: the dependency is visible at the call site."""
    return f"Hello, {user_name}"


# 3. "Errors should never pass silently."
def silently_parse_count(raw_value: str) -> int | None:
    """Violation: every error is swallowed without explanation."""
    try:
        return int(raw_value)
    except Exception:
        return None


def parse_count(raw_value: str) -> int:
    """Fix: catch the expected error and add useful context."""
    try:
        return int(raw_value)
    except ValueError as error:
        raise ValueError(
            f"count must be an integer, got {raw_value!r}"
        ) from error


# 4. "In the face of ambiguity, refuse the temptation to guess."
def guess_date(raw_value: str) -> date:
    """Violation: silently assumes that 07/08 means July 8."""
    month, day, year = map(int, raw_value.split("/"))
    return date(year, month, day)


def parse_iso_date(raw_value: str) -> date:
    """Fix: require the unambiguous ISO year-month-day format."""
    try:
        return date.fromisoformat(raw_value)
    except ValueError as error:
        raise ValueError("date must use YYYY-MM-DD format") from error


# 5. "Readability counts."
def clever_unique_tags(lines: list[str]) -> list[str]:
    """Violation: too many transformations are packed into one expression."""
    return sorted(
        set(
            tag.strip().lower()
            for line in lines
            for tag in line.split(",")
            if tag.strip()
        )
    )


def readable_unique_tags(lines: list[str]) -> list[str]:
    """Fix: name the collection and make each transformation visible."""
    unique_tags: set[str] = set()

    for line in lines:
        for raw_tag in line.split(","):
            tag = raw_tag.strip().lower()
            if tag:
                unique_tags.add(tag)

    return sorted(unique_tags)


# 6. "There should be one-- and preferably only one --obvious way to do it."
def normalize_imported_title(title: str) -> str:
    """Violation: one subsystem normalizes titles this way."""
    return title.strip().capitalize()


def normalize_api_title(title: str) -> str:
    """Violation: another subsystem uses a conflicting rule."""
    return " ".join(title.split()).title()


def normalize_title(title: str) -> str:
    """Fix: one shared canonical rule is used by every entry point."""
    return " ".join(title.split()).capitalize()


def main() -> None:
    admin = {"name": "Ada", "active": True, "role": "admin"}
    print("1. Flat is better than nested.")
    print(nested_access_check(admin), "->", flat_access_check(admin))

    print("\n2. Explicit is better than implicit.")
    print(implicit_greeting(), "->", explicit_greeting("Ada"))

    print("\n3. Errors should never pass silently.")
    print(f"Violation returned: {silently_parse_count('many')!r}")
    try:
        parse_count("many")
    except ValueError as error:
        print(f"Fix raised: {error}")

    print("\n4. In the face of ambiguity, refuse the temptation to guess.")
    print(f"Violation guessed: {guess_date('07/08/2026')}")
    print(f"Fix requires ISO: {parse_iso_date('2026-07-08')}")

    tags = [" Python, Design ", "design, testing"]
    print("\n5. Readability counts.")
    print(clever_unique_tags(tags), "->", readable_unique_tags(tags))

    raw_title = "  ship   the API  "
    print(
        "\n6. There should be one obvious way to do it.\n"
        f"Conflicting results: {normalize_imported_title(raw_title)!r}, "
        f"{normalize_api_title(raw_title)!r}\n"
        f"Canonical result: {normalize_title(raw_title)!r}"
    )


if __name__ == "__main__":
    main()
