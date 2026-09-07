# REQ-IMPORT-001 — Transfer photos to the local library

- Status: `Draft`
- Priority: `Must`
- Source/goal: `PRD-IMPORT-001`
- Affected journey/UX rule: `To be defined after Q-001, Q-002, and Q-004 are resolved`

## Behavior

When the user initiates an import from a supported attached device, the system
must transfer the selected supported photos into the configured local photo
library and report the outcome for every selected file.

## Acceptance examples

```gherkin
Given a supported attached source containing selected photos
And a configured local photo library
When the user initiates an import
Then each successfully imported photo exists in the local photo library
And the outcome of every selected file is reported
```

## Edge and error cases

- Device access, copy-versus-move behavior, interruption recovery, duplicate handling, and unsupported files remain `UNKNOWN` pending Q-002, Q-004, and Q-005.

## Verification

- Test level: `System`
- Evidence: End-to-end import scenario with controlled source and destination directories; exact setup remains to be defined.

## Change history

- `2026-09-07`: Initial Draft derived from the stated project goal.
