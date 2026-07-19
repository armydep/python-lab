# Python Learning Roadmap — Beginner to Senior Backend Engineer

A hands-on, project-driven roadmap. Every phase produces working code, and most
phases contribute to one evolving project — **TaskForge**, a task-tracking
application that starts as a tiny script and ends as a well-architected,
tested, typed, concurrent backend-style application. TaskForge is deliberately
shaped like a web backend so that when you move to FastAPI, you will wrap an
HTTP layer around code you already understand deeply.

Primary references:

- Python Tutorial: https://docs.python.org/3/tutorial/index.html
- Python Standard Library: https://docs.python.org/3/library/index.html
- Language Reference (used sparingly, for precise semantics): https://docs.python.org/3/reference/index.html

---

## 1. Recommended Learning Approach

### Balance of theory and practice — the 20/80 rule

For each phase: read just enough to attempt the exercises (roughly 20% of your
time), then spend the remaining 80% writing code. Read the recommended docs
section *once* before coding, then return to it *while* coding when you hit a
question. Theory you read before you needed it evaporates; theory you look up
to unblock working code sticks.

Concretely, a phase loop looks like:

1. Skim the recommended documentation sections (30–60 min).
2. Do the small exercises without looking at solutions.
3. Do the larger assignment.
4. Take the self-assessment quiz *from memory*.
5. Revisit docs for anything you got wrong, and fix your code accordingly.

### How to use official documentation effectively

- **Tutorial first, library reference second, language reference last.** The
  tutorial teaches concepts; the library reference is a lookup tool, not a
  book — never read it cover to cover.
- **Learn to read function signatures.** `dict.get(key, default=None)`,
  `sorted(iterable, /, *, key=None, reverse=False)` — by the end of Phase 2
  you should be able to read any stdlib signature, including `/` and `*`
  markers.
- **Use the REPL as your doc companion.** `help(str.split)`, `dir(obj)`, and
  quick experiments in `python -i` answer most questions faster than search.
- **Bookmark, don't memorize.** Keep a personal `NOTES.md` in this repo with
  links to the doc sections you keep returning to. That file becomes your map
  of the stdlib.

### How exercise difficulty should ramp

Each phase moves through three levels:

1. **Mechanics** — small, single-concept drills ("write a function that…").
2. **Combination** — exercises that force the new concept to interact with
   previous ones (a generator that reads files, a decorator that uses closures).
3. **Application** — the phase assignment, where the concept is used inside
   TaskForge under realistic constraints (edge cases, bad input, growth).

If a "mechanics" exercise takes you more than ~20 minutes, re-read the docs.
If the "application" assignment feels easy, you're ready to move on early.

### When to refactor earlier assignments

Refactoring old code with new knowledge is the single highest-value habit in
this roadmap. Do it at these scheduled points (they're marked in the phases):

- After **Phase 7 (OOP)**: rewrite TaskForge's dict-based records as classes.
- After **Phase 9 (Decorators/Context managers)**: replace repeated
  open/close and logging boilerplate.
- After **Phase 10 (Typing)**: annotate the entire codebase, fix what the type
  checker reveals.
- After **Phase 11 (Testing)**: write tests for existing code — you will find
  bugs, and you will discover which parts of your design are hard to test
  (that pain is a design lesson, not a testing lesson).

Rule of thumb: refactor when a new tool removes duplication or clarifies
intent, not merely because the new tool exists.

### How to verify you understand a topic

Use these checks, in increasing order of rigor:

1. **Predict-then-run**: before running any snippet, write down what it will
   print. Wrong predictions are the highest-signal learning events you have.
2. **Explain out loud** (or in `NOTES.md`) in two sentences without jargon.
3. **Rebuild from a blank file**: re-implement the key exercise the next day
   without looking at your previous solution.
4. **Break it on purpose**: introduce a bug (mutate a shared default, remove a
   `close()`, swap `is` for `==`) and predict the failure mode before running.

### How to avoid copying solutions without learning

- Type every line yourself; never paste.
- When stuck, get *hints* not solutions: look up the one function you're
  missing, not a full answer.
- If you do read a solution, close it, wait an hour, and re-implement from
  memory. If you can't, you didn't learn it yet.
- Keep a "struggle log": one line per exercise about where you got stuck.
  Recurring entries tell you what to re-study.
- Use AI assistants (including me) as a *reviewer* of code you wrote, not a
  generator of code you read.

### How this roadmap prepares you for FastAPI

FastAPI is a thin, elegant layer over exactly the Python this roadmap drills:

| FastAPI concept | Prepared by |
|---|---|
| Path/query/body parameters, `Depends()` | Phase 2 (parameter handling, keyword-only args) |
| Pydantic models, response models | Phases 7 & 10 (classes, dataclasses, type annotations) |
| `async def` endpoints, background tasks | Phase 13 (asyncio) |
| Middleware, dependency injection | Phases 8–9 (generators, decorators, context managers) |
| Routers, project layout | Phase 4 (modules and packages) |
| Error handlers, HTTPException | Phase 5 (exception design) |
| Testing with `TestClient` | Phase 11 (pytest, fixtures) |
| Settings, logging, lifespan events | Phases 9 & 12 (context managers, logging) |
| Service/repository layering | Phases 14–15 (architecture) |

By the capstone, TaskForge will have a service layer with typed functions,
a storage backend behind an interface, structured logging, and tests — adding
FastAPI to it will take days, not weeks.

---

## 2. Roadmap Overview

| # | Phase | Core topics | TaskForge milestone | Difficulty |
|---|-------|-------------|---------------------|------------|
| 1 | Foundations | Environment, variables, expressions, basic types, control flow | — (standalone drills) | ★☆☆☆☆ |
| 2 | Functions | Definitions, parameters, `*args/**kwargs`, scope, closures, lambdas | — (standalone drills) | ★★☆☆☆ |
| 3 | Core data structures | list, tuple, dict, set, strings, comprehensions, sorting | TaskForge v0.1: in-memory task store | ★★☆☆☆ |
| 4 | Modules & packages | imports, `__init__.py`, `__main__`, venvs, project layout | v0.1 → installable package with CLI | ★★☆☆☆ |
| 5 | Exceptions & error handling | try/except/else/finally, exception design, EAFP | v0.2a: robust input handling, custom errors | ★★★☆☆ |
| 6 | Files & data handling | pathlib, encodings, JSON, CSV, atomic writes | v0.2: JSON persistence, CSV import/export | ★★★☆☆ |
| 7 | Classes & OOP | classes, dunders, dataclasses, composition vs inheritance, protocols | v0.3a: domain model + repository (refactor) | ★★★★☆ |
| 8 | Iterators & generators | iteration protocol, `yield`, generator pipelines, `itertools` | v0.3b: streaming reports and filters | ★★★★☆ |
| 9 | Decorators & context managers | closures applied, `functools.wraps`, `with`, `contextlib` | v0.3: timing/logging decorators, storage as context manager (refactor) | ★★★★☆ |
| 10 | Type annotations | typing basics, generics, `Protocol`, mypy/pyright | v0.4a: fully typed codebase (refactor) | ★★★☆☆ |
| 11 | Testing | pytest, fixtures, parametrize, mocking, coverage | v0.4b: test suite ≥85% coverage (refactor) | ★★★★☆ |
| 12 | Debugging, logging & stdlib essentials | pdb, `logging`, `argparse`, `datetime`, `collections`, `re` | v0.4: real CLI, structured logs | ★★★☆☆ |
| 13 | Concurrency | threading, multiprocessing, GIL, `asyncio` | v0.5: concurrent import, async sync-client | ★★★★★ |
| 14 | Performance & memory | profiling, big-O in practice, `__slots__`, caching | v0.9: profiled and optimized | ★★★★★ |
| 15 | Pythonic design & architecture | SOLID in Python, layering, DI, packaging for reuse | v1.0 capstone | ★★★★★ |

Stages: Phases 1–4 = **Beginner**, 5–9 = **Intermediate**, 10–13 =
**Advanced**, 14–15 = **Senior**. No calendar schedule — advance when you meet
each phase's completion criteria, not when a week has passed.

Suggested repo layout as you progress:

```
python-lab/
├── PYTHON_ROADMAP.md
├── NOTES.md                  # your running notes & struggle log
├── exercises/
│   ├── phase01/ ... phase15/ # small exercises, one file each
└── taskforge/                # the evolving project (Phase 3 onward)
```

---

## 3. Detailed Phases

---

### Phase 1 — Foundations: Environment, Types, Control Flow

**Difficulty:** ★☆☆☆☆ (Beginner)

#### Learning objectives
- Set up a reproducible Python environment (Python ≥3.12, venv, a formatter).
- Fluently use numbers, strings, booleans, and `None`.
- Write any control-flow shape: branching, loops, early exit.
- Understand *names vs objects* — the mental model everything else builds on.

#### Topics and subtopics
- Installing Python; `python -m venv .venv`; the REPL; running scripts.
- Variables as *names bound to objects*; dynamic typing; `type()`, `id()`.
- `int`, `float`, `bool`, `str`, `None`; conversion (`int("42")`), f-strings.
- Truthiness; `==` vs `is`; chained comparisons (`0 <= x < 10`).
- `if`/`elif`/`else`; conditional expressions (`a if cond else b`).
- `while`, `for` + `range()`; `break`, `continue`, `for`/`else`.
- `match` statement (structural pattern matching) — recognition level.
- Getting input (`input()`), printing, string methods (`strip`, `split`, `lower`).

#### Important concepts to understand
- **Assignment never copies data** — it binds a name to an object. This is why
  `b = a` for a list means both names see the same list (fully explored in
  Phase 3, planted here).
- Integer division `//` vs true division `/`; float imprecision
  (`0.1 + 0.2 != 0.3`) and when to reach for `decimal`.
- `is` compares identity, `==` compares value; use `is` only for `None`.
- A `for` loop iterates over *any iterable*, not indexes — un-learn the
  C-style `for i in range(len(xs))` habit immediately.

#### Small coding exercises (`exercises/phase01/`)
1. **fizzbuzz_plus.py** — Classic FizzBuzz for 1–100, then a variant where the
   rules (divisor → word) come from a dict so adding a rule requires no new
   `if`.
2. **temp_table.py** — Print a Celsius→Fahrenheit conversion table from -20 to
   40 in steps of 5, aligned in columns using f-string format specs
   (`f"{c:>6.1f}"`).
3. **number_guess.py** — The computer picks a random number 1–100
   (`random.randint`); the user guesses; respond higher/lower; count attempts;
   reject non-numeric input without crashing (a taste of validation before you
   formally learn exceptions).
4. **collatz.py** — Given n, print the Collatz sequence and its length. Loop
   until 1; guard against n < 1.
5. **predict.py** — Write down your prediction, *then* run: `5 / 2`, `5 // 2`,
   `-5 // 2`, `2 ** 100`, `"ab" * 3`, `bool("False")`, `0.1 + 0.2 == 0.3`,
   `1 == True`, `"10" > "9"`. Explain every surprise in a comment.

#### Larger practical assignment — **Terminal Quiz Game**
Build `quiz.py`: a multiple-choice quiz that runs in the terminal.
- Questions live in a list of tuples at the top of the file (you'll move them
  to a JSON file in Phase 6).
- Shuffle question order (`random.shuffle`); accept answers `a`–`d`;
  re-prompt on invalid input; track score; show a percentage and a
  letter-grade at the end using `match` or `elif` chains.
- A `--reverse` mode: show the answer, user picks the question (forces you to
  restructure, not hard-code).

#### Common mistakes and pitfalls
- Using `is` for value comparison (works by accident for small ints, then
  breaks mysteriously).
- `input()` returns `str` — forgetting to convert before arithmetic.
- Infinite `while` loops from updating the wrong variable.
- Shadowing builtins: naming variables `list`, `str`, `input`, `id`.
- Relying on float equality; compare with `math.isclose` instead.

#### Recommended documentation
- Tutorial §3 "An Informal Introduction to Python", §4 "More Control Flow Tools"
  (https://docs.python.org/3/tutorial/introduction.html, https://docs.python.org/3/tutorial/controlflow.html)
- Library: `builtins` functions table (https://docs.python.org/3/library/functions.html) — skim the whole table once.
- `venv` (https://docs.python.org/3/library/venv.html)

#### Completion criteria
- All five exercises and the quiz game run correctly with hostile input
  (letters where numbers are expected, empty input).
- You can explain `==` vs `is` and `/` vs `//` in one sentence each.
- You wrote every predict-then-run answer *before* executing.

#### Self-assessment quiz
1. What does `x = y` do — copy the object or bind a name? What experiment with
   `id()` proves your answer?
2. Predict: `bool([])`, `bool("0")`, `bool(0.0)`, `bool(None)`.
3. Why does `while input("> ") != "quit":` sometimes loop forever in ways that
   surprise beginners? (Hint: whitespace, case.)
4. What is the value of `x` after `for x in range(3): pass` — and why is that
   evidence that `for` doesn't create a new scope?
5. When does the `else` clause of a `for` loop run?

---

### Phase 2 — Functions and Parameter Handling

**Difficulty:** ★★☆☆☆ (Beginner)

#### Learning objectives
- Design small, single-purpose functions with clear signatures.
- Master every parameter kind Python offers — this is direct FastAPI prep,
  since `Depends`, query params, and body params all ride on this machinery.
- Understand scope (LEGB), closures, and why mutable default arguments bite.

#### Topics and subtopics
- `def`, `return`, returning tuples (multiple values), docstrings.
- Positional vs keyword arguments; default values.
- `*args`, `**kwargs`; argument unpacking with `*` and `**` at call sites.
- Positional-only (`/`) and keyword-only (`*`) parameters.
- Scope: local, enclosing, global, builtins (LEGB); `global` and `nonlocal`
  (and why you should rarely need them).
- Functions as objects: passing, returning, storing in dicts.
- Closures; `lambda` and its limits; `sorted(key=...)` as the canonical use.
- Recursion basics (base case, call stack, recursion limit).

#### Important concepts to understand
- **Default values are evaluated once, at `def` time.** A mutable default
  (`def f(x, acc=[])`) is shared across calls — the most famous Python bug.
  The idiom: default to `None`, create inside.
- Arguments are passed by *assignment* (object references), not by value or
  reference — mutating a passed list changes the caller's list; rebinding the
  parameter does not.
- A closure captures *variables*, not values — the late-binding loop trap
  (`[lambda: i for i in range(3)]` all return 2).
- Keyword-only parameters make call sites self-documenting; this is why
  modern APIs (and FastAPI signatures) use them heavily.

#### Small coding exercises (`exercises/phase02/`)
1. **stats.py** — `describe(*numbers)` returning `(minimum, maximum, mean)`;
   raise `ValueError` on empty input. Call it with a list using unpacking.
2. **greet.py** — `greet(name, /, *, greeting="Hello", punctuation="!")` —
   experiment with which call forms work and which raise `TypeError`; record
   each attempt in comments.
3. **make_counter.py** — `make_counter()` returns a function that returns 1,
   2, 3… on successive calls (closure + `nonlocal`). Then create two
   independent counters and prove they don't share state.
4. **dispatch.py** — A calculator where operations live in a dict mapping
   `"add"`, `"sub"`, `"mul"`, `"div"` to functions (some `lambda`, some
   `def`). No `if` chains allowed.
5. **buggy_default.py** — Write the classic mutable-default bug on purpose,
   demonstrate the failure with three calls, then fix it with the
   `None` idiom. Keep both versions with comments.
6. **apply_n.py** — `apply_n(func, value, times)` applies `func` repeatedly.
   Use it with `lambda x: x * 2` and with `str.upper`. Then write it
   recursively.

#### Larger practical assignment — **Text Statistics Toolkit**
Build `textstats.py`: a set of pure functions analyzing text, and a small
driver that runs them on a paragraph.
- `word_count(text)`, `char_frequencies(text, *, ignore_case=True,
  ignore_spaces=True)`, `longest_words(text, n=5)`,
  `average_word_length(text)`, `find_words(text, *, starts_with=None,
  min_length=0)`.
- A registry: `ANALYSES = {"words": word_count, ...}` and a
  `run(text, *names, **options)` dispatcher that runs the named analyses and
  returns a dict of results — you are building a miniature of how frameworks
  route by name to handler functions.
- Every function gets a docstring with an example; no function longer than 15
  lines; no global mutable state.

#### Common mistakes and pitfalls
- Mutable default arguments (see above) — you must be able to spot this in
  review instantly.
- Returning `None` implicitly on one branch and a value on another.
- Overusing `lambda` for anything with logic — if it needs a name to be
  understood, use `def`.
- Using `global` to avoid passing parameters.
- Writing functions that both compute *and* print — separate computation from
  I/O now; testing (Phase 11) will punish you otherwise.

#### Recommended documentation
- Tutorial §4.7–4.9 "Defining Functions", "More on Defining Functions"
  (https://docs.python.org/3/tutorial/controlflow.html#defining-functions)
- FAQ: "Why are default values shared between objects?"
  (https://docs.python.org/3/faq/programming.html#why-are-default-values-shared-between-objects)
- Language reference on calls — skim once: https://docs.python.org/3/reference/expressions.html#calls

#### Completion criteria
- You can write, from memory, a signature using all five parameter kinds in
  the correct order: `def f(pos_only, /, normal, *args, kw_only, **kwargs)`.
- The dispatcher exercise works with zero `if/elif` chains.
- You can explain the mutable-default bug *and* the closure-late-binding trap
  with code you wrote yourself.

#### Self-assessment quiz
1. What prints? `def f(x, acc=[]): acc.append(x); return acc` — after
   `f(1)`, `f(2)`?
2. What's the difference between `f(*xs)` in a call and `def f(*xs)` in a
   definition?
3. Why does `sorted(words, key=len)` work — what is being passed, and what is
   *not* being called?
4. When do you need `nonlocal`? Write a 3-line example from memory.
5. In `def f(a, /, b, *, c)`: which of `f(1, 2, 3)`, `f(1, 2, c=3)`,
   `f(1, b=2, c=3)`, `f(a=1, b=2, c=3)` are valid?

---

### Phase 3 — Core Data Structures

**Difficulty:** ★★☆☆☆ (Beginner)  ·  **TaskForge v0.1 begins**

#### Learning objectives
- Choose the right structure (list/tuple/dict/set) by access pattern, and
  say *why* in terms of cost (Phase 14 formalizes this).
- Write comprehensions fluently, including nested and filtered forms.
- Master mutation vs copying — aliasing bugs end here.

#### Topics and subtopics
- Lists: indexing, slicing (`xs[1:-1]`, `xs[::-1]`), `append`/`extend`/
  `insert`/`pop`/`remove`, `sort` vs `sorted`, `in`.
- Tuples: immutability, packing/unpacking, swapping, `namedtuple` preview.
- Dicts: creation, `d[k]` vs `d.get(k)`, `setdefault`, iteration over
  `items()`, dict ordering guarantees, merging (`|`), nested dicts.
- Sets: membership, `add`/`discard`, union/intersection/difference,
  `frozenset`; when a set beats a list.
- Strings as immutable sequences; `join`/`split`; why `+=` in a loop is wrong
  (build a list, join once).
- Comprehensions: list, dict, set; generator expressions (preview of Phase 8);
  nested comprehensions and when they stop being readable.
- Shallow vs deep copy (`list(xs)`, `xs[:]`, `copy.deepcopy`).
- Unpacking in assignments: `first, *rest = xs`; `enumerate`, `zip`.

#### Important concepts to understand
- **Aliasing**: `b = a` shares; `b = a[:]` copies the list but shares the
  elements. Draw the object diagrams until this is instinct.
- Never mutate a list while iterating over it — iterate over a copy or build
  a new list.
- Dict keys and set elements must be hashable — which is *why* tuples can be
  keys and lists cannot.
- `list.sort()` mutates and returns `None`; `sorted()` returns new. The
  `x = xs.sort()` bug.
- Comprehensions are expressions that *build values*; loops are statements
  that *do things*. Use each for its purpose.

#### Small coding exercises (`exercises/phase03/`)
1. **dedupe.py** — Remove duplicates from a list preserving order, two ways:
   with a seen-set, and with `dict.fromkeys`. Compare both on
   `["b","a","b","c","a"]`.
2. **invert.py** — Invert `{"alice": "admin", "bob": "user", "carol":
   "admin"}` into `{"admin": ["alice","carol"], "user": ["bob"]}` — once with
   a loop and `setdefault`, once with `collections.defaultdict`.
3. **gradebook.py** — Given `[("math", 90), ("art", 75), ("math", 85), ...]`,
   produce per-subject average, best subject, and all subjects above a
   threshold — using comprehensions where they help.
4. **matrix.py** — Represent a 3×3 matrix as a list of lists: transpose it
   with a nested comprehension and with `zip(*m)`; explain why
   `[[0]*3]*3` is a broken way to build one (aliasing!).
5. **anagrams.py** — Group a word list into anagram groups using a dict keyed
   by `"".join(sorted(word))`.
6. **set_ops.py** — Given two files' worth of usernames (two lists), find:
   users in both, users only in the first, users in either — in one line
   each with sets.

#### Larger practical assignment — **TaskForge v0.1 (in-memory)**
Create `taskforge/` with a single module `taskforge/core.py` and a driver
`taskforge/__main__.py` (structure gets proper treatment in Phase 4).
- A task is a dict: `{"id": int, "title": str, "done": bool, "tags":
  set[str], "priority": int}` — ids assigned by an incrementing counter.
- Functions (all pure where possible, operating on a list of task dicts):
  `add_task`, `complete_task`, `remove_task`, `find_by_tag`,
  `pending_sorted_by_priority`, `stats` (counts by tag, done ratio),
  `rename_tag(tasks, old, new)`.
- A REPL loop in `__main__.py`: commands `add`, `done <id>`, `ls`,
  `ls <tag>`, `stats`, `quit` — parsed with `str.split`, dispatched via a
  dict of functions (Phase 2 pattern).
- Constraint: **no function mutates its input and also returns a value** —
  pick one per function and document it. This forces you to think about
  mutation deliberately.

#### Common mistakes and pitfalls
- `x = xs.sort()` (now `x` is `None`).
- Mutating a list while iterating over it — deleting items skips neighbors.
- `[[0]*n]*m` shared-row aliasing.
- Using a list for membership tests inside a loop (quadratic behavior — you'll
  measure it in Phase 14, but avoid it now).
- `dict[key]` raising `KeyError` where `.get` with a default was intended —
  or the reverse: `.get` silently hiding a real bug.

#### Recommended documentation
- Tutorial §5 "Data Structures" (https://docs.python.org/3/tutorial/datastructures.html) — read fully.
- Library "Built-in Types" — sequence, mapping, set sections
  (https://docs.python.org/3/library/stdtypes.html)
- "Sorting Techniques" HOWTO (https://docs.python.org/3/howto/sorting.html)

#### Completion criteria
- TaskForge v0.1 REPL works end-to-end; `rename_tag` handles tags shared by
  many tasks correctly.
- You can predict aliasing behavior of `b = a`, `b = a[:]`,
  `b = copy.deepcopy(a)` for nested structures without running.
- You use a comprehension where it clarifies and a loop where it doesn't —
  and can defend each choice.

#### Self-assessment quiz
1. Predict: `a = [1, [2, 3]]; b = a[:]; b[1].append(4); print(a)`.
2. Why can't a list be a dict key, and what would you convert it to?
3. What's wrong with `for x in xs: if bad(x): xs.remove(x)` — and give two
   correct alternatives.
4. Rewrite `result = []` / `for n in nums:` / `if n % 2: result.append(n*n)`
   as one comprehension.
5. When is a `namedtuple`-style record better than a dict, and vice versa?

---

### Phase 4 — Modules, Packages, and Project Structure

**Difficulty:** ★★☆☆☆ (Beginner)  ·  **TaskForge becomes a real package**

#### Learning objectives
- Split code across modules and packages with clean import lines.
- Understand what happens at import time — once, cached, top-to-bottom.
- Set up the standard project layout you will use for every future project,
  including FastAPI services.

#### Topics and subtopics
- `import x`, `from x import y`, aliasing; why `from x import *` is banned.
- Module search path (`sys.path`), the `__pycache__` directory.
- `if __name__ == "__main__":` — what it's actually for.
- Packages: `__init__.py`, subpackages, relative vs absolute imports.
- `python -m package` and `__main__.py`.
- Virtual environments in practice; `pip install`, `requirements.txt` /
  `pyproject.toml` (declarative minimum); installing your own package
  editable (`pip install -e .`).
- Import-time side effects and why module top-level should mostly be
  definitions.
- Circular imports: how they happen, how to break them.

#### Important concepts to understand
- A module is executed **once** on first import and cached in `sys.modules` —
  module-level code is initialization code, so keep it cheap and
  side-effect-free.
- **Circular imports** are almost always a design smell: two modules that need
  each other are one concept split wrongly, or need a third module both can
  import.
- The difference between a script (`python file.py`) and a module in a package
  (`python -m pkg.mod`) — and why relative imports fail in the former.
- Your package's public API is what `__init__.py` exports; everything else is
  internal.

#### Small coding exercises (`exercises/phase04/`)
1. **shapes/** — A package with `circle.py`, `rectangle.py` each defining
   `area`/`perimeter`, and an `__init__.py` exposing a unified
   `area(shape_name, **dims)`. Use it from an outside script with three
   different import styles.
2. **import_order.py** — Two modules that print at import time; import them in
   different orders, twice each; write down what printed and why (once each —
   caching).
3. **circular/** — Deliberately create a circular import between `a.py` and
   `b.py`, observe the exact error, then fix it two ways: (a) move the shared
   piece to `c.py`, (b) import inside the function. Note in comments which
   fix is better and when.
4. **cli_module.py** — A module with a `main()` guarded by
   `if __name__ == "__main__":`; prove it runs as a script *and* imports
   cleanly (no output) from the REPL.

#### Larger practical assignment — **TaskForge v0.1 as a package**
Restructure into the layout you'll keep for the rest of the roadmap:

```
taskforge/
├── pyproject.toml            # name, version, [project.scripts] entry point
├── src/taskforge/
│   ├── __init__.py           # public API: __version__, key functions
│   ├── __main__.py           # python -m taskforge
│   ├── core.py               # task operations (from Phase 3)
│   └── cli.py                # REPL loop, parsing — I/O lives here only
└── tests/                    # empty for now; Phase 11 fills it
```

- `core.py` must not import `cli.py` (dependency points one way: outer→inner).
- `pip install -e .` into your venv; the `taskforge` console script and
  `python -m taskforge` both launch the REPL.
- Add a `version` command to the CLI that reads `taskforge.__version__`.

#### Common mistakes and pitfalls
- Working code that breaks the moment it's run from a different directory
  (accidental reliance on cwd for imports).
- `from x import *` polluting namespaces and hiding origins.
- Heavy work (file reads, network) at module top level.
- Naming a module the same as a stdlib module (`json.py`, `logging.py` in your
  project shadow the real ones — a legendarily confusing failure).
- Mixing relative and absolute imports randomly; pick absolute-within-package
  and stay consistent.

#### Recommended documentation
- Tutorial §6 "Modules" (https://docs.python.org/3/tutorial/modules.html)
- Library: `venv`; "Installing Python Modules" (https://docs.python.org/3/installing/index.html)
- Packaging tutorial — sections on `pyproject.toml` and src layout
  (https://packaging.python.org/en/latest/tutorials/packaging-projects/)

#### Completion criteria
- `pip install -e .` + `taskforge` command works from any directory.
- You can explain why `python src/taskforge/cli.py` fails while
  `python -m taskforge` works.
- You broke and fixed a circular import and can describe the general cure.

#### Self-assessment quiz
1. What two things does `if __name__ == "__main__":` distinguish between?
2. Module `a` imports `b`; `b` imports `a`. Walk through exactly what Python
   does and where it fails.
3. Why does a file named `random.py` in your project break
   `import random` — and what is the search-path explanation?
4. What's the difference between `import taskforge.core` and
   `from taskforge import core` in terms of what names exist afterward?
5. Why should `core.py` never import `cli.py` in our layout?

---

### Phase 5 — Exceptions and Error Handling

**Difficulty:** ★★★☆☆ (Intermediate)

#### Learning objectives
- Use `try/except/else/finally` precisely — narrow scopes, specific types.
- Design an exception hierarchy for a library, and know where to catch vs
  where to raise.
- Internalize EAFP ("easier to ask forgiveness than permission") as the
  Python default, and when LBYL is still right.

#### Topics and subtopics
- The exception hierarchy: `BaseException` → `Exception` → concrete types;
  why you (almost) never catch `BaseException` or bare `except:`.
- `try/except/else/finally` — what belongs in each block.
- `raise`, re-raising (`raise` alone), exception chaining
  (`raise X from err`) and why the cause matters in logs.
- Custom exceptions: one base class per library, narrow subclasses, carrying
  data on the exception.
- EAFP vs LBYL; `KeyError`/`IndexError`/`ValueError`/`TypeError` semantics —
  raising the *conventional* type.
- `finally` vs `with` for cleanup (preview of Phase 9).
- Where errors should surface: libraries raise, applications catch at the
  boundary (CLI loop, request handler) — the exact model FastAPI uses with
  exception handlers.

#### Important concepts to understand
- **Catch narrowly, and only where you can act.** An `except` that can't fix,
  retry, or meaningfully report should not exist — let it propagate.
- Swallowed exceptions (`except: pass`) turn crashes into silent corruption —
  the worst trade in software.
- `else` on `try` exists to keep the protected region minimal: only the line
  that can raise goes in `try`.
- Exceptions are control flow in Python (`StopIteration` powers `for`!) — they
  are not "exceptional" in cost or in style the way other languages teach.
- Chaining: `raise AppError("config invalid") from err` preserves the real
  cause; `from None` deliberately hides it — know both.

#### Small coding exercises (`exercises/phase05/`)
1. **safe_convert.py** — `to_int(s, default=None)` that converts or returns
   the default — but *only* catches `ValueError`/`TypeError`. Show that
   passing a list triggers the right path and a KeyboardInterrupt does not
   get swallowed.
2. **retry.py** — `call_with_retry(func, attempts=3)` that retries on
   `OSError` only, re-raises the last error after exhausting attempts (with
   the original as `__cause__`), and never retries on other exceptions. Test
   with a fake flaky function using a closure counter (Phase 2!).
3. **hierarchy.py** — Design exceptions for a banking module:
   `BankError(Exception)` → `InsufficientFunds` (carries `shortfall`),
   `AccountNotFound` (carries `account_id`). Write `withdraw()` that raises
   them, and a caller that handles each differently and prints the carried
   data.
4. **finally_order.py** — Predict-then-run: a function with `return` in
   `try`, in `except`, and in `finally` — establish exactly when `finally`
   runs and what a `return` in `finally` does (and why it's forbidden in
   style guides).
5. **eafp_vs_lbyl.py** — Read a key from a nested dict
   `cfg["db"]["port"]` three ways: LBYL (`in` checks), EAFP
   (`try/except KeyError`), and `.get` chains. Note in comments which reads
   best and which hides bugs.

#### Larger practical assignment — **TaskForge v0.2a: robust core**
- Create `src/taskforge/errors.py`: `TaskForgeError(Exception)` base, with
  `TaskNotFound(task_id)`, `InvalidTask(reason)`, `DuplicateTask(title)`.
- `core.py` raises these — it never prints, never exits, never catches what
  it can't handle.
- `cli.py` becomes the **error boundary**: one `except TaskForgeError as e:`
  around command dispatch turns any domain error into a friendly one-line
  message and keeps the REPL alive; unexpected exceptions still crash loudly
  (do *not* catch `Exception` here yet — you'll add logging in Phase 12).
- Add input validation: empty titles, negative priorities, unknown ids —
  each mapped to the right exception with a helpful message.
- Manual test script `abuse.py` that drives 10 hostile inputs through the
  public API and prints the caught error types (Phase 11 turns this into
  real tests).

#### Common mistakes and pitfalls
- `except Exception:` (or worse, bare `except:`) around large blocks —
  catching `NameError` typos and hiding them.
- Catching where you can't act, "just in case."
- Raising strings/generic `Exception` instead of typed exceptions.
- Using exceptions for expected alternatives that a return value expresses
  better (`find()` returning `None` vs `get()` raising — know both patterns
  from dicts).
- Losing the original traceback by raising a new error without `from err`.

#### Recommended documentation
- Tutorial §8 "Errors and Exceptions" (https://docs.python.org/3/tutorial/errors.html) — read fully.
- Library: "Built-in Exceptions" — study the hierarchy diagram
  (https://docs.python.org/3/library/exceptions.html)

#### Completion criteria
- TaskForge survives your entire `abuse.py` hostile-input script with
  friendly messages and zero stack traces — while a genuine bug (add one
  temporarily) still crashes with a full traceback.
- Every `except` in your codebase names specific types and does something
  meaningful.
- You can draw the `BankError` hierarchy exercise from memory.

#### Self-assessment quiz
1. Why is `except: pass` worse than letting the program crash?
2. What is the difference between `raise NewError(...) from err` and plain
   `raise NewError(...)` inside an `except` block — in the traceback a user
   sees?
3. When does `else` on a `try` run, and what problem does it solve over
   putting the code inside `try`?
4. Which builtin exception should `xs[10]` raise vs `d["missing"]` vs
   `int("abc")` — and why does matching convention matter for callers?
5. In a library/application split, who raises and who catches? Where is the
   "boundary" in TaskForge — and what will it be in a FastAPI app?

---

### Phase 6 — Files and Data Handling

**Difficulty:** ★★★☆☆ (Intermediate)  ·  **TaskForge v0.2: persistence**

#### Learning objectives
- Read and write text, JSON, and CSV safely: encodings, newlines, cleanup.
- Use `pathlib` for all path work.
- Implement durable saving (write-temp-then-rename) — a real backend skill.

#### Topics and subtopics
- `open()` modes; text vs binary; **always** `encoding="utf-8"` explicitly.
- `with open(...) as f:` — files as context managers (mechanics now, theory
  in Phase 9).
- Reading patterns: `read()`, iteration line by line (and why line iteration
  scales when `read()` doesn't).
- `pathlib.Path`: joining with `/`, `exists`, `mkdir(parents=True,
  exist_ok=True)`, `glob`, `read_text`/`write_text`, `home()`.
- `json`: `dump/load`, `dumps/loads`, `indent`, `sort_keys`; what JSON can't
  represent (sets, tuples→lists, datetime) and writing converters.
- `csv`: `reader/writer`, `DictReader/DictWriter`, `newline=""` requirement.
- Atomic writes: write to a temp file, `os.replace` over the target.
- A quick look at `tempfile` and `shutil`.

#### Important concepts to understand
- Encodings are not optional knowledge: the default encoding is
  platform-dependent; a file written on one machine can fail to read on
  another unless you pin `utf-8`.
- JSON round-tripping is *lossy* for Python types: `tuple`→`list`, `set`→
  error, `int` keys→`str` keys. Your storage layer must convert explicitly
  both directions.
- Crash-safety: a half-written JSON file is corruption; temp-file + atomic
  rename means readers see either the old or the new file, never a hybrid.
- Iterating a file yields lines *with* their `\n` — the `strip()` habit.

#### Small coding exercises (`exercises/phase06/`)
1. **wordfreq.py** — Read a text file, print the 10 most common words
   (case-folded, punctuation stripped). Handle `FileNotFoundError` with a
   friendly message (Phase 5!).
2. **jsonround.py** — Build a dict containing a tuple, a set, and an int-keyed
   dict; dump to JSON and load back; assert on and then document every
   difference; write `to_jsonable`/`from_jsonable` converters that make the
   round trip faithful.
3. **logscan.py** — Given a fake server log (make one: 200 lines of
   `TIMESTAMP LEVEL message`), stream it line by line, count by level, and
   extract the last 5 `ERROR` lines — without ever holding the whole file in
   memory.
4. **csv_clean.py** — Read a messy CSV (extra whitespace, blank lines, a bad
   row with too few columns) with `DictReader`; write a cleaned version with
   `DictWriter`; report skipped rows with line numbers.
5. **treewalk.py** — Using `pathlib.Path.glob("**/*.py")`, print every Python
   file under a directory with its size, largest first, total at the bottom.
6. **atomic.py** — Implement `atomic_write_text(path, text)` using
   `tempfile.NamedTemporaryFile(dir=path.parent, delete=False)` +
   `os.replace`. Prove it: raise an exception mid-write and show the original
   file is untouched.

#### Larger practical assignment — **TaskForge v0.2: JSON persistence**
- New module `src/taskforge/storage.py`:
  `load_tasks(path) -> list[dict]`, `save_tasks(path, tasks)`.
  - JSON on disk at `~/.taskforge/tasks.json` (`Path.home()`, auto-create
    dir); `tags` stored as sorted lists, converted back to sets on load.
  - `save_tasks` uses your atomic-write pattern.
  - Missing file → empty list; corrupt file → raise
    `StorageError(TaskForgeError)` chaining the original
    `json.JSONDecodeError` (Phase 5 skills).
- CLI: load at start, save after every mutating command; new commands
  `export csv <path>` and `import csv <path>` (round-trip your own export;
  skip and report bad rows on import).
- Move the Phase 1 quiz's questions into a JSON file and reload the quiz from
  it — a 20-minute refactor that proves the old code still makes sense to
  you.

#### Common mistakes and pitfalls
- Omitting `encoding="utf-8"` and shipping code that breaks on another OS.
- Building paths by string concatenation (`dir + "/" + name`) instead of
  `Path`.
- Reading whole huge files with `.read()` when line iteration streams.
- Forgetting `newline=""` when opening CSV files for writing (blank lines on
  Windows).
- Writing directly over the target file, so a crash mid-write destroys data.
- Storing sets/datetimes in JSON without a conversion plan.

#### Recommended documentation
- Tutorial §7.2 "Reading and Writing Files" (https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files)
- Library: `pathlib` (https://docs.python.org/3/library/pathlib.html), `json`
  (https://docs.python.org/3/library/json.html), `csv`
  (https://docs.python.org/3/library/csv.html), `tempfile`, `shutil`

#### Completion criteria
- Kill TaskForge mid-save (add a deliberate crash) — the tasks file is never
  corrupted.
- CSV export→import round-trips your task list exactly (including tags).
- You can explain why `json.dumps({1: "a"})` then `loads` gives `{"1": "a"}`.

#### Self-assessment quiz
1. What can go wrong if you open a file without specifying an encoding?
2. Why does iterating over a file object scale to files larger than RAM,
   while `f.read().split("\n")` does not?
3. What does the atomic-rename pattern guarantee that plain writing does not?
4. List three Python values that don't survive a JSON round trip and the
   conventional fix for each.
5. Why `newline=""` for CSV files?

---

### Phase 7 — Classes and Object-Oriented Programming

**Difficulty:** ★★★★☆ (Intermediate)  ·  **TaskForge v0.3a: the big refactor**

#### Learning objectives
- Model a domain with classes: state, behavior, invariants, representation.
- Use dataclasses for data-shaped classes and know when *not* to.
- Choose composition over inheritance by default; use inheritance and ABCs/
  protocols where substitution is real.
- This phase is the foundation for Pydantic models and dependency-injected
  services in FastAPI.

#### Topics and subtopics
- `class`, `__init__`, `self`, instance vs class attributes (and the shared
  mutable class-attribute trap).
- Methods, `@classmethod` (alternate constructors: `from_dict`),
  `@staticmethod` (and why plain module functions often beat it).
- Dunder methods: `__repr__` vs `__str__`, `__eq__` (+ why it kills
  hashability), `__hash__`, `__lt__` + `functools.total_ordering`,
  `__len__`, `__contains__`, `__getitem__`.
- Properties: computed attributes, validation on set; when a property hides
  too much work.
- `@dataclass`: `field(default_factory=...)`, `frozen=True`, `slots=True`,
  `asdict`; dataclass vs dict vs namedtuple vs plain class.
- Encapsulation by convention: `_single_underscore`; name mangling `__double`
  (know it, rarely use it).
- Inheritance: method overriding, `super().__init__`, when `isinstance`
  checks signal a design problem.
- Composition: objects holding objects; delegation.
- Abstract base classes (`abc.ABC`, `@abstractmethod`); duck typing;
  `typing.Protocol` as the modern structural alternative (deepened in
  Phase 10).
- MRO in one sitting: what `super()` really resolves to; recognize diamond
  problems, then avoid designs that create them.

#### Important concepts to understand
- **A class earns its existence by protecting an invariant** ("a Task's id
  never changes"; "status transitions are legal"). Data with no invariants
  and no behavior can stay a dataclass — or a dict.
- Class attributes are shared: a mutable class attribute
  (`tags: list = []` at class level) is the OOP version of the mutable
  default argument.
- **Composition vs inheritance**: inheritance means *is-substitutable-for*
  (Liskov), not *shares-some-code*. Code sharing without substitution is
  composition's job. Default to composition; you should be able to argue
  each choice.
- Duck typing: Python cares what an object *can do*, not what it *is* —
  ABCs and Protocols formalize "can do" only where you need the guarantee.
- `__repr__` is for developers (unambiguous, ideally eval-able); implement
  it on everything — your debugging speed depends on it.

#### Small coding exercises (`exercises/phase07/`)
1. **money.py** — An immutable `Money` dataclass (`frozen=True`): `amount:
   Decimal`, `currency: str`; `+` and comparison only within a currency
   (raise `ValueError` across); nice `__repr__`. Show it works as a dict key.
2. **vector.py** — A 2D `Vector` with `+`, `-`, scalar `*`, `abs()`
   (magnitude), `==`, and a full set of predict-then-run cases including
   `v * 3` vs `3 * v` (`__rmul__`).
3. **temperature.py** — A `Temperature` class storing kelvin internally, with
   `celsius`/`fahrenheit` as properties (get and set), rejecting values below
   absolute zero in *every* path.
4. **shapes_abc.py** — `Shape(ABC)` with abstract `area()`; `Circle`,
   `Rect` implement it; `total_area(shapes)` works on a mixed list. Then add
   a `Squarish` **Protocol** with `side` and show a class satisfying it with
   no inheritance at all.
5. **composition.py** — Model `Engine`, `GPS`, `Car`: the car *has* an engine
   (composition) and delegates `start()`. Then write the inheritance version
   (`Car(Engine)`) and a comment explaining three concrete ways it's worse.
6. **classattr_trap.py** — Build the shared-mutable-class-attribute bug with
   two instances polluting each other; fix with `__init__` (or
   `default_factory`); keep both versions.

#### Larger practical assignment — **TaskForge v0.3a: domain model + repository**
The scheduled Phase-7 refactor — dicts become a real model:
- `src/taskforge/models.py`:
  - `Priority(enum.IntEnum)`: LOW/MEDIUM/HIGH.
  - `@dataclass class Task`: `id: int | None`, `title: str`,
    `done: bool = False`, `tags: set[str] = field(default_factory=set)`,
    `priority: Priority = Priority.MEDIUM`, `created_at: datetime`.
    Validation in `__post_init__` (non-empty title). Methods: `complete()`,
    `matches(query)`. Classmethod `from_dict` / method `to_dict` — the JSON
    conversion knowledge from Phase 6 now lives *on the model*.
- `src/taskforge/repository.py`:
  - `TaskRepository(ABC)`: `add`, `get`, `remove`, `list`, `save`
    (abstract).
  - `MemoryRepository` and `JsonRepository(path)` implementations —
    the storage functions from Phase 6 become one class.
  - The repository assigns ids (the counter moves inside — encapsulated
    state with an invariant).
- `cli.py` talks only to the `TaskRepository` interface; swapping
  memory↔JSON is a one-line change in `__main__.py`. **This is dependency
  inversion, and it is exactly how you'll swap a fake database for a real
  one in FastAPI tests.**
- Everything must still work: same commands, same files on disk.

#### Common mistakes and pitfalls
- Mutable class attributes shared across instances.
- Forgetting `self`; calling methods on the class without an instance.
- Inheritance for code reuse ("`JsonRepository(dict)`" style) — you inherit
  a hundred methods that break your invariants.
- God classes: one class that models, stores, formats, and prints. Each
  TaskForge class should have a one-sentence responsibility.
- Overriding `__eq__` without thinking about `__hash__` (your objects
  silently stop working in sets/dicts).
- Getters/setters Java-style instead of plain attributes + properties when
  needed.

#### Recommended documentation
- Tutorial §9 "Classes" (https://docs.python.org/3/tutorial/classes.html) — read fully.
- Library: `dataclasses` (https://docs.python.org/3/library/dataclasses.html),
  `enum` (https://docs.python.org/3/library/enum.html), `abc`
  (https://docs.python.org/3/library/abc.html)
- Reference: "Data model" §3.3 special methods — skim the table
  (https://docs.python.org/3/reference/datamodel.html)

#### Completion criteria
- TaskForge runs identically to v0.2 but with `Task` objects and swappable
  repositories; the CLI contains zero JSON knowledge.
- You can state each class's single responsibility in one sentence.
- You can argue composition-vs-inheritance with your `Car` example from
  memory, and Liskov substitution in plain words.

#### Self-assessment quiz
1. Predict: `class C: xs = []` — two instances, `a.xs.append(1)`; what does
   `b.xs` show and why? Where does `a.xs = [2]` bind?
2. When is `@classmethod` the right tool? Name the canonical use case.
3. Your `Task` defines `__eq__` by id. What just happened to its
   hashability, and how do you restore it?
4. "Prefer composition over inheritance" — give the substitution-based
   criterion for when inheritance *is* right.
5. What's the difference between an ABC and a Protocol in how a class comes
   to satisfy them?

---

### Phase 8 — Iterables, Iterators, and Generators

**Difficulty:** ★★★★☆ (Intermediate)

#### Learning objectives
- Understand the iteration protocol well enough to implement it by hand once
  — then never again, because generators do it better.
- Write generator functions and pipelines that process data lazily.
- Use `itertools` as your streaming toolkit.
- Generators are the machinery behind FastAPI dependencies with cleanup and
  streaming responses — this phase is direct preparation.

#### Topics and subtopics
- The protocol: `iter()`/`__iter__`, `next()`/`__next__`, `StopIteration`;
  iterable vs iterator (the container vs the bookmark).
- Why an iterator is single-use, and the classic exhausted-iterator bug.
- Implement one class-based iterator by hand (`Countdown`) — to demystify,
  not as a pattern to use.
- Generator functions: `yield`, lazy evaluation, state suspension;
  generators are iterators.
- Generator expressions; passing them straight into `sum()`, `max()`,
  `any()`.
- Pipelines: generators consuming generators; reading-a-huge-file-through-
  filters as the canonical case.
- `yield from`; `return` in a generator.
- `itertools`: `count`, `islice`, `chain`, `groupby` (and its
  must-be-sorted trap), `pairwise`, `batched`, `takewhile`.
- Generator `.close()` and `try/finally` inside generators (bridge to
  Phase 9's `@contextmanager`).

#### Important concepts to understand
- **Laziness**: a generator computes nothing until asked. This changes both
  memory (streams beat lists) and *timing* — exceptions inside a generator
  happen at consumption, not creation. Both matter in production.
- A `for` loop desugars to `iter()` + repeated `next()` + catching
  `StopIteration` — you should be able to write that desugaring.
- Iterators exhaust: iterating twice over a generator silently yields
  nothing the second time — a bug class you must experience deliberately.
- A generator with `try/finally` runs cleanup when closed/garbage-collected —
  this is exactly how `@contextmanager` and FastAPI's `yield`-dependencies
  provide setup/teardown.

#### Small coding exercises (`exercises/phase08/`)
1. **countdown.py** — Class-based `Countdown(n)` iterator (both `__iter__`
   and `__next__`); then a 3-line generator version; then desugar a `for`
   loop over it into `while`/`next`/`except StopIteration` by hand.
2. **exhausted.py** — Create a generator, run `list()` on it twice; then
   `zip` two references to the *same* iterator and predict the output.
   Document the bug class.
3. **fib.py** — Infinite Fibonacci generator; take the first 10 with
   `islice`; first-above-a-million with `next(filter(...))` or a loop.
4. **pipeline.py** — For your Phase 6 fake server log: build
   `read_lines(path)` → `parse(lines)` → `only_errors(records)` →
   `to_messages(records)` as four generators; consume with a single `for`.
   Add a counter proving `parse` ran exactly as many times as lines
   consumed (laziness made visible).
5. **chunks.py** — `chunked(iterable, size)` yielding lists of ≤size items —
   works on any iterable including generators (no `len()` allowed). Compare
   with `itertools.batched`.
6. **groupby_trap.py** — Use `itertools.groupby` on unsorted data, observe
   the wrong result, fix with `sorted(key=...)`; write the moral in a
   comment.

#### Larger practical assignment — **TaskForge v0.3b: streaming reports**
- `src/taskforge/reports.py` — all functions return *iterators/generators*,
  not lists:
  - `filter_tasks(tasks, *, tag=None, done=None, min_priority=None)` — a
    generator; combines conditions lazily.
  - `overdue(tasks, now)` (add an optional `due: datetime | None` to Task).
  - `by_tag(tasks)` — yields `(tag, count)` pairs using `groupby` correctly.
  - `search(tasks, query)` — lazy; CLI shows first 10 via `islice` with
    "…and N more" only if cheap to know.
- CSV import from Phase 6 becomes a generator pipeline:
  `read_rows` → `clean` → `to_tasks` → repository add; bad rows yielded to
  a separate error report instead of crashing the stream.
- The CLI `ls` command now composes: `ls work --pending --top 5` chains
  `filter_tasks` + sorting + `islice`.

#### Common mistakes and pitfalls
- Consuming an iterator twice and silently processing nothing.
- Returning a list where an iterator was promised (or vice versa) — decide
  and document per function.
- `groupby` on unsorted input.
- Building a list inside a "generator" function, defeating laziness.
- Holding a reference to the underlying file after the pipeline ends —
  who closes the file? (Phase 9 answers this properly.)
- Using a generator where you need `len()`, indexing, or multiple passes —
  laziness is a tool, not a religion.

#### Recommended documentation
- Tutorial §9.8–9.10 "Iterators, Generators, Generator Expressions"
  (https://docs.python.org/3/tutorial/classes.html#iterators)
- Library: `itertools` — including the recipes section at the bottom, which
  is some of the best Python ever written
  (https://docs.python.org/3/library/itertools.html)
- Functional Programming HOWTO (https://docs.python.org/3/howto/functional.html)

#### Completion criteria
- The log pipeline processes a 100k-line file with flat memory (verify
  roughly with a generator-based line counter vs a list-based one).
- You can hand-write the `for`-loop desugaring and explain iterable vs
  iterator with the book/bookmark analogy in your own words.
- TaskForge `ls` composes filters lazily and correctly.

#### Self-assessment quiz
1. What's the difference between an iterable and an iterator? Which is a
   list? Which is a generator?
2. Predict: `g = (x*x for x in range(3)); list(g); list(g)`.
3. Why does `zip(it, it)` (same iterator twice) pair `(0,1), (2,3)` instead
   of `(0,0), (1,1)`?
4. When is a generator the *wrong* choice? Name two concrete signals.
5. Where does an exception raised inside a generator body surface — at
   creation or consumption — and why does that matter for error handling?

---

### Phase 9 — Decorators and Context Managers

**Difficulty:** ★★★★☆ (Intermediate)  ·  **TaskForge v0.3 complete**

#### Learning objectives
- Read and write decorators confidently, including parameterized ones.
- Write context managers both as classes and with `@contextmanager`.
- Recognize both as the same idea — wrapping code around code — and know
  which fits where. FastAPI's route decorators, dependencies, middleware,
  and lifespan handlers are all this phase wearing different hats.

#### Topics and subtopics
- Decorators from first principles: `@d` is `f = d(f)` — closures (Phase 2)
  applied.
- The standard shape: wrapper with `*args, **kwargs`, return value passed
  through; `functools.wraps` and what breaks without it.
- Decorators with arguments (three-layer form); stacking order.
- Practical decorators: timing, logging, retry (port your Phase 5
  `call_with_retry`), memoization; then `functools.cache`/`lru_cache`
  instead of hand-rolling.
- Class-level uses you already met, now understood: `@property`,
  `@classmethod`, `@dataclass` is a class decorator.
- Context managers: the `with` protocol (`__enter__`/`__exit__`); exception
  handling in `__exit__` (the meaning of returning `True`).
- `contextlib.contextmanager`: generator + `try/finally` (Phase 8 machinery)
  as the concise form.
- `contextlib` extras: `suppress`, `closing`, `ExitStack` (recognition
  level).
- When to pick decorator vs context manager vs plain function.

#### Important concepts to understand
- A decorator replaces the function object — without `functools.wraps`,
  `__name__`/`__doc__`/introspection (and some frameworks' behavior) break.
- The three-layer decorator (`def deco(arg): def wrap(f): def inner(...)`)
  is mechanical once you see each layer's job: configure → receive function
  → replace call. Write it slowly once; it's yours forever.
- `__exit__` receives the exception info; returning `True` swallows the
  exception — almost always wrong except in tools like `suppress`.
- `with` guarantees cleanup on *every* exit path (return, exception, break)
  — it is `try/finally` with a name and a scope.
- Decorators compose bottom-up: `@a` over `@b` means `a(b(f))`.

#### Small coding exercises (`exercises/phase09/`)
1. **timing.py** — `@timed` printing duration via `time.perf_counter`; with
   and without `functools.wraps` — show what `help(func)` and
   `func.__name__` report in each case.
2. **logged.py** — `@logged(level="INFO")` (parameterized) printing
   call/args/result. Stack `@timed` and `@logged` both ways and explain the
   output order.
3. **retry_deco.py** — Port Phase 5's retry into
   `@retry(attempts=3, on=(OSError,))`. The test fake from Phase 5 must
   still work.
4. **memo.py** — Hand-roll `@memoize` with a dict (what are the limits —
   unhashable args?); then replace with `functools.lru_cache` and compare
   `fib(35)` timings with/without.
5. **timer_cm.py** — A `Timer` context manager, class-based, that records
   elapsed time on itself (`with Timer() as t: ...; print(t.elapsed)`), and
   doesn't lose the timing when the body raises. Then rewrite in 6 lines
   with `@contextmanager`.
6. **chdir_cm.py** — `working_directory(path)` context manager: chdir in,
   *always* chdir back (test the exception path). Compare with
   `contextlib.chdir`.
7. **exit_semantics.py** — Predict-then-run: an `__exit__` that returns
   `True`; a `with` body containing `return`; nested `with` blocks' cleanup
   order.

#### Larger practical assignment — **TaskForge v0.3: cross-cutting concerns**
The scheduled Phase-9 refactor:
- `src/taskforge/instrument.py`: `@timed` (debug-level log later),
  `@logged`, `@retry(on=(OSError,))` — apply `@retry` to
  `JsonRepository.save`.
- Turn the repository into a context manager:
  `with JsonRepository(path) as repo:` — `__enter__` loads, `__exit__` saves
  **only if no exception occurred** (decide this semantic deliberately and
  write it down). Provide it both class-based and as a
  `@contextmanager`-based `open_repository(path)`; keep the one you find
  clearer and note why.
- The atomic-write from Phase 6 becomes
  `@contextmanager def atomic_write(path):` yielding a file object — your
  three file-handling patterns (open, temp, replace) collapse into one
  reusable line at call sites.
- Sweep the codebase: every place with paired setup/teardown or duplicated
  wrapping logic either becomes a `with` or a decorator — or gets a comment
  saying why not.

#### Common mistakes and pitfalls
- Forgetting `functools.wraps` (breaks introspection and stacking).
- Forgetting to `return` the wrapper's result (`wrapper` calls `f` but
  drops the value — every decorated function suddenly returns `None`).
- Decorating with side effects at import time (decorators run at `def`
  time — keep them cheap).
- Returning `True` from `__exit__` accidentally, swallowing everything.
- `@contextmanager` generator without `try/finally` — cleanup silently
  skipped on exceptions.
- Using a memoizing decorator on functions with mutable/unhashable args.

#### Recommended documentation
- Library: `functools` (`wraps`, `lru_cache`, `cache`)
  (https://docs.python.org/3/library/functools.html), `contextlib`
  (https://docs.python.org/3/library/contextlib.html)
- Reference: "with statement" semantics
  (https://docs.python.org/3/reference/compound_stmts.html#the-with-statement)
- Glossary entries: "decorator", "context manager"
  (https://docs.python.org/3/glossary.html)

#### Completion criteria
- You can write the three-layer parameterized decorator from a blank file,
  correctly, without reference.
- `with open_repository(path) as repo:` is the only way the CLI touches
  storage, and the exception path provably skips the save.
- You can explain in one sentence each why `@app.get("/")` in FastAPI is
  "just" this phase's material.

#### Self-assessment quiz
1. Desugar `@timed` `def f(): ...` into assignment form. Now desugar
   `@logged(level="X")` — how many calls happen at decoration time?
2. Without `functools.wraps`, what does `decorated.__name__` return and name
   one real thing that breaks.
3. In `@a` `@b` `def f():` — which decorator's wrapper runs first at call
   time?
4. What are the three arguments to `__exit__`, and what does returning
   `True` mean?
5. Why must the `yield` in a `@contextmanager` generator sit inside
   `try/finally` for reliable cleanup?

---

### Phase 10 — Type Annotations

**Difficulty:** ★★★☆☆ (Advanced)  ·  **TaskForge v0.4a: fully typed**

#### Learning objectives
- Annotate everything; run a type checker (mypy or pyright) as a habit.
- Use generics, `Optional`, unions, `Protocol`, `TypedDict`, `Literal`.
- Typing is Pydantic's and FastAPI's native language — `def get(id: int) ->
  Task | None` *is* a FastAPI endpoint minus the decorator.

#### Topics and subtopics
- Annotation syntax: variables, parameters, returns; annotations are not
  enforced at runtime (know what they *are* — metadata).
- Builtin generics: `list[int]`, `dict[str, list[Task]]`, `tuple[int, ...]`.
- `X | None` (Optional) and the checker forcing you to handle `None` —
  annotations as bug finders, not decoration.
- `Literal`, `Final`, `TypeAlias`; `Any` vs `object` (and why `Any` is an
  escape hatch to minimize).
- Callables: `Callable[[int, str], bool]`; typing decorators with
  `ParamSpec` (recognition level).
- `TypeVar` and generic functions (`def first(xs: list[T]) -> T`); generic
  classes (`Repository[T]`, recognition level).
- `Protocol` for structural typing — typing the duck typing you did in
  Phase 7.
- `TypedDict` for dict-shaped data (your JSON layer); `cast`; `# type:
  ignore` discipline (always with a reason).
- Running mypy/pyright; strictness options; gradual typing strategy.

#### Important concepts to understand
- Python types are checked by external tools, not the interpreter — the
  value is *design pressure* and *bug discovery*, and it works only if the
  checker runs (locally + CI).
- `X | None` forces callers to confront absence — most checker findings in
  freshly-typed code are genuine unhandled-`None` bugs. Expect to find
  real bugs in TaskForge; that's the point.
- A function that's hard to annotate (returns `str | list[str] | None`
  depending on flags) is the checker telling you the *design* is confused —
  fix the design, not the annotation.
- `Protocol` decouples: the repository consumer defines what it needs; the
  implementation never imports the protocol. Compare with the ABC from
  Phase 7 — nominal vs structural.

#### Small coding exercises (`exercises/phase10/`)
1. **annotate_old.py** — Copy three of your Phase 2/3 exercise files and
   fully annotate them; run mypy in strict mode; fix every finding and note
   which were real bugs vs annotation gaps.
2. **optional_chain.py** — `find_user(id) -> User | None` plus a caller;
   watch the checker reject unguarded access; fix with a guard, then with
   an early raise — feel the difference.
3. **generic_first.py** — Write `first(xs: Iterable[T], default: T | None =
   None) -> T | None` and verify the checker infers `first([1,2])` as
   `int | None`.
4. **proto.py** — Define `class Storable(Protocol)` with `to_dict/from_dict`;
   a `save_all(items: Iterable[Storable])`; show `Task` satisfies it with no
   import or inheritance; break the protocol and read the checker error.
5. **typeddict.py** — `class TaskRow(TypedDict)` for your CSV/JSON row shape;
   annotate the Phase 6/8 import pipeline end-to-end; let the checker catch
   a wrong-key typo you introduce on purpose.
6. **badly_typed.py** — Take a flag-dependent multi-return-type function
   (write one), fail to type it cleanly, then refactor into two functions —
   document the lesson.

#### Larger practical assignment — **TaskForge v0.4a: strict typing**
The scheduled Phase-10 refactor:
- Annotate the entire package; mypy (or pyright) passes in strict mode with
  zero `Any` in your own signatures and every `# type: ignore` carrying a
  written reason (target: none).
- Replace the `TaskRepository` ABC with a `Protocol` **or** keep the ABC —
  but write a paragraph in `NOTES.md` defending the choice (there are real
  arguments both ways: registration vs decoupling vs runtime checks).
- Type the JSON boundary with `TypedDict` (`TaskDict`) so
  `Task.from_dict`/`to_dict` are checked end to end.
- Keep a log: every genuine bug the checker found (there will be some —
  usually `None` handling in `get`/`find` paths).
- Add the checker to a `make check` / script entry so it runs with one
  command.

#### Common mistakes and pitfalls
- Sprinkling `Any` to silence the checker — you keep the cost and lose the
  benefit.
- Annotating `dict` (bare) instead of `dict[str, Task]`.
- `Optional` accepted but never narrowed (`if x is None: raise/return`).
- Lying annotations that drift from behavior — the checker only helps if
  you run it continuously.
- Over-engineering: `TypeVar` gymnastics where a concrete type is honest.
- Believing annotations validate at runtime (they don't — that's exactly
  the gap Pydantic fills, which is why FastAPI exists).

#### Recommended documentation
- Library: `typing` (https://docs.python.org/3/library/typing.html) — read
  the top-level narrative, treat the rest as reference.
- The mypy cheat sheet (https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html)
- Glossary: "annotation", "type hint", "generic type"

#### Completion criteria
- Strict checker passes on the whole package; the found-bugs log has honest
  entries.
- You can explain `Any` vs `object`, and ABC-vs-Protocol trade-offs, from
  your own written notes.
- New code you write now gets annotations *as you type it*, not after.

#### Self-assessment quiz
1. What does Python itself do with annotations at runtime?
2. Why does the checker reject `user.name` after `user = find_user(5)` where
   the return is `User | None` — and what are two idiomatic fixes?
3. When would you choose `TypedDict` over a dataclass?
4. What's the difference between `Any` and `object` when you call a method
   on the value?
5. Which does FastAPI use annotations for: documentation, validation,
   conversion, or all three?

---

### Phase 11 — Testing

**Difficulty:** ★★★★☆ (Advanced)  ·  **TaskForge v0.4b: tested**

#### Learning objectives
- Write pytest tests as a design activity, not an afterthought.
- Use fixtures, parametrization, `tmp_path`, and monkeypatching fluently.
- Learn what makes code testable — and refactor what isn't.
- FastAPI testing (`TestClient`, dependency overrides) is this phase plus
  one import.

#### Topics and subtopics
- pytest basics: discovery, plain `assert`, reading failure output
  (pytest's assertion introspection is a teaching tool — use it).
- Arrange–Act–Assert; naming (`test_<unit>_<scenario>_<expectation>`).
- Testing exceptions: `pytest.raises`, checking the message and carried
  data (your Phase 5 exceptions).
- Fixtures: setup/teardown via `yield` fixtures (Phase 8/9 machinery
  again!), fixture composition, scopes.
- Built-in fixtures: `tmp_path` (all file tests), `capsys`, `monkeypatch`.
- `@pytest.mark.parametrize` — one behavior, many cases, including the
  hostile inputs from your Phase 5 `abuse.py`.
- Test doubles: hand-rolled fakes (a `MemoryRepository` *is* one — you
  already built it) vs `unittest.mock` / `MagicMock`; patching where it's
  *looked up*, not where it's defined.
- Coverage (`pytest --cov`): what 85% means and what it doesn't.
- Property-style thinking: round-trip laws (`from_dict(to_dict(t)) == t`).
- What *not* to test: private details, the stdlib, your mocks.

#### Important concepts to understand
- **Testability is a design property.** Pure core + I/O at the edges
  (enforced since Phase 2) is *why* your core tests need no mocks. Pain
  while testing is feedback about coupling — refactor the code, don't
  build a mock tower.
- The repository Protocol earns its keep here: service-level tests run
  against `MemoryRepository`, exactly how you'll override a DB dependency
  in FastAPI tests.
- A test you watched fail is worth ten that were born green — make a test
  fail on purpose (break the code, not the test) to validate it.
- Parametrized edge-case tables (empty, one, many, duplicate, hostile) are
  where the bugs live.
- Coverage measures *executed*, not *verified* — 100% coverage with weak
  asserts is a false passport.

#### Small coding exercises (`exercises/phase11/`)
1. **test_textstats.py** — Test the Phase 2 toolkit: parametrize
   `word_count` over 6 cases (empty, punctuation, unicode, repeated);
   `pytest.raises` where relevant. Fix any bug you find (you will).
2. **test_atomic.py** — Using `tmp_path`: prove `atomic_write` leaves the
   original intact when the body raises (your Phase 6 claim, now enforced
   forever).
3. **fixture_compose.py** — Fixtures `sample_tasks` → `full_repo`
   (composition); tests use them; add a `yield`-fixture that verifies an
   invariant at teardown (e.g., no duplicate ids after any test).
4. **test_with_fake.py** — A `notify_overdue(repo, clock, notifier)`
   function; test it with a fake clock (fixed `now`) and a recording fake
   notifier — no mock library. Then repeat with `MagicMock` and
   `assert_called_once_with`; compare readability in comments.
5. **failing_first.py** — TDD one function: red (write the failing test
   first), green (minimal fix), refactor. `roman_numeral(n)` is a good
   candidate. Commit at each stage so the history shows the cycle.

#### Larger practical assignment — **TaskForge v0.4b: the test suite**
- `tests/` mirrors `src/`: `test_models.py`, `test_repository.py`,
  `test_reports.py`, `test_storage.py`, `test_cli.py`.
- Requirements:
  - Model invariants: title validation, `complete()` idempotence,
    round-trip law `from_dict(to_dict(t)) == t` parametrized over tricky
    tasks (unicode titles, empty tags, all priorities).
  - Both repositories pass **the same test suite**: write the tests once
    against the Protocol, parametrize over implementations (fixture
    returning each) — interface-driven testing.
  - `JsonRepository` tests on `tmp_path` only; include corrupt-file →
    `StorageError` (with chained cause) and crash-mid-save (the Phase 6
    kill test, automated).
  - Report/pipeline tests including `groupby` edge cases and
    exhausted-iterator regressions.
  - CLI: `capsys`-based tests for 3 commands end-to-end on a temp repo.
  - Coverage ≥85% on `src/taskforge`; write in `NOTES.md` what the
    uncovered lines are and why they're acceptable (or fix them).
- The refactor rule: anything that required painful mocking gets redesigned
  (usually: extract pure function, inject dependency). Log each such
  redesign — this list is your personal "what makes code testable" essay.

#### Common mistakes and pitfalls
- Tests that mirror implementation (asserting internal calls) — they break
  on every refactor while catching no bugs.
- Shared mutable state between tests (module-level task lists); order-
  dependent tests.
- Patching where defined instead of where used.
- Testing happy paths only — your Phase 5 hostile inputs are the real suite.
- One giant test function asserting twenty things — first failure hides the
  rest.
- Chasing 100% coverage into `__repr__` and trivial getters while service
  logic edge cases go untested.

#### Recommended documentation
- pytest docs: "Get started", "How to use fixtures", "Parametrize"
  (https://docs.pytest.org/en/stable/)
- Library: `unittest.mock` — the "where to patch" section is required
  reading (https://docs.python.org/3/library/unittest.mock.html#where-to-patch)

#### Completion criteria
- `pytest` green; coverage ≥85%; the shared repository suite runs against
  both implementations via parametrization.
- You watched every new test fail at least once (break code, not test).
- You can name, from your own log, two refactors that testing pressure
  caused — and why the code is better.

#### Self-assessment quiz
1. Why does `MemoryRepository` make service tests fast *and* trustworthy —
   and what is the FastAPI equivalent of this move?
2. What does a `yield` in a pytest fixture do before and after the test?
3. You need to patch `taskforge.storage.datetime.now` — why might patching
   `datetime.datetime` globally not work? ("Where to patch.")
4. Give two things 90% coverage does *not* tell you.
5. When is `MagicMock` the wrong tool even though it would work?

---

### Phase 12 — Debugging, Logging, and Standard-Library Essentials

**Difficulty:** ★★★☆☆ (Advanced)  ·  **TaskForge v0.4 complete**

#### Learning objectives
- Debug with tools (pdb, breakpoints, tracebacks) instead of print-spray.
- Set up `logging` the way applications should: module loggers, levels,
  formatting, and configuration at the entry point only.
- Round out your stdlib toolbelt: `argparse`, `datetime`, `collections`,
  `re`, and friends — the "essentials" pass.

#### Topics and subtopics
- Reading tracebacks bottom-up; chained tracebacks (`from err` from
  Phase 5 paying off).
- `breakpoint()` / pdb: `n`, `s`, `c`, `l`, `p`, `pp`, `w`, `up/down`;
  post-mortem debugging (`pytest --pdb`).
- `logging`: `getLogger(__name__)`, levels, `basicConfig` at the entry
  point only, format strings, `logger.exception()` in `except` blocks,
  lazy `%`-style args vs eager f-strings, `RotatingFileHandler`
  (recognition), why `print` is not logging.
- `argparse`: subcommands (`add`, `ls`, `done`…), typed arguments,
  defaults, `--verbose` count flag.
- `datetime`: aware vs naive (**always UTC internally**,
  `datetime.now(tz=timezone.utc)`), `timedelta`, `isoformat/fromisoformat`,
  formatting for humans at the edge.
- `collections`: `Counter`, `defaultdict`, `deque`, `namedtuple` — replace
  hand-rolled versions from earlier phases.
- `re` essentials: `search/match/findall/sub`, groups, raw strings; when
  string methods beat regex.
- Quick tour (recognition level): `secrets` vs `random`, `hashlib`,
  `subprocess.run`, `sys.argv/exit`, `os.environ`, `time.perf_counter`,
  `textwrap`, `pprint`.

#### Important concepts to understand
- Debugging is hypothesis-driven: predict, probe, confirm — a debugger is
  faster than prints once stepping is muscle memory; `pytest --pdb`
  drops you *into* a failing test's frame.
- Libraries call `getLogger(__name__)` and never configure; the
  application configures once at the entry point. Mixing these two roles
  is the number-one logging mess in real codebases.
- `logger.exception("...")` inside `except` captures the traceback —
  chained causes from Phase 5 appear automatically in logs.
- Naive datetimes are bugs waiting for a timezone; store/compare in UTC,
  render local at the edge (same edge where I/O already lives).
- `Counter` and `defaultdict` aren't conveniences — they remove the
  bug-prone initialization dance you hand-wrote in Phase 3.

#### Small coding exercises (`exercises/phase12/`)
1. **debug_me.py** — Take this roadmap's gift: write a function with three
   planted bugs (off-by-one slice, mutable default, wrong dict key), then
   find all three *using only pdb* — no prints, no staring. Write the pdb
   commands you used in comments.
2. **log_layers.py** — Two modules with `getLogger(__name__)` and a main
   that configures level/format via `--verbose`; show the same run at
   WARNING vs DEBUG; add `logger.exception` catching a chained error and
   inspect the output.
3. **argdemo.py** — Rebuild your Phase 2 text-stats driver with argparse
   subcommands and typed flags; `--help` output must be genuinely helpful.
4. **dates.py** — Given ISO task timestamps: which are older than 7 days;
   group by calendar week; print "3 days ago"-style humanized ages. All
   math in UTC; all display local.
5. **counter_refactor.py** — Rewrite three earlier exercises
   (word-frequency, invert-dict, log-level counts) with
   `Counter`/`defaultdict`; diff the line counts.
6. **regex_extract.py** — From the fake server log: extract IPs and request
   paths with groups; then one task where a plain `split` beats the regex —
   and say why.

#### Larger practical assignment — **TaskForge v0.4: production-grade CLI**
- Replace the hand-rolled REPL parser with `argparse` subcommands
  (`taskforge add "title" --tag work --priority high --due 2026-08-01`,
  `taskforge ls --pending --tag work --top 5`, `export/import`, `stats`).
  Keep the REPL as `taskforge repl` if you like it.
- Logging end-to-end: module loggers everywhere; `-v/-vv` controls level;
  file log at `~/.taskforge/taskforge.log`; the Phase 9 `@timed` decorator
  now logs at DEBUG instead of printing; the CLI boundary logs unexpected
  exceptions with `logger.exception` before exiting nonzero (now — and
  only now — the boundary catches `Exception`).
- `Task.created_at`/`due` become timezone-aware UTC; humanized display in
  `ls` ("due in 3 days", "overdue by 2 days") — reports from Phase 8
  updated.
- All tests still green; new tests for date logic (fake clock fixture from
  Phase 11 pays off) and one `capsys` test asserting log output at DEBUG.

#### Common mistakes and pitfalls
- Debugging by print-and-rerun for an hour when two minutes of
  `pytest --pdb` would answer it.
- `logging.basicConfig` (or handler setup) inside library modules.
- Logging *and* re-raising *and* catching again upstream — the same error
  three times in the log.
- Naive/aware datetime mixing (`TypeError` at comparison — or worse,
  silently wrong math across DST).
- Regex for structured formats that have parsers (JSON, CSV) or for what
  `in`/`startswith` handles; and catastrophic `.*` overreach.
- Swallowing the exit code: CLI errors should `sys.exit(nonzero)` — shells
  and CI depend on it.

#### Recommended documentation
- Logging HOWTO + Cookbook (https://docs.python.org/3/howto/logging.html)
- Library: `pdb` (https://docs.python.org/3/library/pdb.html), `argparse`
  + its tutorial (https://docs.python.org/3/howto/argparse.html),
  `datetime` (https://docs.python.org/3/library/datetime.html),
  `collections` (https://docs.python.org/3/library/collections.html)
- Regex HOWTO (https://docs.python.org/3/howto/regex.html)

#### Completion criteria
- You solved `debug_me.py` with pdb alone and can step through a failing
  test with `pytest --pdb` comfortably.
- `taskforge --help` reads like a tool you'd ship; `-vv` shows a coherent
  DEBUG story of one command's execution.
- No naive datetimes anywhere; grep proves it.

#### Self-assessment quiz
1. In pdb, what's the difference between `n` and `s`? How do you inspect a
   variable two frames up?
2. Why do libraries call `getLogger(__name__)` but never configure
   handlers?
3. What extra thing does `logger.exception(...)` record over
   `logger.error(...)`?
4. Why is `datetime.now()` without a timezone a code smell in a backend?
5. Rewrite `d = {}` / `for w in words: d[w] = d.get(w, 0) + 1` in one line
   with the right `collections` tool.

---

### Phase 13 — Concurrency: Threads, Processes, and asyncio

**Difficulty:** ★★★★★ (Advanced)  ·  **TaskForge v0.5**

#### Learning objectives
- Know the three models — threads, processes, async — and *choose by
  workload*: I/O-bound-and-few → threads; CPU-bound → processes;
  I/O-bound-and-many → asyncio.
- Write correct `asyncio` code: this is the single most important phase for
  FastAPI, whose entire request model is an event loop.

#### Topics and subtopics
- Concurrency vs parallelism; the GIL — what it actually prevents (parallel
  bytecode) and what it doesn't (I/O overlap); the free-threading era
  exists (recognition level) but design for the GIL model.
- `threading`: `Thread`, race conditions (build one!), `Lock`,
  thread-safe queues (`queue.Queue`); daemon threads.
- `concurrent.futures`: `ThreadPoolExecutor` / `ProcessPoolExecutor`,
  `executor.map`, `as_completed` — the high-level API you should reach for
  first.
- `multiprocessing` realities: pickling, spawn vs fork, why
  `if __name__ == "__main__"` guards matter here (Phase 4 payoff).
- `asyncio`: `async def` / `await`; coroutines vs tasks;
  `asyncio.run`, `create_task`, `gather` (and `return_exceptions`),
  `wait_for` / `timeout`; `asyncio.sleep` vs `time.sleep` (the cardinal
  sin); async generators & `async for`; `async with` (Phase 9 mapped to
  async); `asyncio.to_thread` for escaping to blocking code.
- The one mental model: the event loop runs ONE thing at a time and only
  switches at `await` — cooperative, not preemptive.
- How this maps to FastAPI: `async def` endpoints must not block; sync
  endpoints get a thread; `await` is where other requests make progress.

#### Important concepts to understand
- **Blocking the loop starves everyone**: one `time.sleep(1)` (or heavy
  CPU) inside `async def` freezes *all* concurrent tasks. In FastAPI, that
  is one slow endpoint freezing the whole worker. `asyncio.to_thread` and
  process pools are the escape hatches.
- A race condition is not a rare event — it is a certainty you haven't
  observed yet. You will build one (unsynchronized counter), watch it lose
  updates, and fix it with a `Lock`; then prefer designs (queues, executors,
  message passing) where no state is shared at all.
- `await` marks the *only* points where an async task can be interrupted —
  between awaits, your code is atomic w.r.t. the loop. This is why async
  code needs fewer locks, and why one blocking call is so poisonous.
- Coroutines do nothing until awaited/scheduled — calling `fetch()` without
  `await` is a silent no-op bug (a warning if you're lucky).
- Executors + `map`/`as_completed` solve 90% of thread/process needs
  without a single manual `Thread` or `Lock`.

#### Small coding exercises (`exercises/phase13/`)
1. **race.py** — Two threads increment a shared counter 100k times each
   without a lock; run 5 times, record the (wrong, varying) totals; fix
   with `Lock`; then rewrite with `ThreadPoolExecutor.map` + `sum` so no
   state is shared at all. Three versions, one file.
2. **io_pool.py** — Simulate 10 "downloads" (`time.sleep(0.5)` each):
   sequential vs `ThreadPoolExecutor(max_workers=5)`; measure with
   `perf_counter`; explain the ~5x, and why the GIL didn't prevent it.
3. **cpu_pool.py** — A CPU-heavy function (e.g., sum of squares to 10⁷) ×4:
   sequential vs threads vs processes, timed. Threads won't help; processes
   will. Write the two-line explanation.
4. **first_async.py** — `async def fetch(name, delay)` with
   `asyncio.sleep`; run three sequentially (awaits in a row) vs
   concurrently (`gather`); timings prove the model. Then replace one
   `asyncio.sleep` with `time.sleep` and watch concurrency die — the most
   important negative result in this roadmap.
5. **task_timeout.py** — `gather` five tasks with random delays under
   `asyncio.timeout`/`wait_for`; handle the timeout; then
   `gather(..., return_exceptions=True)` with one task raising — inspect
   what comes back.
6. **async_producer.py** — Producer/consumer with `asyncio.Queue`: one
   producer, three consumers, sentinel/`task_done` shutdown done cleanly.
7. **to_thread.py** — An async main that needs a blocking function (your
   JSON `load_tasks`): first call it directly inside async (observe/reason
   about the freeze with a concurrent heartbeat task printing dots), then
   via `asyncio.to_thread` — heartbeat keeps beating.

#### Larger practical assignment — **TaskForge v0.5: concurrent edges**
Real backends do concurrent I/O at the edges while the core stays sync and
pure — build exactly that:
- **Concurrent import**: `taskforge import csv a.csv b.csv c.csv` parses
  files in a `ThreadPoolExecutor`, merges results in the main thread (no
  shared mutation), reports per-file successes/failures via
  `as_completed`.
- **Async sync-client**: a new module `sync.py` simulating "push tasks to a
  server": `async def push_task(task)` (latency = `asyncio.sleep`, a few
  % random failures). `taskforge push` pushes all pending tasks with
  bounded concurrency (an `asyncio.Semaphore(5)`), a timeout per push,
  `gather(return_exceptions=True)`, retry-once on failure (port the retry
  idea to async), and a final report: pushed/failed/duration. Repository
  writes stay in the main flow — document *why* (single-writer rule).
- A `--sequential` flag for A/B timing, logged via Phase 12 logging.
- Tests: pytest with async tests (anyio/pytest-asyncio) for `push_task`
  success/failure/timeout paths using a fake with controllable delays —
  your fake-clock instincts from Phase 11 extended to async.

#### Common mistakes and pitfalls
- `time.sleep` / `requests` / heavy CPU inside `async def` — blocking the
  loop (the #1 FastAPI performance bug in the wild).
- Forgetting `await`: `push_task(t)` alone creates a coroutine and drops
  it.
- Creating tasks and never awaiting/gathering them (silent cancellation at
  loop shutdown, lost work).
- Unbounded concurrency: `gather` on 10k coroutines with no semaphore.
- Sharing mutable state across threads "just this once."
- Threads for CPU-bound work (GIL), processes for tiny tasks (overhead
  dominates), async for CPU (wrong tool entirely).
- Missing `if __name__ == "__main__":` with multiprocessing on
  spawn-platforms — infinite process bombs.

#### Recommended documentation
- Library: `asyncio` — start with "Coroutines and Tasks"
  (https://docs.python.org/3/library/asyncio-task.html)
- `concurrent.futures` (https://docs.python.org/3/library/concurrent.futures.html)
- `threading` (https://docs.python.org/3/library/threading.html),
  `queue`, `multiprocessing` — guarded-main section
- Glossary: "GIL", "coroutine", "awaitable"

#### Completion criteria
- Your three timing experiments (io_pool, cpu_pool, first_async) produce
  the predicted shapes, and you can explain each in two sentences from the
  GIL/event-loop model.
- `taskforge push` handles 50 fake tasks with bounded concurrency,
  timeouts, retries, and a truthful report; async tests green.
- You can state precisely when you'd pick threads vs processes vs asyncio
  — and what breaks if an async endpoint blocks.

#### Self-assessment quiz
1. Why do threads speed up simulated downloads but not sum-of-squares?
   Where exactly is the GIL in each story?
2. What happens, line by line, when you call an `async def` function
   without `await`?
3. `await asyncio.sleep(0)` — what is this idiom for?
4. Why does one `time.sleep(1)` in one coroutine delay *all* tasks, while
   `asyncio.sleep(1)` delays only its own?
5. In FastAPI: endpoint does a blocking DB call. What are your three
   options (change endpoint to sync def / to_thread / async driver) and
   the trade-offs?

---

### Phase 14 — Performance and Memory

**Difficulty:** ★★★★★ (Senior)  ·  **TaskForge v0.9**

#### Learning objectives
- Measure before optimizing — always; profile, find the real hot spot, fix
  it, measure again.
- Know the cost model of Python's structures (the Phase 3 promises, now
  with numbers) and the standard optimization moves.
- Understand memory behavior: references, `sys.getsizeof`, `__slots__`,
  generators-as-memory-tool revisited.

#### Topics and subtopics
- The optimization discipline: correctness first, measure, optimize the
  proven hot spot only, re-measure; "premature optimization" in practice.
- `timeit` for micro; `time.perf_counter` for sections; `cProfile` +
  `pstats` (sort by cumulative/tottime) for programs; profiling *tests* as
  a shortcut to hot paths.
- Big-O in practice: list `in` vs set `in`; dict lookup; `list.insert(0)`
  vs `deque.appendleft`; string `+=` vs `join` — *measure each*, don't
  recite.
- Common speedups: hoist work out of loops, precompute, right data
  structure, batch I/O, `functools.cache` (Phase 9 payoff), local variable
  binding in hot loops (know it exists; use it last).
- Memory: names/references recap, `sys.getsizeof` and its limits,
  list-of-dataclasses vs `slots=True` vs tuples (measure with
  `tracemalloc`), generators for streaming (Phase 8 as a memory strategy).
- `tracemalloc` for "where did the memory go"; reference cycles and `gc`
  (recognition level).
- When Python is the wrong layer: numpy/C extensions/subprocess — know the
  exits exist (recognition level).

#### Important concepts to understand
- **The hot spot is never where you think.** The whole discipline exists
  because intuition about performance is reliably wrong — including after
  years of experience. Profile output beats opinion, every time.
- Most real-world Python slowness is algorithmic (O(n²) hiding in a loop
  with `in list`, or n+1 I/O operations), not "Python is slow." Fixing the
  algorithm gives 100x; micro-tricks give 1.1x.
- A benchmark must be honest: same data, warm caches, multiple runs,
  realistic size. `timeit` handles the ceremony for micro-benchmarks.
- Generators trade memory for recomputability; lists trade memory for
  random access and re-iteration — you've used both, now you can *price*
  them.
- Optimize for the reader first: fast-but-unreadable is a cost you pay on
  every future change. Readability is the default; speed is a requirement
  with a number attached.

#### Small coding exercises (`exercises/phase14/`)
1. **contains.py** — Membership test of 10k needles against list vs set vs
   dict at sizes 1k/10k/100k with `timeit`; graph or table the growth
   shapes; connect to the Phase 3 warning.
2. **concat.py** — Build a 100k-piece string via `+=` vs `"".join(...)` vs
   `io.StringIO`; explain the quadratic shape you observe.
3. **profile_me.py** — Write a deliberately slow pipeline (nested-loop
   dedupe, repeated file reads inside the loop, per-item sort); `cProfile`
   it; fix ONLY the top item; re-profile; repeat until diminishing
   returns. Keep the profile snapshots as comments — the narrative is the
   deliverable.
4. **slots_mem.py** — One million `Task`-like objects: dict-based
   dataclass vs `slots=True` vs plain tuple; measure with `tracemalloc`;
   report bytes/object.
5. **cache_win.py** — An expensive pure function called with repeating
   args in a loop; measure, add `functools.cache`, measure; then show a
   case where caching is *wrong* (mutable arg or time-dependent result).
6. **generator_mem.py** — Sum a 10-million-line synthetic file's numbers:
   list-based vs generator-based; `tracemalloc` peak for each.

#### Larger practical assignment — **TaskForge v0.9: profile and tune**
- Build a data generator: `taskforge seed 100000` creates 100k synthetic
  tasks (varied tags, dates, priorities).
- Write a benchmark script `bench.py` (perf_counter + repetitions) for:
  load, save, `ls` with filters, `search`, `stats`, CSV export.
  Record baseline numbers in `NOTES.md`.
- Profile the two slowest operations with `cProfile`; form a hypothesis
  *in writing* before looking at the code; then fix. Likely findings you
  planted along the way: linear `get(id)` scans → index dict in the
  repository; per-call JSON reloads; sorting inside loops; `in list`
  membership.
- Constraints: public API unchanged (tests stay green — Phase 11 payoff);
  each optimization is one commit with before/after numbers in the commit
  message; stop when the top remaining cost is I/O or under your target.
- Add `slots=True` to `Task` and measure the memory delta on the 100k
  seed; keep it only if it's a real win.
- Write a half-page performance report in `NOTES.md`: what was slow, how
  you found it, what you did, what you *chose not to do* and why. Senior
  engineers are distinguished by the last item.

#### Common mistakes and pitfalls
- Optimizing without measuring (the cardinal sin); optimizing the wrong
  layer (micro-tuning code that's 2% of runtime).
- Benchmarking unrealistically: tiny data, cold vs warm confusion, one
  run, debug logging left on.
- Caching functions with mutable arguments or side effects.
- `sys.getsizeof` on a container and believing it (it doesn't include
  referenced objects — use `tracemalloc` for truth).
- Sacrificing the architecture (merging layers "to be fast") for
  single-digit-% wins.
- Cargo-culted tricks (`__slots__` everywhere, `map` vs comprehension
  wars) without numbers.

#### Recommended documentation
- Library: `timeit` (https://docs.python.org/3/library/timeit.html),
  `profile`/`cProfile` (https://docs.python.org/3/library/profile.html),
  `tracemalloc` (https://docs.python.org/3/library/tracemalloc.html)
- "Time Complexity" of CPython operations (https://wiki.python.org/moin/TimeComplexity)
- `functools.cache`/`lru_cache` docs

#### Completion criteria
- `bench.py` shows measured, honest improvements on the seeded 100k
  dataset with the test suite untouched and green.
- Your performance report exists and includes at least one "measured it,
  left it alone" decision.
- You can sketch the list/set/dict cost table from memory and cite your
  own measurements.

#### Self-assessment quiz
1. What is the first command you run when "the app is slow" — and what is
   the first thing you do *before* reading the code?
2. Why is `s += piece` in a loop quadratic? What are two fixes?
3. What does `__slots__` remove from each instance, what does it cost you
   in flexibility, and how would you *verify* the memory win?
4. `cProfile` says a function has huge `cumtime` but tiny `tottime` —
   what does that tell you and where do you look next?
5. When is a generator *slower* than a list despite using less memory?

---

### Phase 15 — Pythonic Design and Application Architecture

**Difficulty:** ★★★★★ (Senior)  ·  **prepares the v1.0 capstone**

#### Learning objectives
- Consolidate everything into design judgment: layering, dependency
  direction, cohesion — and the ability to *explain* your choices.
- Apply SOLID the Pythonic way (protocols and functions, not class
  ceremonies).
- Design the architecture you will reuse for every FastAPI service:
  domain / services / adapters / entry-points.

#### Topics and subtopics
- The Zen of Python (`import this`) applied to real trade-offs — explicit
  over implicit, flat over nested, errors never silent (you've lived each
  one by now; make them explicit rules).
- Idiom sweep: EAFP, unpacking, comprehensions, `enumerate`/`zip`,
  truthiness, `with` everywhere — codifying habits into review checklists.
- SOLID in Python: SRP (one sentence per module/class — you've practiced
  since Phase 7), OCP via the registry/dispatch pattern (since Phase 2!),
  LSP (Phase 7), ISP (small protocols, Phase 10), DIP (repository,
  Phase 7 — now named and generalized).
- Layered architecture: domain (models, pure logic) ← services (use
  cases) ← adapters (storage, sync client) ← entry points (CLI; later,
  FastAPI routers). Dependencies point inward, ONLY.
- Dependency injection in Python: pass dependencies as parameters —
  no framework needed; composition root (`__main__.py`) as the single
  place where concrete objects are built and wired.
- Configuration: environment variables (`os.environ`) + a typed frozen
  `Config` dataclass built at the composition root; no scattered
  constants, no global mutable config.
- API design: naming, keyword-only booleans, small surfaces,
  `__init__.py` as the public face; docstrings that state contracts
  (args, returns, raises).
- Anti-pattern catalog from your own history: god module, circular
  imports, global state, boolean traps, deep nesting → early returns.
- Code review practice: review your own Phase 3 code with senior eyes;
  write the review as if to a junior colleague.

#### Important concepts to understand
- **Dependency direction is the architecture.** Everything else is
  decoration. `core`/`models` import nothing of yours; `cli` imports
  everything; never the reverse. You enforced this since Phase 4 — now
  you can defend *why*: the inner layers are the stable, testable,
  reusable asset.
- The composition root pattern: exactly one place knows the concrete
  wiring (which repository, which config, which logger setup). Everything
  else receives its dependencies. This is FastAPI's `Depends` — minus the
  framework.
- Every abstraction has a cost. A protocol with one implementation and no
  test-double need is ceremony; the senior skill is *deciding*, in
  writing, which abstractions pay rent. Revisit each of yours.
- Pythonic SOLID: "interfaces" are usually a function parameter typed
  with a small Protocol, and "strategy pattern" is passing a function.
  If a design pattern adds a class that only wraps one method — pass the
  method.
- Boring is a feature: predictable structure, stdlib-first, few clever
  tricks. Senior code is code a mid-level engineer can extend without
  fear.

#### Small coding exercises (`exercises/phase15/`)
1. **zen_violations.py** — Write six short snippets each violating a Zen
   line (nested where flat works, silent `except`, implicit magic…);
   fix each; label with the line it violates. Fastest deep review of the
   Zen there is.
2. **strategy.py** — A report formatter three ways: if/elif chain →
   class-based strategy pattern → dict-of-functions registry. Write the
   two-sentence verdict on when each earns its keep.
3. **di_kata.py** — A `ReminderService` needing a clock, a repository,
   and a notifier: wire it with hard-coded globals (bad), then with
   constructor injection + a composition root; write the same test twice
   against both versions and let the diff argue for you.
4. **config.py** — A frozen `Config` dataclass loaded from `os.environ`
   with defaults and validation at the root; threaded down into two
   services as plain parameters — no module reads `environ` except the
   root.
5. **review_yourself.py** — Take your actual Phase 3 `core.py` from git
   history; write a numbered code review (12+ findings, each with the
   phase whose lesson it violates). This document is your own progress
   report, in your own voice.

#### Larger practical assignment — **Capstone architecture (design doc)**
Before writing capstone code, write `docs/architecture.md` (1–2 pages):
- The four layers of TaskForge v1.0, what lives in each, and the import
  rules between them (a simple diagram — ASCII is fine).
- Every abstraction (protocols, base classes) and one sentence on why
  each pays rent — plus at least one you *removed* for not paying.
- Config strategy, error-handling strategy (where raised, where caught,
  what the user sees), logging strategy, and the concurrency boundary.
- A "how this maps to FastAPI" column: which module becomes routers,
  which becomes dependencies, what Pydantic replaces.
This document is a senior deliverable in its own right: architecture you
can *articulate* is the skill interviews and design reviews test.

#### Common mistakes and pitfalls
- Abstraction ceremony: patterns imported from Java that a function
  solves (the "kingdom of nouns").
- The opposite sin: "simple" scripts where one 400-line module secretly
  contains four layers — cohesion by proximity is not cohesion.
- Global mutable state as invisible coupling (config singletons, module-
  level caches touched from everywhere).
- Boolean parameters multiplying (`f(True, False, True)`) — keyword-only
  arguments, enums, or separate functions.
- Designing for imagined future requirements ("we might need MongoDB")
  while real requirements (testability, today) go unserved.
- Writing the architecture doc *after* the code as fiction, instead of
  before as a plan.

#### Recommended documentation
- The Zen: `python -c "import this"`
- PEP 8 (https://peps.python.org/pep-0008/) — full read now that every
  rule has context; note where your habits differ and decide consciously.
- Glossary end-to-end (https://docs.python.org/3/glossary.html) — you
  now know essentially every entry; the ones you don't are your reading
  list.
- Revisit `itertools` recipes and `functools` docs with senior eyes.

#### Completion criteria
- `architecture.md` exists and a colleague (or mentor — bring it to me)
  could implement the capstone from it without asking you questions.
- Your self-review of Phase 3 code has 12+ substantive findings.
- You can explain dependency direction, composition root, and
  "abstractions must pay rent" without notes — these three carry most
  senior design interviews.

#### Self-assessment quiz
1. Which direction do dependencies point in a layered application, and
   what concretely breaks (name two things) when one arrow reverses?
2. What is a composition root? What is the FastAPI feature that plays
   this role?
3. A "strategy pattern" in idiomatic Python is often just — what?
4. Give two signals an abstraction is NOT paying rent, and two that it
   is.
5. Your teammate proposes `utils.py`. Make the senior argument about
   cohesion — where should its contents live?

---

## 4. Assignments and Milestone Projects — the TaskForge Thread

How the one project grows across phases (each milestone is also your
refactor checkpoint):

| Milestone | After phase | What TaskForge gains | Skills locked in |
|---|---|---|---|
| v0.1 | 3–4 | In-memory task store, REPL, installable package with entry point | data structures, functions, project layout |
| v0.2 | 5–6 | Custom exception hierarchy + error boundary; atomic JSON persistence; CSV import/export | error design, files, formats, durability |
| v0.3 | 7–9 | `Task` dataclass + enum; swappable repositories (memory/JSON); streaming reports; `@timed`/`@retry`; storage as context manager | OOP, iteration, decorators, context managers |
| v0.4 | 10–12 | Strict typing (checker in CI-style script); ≥85% test coverage with interface-driven tests; argparse CLI; structured logging; UTC-aware dates | typing, testing, tooling, stdlib |
| v0.5 | 13 | Threaded multi-file import; async push client with semaphore, timeouts, retries; async tests | concurrency models, asyncio |
| v0.9 | 14 | 100k-task seeding; benchmark suite; profiled + optimized (indexes, caching, slots) with a written report | performance discipline |
| v1.0 | 15 | Capstone (below), built to the architecture doc | design & architecture |

Standalone milestone projects (outside TaskForge, for breadth — do them if a
phase's material needs another rep):

- **After Phase 6 — Log Analyzer CLI**: point at a directory of log files,
  stream-parse, aggregate by level/hour, output JSON or CSV summary. (files,
  generators-preview, argparse later)
- **After Phase 9 — Mini Cache Library**: an `@cached(ttl=...)` decorator
  with a pluggable backend (dict, JSON file), a `with cache.batch():`
  context manager, tests. Package it and `pip install -e .` it into another
  project. (decorators, CMs, packaging)
- **After Phase 13 — Concurrent Site Checker**: read 200 URLs from a file,
  check reachability with bounded async concurrency + timeouts, write a CSV
  report, compare against a threaded version. (asyncio, files, argparse)

---

## 5. Final Python Capstone Project — TaskForge v1.0

**Goal:** a portfolio-grade application proving every phase, built to your
Phase 15 architecture doc. This is the project you bring to the FastAPI
roadmap — where it becomes a real web service.

### Scope

Layered layout (names indicative):

```
src/taskforge/
├── domain/        # models.py, errors.py — imports nothing of yours
├── services/      # tasks.py, reports.py, sync.py — use cases, pure logic
├── adapters/      # json_repo.py, sqlite_repo.py, csv_io.py, push_client.py
├── cli/           # argparse entry points, formatting, error boundary
├── config.py      # frozen Config from environment
└── __main__.py    # composition root: build config → wire adapters → run
```

Required capabilities (almost all are upgrades of things you built):

1. **Domain**: `Task` (+`Project` grouping — one genuinely new entity to
   force a design decision under your own rules), validation, invariants.
2. **Storage**: `sqlite3`-backed repository (stdlib — new adapter, same
   Protocol) *and* the JSON repository; a `taskforge migrate` command
   moving data between them. Same interface tests pass for both
   (Phase 11's parametrized suite extended).
3. **Services**: filtering/search/stats as lazy pipelines; recurring
   tasks ("every monday" → next occurrence generation — dates under test);
   overdue detection with the UTC discipline.
4. **Async edge**: the push client behind a Protocol, with bounded
   concurrency, timeout, retry — plus a `--dry-run` mode.
5. **CLI**: full argparse surface with `--json` output flags (machine-
   readable output = your future API responses taking shape).
6. **Quality gates**: strict type-check clean; tests ≥85% including async
   and both repositories; logging with `-v/-vv`; benchmark script with
   recorded numbers on 100k tasks.
7. **Docs**: README (install, usage, examples), `architecture.md` kept
   truthful, CHANGELOG summarizing v0.1→v1.0 — the roadmap itself is your
   material.

### Definition of done

- A stranger can `pip install -e .` and use it from `--help` alone.
- You can add a new storage backend or a new report *without touching*
  domain or services — demonstrate with a short screencast-style walkthrough
  in the README (text is fine).
- Every quality gate passes with one command each (`make check` or a
  `scripts/check.sh`: format, type-check, tests, bench-smoke).
- You can defend three design decisions and name three things you'd do
  differently — written in the README's "Design notes" section.

---

## 6. Readiness Checklist for FastAPI

Move to the FastAPI roadmap when you can honestly check every box. "Explain"
means out loud, unaided, in a couple of sentences.

**Language mechanics**
- [ ] I can write `def f(a, /, b, *args, c, **kwargs)` and predict which
      call forms are valid — and I know why frameworks lean on keyword-only
      parameters.
- [ ] I can explain the mutable-default bug, the aliasing bug, and the
      exhausted-iterator bug — with fixes, from memory.
- [ ] I can desugar a decorator (including a parameterized one) and a
      `with` block into their plain-Python equivalents.

**Data and errors**
- [ ] I convert cleanly between objects and JSON-safe dicts, including
      sets/datetimes, and know why annotations alone don't validate
      (the gap Pydantic fills).
- [ ] I design exception hierarchies and put the catch at the boundary —
      and I can say what the "boundary" is in a web service.
- [ ] All my persistent writes are atomic; all my datetimes are UTC-aware.

**Design**
- [ ] My code separates pure core from I/O edges, and dependencies point
      inward; I can draw TaskForge's layers from memory.
- [ ] I can explain dependency injection as plain parameter-passing and a
      composition root — and map it to FastAPI's `Depends`.
- [ ] I can argue composition vs inheritance, and ABC vs Protocol, with
      examples I wrote.

**Typing and testing**
- [ ] The type checker runs clean in strict mode on code I write, first
      try, most of the time.
- [ ] I write pytest tests with fixtures and parametrization by default;
      I've tested one interface against two implementations.
- [ ] I have swapped a real dependency for a fake in a test without any
      patching, because the design allowed it.

**Concurrency (the FastAPI gate)**
- [ ] I can explain the event loop model: single-threaded, cooperative,
      switches only at `await`.
- [ ] I know why `time.sleep`/blocking I/O inside `async def` is poison,
      and my three escape hatches.
- [ ] I have written `gather` with a semaphore, timeouts, and
      `return_exceptions=True` — and tests for it.
- [ ] I can say when to choose threads vs processes vs asyncio for a given
      workload, with the GIL in the explanation.

**Operational habits**
- [ ] Module loggers everywhere; configuration only at the entry point;
      `logger.exception` at boundaries.
- [ ] I profile before optimizing and can show a before/after with
      numbers.
- [ ] `make check` (format, types, tests) is muscle memory before every
      commit.

When every box is checked, TaskForge v1.0 is sitting there with a service
layer, typed models, swappable storage, async edges, and tests — the FastAPI
roadmap will begin by putting an HTTP interface on it. See you there.
