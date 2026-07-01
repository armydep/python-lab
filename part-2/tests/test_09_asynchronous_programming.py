import unittest
from timeit import default_timer

from tests.helpers import load_challenge


async_demo = load_challenge("09-asynchronous-programming")


class AsynchronousProgrammingChallengeTest(unittest.IsolatedAsyncioTestCase):
    async def test_load_data_returns_labelled_result(self) -> None:
        result = await async_demo.load_data(0.01)

        self.assertEqual(result, "data-after-0.01s")

    async def test_load_all_returns_results_in_order(self) -> None:
        results = await async_demo.load_all([0.02, 0.01])

        self.assertEqual(results, ["data-after-0.02s", "data-after-0.01s"])

    async def test_load_all_runs_concurrently(self) -> None:
        delays = [0.1, 0.1, 0.1]

        start = default_timer()
        await async_demo.load_all(delays)
        elapsed = default_timer() - start

        self.assertLess(elapsed, sum(delays))

    def test_run_all_wraps_load_all_synchronously(self) -> None:
        results = async_demo.run_all([0.01, 0.02])

        self.assertEqual(results, ["data-after-0.01s", "data-after-0.02s"])


if __name__ == "__main__":
    unittest.main()
