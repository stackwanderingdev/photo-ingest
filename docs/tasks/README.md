# Work Items

Every implementation increment receives a small change contract. Tasks should
cover one use case or tightly bounded technical prerequisite and normally touch
only a few production and test files.

## Workflow

1. Copy `TASK-template.md` to `TASK-NNN-short-title.md`.
2. Reference requirements, invariants, UX rules, ADRs, and allowed files.
3. Clarify acceptance criteria and verification commands before implementation.
4. Set status to `Ready` only when no decision-critical ambiguity remains.
5. Record verification results and risks after implementation.

Split tasks that contain independent use cases, unrelated modules, different
business goals, or no acceptance outcome that fits in one sentence.

## Task index

| Task | Title | Status | Owner |
|---|---|---|---|
| `<TASK-ID>` | `<TITLE>` | `<STATUS>` | `<OWNER>` |

Keep this index synchronized and define each concrete task in exactly one
separate `TASK-NNN-short-title.md` file.
