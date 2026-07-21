"""Exercise 4.3 — build a circular import ON PURPOSE.

Make a.py import something from b.py and b.py import something from a.py;
run `python a.py` and paste the exact error as a comment. Then fix it two
ways: (a) move the shared piece to c.py, (b) import inside the function.
Keep the broken version in comments; note which fix is better and when.

Skills practiced:
- Circular imports: how they arise
- Two fixes: extract a third module, or import inside a function
"""

# Broken version:
#
# # a.py
# from b import message_from_b
#
# def message_from_a():
#     return "message from a"
#
# # b.py
# from a import message_from_a
#
# def message_from_b():
#     return "message from b"
#
# Running ``python a.py`` failed with:
# ImportError: cannot import name 'message_from_b' from partially initialized
# module 'b' (most likely due to a circular import)

# Fix 1 (preferred): both modules import their shared dependency from c.py.
from b import message_from_b
from c import format_message


def message_from_a():
    """Return a message identifying module a."""
    return format_message("a")


def combined_message():
    """Use both modules after their imports have completed safely."""
    return f"{message_from_a()}; {message_from_b()}"


# Fix 2 is demonstrated by message_from_a_late() in b.py. Moving an import
# inside a function delays it until both modules are initialized. This is handy
# when extracting shared code is impractical, but c.py is usually clearer and
# gives the modules a clean, one-way dependency structure.


if __name__ == "__main__":
    print(combined_message())
