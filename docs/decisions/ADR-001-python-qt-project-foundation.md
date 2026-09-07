# ADR-001: Python and Qt project foundation

- Status: `Accepted`
- Date: `2026-09-07`
- Decision makers: `Daniel (Architecture Owner)`
- Supersedes: `Not applicable`
- Superseded by: `Not applicable`

## Context

PhotoIngest requires a graphical desktop application for Linux, deterministic
domain behavior, filesystem integration, and automated GUI and non-GUI tests.
The first increment is a non-mutating filesystem import preview. The supported
photo formats and metadata library are not yet decided.

## Decision

Use Python 3.14 and PySide6 with a `pyproject.toml`-based Python project and a
`src/` layout. Use uv for dependency management and locking, pytest and
pytest-qt for tests, Ruff for formatting and linting, and mypy for static type
checking. Start product versioning at `0.1.0` and license the project under MIT.
Use the Minimal UX effort level.

This decision does not select an image or metadata library, packaging format,
MTP integration, or network-source integration. Those choices require the
remaining format and source-architecture decisions.

## Alternatives considered

### Another implementation language or GUI toolkit

- Benefits: Could offer different deployment, native integration, or static-typing characteristics.
- Drawbacks: Would not match the approved Python/Qt foundation.
- Reason not selected: Daniel explicitly accepted the recommended Python and PySide6 stack.

### pip-only dependency management

- Benefits: Uses Python's established package installer directly.
- Drawbacks: Requires additional decisions and tools for project environments and reproducible locking.
- Reason not selected: Daniel accepted uv as the project and dependency manager.

## Consequences

- Positive: GUI, domain, and integration behavior can be tested within one Python project.
- Negative/trade-off: PySide6 adds substantial binary dependencies and its LGPL/GPL/commercial licensing must be respected when distributing binaries.
- Prohibited unless this ADR is superseded: Replacing the accepted runtime, GUI toolkit, dependency manager, test framework, formatter/linter, type checker, or project layout as an incidental implementation choice.
- Required follow-up: Decide supported photo formats and metadata library; complete exact tool versions, commands, manifest, lockfile, and CI in the stack profile.

## Evidence and review

- Affected requirements: `REQ-PREVIEW-001`, `REQ-IMPORT-001`, `NFR-PORT-001` (planned)
- Verification criteria: Project commands execute reproducibly on the supported Linux environment and exercise GUI and non-GUI tests.
- Revisit when: Python 3.14 or a selected tool loses support, distribution requirements change materially, or another target platform is accepted.
