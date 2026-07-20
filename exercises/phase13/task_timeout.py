"""Exercise 13.5 — timeouts and partial failure (script).

Five tasks with random delays (0.1–2s):
1. Run them under asyncio.timeout(1.0) (or wait_for) — handle
   TimeoutError; what happened to the unfinished tasks?
2. Make one task raise; compare gather(...) vs
   gather(..., return_exceptions=True) — print exactly what comes back in
   each case and label the items.
"""

import asyncio
import random

# TODO

if __name__ == "__main__":
    pass
