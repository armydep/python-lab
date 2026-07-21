"""Exercise 8.2 — exhaustion (demo script, no test).

1. g = (x*x for x in range(5)); list(g) twice — predict, run, explain.
2. it = iter(range(6)); list(zip(it, it)) — predict, run, explain why you
   get (0,1),(2,3),(4,5) and not (0,0),(1,1)...
Document the bug class this creates in real code (e.g. logging an iterator
then processing it).

Skills practiced:
- Iterators are single-use and exhaust
- The zip-on-the-same-iterator gotcha
"""

# TODO
