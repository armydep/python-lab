import unittest
from pathlib import Path
from tempfile import TemporaryDirectory

from tests.helpers import load_challenge


resources = load_challenge("08-managing-external-resources")


class ManagingExternalResourcesChallengeTest(unittest.TestCase):
    def test_write_with_context_manager_overwrites_existing_content(self) -> None:
        with TemporaryDirectory() as tmp:
            path = Path(tmp) / "output.txt"
            path.write_text("old")

            resources.write_with_context_manager(path, "Lorem ipsum dolar")

            self.assertEqual(path.read_text(), "Lorem ipsum dolar")

    def test_copy_with_context_manager(self) -> None:
        with TemporaryDirectory() as tmp:
            source = Path(tmp) / "source.txt"
            destination = Path(tmp) / "destination.txt"
            source.write_text("hello world")

            resources.copy_with_context_manager(source, destination)

            self.assertEqual(destination.read_text(), "hello world")

    def test_safe_read_returns_default_when_missing(self) -> None:
        with TemporaryDirectory() as tmp:
            missing = Path(tmp) / "missing.txt"

            self.assertEqual(resources.safe_read(missing, default="n/a"), "n/a")

    def test_safe_read_returns_contents_when_present(self) -> None:
        with TemporaryDirectory() as tmp:
            path = Path(tmp) / "present.txt"
            path.write_text("here")

            self.assertEqual(resources.safe_read(path), "here")


if __name__ == "__main__":
    unittest.main()
