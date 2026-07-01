"""Exercise 14: function parameters.

Based on Microsoft Python for Beginners lesson "14 - Function parameters".

Replace each NotImplementedError with your own code, then run:

    python3 -m unittest tests.test_14_function_parameters
"""


def get_initial(name: str, force_uppercase: bool = True) -> str:
    """Return the first letter of name.

    By default the initial should be uppercase. When force_uppercase is False,
    keep the original letter case.
    """
    initial = name[0:1]

    if force_uppercase:
        return initial.upper()
    else:
        return initial


def get_initials(
    first_name: str,
    last_name: str,
    force_uppercase: bool = True,
    separator: str = "",
) -> str:
    """Return initials for first_name and last_name.

    This function should work with positional arguments and named arguments.
    The separator goes between the two initials.
    """
    initials = first_name[0] + separator + last_name[0]

    if force_uppercase:
        return initials.upper()

    return initials


def format_user_label(
    first_name: str,
    last_name: str,
    role: str = "Student",
) -> str:
    """Return a label using a default role.

    Example: "Ada Lovelace - Student"
    """
    return f"{first_name} {last_name} - {role}"
