"""Shared code extracted from a.py and b.py to prevent circular imports."""


def format_message(module_name):
    """Build the message shared by modules a and b."""
    return f"message from {module_name}"
