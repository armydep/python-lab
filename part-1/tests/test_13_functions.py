import unittest

from tests.helpers import load_challenge


functions = load_challenge("13-functions")


#@unittest.skip("Disabled while focusing on 12-loops.")
class FunctionsChallengeTest(unittest.TestCase):
    def test_calculator_adds_numbers(self) -> None:
        self.assertEqual(functions.calculator(6, 4, "add"), 10.0)
        self.assertEqual(functions.calculator("6", "4", "ADD"), 10.0)

    def test_calculator_subtracts_numbers(self) -> None:
        self.assertEqual(functions.calculator(6, 4, "subtract"), 2.0)
        self.assertEqual(functions.calculator("6", "4", "SUBTRACT"), 2.0)

    def test_calculator_rejects_invalid_operation(self) -> None:
        self.assertEqual(
            functions.calculator(6, 4, "divide"),
            functions.INVALID_OPERATION_MESSAGE,
        )


if __name__ == "__main__":
    unittest.main()
