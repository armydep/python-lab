"""Exercise 15.4 — typed config from the environment.

A FROZEN dataclass Config: data_dir (Path), log_level (str, default
"WARNING", must be a valid level name), max_results (int, default 20,
must be > 0). Config.from_env(environ) takes a MAPPING (not os.environ
directly — testability!) reading TASKFORGE_DATA_DIR, TASKFORGE_LOG_LEVEL,
TASKFORGE_MAX_RESULTS. Missing required key or invalid value ->
ValueError with a message naming the variable.

Only the composition root ever touches os.environ; everything else
receives Config. No module-level reads.
"""

from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class Config:
    data_dir: Path
    log_level: str = "WARNING"
    max_results: int = 20

    @classmethod
    def from_env(cls, environ):
        raise NotImplementedError
