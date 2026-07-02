import unittest

from tests.helpers import load_challenge


mixins = load_challenge("05-mixins")

@unittest.skip("Disabled")
class MixinsChallengeTest(unittest.TestCase):
    def test_sql_database_combines_both_mixins(self) -> None:
        database = mixins.SqlDatabase()

        self.assertEqual(database.connect(), "Connecting to database on Some_Server")
        self.assertEqual(database.log(), "Log message from Sql Connection Demo")

    def test_run_framework_calls_connect_then_log(self) -> None:
        database = mixins.SqlDatabase()

        self.assertEqual(
            mixins.run_framework(database),
            [
                "Connecting to database on Some_Server",
                "Log message from Sql Connection Demo",
            ],
        )

    def test_run_framework_skips_missing_capabilities(self) -> None:
        logger = mixins.Loggable()
        logger.title = "Standalone"

        self.assertEqual(mixins.run_framework(logger), ["Log message from Standalone"])


if __name__ == "__main__":
    unittest.main()
