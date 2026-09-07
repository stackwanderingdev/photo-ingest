# Instructions for Coding Agents

These rules apply to the entire repository. Nested `AGENTS.md` files may refine
them for their scope but must not silently override them.

Before project initialization or template maintenance, read
`template-manifest.yml`. Its template version identifies the workflow and
document contract in use; it does not represent the derived product's version.

When changing or releasing this template itself, also follow
`docs/template-governance.md` and update `CHANGELOG.md` for notable changes.

For product development, follow `docs/development-workflow.md`. It defines when
normative artifacts may advance in status and how implementation evidence feeds
back into requirements, UX, architecture, decisions, and tasks.

## Repository entry and project initialization

At the start of work in a repository derived from this template:

1. Read this `AGENTS.md` completely.
2. Read `template-manifest.yml` completely, including its `artifacts` map.
3. Check `derived_project.name` before beginning normal project work.
4. If the value is still `<PROJECT_NAME>`, treat the repository as not yet
   initialized and follow `docs/project-bootstrap/bootstrap.md` before beginning
   implementation work.
5. After initialization, continue to use the artifact map as the machine-readable
   routing contract for project documentation.

Do not infer initialization state from repository age, commit history, README
content, or the presence of source code. The `<PROJECT_NAME>` sentinel is the
canonical initialization-state check.

## Authority and conflicts

Normative sources have the following order of authority:

1. Product, functional, and non-functional requirements
2. Accepted UX rules, accessibility goals, and interaction contracts
3. System invariants and architecture documentation
4. Accepted Architecture Decision Records (ADRs)
5. The current task within the preceding constraints
6. Engineering rules and the Definition of Done
7. Tests and usability evidence
8. Existing code

Explicit user instructions take precedence for the current request, but change
documented product or architecture decisions only when that change is explicitly
part of the request.

Existing code is descriptive, not normative. Tests provide evidence but are not
an independent requirements source. Classify issues as:

- `UNKNOWN`: required behavior is not specified.
- `AMBIGUOUS`: multiple interpretations are possible.
- `CONFLICT`: authoritative sources disagree.

Report exact references and impact. Stop before semantic modification; do not
choose a plausible interpretation independently.

## Scope

Modify only files required and allowed by the current task. Unless explicitly requested, do not:

- refactor or format unrelated code,
- add dependencies,
- change public interfaces, requirements, or architecture,
- remove or skip tests, or weaken assertions,
- suppress warnings through broad exclusions,
- leave new TODOs instead of required functionality.

Preserve unrelated or pre-existing changes made by others.

## Documentation pre-write check

Before creating or modifying documentation:

1. Read the `artifacts` map in `template-manifest.yml`.
2. Determine which existing artifact is authoritative for the intended content.
3. Inspect that artifact and its relevant index or entity directory before writing.
4. If an appropriate artifact exists, update it rather than creating an
   overlapping or parallel document.
5. If no existing artifact adequately covers the responsibility, evaluate whether
   a new artifact has a clear, non-overlapping purpose and fits the repository
   structure. A new document is allowed when that justification exists or when
   explicitly requested.
6. Do not create competing authoritative sources for the same responsibility.
7. When a new document introduces a durable documentation responsibility, update
   the artifact map so future agents can route the same information consistently.

The pre-write check is required even when creating a new document appears more
convenient than updating the existing structure.

## Workflow

For every task:

1. Read the task and all referenced requirements completely.
2. Read the active `docs/engineering/stack-profile.md`.
3. Identify applicable UX, coding, and architecture standards and external profiles.
4. Inspect existing code and relevant tests.
5. Establish current behavior, required behavior, affected files, tests, and conflicts.
6. Plan the smallest verifiable change.
7. Add or modify tests when behavior changes.
8. Implement the smallest sufficient production change.
9. Run targeted checks followed by the regression suite.
10. Review the diff for scope violations and unintended changes.
11. Report changes, verification results, and remaining risks.

Discovery, analysis, planning, verification, and reporting phases are read-only.
During implementation, only files or modules allowed by the task may change.

## Binding project commands

The sole normative command reference is
`docs/engineering/stack-profile.md`. Do not infer commands from filenames or
another technology stack. Before the first implementation task, it must define
installation, formatting check, linting, type checking, targeted and complete
tests, build, and local start commands.

`<COMMAND>` means `not configured` and must never be executed. If an operation
does not apply, the stack profile must state `Not applicable` and explain why.

Report missing tools and checks that could not run. Never claim full verification
when required checks were not executed.

## General design rules

- Keep responsibilities and dependencies explicit.
- Separate domain logic from UI, transport, persistence, and operating-system access.
- Encapsulate side effects at clear system boundaries.
- Prefer deterministic behavior and avoid hidden global state.
- Handle errors at the appropriate boundary while preserving their cause.
- Do not silently weaken security, privacy, or backward compatibility.
- Comments explain decisions and constraints, not obvious code.

Project-specific rules in `docs/architecture/dependency-rules.md` and
`docs/engineering/coding-guidelines.md` must replace abstract slogans with
concrete, verifiable statements.

Identifiers `UX-*`, `CODE-*`, `ARCH-*`, `DEP-*`, `REQ-*`, `NFR-*`, and `INV-*`
are binding references. If a rule does not apply, keep it and document why it is
outside the task or project scope.

Growing, independently referenceable artifacts use one concrete entity per
file. This applies to `PRD-*`, `REQ-*`, `NFR-*`, `INV-*`, `UJ-*`, `ADR-*`, and
`TASK-*`. Store them in their documented artifact directories and keep the
corresponding index synchronized. Do not append multiple entities to an index or
to another entity file. Standards catalogs such as `CODE-*`, `ARCH-*`, and
`UX-*` remain grouped because their ordering and combined review are part of the
standard contract.
