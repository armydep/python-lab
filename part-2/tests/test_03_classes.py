import unittest

from tests.helpers import load_challenge


classes = load_challenge("03-classes")


class ClassesChallengeTest(unittest.TestCase):
    def test_name_is_title_cased_on_construction(self) -> None:
        presenter = classes.Presenter("chris")

        self.assertEqual(presenter.name, "Chris")

    def test_name_setter_title_cases_new_value(self) -> None:
        presenter = classes.Presenter("Chris")

        presenter.name = "christopher"

        self.assertEqual(presenter.name, "Christopher")

    def test_greet_uses_current_name(self) -> None:
        presenter = classes.Presenter("Susan")

        self.assertEqual(presenter.greet(), "Hello, Susan")


if __name__ == "__main__":
    unittest.main()
