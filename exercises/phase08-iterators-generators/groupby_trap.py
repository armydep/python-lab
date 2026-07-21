"""Exercise 8.6 — the groupby trap.

counts_by_key(pairs): pairs is an UNSORTED iterable of (key, value);
return {key: count} using itertools.groupby CORRECTLY (sort first!).
First do it wrong on purpose in a scratch demo, observe the fragmented
groups, then write the moral as a comment.

Skills practiced:
- itertools.groupby requires pre-sorted input
- The sort-then-group pattern
"""

from itertools import groupby


def counts_by_key(pairs):
    sorted_pairs = sorted(pairs, key=lambda pair: pair[0])
    return {
        key: sum(1 for _ in group)
        for key, group in groupby(sorted_pairs, key=lambda pair: pair[0])
    }


# Moral:
# itertools.groupby only groups adjacent items with the same key, so input
# must be sorted by that key first when all matching items should form one group.
