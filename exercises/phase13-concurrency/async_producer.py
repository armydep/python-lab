"""Exercise 13.6 — producer/consumer with asyncio.Queue (script).

One producer putting 20 jobs, three consumers processing them
(await asyncio.sleep per job to simulate work). Shut down CLEANLY: either
sentinel values (one per consumer) or queue.join() + task_done() +
cancellation. Print which consumer handled which job; totals must add up.

Skills practiced:
- asyncio.Queue producer/consumer
- Clean shutdown of consumers
"""

import asyncio


NUMBER_OF_JOBS = 20
NUMBER_OF_CONSUMERS = 3
QUEUE_MAX_SIZE = 5
STOP = None


async def producer(queue: asyncio.Queue[int | None]) -> None:
    """Put all jobs followed by one stop sentinel per consumer."""
    for job in range(1, NUMBER_OF_JOBS + 1):
        await queue.put(job)
        print(f"Producer queued job {job}")

    for _ in range(NUMBER_OF_CONSUMERS):
        await queue.put(STOP)

    print("Producer finished")


async def consumer(name: str, queue: asyncio.Queue[int | None]) -> int:
    """Process jobs until a stop sentinel arrives."""
    jobs_processed = 0

    while True:
        job = await queue.get()
        try:
            if job is STOP:
                print(f"{name} stopped")
                return jobs_processed

            # Different durations make the work distribution visible.
            await asyncio.sleep(0.05 + (job % 3) * 0.02)
            jobs_processed += 1
            print(f"{name} handled job {job}")
        finally:
            # Every queue.get(), including a sentinel, must have exactly one
            # matching task_done() so queue.join() can finish.
            queue.task_done()


async def main() -> None:
    queue: asyncio.Queue[int | None] = asyncio.Queue(
        maxsize=QUEUE_MAX_SIZE
    )
    consumers = [
        asyncio.create_task(
            consumer(f"Consumer {index}", queue),
            name=f"Consumer {index}",
        )
        for index in range(1, NUMBER_OF_CONSUMERS + 1)
    ]

    await producer(queue)
    await queue.join()
    totals = await asyncio.gather(*consumers)

    print("\nJobs handled per consumer:")
    for task, total in zip(consumers, totals, strict=True):
        print(f"{task.get_name()}: {total}")

    grand_total = sum(totals)
    print(f"Total: {grand_total}/{NUMBER_OF_JOBS}")
    assert grand_total == NUMBER_OF_JOBS


if __name__ == "__main__":
    asyncio.run(main())
