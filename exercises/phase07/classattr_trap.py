"""Exercise 7.6 — the shared mutable class attribute trap (demo, no test).

1. BuggyTask with `tags = []` at CLASS level; two instances; append to one;
   print both — document the pollution.
2. FixedTask initializing tags in __init__ (or a dataclass with
   default_factory); prove independence.
Keep both versions. In a comment: how is this the same bug as the mutable
default argument from Phase 2?
"""

# TODO
