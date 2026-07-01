import json
import unittest

from tests.helpers import load_challenge


json_challenge = load_challenge("17-json")


@unittest.skip("Disabled while focusing on 12-loops.")
class JsonChallengeTest(unittest.TestCase):
    def test_create_person(self) -> None:
        self.assertEqual(
            json_challenge.create_person("Christopher", "Harrison", "Seattle"),
            {"first": "Christopher", "last": "Harrison", "City": "Seattle"},
        )

    def test_add_languages_updates_same_dictionary(self) -> None:
        person = {"first": "Christopher", "last": "Harrison", "City": "Seattle"}

        result = json_challenge.add_languages(person, ["CSharp", "Python"])

        self.assertIs(result, person)
        self.assertEqual(person["languages"], ["CSharp", "Python"])

    def test_person_to_json(self) -> None:
        person_json = json_challenge.person_to_json(
            {"first": "Christopher", "last": "Harrison", "City": "Seattle"}
        )

        self.assertEqual(
            json.loads(person_json),
            {"first": "Christopher", "last": "Harrison", "City": "Seattle"},
        )

    def test_staff_to_json(self) -> None:
        staff_json = json_challenge.staff_to_json(
            "Program Manager",
            {"first": "Christopher", "last": "Harrison"},
        )

        self.assertEqual(
            json.loads(staff_json),
            {"Program Manager": {"first": "Christopher", "last": "Harrison"}},
        )

    def test_city_from_json(self) -> None:
        person_json = '{"first": "Christopher", "last": "Harrison", "City": "Seattle"}'

        self.assertEqual(json_challenge.city_from_json(person_json), "Seattle")


if __name__ == "__main__":
    unittest.main()
