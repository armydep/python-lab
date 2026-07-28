# TaskForge Architecture Diagrams

This document captures the TaskForge architecture immediately before Phase 6
and after the Phase 6 persistence/CSV changes.

## Before Phase 6: Phase 5 architecture

Phase 5 had an in-memory REPL. The CLI owned user interaction and friendly
error reporting. The core owned task rules and raised typed domain errors.
There was no durable storage boundary.

Dependency direction:

```text
__main__ → cli → core → errors
```

### Sequence diagram: add a task before Phase 6

```mermaid
sequenceDiagram
    actor User
    participant Main as taskforge.__main__
    participant CLI as taskforge.cli
    participant Core as taskforge.core
    participant Errors as taskforge.errors

    User->>Main: python -m taskforge
    Main->>CLI: main()
    CLI->>CLI: tasks = []
    CLI-->>User: prompt

    User->>CLI: add Ship API
    CLI->>CLI: parse command and arguments
    CLI->>Core: add_task(tasks, "Ship API")

    alt valid task
        Core->>Core: validate title, priority, duplicate title
        Core->>Core: append task with set tags
        Core-->>CLI: None
        CLI-->>User: Added task <id>: Ship API
    else expected domain failure
        Core->>Errors: raise InvalidTask or DuplicateTask
        Errors-->>CLI: TaskForgeError
        CLI-->>User: Error: <friendly message>
    end

    CLI-->>User: next prompt
```

### Class/module diagram before Phase 6

```mermaid
classDiagram
    class Main {
        <<module: __main__.py>>
        +main()
    }

    class CLI {
        <<module: cli.py>>
        +COMMANDS
        +main()
        +add_command(tasks, arguments)
        +done_command(tasks, arguments)
        +list_command(tasks, arguments)
        +stats_command(tasks, arguments)
        +version_command(tasks, arguments)
        +quit_command(tasks, arguments)
    }

    class Core {
        <<module: core.py>>
        +Task
        +add_task(tasks, title, tags=None, priority=1)
        +complete_task(tasks, task_id)
        +remove_task(tasks, task_id)
        +find_by_tag(tasks, tag)
        +pending_sorted_by_priority(tasks)
        +stats(tasks)
        +rename_tag(tasks, old, new)
    }

    class Errors {
        <<module: errors.py>>
        +TaskForgeError
        +InvalidTask
        +DuplicateTask
        +TaskNotFound
    }

    Main --> CLI : starts REPL
    CLI --> Core : calls domain operations
    Core --> Errors : raises expected failures
    CLI --> Errors : catches TaskForgeError
```

## After Phase 6: durable JSON persistence and CSV interchange

Phase 6 added adapters around the in-memory domain model. The core remains
free of filesystem, JSON, CSV, input, and printing concerns. The CLI now
decides when to load and save. Storage and CSV adapters own serialization and
file behavior.

Dependency direction:

```text
__main__ → cli → core
              ├→ storage → errors
              ├→ csv_adapter → errors
              └→ errors
```

### Sequence diagram: REPL startup and successful mutation after Phase 6

```mermaid
sequenceDiagram
    actor User
    participant Main as taskforge.__main__
    participant CLI as taskforge.cli
    participant Storage as taskforge.storage
    participant Core as taskforge.core
    participant Errors as taskforge.errors

    User->>Main: taskforge / python -m taskforge
    Main->>CLI: main(DEFAULT_DATA_PATH)
    CLI->>Storage: load_tasks(~/.taskforge/tasks.json)

    alt file exists and JSON is valid
        Storage->>Storage: read UTF-8 JSON
        Storage->>Storage: convert tag lists to sets
        Storage-->>CLI: list[Task]
    else file is missing
        Storage-->>CLI: []
    else corrupt JSON or expected I/O failure
        Storage->>Errors: raise StorageError
        Errors-->>CLI: TaskForgeError
        CLI-->>User: Error: <storage message>
        CLI->>CLI: continue with empty list
    end

    CLI->>Core: sync_next_task_id(tasks)
    CLI-->>User: prompt

    User->>CLI: add Ship API
    CLI->>Core: add_task(tasks, "Ship API")

    alt valid mutation
        Core->>Core: validate and append task
        Core-->>CLI: None
        CLI-->>User: Added task <id>: Ship API
        CLI->>Storage: save_tasks(DEFAULT_DATA_PATH, tasks)
        Storage->>Storage: convert tag sets to sorted lists
        Storage->>Storage: write temp file in target directory
        Storage->>Storage: flush, fsync, close
        Storage->>Storage: os.replace(temp, target)
        Storage-->>CLI: None
    else expected domain failure
        Core->>Errors: raise InvalidTask or DuplicateTask
        Errors-->>CLI: TaskForgeError
        CLI-->>User: Error: <friendly message>
        Note over CLI,Storage: no save after failed mutation
    end
```

### Sequence diagram: CSV export/import after Phase 6

```mermaid
sequenceDiagram
    actor User
    participant CLI as taskforge.cli
    participant CSV as taskforge.csv_adapter
    participant Storage as taskforge.storage
    participant Core as taskforge.core
    participant Errors as taskforge.errors

    User->>CLI: export csv tasks.csv
    CLI->>CSV: export_tasks(Path("tasks.csv"), tasks)
    CSV->>CSV: write UTF-8 CSV with newline=""
    CSV->>CSV: encode tags as JSON list text
    CSV-->>CLI: None
    CLI-->>User: Exported N task(s)
    Note over CLI,Storage: export is read-only for JSON store, so no save

    User->>CLI: import csv tasks.csv
    CLI->>CSV: import_tasks(Path("tasks.csv"))
    CSV->>CSV: read UTF-8 CSV with newline=""
    CSV->>CSV: parse id, title, done, priority, tags

    alt row is valid
        CSV->>CSV: append task with tags as set
    else row is malformed
        CSV->>CSV: record CSV line number
    end

    CSV-->>CLI: imported tasks and malformed line numbers
    CLI->>CLI: replace in-memory task list
    CLI->>Core: sync_next_task_id(tasks)
    CLI-->>User: skipped line messages, import summary
    CLI->>Storage: save_tasks(DEFAULT_DATA_PATH, tasks)

    alt storage save succeeds
        Storage-->>CLI: None
    else expected persistence failure
        Storage->>Errors: raise StorageError
        Errors-->>CLI: TaskForgeError
        CLI-->>User: Error: <storage message>
    end
```

### Class/module diagram after Phase 6

```mermaid
classDiagram
    class Main {
        <<module: __main__.py>>
        +main()
    }

    class CLI {
        <<module: cli.py>>
        +DEFAULT_DATA_PATH
        +COMMANDS
        +MUTATING_COMMANDS
        +main(storage_path=DEFAULT_DATA_PATH)
        +add_command(tasks, arguments)
        +done_command(tasks, arguments)
        +list_command(tasks, arguments)
        +stats_command(tasks, arguments)
        +export_command(tasks, arguments)
        +import_command(tasks, arguments)
        +version_command(tasks, arguments)
        +quit_command(tasks, arguments)
    }

    class Core {
        <<module: core.py>>
        +Task
        +add_task(tasks, title, tags=None, priority=1)
        +complete_task(tasks, task_id)
        +remove_task(tasks, task_id)
        +find_by_tag(tasks, tag)
        +pending_sorted_by_priority(tasks)
        +stats(tasks)
        +rename_tag(tasks, old, new)
        +sync_next_task_id(tasks)
    }

    class Storage {
        <<module: storage.py>>
        +load_tasks(path)
        +save_tasks(path, tasks)
        -_task_to_jsonable(task)
        -_task_from_jsonable(task)
    }

    class CSV {
        <<module: csv_adapter.py>>
        +FIELDNAMES
        +export_tasks(path, tasks)
        +import_tasks(path)
        -_format_task(task)
        -_parse_task(row)
    }

    class Errors {
        <<module: errors.py>>
        +TaskForgeError
        +InvalidTask
        +DuplicateTask
        +TaskNotFound
        +StorageError
    }

    Main --> CLI : starts REPL
    CLI --> Core : domain operations
    CLI --> Storage : load/save JSON store
    CLI --> CSV : export/import CSV files
    CLI --> Errors : catches TaskForgeError
    Core --> Errors : raises domain failures
    Storage --> Errors : raises StorageError
    CSV --> Errors : raises StorageError for expected file/header failures
```

## Key architectural change in Phase 6

The important change is the new adapter boundary:

- `core.py` still only manages task rules and in-memory task dictionaries.
- `storage.py` owns durable JSON persistence and atomic writes.
- `csv_adapter.py` owns CSV-specific formatting/parsing.
- `cli.py` coordinates user commands, load/save timing, and expected-error
  reporting.
- `errors.py` remains the shared expected-failure vocabulary, extended with
  `StorageError`.
