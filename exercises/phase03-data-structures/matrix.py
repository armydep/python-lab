"""Exercise 3.4 — matrices as lists of lists.

transpose_comp uses a nested comprehension; transpose_zip uses zip(*m).
Both return list of lists: [[1,2],[3,4],[5,6]] -> [[1,3,5],[2,4,6]].

Then, in comments at the bottom, explain why [[0]*3]*3 is a broken way to
build a matrix (aliasing!) — demonstrate with a snippet.

Skills practiced:
- Nested list comprehensions
- Transpose with zip(*m)
- The list-aliasing pitfall ([[0]*n]*m)
"""


def transpose_comp(m):
    """Transpose a matrix using a nested list comprehension."""
    if not m:
        return []
    return [[row[column] for row in m] for column in range(len(m[0]))]


def transpose_zip(m):
    """Transpose a matrix using argument unpacking and ``zip``."""
    return [list(column) for column in zip(*m)]


# Why [[0]*3]*3 is broken:
# Multiplying the outer list copies references to the same inner list rather
# than creating three independent rows:
# matrix = [[0] * 3] * 3
# matrix[0][1] = 7
# matrix  # [[0, 7, 0], [0, 7, 0], [0, 7, 0]]
# Build independent rows instead: [[0] * 3 for _ in range(3)].
