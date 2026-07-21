"""Exercise 7.6 — the shared mutable class attribute trap (demo, no test).

1. BuggyTask with `tags = []` at CLASS level; two instances; append to one;
   print both — document the pollution.
2. FixedTask initializing tags in __init__ (or a dataclass with
   default_factory); prove independence.
Keep both versions. In a comment: how is this the same bug as the mutable
default argument from Phase 2?

Skills practiced:
- The shared mutable class-attribute pitfall
- Initialising per-instance state in __init__/default_factory
"""

class BuggyTask:
    """Incorrectly shares one mutable tags list across every instance."""

    tags = []


class FixedTask:
    """Creates an independent tags list for every instance."""

    def __init__(self):
        self.tags = []


# This is the same bug as a mutable default argument: the list is created only
# once (at class definition or function definition time), then reused by every
# instance or call. Creating the list in __init__ gives each instance a new
# object, just as using a None sentinel/default_factory does for other cases.


if __name__ == "__main__":
    buggy_first = BuggyTask()
    buggy_second = BuggyTask()
    buggy_first.tags.append("urgent")
    print("Buggy first: ", buggy_first.tags)
    print("Buggy second:", buggy_second.tags)  # Also contains "urgent".

    fixed_first = FixedTask()
    fixed_second = FixedTask()
    fixed_first.tags.append("urgent")
    print("Fixed first: ", fixed_first.tags)
    print("Fixed second:", fixed_second.tags)  # Remains empty.
