"""Black-box contract for the Phase 5 hostile-input script."""

from pathlib import Path
import subprocess
import sys


ABUSE_SCRIPT = (
    Path(__file__).parents[1] / "src" / "taskforge" / "abuse.py"
)


def test_abuse_script_exercises_expected_domain_failures() -> None:
    assert ABUSE_SCRIPT.exists(), "create src/taskforge/abuse.py"

    result = subprocess.run(
        [sys.executable, str(ABUSE_SCRIPT)],
        text=True,
        capture_output=True,
        check=False,
    )

    assert result.returncode == 0, result.stderr
    assert "Traceback" not in result.stdout
    assert "Traceback" not in result.stderr
    assert "UNEXPECTED SUCCESS" not in result.stdout
    assert result.stdout.count("CASE ") >= 10
    assert "InvalidTask:" in result.stdout
    assert "DuplicateTask:" in result.stdout
    assert "TaskNotFound:" in result.stdout
    assert "VALID AFTER FAILURES: OK" in result.stdout
