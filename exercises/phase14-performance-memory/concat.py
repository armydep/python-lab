"""Exercise 14.2 — string building, measured (script).

Build a 100_000-piece string three ways: += in a loop, "".join(list),
io.StringIO. Time each at sizes 10k/50k/100k. Explain in comments why +=
is quadratic (immutability -> full copy per step) and which you'd use by
default.

Skills practiced:
- String-building cost: += vs join vs StringIO
- Why += in a loop is quadratic
"""

# TODO
