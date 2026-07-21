"""Exercise 8.6 — the groupby trap.

counts_by_key(pairs): pairs is an UNSORTED iterable of (key, value);
return {key: count} using itertools.groupby CORRECTLY (sort first!).
First do it wrong on purpose in a scratch demo, observe the fragmented
groups, then write the moral as a comment.

Skills practiced:
- itertools.groupby requires pre-sorted input
- The sort-then-group pattern
"""


def counts_by_key(pairs):
    raise NotImplementedError


# Moral:
#
