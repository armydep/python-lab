"""Exercise 13.2 — threads for I/O-bound work (script).

Simulate 10 'downloads' (time.sleep(0.5) each): sequential loop vs
ThreadPoolExecutor(max_workers=5). Measure both with time.perf_counter.
In comments: explain the ~5x speedup, and precisely why the GIL did NOT
prevent it (where is the GIL released?).
"""

# TODO
