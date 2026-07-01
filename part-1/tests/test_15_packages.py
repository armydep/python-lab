import unittest

from tests.helpers import load_challenge


packages = load_challenge("15-packages")


#@unittest.skip("Disabled while focusing on 12-loops.")
class PackagesChallengeTest(unittest.TestCase):
    def test_load_display_function_imports_helper_function(self) -> None:
        display = packages.load_display_function()

        self.assertTrue(callable(display))
        self.assertEqual(display.__name__, "display")
        self.assertEqual(display("Hello"), "Hello")

    def test_display_message_uses_helper(self) -> None:
        self.assertEqual(packages.display_message("Not a warning"), "Not a warning")

    def test_display_warning_uses_helper_warning_mode(self) -> None:
        self.assertEqual(packages.display_warning("Check this"), "Warning!!\nCheck this")


if __name__ == "__main__":
    unittest.main()
