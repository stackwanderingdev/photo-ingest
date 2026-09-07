# REQ-ORGANIZE-002 — File imported photos from EXIF data

- Status: `Draft`
- Priority: `Must`
- Source/goal: `PRD-IMPORT-001`
- Affected journey/UX rule: `To be defined after Q-001 and Q-003 are resolved`

## Behavior

When a photo is imported, the system must derive its destination directory from
the photo's EXIF data according to an approved deterministic filing rule.

## Acceptance examples

```gherkin
Given a photo with the EXIF values required by the approved filing rule
When the photo is imported
Then it is stored at the directory path derived from those values
```

## Edge and error cases

- Exact directory pattern, timezone, missing metadata, invalid path values, and pre-existing directories remain `UNKNOWN` pending Q-003 and Q-005.

## Verification

- Test level: `Unit | Integration`
- Evidence: Deterministic path examples plus filesystem integration tests after the filing rule is approved.

## Change history

- `2026-09-07`: Initial Draft derived from the stated project goal.
