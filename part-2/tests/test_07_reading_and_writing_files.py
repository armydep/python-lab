import unittest
from pathlib import Path
from tempfile import TemporaryDirectory

from tests.helpers import load_challenge


files = load_challenge("07-reading-and-writing-files")

class ReadingAndWritingFilesChallengeTest(unittest.TestCase):
    def test_read_first_line(self) -> None:
        with TemporaryDirectory() as tmp:
            path = Path(tmp) / "demo.txt"
            path.write_text("first\nsecond\n")

            self.assertEqual(files.read_first_line(path), "first")

    def test_read_all_lines(self) -> None:
        with TemporaryDirectory() as tmp:
            path = Path(tmp) / "demo.txt"
            path.write_text("first\nsecond\nthird")

            self.assertEqual(files.read_all_lines(path), ["first", "second", "third"])

    def test_write_lines_overwrites_existing_content(self) -> None:
        with TemporaryDirectory() as tmp:
            path = Path(tmp) / "output.txt"
            path.write_text("old content")

            files.write_lines(path, ["Susan", "Christopher"])

            self.assertEqual(path.read_text(), "Susan\nChristopher\n")

    def test_append_line_adds_to_end_of_file(self) -> None:
        with TemporaryDirectory() as tmp:
            path = Path(tmp) / "output.txt"
            path.write_text("first\n")

            files.append_line(path, "second")

            self.assertEqual(path.read_text(), "first\nsecond\n")


if __name__ == "__main__":
    unittest.main()
