"""Exercise 8.5 — chunking any iterable.

chunked(iterable, size) yields lists of up to `size` items. Must work on
ANY iterable including generators — no len(), no indexing. The last chunk
may be short. size < 1 -> ValueError. Compare with itertools.batched in a
comment.

Skills practiced:
- Generators over any iterable (no len/index)
- Comparison with itertools.batched
"""


def chunked(itr, size):
    if size < 1:
        raise ValueError('size < 1')
    iterator = iter(itr)
    while True:
        items = []
        for _ in range(size):
            try:
                item = next(iterator)
                items.append(item)
            except StopIteration:
                break
        if not items:
            return
        yield items
