"""Exercise 17: JSON.

Based on Microsoft Python for Beginners lesson "17 - JSON".

Replace each NotImplementedError with your own code, then run:

    python3 -m unittest tests.test_17_json
"""


def create_person(first: str, last: str, city: str) -> dict[str, str]:
    """Return a dictionary with first, last, and City keys."""
    raise NotImplementedError("Create the person dictionary.")


def add_languages(person: dict, languages: list[str]) -> dict:
    """Add a languages key to person and return the same dictionary."""
    raise NotImplementedError("Add the languages list to the person dictionary.")


def person_to_json(person: dict) -> str:
    """Convert a person dictionary to a JSON string."""
    raise NotImplementedError("Use json.dumps() to create JSON.")


def staff_to_json(role: str, person: dict) -> str:
    """Create a nested staff dictionary and convert it to JSON.

    Example shape:
    {"Program Manager": {"first": "Christopher", "last": "Harrison"}}
    """
    raise NotImplementedError("Create the nested dictionary and convert it to JSON.")


def city_from_json(person_json: str) -> str:
    """Read and return the City value from a JSON string."""
    raise NotImplementedError("Use json.loads() and read the City key.")
