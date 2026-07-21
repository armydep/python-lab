"""Exercise 14.5 — caching: the win and the trap (script).

1. An expensive pure function (recursive fib or a slow computation) called
   with repeating args in a loop: time it, add functools.cache, time again
   — record the numbers.
2. The trap: show a case where caching is WRONG — a function whose result
   depends on mutable state or time. Demonstrate the stale result and
   write the rule: what must be true of a function before you cache it?

Skills practiced:
- functools.cache wins
- When caching is wrong (mutable or time-dependent results)
"""

# TODO
