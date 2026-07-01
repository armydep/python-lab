import unittest

from tests.helpers import load_challenge


lambdas = load_challenge("02-lambdas")


class LambdasChallengeTest(unittest.TestCase):
    def test_sort_by_field_returns_new_list_sorted_by_field(self) -> None:
        presenters = [
            {"name": "Susan", "age": 50},
            {"name": "Christopher", "age": 47},
        ]

        result = lambdas.sort_by_field(presenters, "name")

        self.assertEqual([p["name"] for p in result], ["Christopher", "Susan"])
        self.assertIsNot(result, presenters)
        self.assertEqual(presenters[0]["name"], "Susan")

    def test_sort_by_field_sorts_by_numeric_field(self) -> None:
        presenters = [
            {"name": "Susan", "age": 50},
            {"name": "Christopher", "age": 47},
        ]

        result = lambdas.sort_by_field(presenters, "age")

        self.assertEqual([p["age"] for p in result], [47, 50])

    def test_sort_by_name_length(self) -> None:
        result = lambdas.sort_by_name_length(["Christopher", "Susan", "Ada"])

        self.assertEqual(result, ["Ada", "Susan", "Christopher"])

    def test_square_all(self) -> None:
        self.assertEqual(lambdas.square_all([1, 2, 3]), [1, 4, 9])
        self.assertEqual(lambdas.square_all([]), [])

    def test_keep_even(self) -> None:
        self.assertEqual(lambdas.keep_even([1, 2, 3, 4, 5, 6]), [2, 4, 6])
        self.assertEqual(lambdas.keep_even([]), [])


if __name__ == "__main__":
    unittest.main()
