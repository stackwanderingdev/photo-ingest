# REQ-ORGANIZE-001 — Name imported photos from EXIF data

- Status: `Draft`
- Priority: `Must`
- Source/goal: `PRD-IMPORT-001`
- Affected journey/UX rule: `To be defined after Q-001 and Q-003 are resolved`

## Behavior

When a photo is imported, the system must derive its destination filename from
the photo's EXIF data according to an approved deterministic naming rule.

## Acceptance examples

```gherkin
Given a photo with the EXIF values required by the approved naming rule
When the photo is imported
Then its destination filename equals the name derived from those values
```

## Edge and error cases

- Exact EXIF fields, formatting, timezone, missing metadata, collisions, and malformed metadata remain `UNKNOWN` pending Q-003 and Q-005.

## Verification

- Test level: `Unit | Integration`
- Evidence: Deterministic naming examples plus EXIF-reading integration tests after the naming rule is approved.

## Change history

- `2026-09-07`: Initial Draft derived from the stated project goal.
