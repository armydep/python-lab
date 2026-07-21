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

# Prediction: the first conversion produces [0, 1, 4, 9, 16], and the
# second produces [] because the generator has already been exhausted.
g = (x * x for x in range(5))
first_pass = list(g)
second_pass = list(g)

print("First pass: ", first_pass)
print("Second pass:", second_pass)

# Actual:
# First pass:  [0, 1, 4, 9, 16]
# Second pass: []


# Prediction: zip calls next() twice on the same iterator for every pair, so
# the result is [(0, 1), (2, 3), (4, 5)].
it = iter(range(6))
pairs = list(zip(it, it))

print("Pairs:", pairs)

# Actual:
# Pairs: [(0, 1), (2, 3), (4, 5)]


# Real bug class: consuming an iterator for logging, validation, or counting
# exhausts it. Later processing then receives no values and may silently do no
# work. Materialize it once when reuse is required, or create a fresh iterator
# for each pass.
