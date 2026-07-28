# TaskForge Phase 7 Design Diagrams

This document describes the target architecture for TaskForge Phase 7
(`v0.3a`). It is a design target, not the current implementation until the
Phase 7 refactor is completed.

## Layer diagram

Phase 7 introduces an object-oriented domain model and a repository boundary.
The CLI stops owning a raw `list[dict]` and instead talks to a repository
interface.

```mermaid
flowchart TD
    User[User]
    Main[taskforge.__main__]
    CLI[taskforge.cli]
    RepoABC[TaskRepository interface]
    MemoryRepo[MemoryRepository]
    JsonRepo[JsonRepository]
    CSV[csv_adapter]
    Model[models Task and Priority]
    Errors[errors]
    JSONFile[(tasks.json)]
    CSVFile[(user CSV file)]

    User --> Main
    Main --> CLI
    CLI --> RepoABC
    RepoABC -.implemented by.-> MemoryRepo
    RepoABC -.implemented by.-> JsonRepo
    MemoryRepo --> Model
    JsonRepo --> Model
    JsonRepo --> JSONFile
    CLI --> CSV
    CSV --> Model
    CSV --> CSVFile
    Model --> Errors
    MemoryRepo --> Errors
    JsonRepo --> Errors
    CSV --> Errors
    CLI --> Errors
```

Dependency rule:

```text
__main__ → cli → repository → models → errors
              └→ csv_adapter → models/errors
```

`core.py` should no longer be the primary domain layer. It may be removed or
kept only as a documented compatibility wrapper.

## Sequence diagram: CLI startup with `JsonRepository`

```mermaid
sequenceDiagram
    actor User
    participant Main as taskforge.__main__
    participant CLI as taskforge.cli
    participant Repo as JsonRepository
    participant Task as Task model
    participant Disk as tasks.json
    participant Errors as taskforge.errors

    User->>Main: taskforge / python -m taskforge
    Main->>Repo: JsonRepository(DEFAULT_DATA_PATH)
    Repo->>Disk: read UTF-8 JSON

    alt file exists and JSON is valid
        Disk-->>Repo: JSON task dictionaries
        loop each saved task
            Repo->>Task: Task.from_dict(data)
            Task-->>Repo: Task instance
        end
        Repo->>Repo: set next id after max existing id
    else file is missing
        Repo->>Repo: start with empty collection
    else corrupt JSON or expected I/O failure
        Repo->>Errors: raise StorageError
    end

    Main->>CLI: main(repository)
    CLI-->>User: prompt
```

## Sequence diagram: successful `add` command

```mermaid
sequenceDiagram
    actor User
    participant CLI as taskforge.cli
    participant Repo as TaskRepository
    participant Task as Task model
    participant Disk as tasks.json
    participant Errors as taskforge.errors

    User->>CLI: add Ship OOP refactor
    CLI->>Task: Task(id=None, title="Ship OOP refactor")

    alt title is valid
        Task-->>CLI: unsaved Task
    else title is blank
        Task->>Errors: raise InvalidTask
        Errors-->>CLI: TaskForgeError
        CLI-->>User: Error: <friendly message>
    end

    CLI->>Repo: add(task)

    alt title is unique
        Repo->>Repo: assign next id
        Repo->>Repo: store Task
        Repo-->>CLI: saved Task
        CLI-->>User: Added task <id>: Ship OOP refactor
        CLI->>Repo: save()
        Repo->>Task: task.to_dict()
        Task-->>Repo: JSON-safe dict
        Repo->>Disk: atomic write using temp file + os.replace
    else duplicate title
        Repo->>Errors: raise DuplicateTask
        Errors-->>CLI: TaskForgeError
        CLI-->>User: Error: <friendly message>
        Note over CLI,Repo: no save after failed mutation
    end
```

## Sequence diagram: `done` command

```mermaid
sequenceDiagram
    actor User
    participant CLI as taskforge.cli
    participant Repo as TaskRepository
    participant Task as Task model
    participant Errors as taskforge.errors

    User->>CLI: done 3
    CLI->>CLI: parse id as int
    CLI->>Repo: get(3)

    alt task exists
        Repo-->>CLI: Task
        CLI->>Task: complete()
        Task->>Task: done = True
        CLI-->>User: Completed task 3
        CLI->>Repo: save()
    else unknown id
        Repo->>Errors: raise TaskNotFound
        Errors-->>CLI: TaskForgeError
        CLI-->>User: Error: <friendly message>
        Note over CLI,Repo: no save after failed mutation
    end
```

## Sequence diagram: CSV export/import

```mermaid
sequenceDiagram
    actor User
    participant CLI as taskforge.cli
    participant Repo as TaskRepository
    participant CSV as csv_adapter
    participant Task as Task model
    participant CSVFile as CSV file

    User->>CLI: export csv tasks.csv
    CLI->>Repo: list()
    Repo-->>CLI: task list
    CLI->>CSV: export_tasks(path, tasks)
    loop each task
        CSV->>Task: task.to_dict()
        Task-->>CSV: JSON-safe task data
        CSV->>CSV: format CSV row
    end
    CSV->>CSVFile: write UTF-8 CSV
    CSV-->>CLI: None
    CLI-->>User: Exported N task(s)
    Note over CLI,Repo: export is read-only, so repository.save() is not called

    User->>CLI: import csv tasks.csv
    CLI->>CSV: import_tasks(path)
    CSV->>CSVFile: read UTF-8 CSV

    loop each CSV row
        alt row is valid
            CSV->>Task: Task.from_dict(row data)
            Task-->>CSV: Task instance
        else row is malformed
            CSV->>CSV: record line number
        end
    end

    CSV-->>CLI: valid tasks and malformed line numbers
    CLI->>Repo: replace_all(valid tasks)
    Repo->>Repo: reset next id after max imported id
    CLI-->>User: skipped line messages and import summary
    CLI->>Repo: save()
```

`replace_all()` is not listed in the minimal roadmap interface, but Phase 6
already uses replacement semantics for CSV import. Phase 7 should either add
this repository method explicitly or implement the same behavior through a
documented repository operation. Adding an explicit method is cleaner because
the CLI should not mutate repository internals.

## Class/module diagram

```mermaid
classDiagram
    class Main {
        module __main__
        +main()
    }

    class CLI {
        module cli
        +DEFAULT_DATA_PATH
        +COMMANDS
        +main(repository=None)
        +add_command(repo, arguments)
        +done_command(repo, arguments)
        +list_command(repo, arguments)
        +stats_command(repo, arguments)
        +export_command(repo, arguments)
        +import_command(repo, arguments)
        +version_command(repo, arguments)
        +quit_command(repo, arguments)
    }

    class Priority {
        IntEnum
        LOW
        MEDIUM
        HIGH
    }

    class Task {
        dataclass
        +id
        +title
        +done
        +tags
        +priority
        +created_at
        +__post_init__()
        +complete()
        +matches(query)
        +to_dict()
        +from_dict(data)
    }

    class TaskRepository {
        ABC
        +add(task) Task
        +get(task_id) Task
        +remove(task_id)
        +list() list
        +save()
    }

    class MemoryRepository {
        -tasks
        -next_id
        +add(task) Task
        +get(task_id) Task
        +remove(task_id)
        +list() list
        +save()
        +replace_all(tasks)
    }

    class JsonRepository {
        -path
        -tasks
        -next_id
        +add(task) Task
        +get(task_id) Task
        +remove(task_id)
        +list() list
        +save()
        +replace_all(tasks)
        -load()
        -atomic_write(text)
    }

    class CSVAdapter {
        module csv_adapter
        +FIELDNAMES
        +export_tasks(path, tasks)
        +import_tasks(path)
        -format_task(task)
        -parse_task(row)
    }

    class Errors {
        module errors
        +TaskForgeError
        +InvalidTask
        +DuplicateTask
        +TaskNotFound
        +StorageError
    }

    Main --> CLI : creates/defaults repository
    CLI --> TaskRepository : uses interface
    CLI --> Task : constructs new tasks
    CLI --> CSVAdapter : CSV import/export
    TaskRepository <|.. MemoryRepository
    TaskRepository <|.. JsonRepository
    MemoryRepository --> Task : stores
    JsonRepository --> Task : stores and serializes
    Task --> Priority : uses
    Task --> Errors : raises InvalidTask
    MemoryRepository --> Errors : duplicate/not found
    JsonRepository --> Errors : duplicate/not found/storage
    CSVAdapter --> Task : parses/formats
    CSVAdapter --> Errors : storage/header failures
```

## Responsibilities by layer

| Layer | Module | Responsibility |
|---|---|---|
| Entry point | `__main__.py` | Start the app and select the default repository implementation. |
| Interface | `cli.py` | Parse commands, print output, catch expected `TaskForgeError` failures. |
| Repository | `repository.py` | Own task collections, assign IDs, enforce collection-level rules, persist when needed. |
| Domain model | `models.py` | Represent one task, protect task invariants, serialize/deserialize task data. |
| Interchange | `csv_adapter.py` | Convert between `Task` objects and stable CSV rows. |
| Error vocabulary | `errors.py` | Define expected failures shared across layers. |

## Main design decisions

- `Task` protects per-task invariants: valid title, valid priority, tag default
  isolation, completion behavior.
- Repository classes protect collection invariants: unique titles, known IDs,
  ID assignment.
- `JsonRepository` owns JSON persistence and atomic writes. The CLI should not
  know JSON details.
- CSV remains an adapter, not the canonical persistence store.
- CSV import should replace the repository contents using an explicit
  repository operation such as `replace_all(tasks)`.
- `TaskRepository` enables dependency inversion: tests can use
  `MemoryRepository`, while the real CLI uses `JsonRepository`.
