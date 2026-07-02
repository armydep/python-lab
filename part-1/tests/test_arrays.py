import importlib.util
import unittest
from array import array
from pathlib import Path


ARRAYS_PATH = Path(__file__).resolve().parents[1] / "11-collections" / "arrays.py"
spec = importlib.util.spec_from_file_location("arrays_exercise", ARRAYS_PATH)
arrays_exercise = importlib.util.module_from_spec(spec)
assert spec is not None
assert spec.loader is not None
spec.loader.exec_module(arrays_exercise)


#@unittest.skip("Disabled while focusing on 12-loops.")
class ArraysExerciseTest(unittest.TestCase):
    def test_make_scores_creates_float_array(self) -> None:
        scores = arrays_exercise.make_scores([97, 88.5, 91])

        self.assertIsInstance(scores, array)
        self.assertEqual(scores.typecode, "d")
        self.assertEqual(scores.tolist(), [97.0, 88.5, 91.0])

    def test_add_score_appends_to_same_array(self) -> None:
        scores = array("d", [80.0, 90.0])

        result = arrays_exercise.add_score(scores, 95)

        self.assertIs(result, scores)
        self.assertEqual(scores.tolist(), [80.0, 90.0, 95.0])

    def test_average_score(self) -> None:
        self.assertEqual(arrays_exercise.average_score(array("d", [80, 90, 100])), 90)
        self.assertEqual(arrays_exercise.average_score(array("d")), 0.0)

    def test_highest_score(self) -> None:
        self.assertEqual(arrays_exercise.highest_score(array("d", [82.5, 99, 91])), 99)
        self.assertIsNone(arrays_exercise.highest_score(array("d")))

    def test_first_even_numbers_creates_integer_array(self) -> None:
        numbers = arrays_exercise.first_even_numbers(5)

        self.assertIsInstance(numbers, array)
        self.assertEqual(numbers.typecode, "i")
        self.assertEqual(numbers.tolist(), [0, 2, 4, 6, 8])

    def test_to_list(self) -> None:
        self.assertEqual(arrays_exercise.to_list(array("i", [3, 6, 9])), [3, 6, 9])


if __name__ == "__main__":
    unittest.main()
