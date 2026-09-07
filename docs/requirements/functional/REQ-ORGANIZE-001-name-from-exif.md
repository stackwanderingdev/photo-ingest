# REQ-ORGANIZE-001 — Name imported photos from EXIF data

- Status: `Draft`
- Priority: `Must`
- Source/goal: `PRD-IMPORT-001`
- Affected journey/UX rule: `UJ-001`, `UX-003`, `UX-006`, `UX-007`, `UX-010`

## Behavior

When a photo is imported, the system must derive the destination filename
`YYYYMMDD_HHMMSS.ext` from the local date and time of the capture timestamp
selected under `REQ-METADATA-001`, while preserving a normalized form of the
source filename extension. It must not convert the selected timestamp to the
executing system's timezone.

## Acceptance examples

```gherkin
Given a photo with the EXIF values required by the approved naming rule
When the photo is imported
Then its destination filename equals the name derived from those values
```

## Edge and error cases

- Missing or invalid capture time and blocking capture-time conflicts produce no
  final filename and block import and deletion release under `INV-SAFETY-001`.
- Extension normalization and filename collisions remain `UNKNOWN` pending
  `Q-005`.

## Verification

- Test level: `Unit | Integration`
- Evidence: Deterministic naming examples plus EXIF-reading integration tests after the naming rule is approved.

## Change history

- `2026-09-07`: Initial Draft derived from the stated project goal.
- `2026-09-07`: Linked naming to the accepted normalized capture-time rules;
  collision and extension rules remain open.
