import unittest

from tests.helpers import load_challenge


parameters = load_challenge("14-function-parameters")


#@unittest.skip("Disabled while focusing on 12-loops.")
class FunctionParametersChallengeTest(unittest.TestCase):
    def test_get_initial_uses_default_uppercase(self) -> None:
        self.assertEqual(parameters.get_initial("christopher"), "C")
        self.assertEqual(parameters.get_initial("Susan"), "S")

    def test_get_initial_can_keep_original_case(self) -> None:
        self.assertEqual(parameters.get_initial("christopher", False), "c")
        self.assertEqual(parameters.get_initial("Susan", False), "S")

    def test_get_initials_uses_multiple_parameters(self) -> None:
        self.assertEqual(parameters.get_initials("christopher", "harrison"), "CH")
        self.assertEqual(parameters.get_initials("Ada", "Lovelace", separator="."), "A.L")

    def test_get_initials_accepts_named_arguments_in_any_order(self) -> None:
        self.assertEqual(
            parameters.get_initials(
                separator="-",
                last_name="harrison",
                first_name="christopher",
            ),
            "C-H",
        )

    def test_get_initials_can_keep_original_case(self) -> None:
        self.assertEqual(
            parameters.get_initials("christopher", "harrison", force_uppercase=False),
            "ch",
        )

    def test_format_user_label_uses_default_role(self) -> None:
        self.assertEqual(
            parameters.format_user_label("Ada", "Lovelace"),
            "Ada Lovelace - Student",
        )

    def test_format_user_label_accepts_custom_role(self) -> None:
        self.assertEqual(
            parameters.format_user_label(
                first_name="Grace",
                last_name="Hopper",
                role="Instructor",
            ),
            "Grace Hopper - Instructor",
        )


if __name__ == "__main__":
    unittest.main()
