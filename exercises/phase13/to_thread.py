"""Exercise 13.7 — escaping to blocking code (script).

An async main runs a 'heartbeat' task printing a dot every 0.2s, alongside
a blocking function (time.sleep(2) standing in for your JSON load):
1. Call the blocking function DIRECTLY inside async — the heartbeat
   freezes. Observe and record.
2. Wrap it in await asyncio.to_thread(...) — the heartbeat keeps beating.
Record both outputs; one sentence on when you'll need this in FastAPI.
"""

import asyncio
import time

# TODO

if __name__ == "__main__":
    pass
