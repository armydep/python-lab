# TaskForge Phase 4 Assignment

## Goal

Turn the Phase 3 in-memory TaskForge application into an installable Python
package with a standard `src` layout, a deliberate public API, and two
equivalent command-line entry points.

Phase 4 changes how TaskForge is organized, imported, installed, and
launched. It should not change the behavior of the Phase 3 core operations.

## Required project layout

```text
taskforge/
├── pyproject.toml
├── src/
│   └── taskforge/
│       ├── __init__.py
│       ├── __main__.py
│       ├── core.py
│       └── cli.py
└── tests/
```

Responsibilities:

- `pyproject.toml` contains build metadata and the console-script entry point.
- `src/taskforge/__init__.py` defines the public package API and version.
- `src/taskforge/__main__.py` supports `python -m taskforge`.
- `src/taskforge/core.py` contains task operations and no input or printing.
- `src/taskforge/cli.py` owns command parsing, the REPL, and all output.
- `tests/` is reserved for the TaskForge test suite added in Phase 11.

The dependency direction must remain:

```text
__main__ → cli → core
```

`core.py` must not import `cli.py`.

## Packaging setup

Install the project into the active virtual environment in editable mode:

```bash
python -m pip install -e ./taskforge
```

Editable installation points Python at `taskforge/src`, so source changes are
available immediately without reinstalling.

After installation, both commands must launch the same REPL:

```bash
taskforge
python -m taskforge
```

They must work from a directory outside the repository.

## Current status

- The Phase 4 small exercises pass: `4 passed`.
- The Phase 3 core implementation has moved to `src/taskforge/core.py`.
- The REPL has moved to `src/taskforge/cli.py`.
- `src/taskforge/__main__.py` launches the CLI.
- `pyproject.toml` defines the package and `taskforge` console command.
- The package is installed in editable mode.
- `taskforge` and `python -m taskforge` have been verified from `/tmp`.

## Remaining task 1: define the public API

Update `src/taskforge/__init__.py`.

Expose `__version__` and the public core operations so callers can use:

```python
import taskforge

taskforge.add_task(...)
taskforge.complete_task(...)
```

The v0.1 public operations are:

- `add_task`
- `complete_task`
- `remove_task`
- `find_by_tag`
- `pending_sorted_by_priority`
- `stats`
- `rename_tag`

Do not use `from ... import *`. The exports should be explicit so
`__init__.py` clearly documents the supported public surface.

## Remaining task 2: add the version command

Update `src/taskforge/cli.py`.

The REPL must support:

```text
taskforge> version
0.1.0
```

Requirements:

- Add a command handler for `version`.
- Register it in the existing command-dispatch dictionary.
- Reject unexpected arguments consistently with the other commands.
- Read the version from `taskforge.__version__`.
- Do not duplicate the version string inside the CLI.

## Verification

Verify the public package API:

```bash
python -c "import taskforge; print(taskforge.__version__)"
python -c "import taskforge; print(taskforge.add_task)"
```

Verify both entry points from outside the repository:

```bash
cd /tmp
taskforge
```

Inside the REPL:

```text
taskforge> version
0.1.0
taskforge> quit
```

Then verify:

```bash
cd /tmp
python -m taskforge
```

## Completion criteria

Phase 4 TaskForge is complete when:

- The package uses the required `src` layout.
- Editable installation succeeds.
- Importing `taskforge` produces no output and does not start the REPL.
- The public core operations are available through `taskforge`.
- `core.py` contains no CLI imports or printing.
- `taskforge` launches the REPL from any directory.
- `python -m taskforge` launches the same REPL from any directory.
- The `version` command prints `taskforge.__version__`.
- No import relies accidentally on the current working directory.
