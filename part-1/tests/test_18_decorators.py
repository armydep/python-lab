import unittest

from tests.helpers import load_challenge


decorators = load_challenge("18-decorators")


#@unittest.skip("Disabled while focusing on 12-loops.")
class DecoratorsChallengeTest(unittest.TestCase):
    def test_uppercase_result_decorator(self) -> None:
        @decorators.uppercase_result
        def greeting():
            return "hello"

        self.assertEqual(greeting(), "HELLO")
        self.assertEqual(greeting.__name__, "greeting")

    def test_uppercase_result_leaves_non_strings_alone(self) -> None:
        @decorators.uppercase_result
        def answer():
            return 42

        self.assertEqual(answer(), 42)

    def test_prefix_result_decorator_factory(self) -> None:
        @decorators.prefix_result("Result: ")
        def status():
            return "ready"

        self.assertEqual(status(), "Result: ready")
        self.assertEqual(status.__name__, "status")

    def test_repeat_decorator_factory(self) -> None:
        calls = []

        @decorators.repeat(3)
        def next_value():
            calls.append(len(calls) + 1)
            return calls[-1]

        self.assertEqual(next_value(), [1, 2, 3])
        self.assertEqual(next_value.__name__, "next_value")


if __name__ == "__main__":
    unittest.main()
