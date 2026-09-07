# REQ-ORGANIZE-001 — Name imported photos from EXIF data

- Status: `Draft`
- Priority: `Must`
- Source/goal: `PRD-IMPORT-001`
- Affected journey/UX rule: `UJ-001`, `UX-003`, `UX-006`, `UX-007`, `UX-010`

## Behavior

When a photo is imported, the system must derive the destination filename
`YYYYMMDD_HHMMSS.ext` from its EXIF capture date and time while preserving a
normalized form of the source filename extension.

## Acceptance examples

```gherkin
Given a photo with the EXIF values required by the approved naming rule
When the photo is imported
Then its destination filename equals the name derived from those values
```

## Edge and error cases

- The authoritative EXIF field, timezone interpretation, extension normalization, missing metadata, collisions, and malformed metadata remain `UNKNOWN` pending Q-003 and Q-005.

## Verification

- Test level: `Unit | Integration`
- Evidence: Deterministic naming examples plus EXIF-reading integration tests after the naming rule is approved.

## Change history

- `2026-09-07`: Initial Draft derived from the stated project goal.
