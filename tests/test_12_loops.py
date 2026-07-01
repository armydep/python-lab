import unittest

from tests.helpers import load_challenge


loops = load_challenge("12-loops")


class LoopsChallengeTest(unittest.TestCase):
    def test_collect_names_returns_new_list_in_order(self) -> None:
        names = ["Christopher", "Susan", "Ada"]

        result = loops.collect_names(names)

        self.assertEqual(result, ["Christopher", "Susan", "Ada"])
        self.assertIsNot(result, names)

    def test_indexes_for_items(self) -> None:
        self.assertEqual(loops.indexes_for_items(["a", "b", "c"]), [0, 1, 2])
        self.assertEqual(loops.indexes_for_items([]), [])

    def test_first_even_numbers(self) -> None:
        self.assertEqual(loops.first_even_numbers(5), [0, 2, 4, 6, 8])
        self.assertEqual(loops.first_even_numbers(0), [])

    def test_total_numbers(self) -> None:
        self.assertEqual(loops.total_numbers([1, 2, 3]), 6)
        self.assertEqual(loops.total_numbers([1.5, 2.5]), 4.0)
        self.assertEqual(loops.total_numbers([]), 0)


if __name__ == "__main__":
    unittest.main()
