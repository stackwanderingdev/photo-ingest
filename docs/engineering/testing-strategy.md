# Testing Strategy

## Goals

Tests provide fast feedback, verify requirements, and protect system invariants.
A passing test never overrides a documented requirement.

## Test levels

| Level | Purpose | Dependencies | Execution |
|---|---|---|---|
| Unit | Verify domain rules in isolation | No real external systems | Every change |
| Integration | Verify adapters and technical boundaries | Controlled real components | CI |
| System/E2E | Verify critical user journeys | Representative environment | CI/release |
| Non-functional | Measure NFRs | Defined measurement environment | `<FREQUENCY>` |

## Rules

- Behavior changes require meaningful evidence.
- Test names or metadata reference affected `REQ-*`/`INV-*` where useful.
- Test errors, boundaries, and negative cases alongside the happy path.
- Keep tests deterministic, independent, and reproducible.
- Control network, time, randomness, and filesystem usage.
- Skipped or quarantined tests require a reason and expiry date.
- Never remove or weaken a regression test merely to make CI pass.

## Test data

- Never use production secrets or personal data.
- Keep fixtures small and expressive.
- Make generated data reproducible and document the seed.

## Binding commands

Executable commands live only in `docs/engineering/stack-profile.md`. This
strategy defines which test types are required; the stack profile defines how
to run them.

## Acceptance

- Required suites pass.
- No new unexplained warnings or flaky behavior.
- Critical requirements and invariants have traceable coverage.
- Coverage is diagnostic evidence; a number does not replace meaningful assertions.
