# Coding Standards and Best Practices

These rules are the technology-independent minimum standard. The active
`stack-profile.md`, official language conventions, and tool configuration refine
them. Deviations require a documented reason and, when significant, an ADR.

## General coding standards

### CODE-001 — Correctness before elegance

- Trace implemented behavior to requirements and acceptance criteria.
- Make preconditions, postconditions, and invariants visible in code or tests.
- Handle boundaries, empty input, invalid states, and failure paths deliberately.
- Never invent unspecified behavior as a `reasonable` assumption.

### CODE-002 — Small, cohesive units

- Give modules, types, and functions one clearly named primary responsibility.
- Keep public interfaces smaller than their implementations and hide details.
- Split long control flow by meaningful steps, not arbitrary line counts.
- Abstract duplication only after demonstrating a shared concept.
- Abstractions must reduce knowledge or coupling; avoid pass-through layers.

### CODE-003 — Clear naming and structure

- Names express domain intent, units, and state.
- Avoid ambiguous abbreviations, misleading booleans, and vague names such as `data`, `manager`, or `helper`.
- Use one repository-wide term for the same concept.
- Align directory and namespace structure with domain or architecture boundaries.
- Follow language conventions unless the stack profile specifies stricter rules.

### CODE-004 — Explicit contracts and types

- Define public inputs, outputs, errors, and side effects unambiguously.
- Use the strongest practical type checking; keep unsafe exceptions local and justified.
- Use domain types when they prevent invalid primitive-value states.
- Give null, optional, and empty results explicit semantics.
- Version serialized and public contracts and evolve them compatibly.

### CODE-005 — Control flow and state changes

- Make the happy path and exit conditions easy to identify.
- Change state in a few explicit locations that protect invariants.
- Avoid hidden global state and temporal coupling.
- Functions must not mutate surprising data outside their contract.
- Release resources deterministically, including during failure and cancellation.

### CODE-006 — Error handling

- Never swallow errors or translate them into meaningless messages.
- Keep business rejection, invalid input, technical failure, and defects distinct.
- Preserve useful context without exposing secrets or unnecessary personal data.
- Limit retries and use them only for suitable idempotent, transient operations.
- Partial failure must not leave silent inconsistent state.

See `error-handling.md` for details.

### CODE-007 — Concurrency and asynchronous behavior

- Make ownership and synchronization of shared state explicit.
- Consider deadlocks, races, duplicate processing, and cancellation paths.
- Propagate timeout and cancellation across system boundaries.
- Never use arbitrary sleeps as synchronization in concurrent tests.
- Document and verify ordering guarantees instead of assuming them.

### CODE-008 — Security and privacy

- Validate external input at trust boundaries and encode output for its context.
- Separate authentication and authorization; authorize at the authoritative boundary.
- Never place secrets in source, logs, tests, sample data, or errors.
- Do not design custom cryptography; use established libraries and secure defaults.
- Keep dependency and artifact provenance reproducible and verifiable.
- Apply least privilege and minimize data collection and retention.

Select the concrete security baseline in `secure-development.md`.

### CODE-009 — Testability and tests

- Treat time, randomness, network, filesystem, and external services as controllable dependencies.
- Test observable behavior rather than private implementation details.
- Give every test one clear reason to fail.
- Test errors and boundaries as deliberately as the happy path.
- Treat flaky tests as defects; do not hide them behind permanent retries.

### CODE-010 — Observability

- Use structured logs with appropriate severity and correlation context.
- Do not log expected business outcomes as technical errors.
- Give critical paths metrics and traces that answer defined operational questions.
- Avoid sensitive telemetry and uncontrolled cardinality.
- Design diagnostics at system boundaries instead of adding them after failure.

### CODE-011 — Performance and resources

- Base optimization on measurement or an `NFR-*` requirement.
- Select algorithms and data structures for expected scale.
- Bound collections, queues, caches, retries, and parallelism.
- Stream or limit large data sets where practical.
- Do not sacrifice clarity and correctness for unproven micro-optimization.

### CODE-012 — Dependencies and supply chain

- A new dependency needs clear value, maintained provenance, and a compatible license.
- Prefer the standard library or existing dependencies when they meet the requirement.
- Pin versions reproducibly and follow the stack profile's lock-file policy.
- Remove unused dependencies when within task scope.
- Never edit generated files manually; document their source and generation command.

### CODE-013 — Documentation and comments

- Comments explain reasons, trade-offs, invariants, and surprising constraints—not syntax.
- Public interfaces document contracts, errors, and relevant side effects.
- Update documentation in the same change as behavior.
- Record significant long-term decisions as ADRs, not only code comments.

### CODE-014 — Changeability and compatibility

- Keep changes small, cohesive, and traceable.
- Evolve public APIs, data formats, and persistence schemas compatibly or provide a migration plan.
- Give feature flags an owner, expiry condition, and defined states.
- Announce, measure, and remove deprecated paths deliberately.
- Refactoring does not change behavior unless explicitly specified and tested.

## Design principles

The following principles supplement `CODE-NNN` standards as review lenses. They
are not architecture styles and do not justify abstractions without evidence.

### SOLID

SOLID helps evaluate responsibilities, contracts, and dependencies. Add an
abstraction only when it reduces concrete coupling, protects an evidenced change
point, or enables required testability.

#### CODE-SOLID-S — Single Responsibility Principle

**Weight: high; apply by default.**

- A unit has one cohesive responsibility and primarily one domain or technical reason to change.
- `One method per class` is not the goal; keep related behavior and invariants together.
- Separate distinct change drivers such as domain policy, persistence, and presentation.

#### CODE-SOLID-O — Open/Closed Principle

**Weight: situational; apply only at evidenced variation points.**

- Stable contracts may support extension without repeatedly modifying proven behavior.
- Create extension points for existing variants, requirements, or confirmed changes—not hypothetical ones.
- Prefer a simple direct change over an unused plugin or inheritance hierarchy.

#### CODE-SOLID-L — Liskov Substitution Principle

**Weight: high whenever subtypes or interchangeable implementations exist.**

- Every implementation honors the complete contract of its base type.
- It does not strengthen preconditions, weaken postconditions, or violate invariants.
- Caller type checks for special cases indicate a poor shared contract or inheritance model.

#### CODE-SOLID-I — Interface Segregation Principle

**Weight: medium to high for public or cross-component interfaces.**

- Consumers depend only on operations they need.
- Split interfaces by consumer roles and capabilities, not by an implementation's complete API.
- Trivial single-method interfaces without distinct consumers or substitution needs are not a goal.

#### CODE-SOLID-D — Dependency Inversion Principle

**Weight: high at architecture, infrastructure, and test boundaries.**

- Domain rules do not depend on UI, persistence, network, or framework details.
- The more stable domain side defines abstractions; technical adapters implement them.
- Direct coupling inside simple stable details is acceptable when abstraction adds no value.
- Concrete direction also follows `docs/architecture/dependency-rules.md`.

#### SOLID review questions

- Which responsibilities and reasons for change belong together?
- Which concrete variation justifies an extension abstraction?
- Do interchangeable implementations honor the same observable contract?
- Does each consumer need its entire interface?
- Do domain dependencies point to stable contracts rather than technical details?
- Would fewer abstractions remain equally clear, testable, and changeable?

### Complementary principles

#### CODE-KISS — Keep It Simple

**Weight: high; apply by default.**

- Prefer the simplest solution that fully satisfies requirements, quality goals, invariants, and architecture rules.
- Simplicity means low necessary complexity, not missing structure, validation, or error handling.
- Keep control flow, state, and dependencies understandable without needless indirection.
- Clever, compact, or generic code is not automatically simpler.

#### CODE-YAGNI — You Aren't Gonna Need It

**Weight: high for unconfirmed extensions.**

- Features, variants, configuration, and extension points require current needs or evidenced changes.
- Hypothetical requirements do not justify extra abstraction, infrastructure, or public APIs.
- Preserve future changeability through reversible decisions and clear modules, not speculative features.
- YAGNI never defers accepted quality, migration, security, or operational requirements.

#### CODE-COMPOSITION — Composition over Inheritance

**Weight: preferred starting point.**

- Compose behavior from small cooperating components.
- Implementation inheritance requires a stable `is-a` relationship and substitutability under `CODE-SOLID-L`.
- Avoid inheritance used only for code reuse or access to internal details.
- Encapsulate framework-required inheritance at a technical boundary when needed.

#### CODE-POLA — Principle of Least Astonishment

**Weight: high for public and cross-team interfaces.**

- Names, returns, errors, and side effects match justified user expectations and stack conventions.
- Similarly named operations behave consistently.
- A read-like operation does not unexpectedly change state.
- Dangerous or irreversible actions are explicit and protected.
- Make unavoidable surprises visible through contracts, documentation, and tests.

#### Complementary review questions

- Is there a simpler solution satisfying the same evidenced requirements?
- Which current need justifies each variant or abstraction?
- Is inheritance truly substitutable or merely code reuse?
- Do names, contracts, errors, and side effects match user expectations?
- Was simplicity misused to omit necessary quality?

## Automated enforcement

The stack profile maps formatting, linting, type checking, tests, build, and
dependency checks to reproducible commands or justified exceptions. Review
non-automated rules by their `CODE-*` identifiers.

## Project-specific additions

| ID | Rule | Scope | Verification | Rationale |
|---|---|---|---|---|
| `CODE-PROJ-001` | `<CONCRETE RULE>` | `<PATHS/MODULES>` | `<TOOL/TEST/REVIEW>` | `<REASON>` |
