"""Exercise 13.1 — build a race condition, then kill it (script).

Version 1: two threads increment a shared counter 100_000 times each with
no lock; run 5 times; record the (wrong, varying) totals in comments.
Version 2: fix with threading.Lock.
Version 3: no shared state at all — ThreadPoolExecutor.map returning
per-worker counts, summed in the main thread.
All three versions in this file, clearly labeled, with your observations.

Skills practiced:
- Race conditions
- threading.Lock
- Sharing no state via ThreadPoolExecutor.map
"""

# TODO
