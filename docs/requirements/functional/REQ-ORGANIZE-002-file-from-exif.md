# REQ-ORGANIZE-002 — File imported photos from EXIF data

- Status: `Draft`
- Priority: `Must`
- Source/goal: `PRD-IMPORT-001`
- Affected journey/UX rule: `UJ-001`, `UX-003`, `UX-006`, `UX-007`, `UX-010`

## Behavior

When a photo is imported, the system must place it below a user-configurable
destination root in the directory structure `YYYY/MM/`, using the local year and
month of the capture timestamp selected under `REQ-METADATA-001`. It must not
convert the selected timestamp to the executing system's timezone.

## Acceptance examples

```gherkin
Given a photo with the EXIF values required by the approved filing rule
When the photo is imported
Then it is stored at the directory path derived from those values
```

## Edge and error cases

- Missing or invalid capture time and blocking capture-time conflicts produce no
  final directory path and block import and deletion release under
  `INV-SAFETY-001`.
- Invalid destination-root values and directory-creation behavior remain
  `UNKNOWN` pending `Q-005`.

## Verification

- Test level: `Unit | Integration`
- Evidence: Deterministic path examples plus filesystem integration tests after the filing rule is approved.

## Change history

- `2026-09-07`: Initial Draft derived from the stated project goal.
- `2026-09-07`: Linked filing to the accepted normalized capture-time rules;
  destination-path operational rules remain open.
