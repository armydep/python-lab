"""Exercise 3.4 — matrices as lists of lists.

transpose_comp uses a nested comprehension; transpose_zip uses zip(*m).
Both return list of lists: [[1,2],[3,4],[5,6]] -> [[1,3,5],[2,4,6]].

Then, in comments at the bottom, explain why [[0]*3]*3 is a broken way to
build a matrix (aliasing!) — demonstrate with a snippet.
"""


def transpose_comp(m):
    raise NotImplementedError


def transpose_zip(m):
    raise NotImplementedError


# Why [[0]*3]*3 is broken:
#
