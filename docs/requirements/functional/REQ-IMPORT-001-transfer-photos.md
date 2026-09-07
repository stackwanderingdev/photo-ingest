# REQ-IMPORT-001 — Transfer photos to the local library

- Status: `Draft`
- Priority: `Must`
- Source/goal: `PRD-IMPORT-001`
- Affected journey/UX rule: `UJ-001`, `UX-003`, `UX-005`, `UX-006`, `UX-007`, `UX-012`

## Behavior

When the user initiates an import from a selected supported source and its
subdirectory, the system must transfer the selected supported photos into
the configured local photo library, verify each destination file, delete its
source only after successful verification, and report the outcome for every
selected file.

## Acceptance examples

```gherkin
Given a selected supported source and subdirectory containing photos
And a configured local photo library
When the user initiates an import
Then each successfully imported photo exists in the local photo library
And each source file is deleted only after its destination is verified
And the outcome of every selected file is reported
```

## Edge and error cases

- The exact verification method, interruption recovery, duplicate handling, and unsupported-file behavior remain `UNKNOWN` pending Q-004 and Q-005.

## Verification

- Test level: `System`
- Evidence: End-to-end import scenario with controlled source and destination directories; exact setup remains to be defined.

## Change history

- `2026-09-07`: Initial Draft derived from the stated project goal.
