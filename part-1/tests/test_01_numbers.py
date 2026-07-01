import importlib
import unittest


numbers = importlib.import_module("exercises.01_numbers")


#@unittest.skip("Disabled while focusing on 12-loops.")
class NumbersExerciseTest(unittest.TestCase):
    def test_add(self) -> None:
        self.assertEqual(numbers.add(2, 3), 5)
        self.assertEqual(numbers.add(-2, 5), 3)

    def test_square(self) -> None:
        self.assertEqual(numbers.square(4), 16)
        self.assertEqual(numbers.square(-3), 9)

    def test_is_even(self) -> None:
        self.assertTrue(numbers.is_even(10))
        self.assertFalse(numbers.is_even(7))

    def test_celsius_to_fahrenheit(self) -> None:
        self.assertEqual(numbers.celsius_to_fahrenheit(0), 32)
        self.assertEqual(numbers.celsius_to_fahrenheit(100), 212)


if __name__ == "__main__":
    unittest.main()
