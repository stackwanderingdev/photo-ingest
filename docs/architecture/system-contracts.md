# System Contracts and Invariants

These rules hold in every permitted system state. Create each invariant as a
separate file under `invariants/` using `invariants/INV-template.md`.

## Invariant index

| Invariant | Title | Status | Scope |
|---|---|---|---|
| [`INV-SAFETY-001`](invariants/INV-SAFETY-001-unresolved-capture-time-blocks-transfer.md) | Unresolved capture time blocks transfer | `Accepted` | Destination planning, import, and deletion eligibility |
| [`INV-DATA-001`](invariants/INV-DATA-001-never-overwrite-destination.md) | Never overwrite a destination object | `Accepted` | Destination planning and mutation |
| [`INV-PLAN-001`](invariants/INV-PLAN-001-never-execute-stale-plan.md) | Never execute a stale plan item | `Accepted` | Import-plan lifecycle and mutation |
| [`INV-SAFETY-002`](invariants/INV-SAFETY-002-verify-before-source-deletion.md) | Verify independently before source deletion | `Accepted` | Content verification, deletion eligibility, and deletion |

Do not define invariants in this index. Use filenames such as
`INV-DATA-001-no-partial-write.md`.

## Changing an invariant

Never change an invariant incidentally in a feature task. Require an explicit
requirements change, architecture review, and ADR where appropriate.
