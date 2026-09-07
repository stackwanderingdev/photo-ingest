# Development Workflow

This document defines the authoritative lifecycle from product idea to verified
software. The workflow is iterative: specify only enough to make the next small
decision safely, then use evidence to refine the correct source. It is not a
waterfall and does not require complete upfront specification.

## Core model

```text
Product idea
    -> product discovery and open questions
    -> product goals and requirements
    -> UX, quality goals, and critical journeys
    -> architecture, invariants, and stack decisions
    -> ADRs for significant decisions
    -> ready, bounded task
    -> tests and implementation
    -> verification and review
    -> evidence fed back to the appropriate source
    -> next increment
```

Work may move backward whenever new evidence invalidates an assumption. A
feedback loop must be explicit: update the authoritative document, record the
decision, and identify affected downstream artifacts before continuing.

## Roles and decision ownership

Assign people or accountable roles during project initialization:

| Decision | Accountable role | May prepare/propose |
|---|---|---|
| Product goals and functional behavior | `<PRODUCT OWNER>` | Stakeholders, developers, agents |
| UX rules and interaction contracts | `<UX/PRODUCT OWNER>` | Researchers, designers, agents |
| Architecture, invariants, and ADRs | `<ARCHITECTURE OWNER>` | Developers, operators, agents |
| Security risk acceptance | `<SECURITY/RISK OWNER>` | Security reviewers, developers, agents |
| Task acceptance and completion | `<TASK OWNER>` | Implementers and reviewers |

An AI agent may analyze, draft, and propose decisions. It must not mark a
normative artifact `Accepted`, accept material risk, or resolve a documented
conflict unless the current user instruction explicitly grants that authority.
For a personal project, one person may hold every role; record that fact rather
than inventing separate participants.

## Artifact states

Use these shared meanings unless a document defines a stricter lifecycle:

- `Draft`: incomplete or under discussion; not an implementation authority.
- `Reviewed`: examined by the accountable role; open issues are visible.
- `Accepted`: approved and normative within its stated scope.
- `Deprecated`: still present for compatibility but not for new work.
- `Superseded`: replaced by an explicitly linked artifact.
- `Rejected`: considered and not selected; retained as decision history.

Status changes record date, decision maker, rationale, and affected identifiers
when the change is material. Never rewrite accepted history to hide a change.

## Phase 1 — Frame the product idea

Capture the product overview in `docs/requirements/product-requirements.md` and
each independently referenceable goal in `docs/requirements/goals/`:

- problem and affected users,
- intended outcomes and success measures,
- constraints and non-goals,
- known assumptions and open questions.

Keep the initial statement solution-neutral where possible. If the idea already
contains a solution constraint, record whether it is mandatory or merely a
starting assumption.

Exit when one small, valuable outcome can be described and decision-critical
unknowns have owners or validation plans.

## Phase 2 — Discover and specify the next increment

Derive atomic, observable `REQ-*` behavior in one file per requirement under
`docs/requirements/functional/` and measurable `NFR-*` quality goals under
`docs/requirements/quality/`.
For interactive systems, establish the UX effort level, relevant users, usage
context, and critical journeys under `docs/ux/`.

Discovery depth is proportional to uncertainty and risk:

- `Minimal`: documented assumptions and a direct walkthrough may be sufficient.
- `Standard`: validate important workflows and states with representative evidence.
- `Extended` or `Critical`: use structured research, accessibility evidence, and repeated evaluation.

Do not specify implementation techniques as functional requirements. Record
unresolved issues as `UNKNOWN`, `AMBIGUOUS`, or `CONFLICT` rather than guessing.

Exit when the behavior and quality expected from the next increment are testable.

## Phase 3 — Establish sufficient architecture

Define only the architecture needed to deliver the next increments safely:

- system and trust boundaries,
- building-block responsibilities and dependency direction,
- critical runtime and data flows,
- system invariants,
- persistence, compatibility, security, and operational constraints,
- active stack and verification commands.

Architecture is sufficient when it constrains important risks without designing
hypothetical future features. Apply KISS and YAGNI while preserving accepted
quality and security requirements.

Exit when the next task can be implemented without inventing structural policy.

## Phase 4 — Record significant decisions

Create an ADR when a decision is hard to reverse, affects multiple components,
establishes a public or data contract, introduces substantial operational risk,
or deliberately deviates from an accepted standard.

Do not create ADRs for routine local implementation details. An ADR becomes
normative only when its status is `Accepted` by the accountable role.

Exit when all decisions required by the next task are accepted or explicitly
identified as blockers.

## Phase 5 — Cut a ready task

Create one task file from `docs/tasks/TASK-template.md`. Keep it close to one coherent
commit and identify:

- requirements, UX rules, invariants, and ADRs,
- current and required observable behavior,
- allowed files or modules and prohibited changes,
- acceptance criteria, edge cases, and user states,
- targeted and regression verification.

A task may move to `Ready` only when:

- its goal and boundaries are unambiguous,
- referenced normative artifacts are accepted,
- required architecture and UX decisions exist,
- acceptance criteria are testable,
- required commands are configured in the stack profile,
- no decision-critical `UNKNOWN`, `AMBIGUOUS`, or `CONFLICT` remains.

If readiness fails, return to the owning phase. Do not use implementation to
discover policy that should be decided in a normative artifact.

## Phase 6 — Implement and verify

Follow `AGENTS.md` and the task contract:

1. inspect relevant sources and confirm the plan,
2. add or update behavioral evidence,
3. implement the smallest sufficient change,
4. run targeted checks and the regression suite,
5. review scope, architecture, UX, security, and compatibility,
6. complete the Definition of Done and report limitations.

Passing tests are necessary evidence, not permission to contradict requirements.
The task moves to `Done` only after its acceptance authority confirms the
required outcome and all applicable completion criteria are satisfied.

## Phase 7 — Feed evidence back

Classify every material implementation or evaluation finding before changing a
normative source:

| Finding | Update first | Typical follow-up |
|---|---|---|
| User need or outcome was misunderstood | Product requirements | Review affected REQ/NFR/UX artifacts |
| Observable behavior is missing or ambiguous | Functional requirements | Update acceptance criteria and tests |
| Quality target is unrealistic or incomplete | Non-functional requirements | Reassess architecture and verification |
| Interaction causes user failure | UX guidelines/interaction design | Add UX finding and corrective task |
| Structural boundary is inadequate | Architecture/invariants | Architecture review and possibly ADR |
| Prior technical choice is no longer valid | New ADR | Supersede old ADR and plan migration |
| Implementation defect only | Task/code/test | Fix without changing normative intent |
| Test contradicts accepted behavior | Test after conflict review | Correct the test; do not redefine behavior silently |

After an upstream change, search all identifier references and assess downstream
requirements, UX contracts, architecture, ADRs, tasks, tests, code, and docs.

## Change control for accepted artifacts

Before changing an accepted normative artifact:

1. state the reason and new evidence,
2. identify the accountable decision owner,
3. list affected identifiers and downstream artifacts,
4. evaluate compatibility, migration, UX, security, and operational impact,
5. update or supersede the artifact explicitly,
6. create bounded follow-up tasks,
7. verify that implementation and documentation converge again.

Urgency does not remove traceability. Emergency changes may shorten review, but
must record the decision and retrospective follow-up.

## Increment planning

Plan only enough future work to expose dependencies and risks. Prefer a sequence
of thin, end-to-end increments that each produce demonstrable evidence. Revisit
priorities after every completed increment, significant finding, or changed
constraint.

The desired loop is:

```text
Specify enough -> decide explicitly -> implement narrowly -> verify honestly
       ^                                                     |
       +---------------- learn and update --------------------+
```
