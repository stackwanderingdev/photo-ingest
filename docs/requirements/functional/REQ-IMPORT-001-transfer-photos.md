# REQ-IMPORT-001 — Transfer photos to the local library

- Status: `Draft`
- Priority: `Must`
- Source/goal: `PRD-IMPORT-001`
- Affected journey/UX rule: `UJ-001`, `UX-003`, `UX-005`, `UX-006`, `UX-007`, `UX-012`

## Behavior

When the user initiates an import from a selected supported source and its
subdirectory, the system must transfer the selected supported photos into
the configured local photo library, conclusively verify each actual destination
against its source, determine deletion eligibility independently for every
source, and report every outcome. It must not copy content again for an
`Already imported` result and must not delete a source automatically.

## Acceptance examples

```gherkin
Given a selected supported source and subdirectory containing photos
And a configured local photo library
When the user initiates an import
Then each successfully imported photo exists in the local photo library
And each source is independently evaluated for deletion eligibility
And no source is deleted without a separate explicit user action
And the outcome of every selected file is reported
```

## Edge and error cases

- Duplicate identity and destination reuse follow `REQ-DUPLICATE-001`.
- Final paths and name collisions follow `REQ-ORGANIZE-003`; an existing target
  is never overwritten.
- Stale plans are not executed under `REQ-PLAN-001`.
- Deletion eligibility and execution follow `REQ-SAFETY-002`.
- Interruption recovery remains `UNKNOWN` under `Q-012`.

## Verification

- Test level: `System`
- Evidence: End-to-end import scenario with controlled source and destination directories; exact setup remains to be defined.

## Change history

- `2026-09-07`: Initial Draft derived from the stated project goal.
- `2026-09-08`: Defined duplicate reuse, per-source deletion eligibility, and
  separate explicit deletion; interruption recovery remains open.
