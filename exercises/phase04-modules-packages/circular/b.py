"""b — exercise.

Skills practiced:
- Circular imports: how they arise and how to break them
"""

from c import format_message


def message_from_b():
    """Return a message identifying module b."""
    return format_message("b")


def message_from_a_late():
    """Demonstrate breaking the cycle with a function-local import."""
    from a import message_from_a

    return message_from_a()
