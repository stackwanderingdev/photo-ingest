# Architecture Standards

This document defines the mandatory architecture baseline and a catalog of
optional external standards. It does not prescribe layered, hexagonal,
microservice, or event-sourced architecture. Select a style only when justified
by requirements and trade-offs.

## Mandatory baseline

### ARCH-001 — Stakeholders and concerns

Name relevant stakeholders, their concerns, and decisions supported by the
architecture description. Every view serves a concrete concern.

### ARCH-002 — System boundary and context

Define the system, users, neighboring systems, trust boundaries, external
dependencies, and responsibilities outside the system.

### ARCH-003 — Quality attributes as scenarios

Express architecture drivers such as security, availability, performance,
changeability, and usability as measurable `NFR-*` scenarios with stimulus,
environment, affected element, response, and measure.

### ARCH-004 — Building blocks and responsibilities

Give significant building blocks explicit responsibilities, public contracts,
and known dependencies. Show static structure and critical runtime paths.

### ARCH-005 — Dependency direction and coupling

Dependencies follow `dependency-rules.md`. Avoid cycles, shared mutable state,
and coupling through implementation details, or justify and verify exceptions.

### ARCH-006 — Data ownership and consistency

For persistent or exchanged data, document owner, system of record, schema,
consistency model, transaction boundary, lifecycle, migration, and deletion.

### ARCH-007 — Interfaces and compatibility

Interfaces have explicit contracts, error semantics, versioning strategy,
timeouts, and compatibility rules. Treat network calls as unreliable.

### ARCH-008 — Security and privacy

Architecture includes trust boundaries, identities, permissions, assets, and
sensitive data flows. Apply least privilege and secure defaults. See
`docs/engineering/secure-development.md`.

### ARCH-009 — Resilience and failure domains

Address single points of failure, overload, partial failure, and recovery in line
with NFRs. Use timeouts, retries, idempotency, backpressure, and compensation
only with explicit semantics.

### ARCH-010 — Observability and operations

Describe how operators detect state, failure, and quality-goal violations.
Address deployment, configuration, secrets, migration, rollback, backup, and
recovery where applicable.

### ARCH-011 — Evolution and decisions

Record hard-to-reverse choices, alternatives, and consequences as ADRs. Public
contracts and data models need migration and compatibility strategies. Keep
technical debt visible and time-bounded.

### ARCH-012 — Verification

Verify architecture rules where practical through architecture tests, static
analysis, contract tests, quality measurements, and deployment exercises.
Diagrams alone are not evidence.

## Minimum architecture views

| View | Question answered | Required? |
|---|---|---|
| Context | Who uses the system and what does it depend on? | Always |
| Building blocks | Which responsibilities and dependencies exist? | Always |
| Runtime | How do critical use cases and failures work? | Always |
| Data | Who owns data and how is it kept consistent? | For persistent/exchanged data |
| Deployment | What runs where and under which operational boundaries? | For deployable software |
| Security | Where are trust boundaries and controls? | For external or sensitive boundaries |

Explain non-applicable views. Diagrams include a legend, abstraction level, and
scope, and must not contradict the text.

## External standards and profiles

| Standard/approach | Suitable for | Use in this template |
|---|---|---|
| ISO/IEC/IEEE 42010:2022 | Any architecture | Structure and concepts for traceable descriptions |
| ISO/IEC 25010:2023 | Quality requirements | Quality checklist used to derive measurable `NFR-*` |
| ISO 9241-210:2019 | Interactive systems | Human-centered iterative UX process |
| NIST SSDF SP 800-218 v1.1 | Secure development | Practices for preparation, protection, development, and response |
| OWASP ASVS | Web applications and APIs | Versioned security requirements and verification level |
| RFC 9110 | HTTP interfaces | Correct method, status, and caching semantics |
| OpenAPI Specification | HTTP APIs | Machine-readable versioned interface contract |
| TOGAF / ArchiMate | Enterprise architecture | Activate only for organization-wide architecture |

ISO standards are reference models, not project-specific requirements. C4,
arc42, Clean/Hexagonal Architecture, and Domain-Driven Design are useful methods
or styles, not automatically binding standards; select them through an ADR.

## Active architecture profile

| Standard/approach | Version | Scope | Binding sections | Rationale/evidence |
|---|---|---|---|---|
| ISO/IEC/IEEE 42010 | `2022` | Architecture documentation | `ARCH-001` through `ARCH-012` | Architecture review |
| `<STANDARD>` | `<VERSION>` | `<SCOPE>` | `<SECTIONS/RULES>` | `<RATIONALE AND CHECK>` |

An entry is not a blanket conformance claim. Claim full conformance only when
scope, criteria, and evidence were explicitly evaluated.

## Architecture review

Review architecture when adding system or trust boundaries, persistent data,
public interfaces, central NFR changes, deployable units, or hard-to-reverse
dependencies. Record:

- affected `REQ-*`, `NFR-*`, `INV-*`, `ARCH-*`, and ADRs,
- alternatives and trade-offs,
- risks, assumptions, and open questions,
- planned automated or manual evidence.

## Official references

- [ISO/IEC/IEEE 42010:2022 — Architecture description](https://www.iso.org/standard/74393.html)
- [ISO/IEC 25010:2023 — Product quality model](https://www.iso.org/standard/78176.html)
- [ISO 9241-210:2019 — Human-centred design](https://www.iso.org/standard/77520.html)
- [NIST SP 800-218 — Secure Software Development Framework](https://csrc.nist.gov/pubs/sp/800/218/final)
- [OWASP Application Security Verification Standard](https://owasp.org/www-project-application-security-verification-standard/)
- [RFC 9110 — HTTP Semantics](https://www.rfc-editor.org/rfc/rfc9110.html)
- [OpenAPI Initiative specifications](https://spec.openapis.org/)
- [The Open Group — TOGAF Standard](https://www.opengroup.org/togaf)

Fix standard versions and applicable sections in the active profile. `Latest`
is not reproducible and is therefore not a valid version.
