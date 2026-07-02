import unittest

from tests.helpers import load_challenge


inheritance = load_challenge("04-inheritance")

class InheritanceChallengeTest(unittest.TestCase):
    def test_person_greet(self) -> None:
        person = inheritance.Person("Christopher")

        self.assertEqual(person.greet(), "Hello, Christopher")

    def test_student_inherits_greet_and_adds_school_song(self) -> None:
        student = inheritance.Student("Christopher", "UVM")

        self.assertEqual(student.greet(), "Hello, Christopher")
        self.assertEqual(student.school_song(), "Ode to UVM")

    def test_describe_person(self) -> None:
        person = inheritance.Person("Susan")

        self.assertEqual(
            inheritance.describe(person),
            {"is_person": True, "is_student": False, "is_student_subclass": False},
        )

    def test_describe_student(self) -> None:
        student = inheritance.Student("Susan", "UVM")

        self.assertEqual(
            inheritance.describe(student),
            {"is_person": True, "is_student": True, "is_student_subclass": True},
        )


if __name__ == "__main__":
    unittest.main()
