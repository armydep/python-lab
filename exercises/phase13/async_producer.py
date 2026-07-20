"""Exercise 13.6 — producer/consumer with asyncio.Queue (script).

One producer putting 20 jobs, three consumers processing them
(await asyncio.sleep per job to simulate work). Shut down CLEANLY: either
sentinel values (one per consumer) or queue.join() + task_done() +
cancellation. Print which consumer handled which job; totals must add up.
"""

import asyncio

# TODO

if __name__ == "__main__":
    pass
