"""Exercise 13.4 — the event-loop model made visible (script).

async def fetch(name, delay): await asyncio.sleep(delay); return name.

1. Run three fetches SEQUENTIALLY (awaits in a row) — time it (~sum).
2. Run them CONCURRENTLY with asyncio.gather — time it (~max).
3. THE BIG ONE: replace one asyncio.sleep with time.sleep and rerun the
   concurrent version. Record what happened to the total time and write
   the explanation: what does blocking the loop do to every other task?
"""

import asyncio
import time

# TODO

if __name__ == "__main__":
    pass  # asyncio.run(main())
