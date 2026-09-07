# Definition of Done

A task is complete only when every applicable item is satisfied. Mark
non-applicable items explicitly and explain why.

## Behavior and scope

- [ ] All acceptance criteria and referenced requirements are satisfied.
- [ ] System invariants and architecture boundaries remain intact.
- [ ] Only required and allowed files changed.
- [ ] No unrequested API, data-format, dependency, or architecture change was introduced.
- [ ] No unresolved `UNKNOWN`, `AMBIGUOUS`, or `CONFLICT` affects the result.
- [ ] Affected user journeys, UX rules, and user states were considered.

## Quality

- [ ] New or changed logic has suitable tests, including edge and error cases.
- [ ] Targeted tests and the complete regression suite pass.
- [ ] Formatting, linting, type checking, and build pass.
- [ ] No test was removed, weakened, or skipped without a documented reason.
- [ ] No unexplained warnings, flaky tests, TODOs, or known defects were introduced.
- [ ] Security, privacy, and error-handling rules are satisfied.
- [ ] Applicable `CODE-*` and `ARCH-*` rules are met or approved deviations documented.
- [ ] Dependencies were checked for need, origin, versioning, license, and known risk.
- [ ] SOLID was used as a design review lens without speculative abstractions.
- [ ] KISS and YAGNI were applied without omitting required quality or behavior.
- [ ] Inheritance and public interfaces were reviewed for composition, substitutability, and predictability.
- [ ] Applicable accessibility and platform conventions were verified.
- [ ] UX changes have the usability evidence required by the task.

## Documentation and handoff

- [ ] Behavior, interfaces, and operational documentation are current.
- [ ] Significant decisions are recorded as ADRs.
- [ ] Active external standards are referenced with version, scope, and evidence.
- [ ] The diff was reviewed for unintended and unrelated changes.
- [ ] The handoff lists changed files, checks, results, and remaining risks.

An implementation with failing regression tests is not done. Report checks that
could not run as limitations.
