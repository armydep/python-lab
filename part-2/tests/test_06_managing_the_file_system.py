import unittest
from pathlib import Path
from tempfile import TemporaryDirectory

from tests.helpers import load_challenge


file_system = load_challenge("06-managing-the-file-system")

class ManagingTheFileSystemChallengeTest(unittest.TestCase):
    def test_join_path(self) -> None:
        result = file_system.join_path("/tmp/demo", "new_file.txt")

        self.assertEqual(result, Path("/tmp/demo/new_file.txt"))

    def test_path_exists(self) -> None:
        with TemporaryDirectory() as tmp:
            existing = Path(tmp) / "here.txt"
            existing.write_text("hi")

            self.assertTrue(file_system.path_exists(existing))
            self.assertFalse(file_system.path_exists(Path(tmp) / "missing.txt"))

    def test_is_directory(self) -> None:
        with TemporaryDirectory() as tmp:
            file_path = Path(tmp) / "here.txt"
            file_path.write_text("hi")

            self.assertTrue(file_system.is_directory(tmp))
            self.assertFalse(file_system.is_directory(file_path))

    def test_file_name_parts(self) -> None:
        result = file_system.file_name_parts("/tmp/demo/notes/demo.txt")

        self.assertEqual(
            result,
            {"name": "demo.txt", "suffix": ".txt", "parent_name": "notes"},
        )

    def test_list_subdirectory_names(self) -> None:
        with TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "b_dir").mkdir()
            (root / "a_dir").mkdir()
            (root / "file.txt").write_text("hi")

            self.assertEqual(
                file_system.list_subdirectory_names(root), ["a_dir", "b_dir"]
            )


if __name__ == "__main__":
    unittest.main()
