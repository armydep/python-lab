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

import random
import threading
import time


INCREMENTS_PER_THREAD = 100_000
NUMBER_OF_RUNS = 5
NUMBER_OF_WORKERS = 2

counter = 0
counter_lock = threading.Lock()

#v2
def increment_counter_v2() -> None:
    global counter

    for _ in range(INCREMENTS_PER_THREAD):
        with counter_lock:
            counter += 1


def increment_counter_v1() -> None:
    global counter

    rng = random.Random()

    for i in range(INCREMENTS_PER_THREAD):
        # counter += 1 conceptually consists of:
        #
        # 1. Read the current value
        # 2. Calculate the new value
        # 3. Write the new value
        #
        # Another thread may modify counter between these steps.
        current_value = counter

        # Make a thread switch more likely so that the race condition
        # can be observed consistently.
        if i % 100 == 0:
            time.sleep(rng.uniform(0, 0.00002))

        counter = current_value + 1


def run_experiment() -> None:
    global counter

    expected_total = INCREMENTS_PER_THREAD * NUMBER_OF_WORKERS

    for run_number in range(1, NUMBER_OF_RUNS + 1):
        counter = 0

        thread_1 = threading.Thread(target=increment_counter_v2)
        thread_2 = threading.Thread(target=increment_counter_v2)

        thread_1.start()
        thread_2.start()

        thread_1.join()
        thread_2.join()

        print(
            f"Run {run_number}: "
            f"expected={expected_total}, actual={counter}"
        )


def count_locally(increments: int) -> int:
    local_counter = 0
    for _ in range(increments):
        local_counter += 1
    return local_counter



def run_experiment_v3() -> None:
    from concurrent.futures import ThreadPoolExecutor
    expected_total = INCREMENTS_PER_THREAD * NUMBER_OF_WORKERS

    for run_number in range(1, NUMBER_OF_RUNS + 1):
        with ThreadPoolExecutor(max_workers=NUMBER_OF_WORKERS) as executor:
            worker_results = executor.map(count_locally,[INCREMENTS_PER_THREAD] * NUMBER_OF_WORKERS)
            total = sum(worker_results)
        print(f"Run {run_number}: "
            f"expected={expected_total}, actual={total}")


if __name__ == "__main__":
    run_experiment_v3()


# Example output from one execution:
#
# Run 1: expected=200000, actual=100000
# Run 2: expected=200000, actual=100100
# Run 3: expected=200000, actual=100000
# Run 4: expected=200000, actual=100200
# Run 5: expected=200000, actual=100100
#
# The actual values will vary between executions.