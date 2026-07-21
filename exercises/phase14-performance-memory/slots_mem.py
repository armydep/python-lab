"""Exercise 14.4 — memory, measured with tracemalloc (script).

One million small task-like objects, three representations: a regular
dataclass, a dataclass with slots=True, a plain tuple. Measure peak memory
for each with tracemalloc (build, snapshot, report bytes/object). In
comments: the ranking, the trade-offs, and why sys.getsizeof alone would
have lied to you.

Skills practiced:
- __slots__ memory savings
- Measuring with tracemalloc
"""

# TODO
