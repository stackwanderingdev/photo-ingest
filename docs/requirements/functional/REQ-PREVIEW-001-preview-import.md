# REQ-PREVIEW-001 — Preview an import without changing files

- Status: `Draft`
- Priority: `Must`
- Source/goal: `PRD-IMPORT-001`
- Affected journey/UX rule: `UJ-001`, `UX-003`, `UX-005`, `UX-006`, `UX-007`, `UX-012`

## Behavior

When the user requests an import preview for a selected local or already mounted
filesystem subdirectory and destination root, the system must show the planned
destination path and outcome for each discovered photo without creating,
changing, moving, or deleting files.

## Acceptance examples

```gherkin
Given a selected source directory containing supported photos
And a selected destination root
When the user requests an import preview
Then each discovered photo is shown with its planned destination path
And no source or destination file is created, changed, moved, or deleted
```

## Edge and error cases

- Missing or invalid capture time and blocking capture-time conflicts must be
  visible as blocking per-file outcomes without a final destination path.
- Duplicate destinations, inaccessible sources, unsupported files, and scan
  errors must be visible in the preview; their exact classifications remain
  `UNKNOWN` pending `Q-005`.

## Verification

- Test level: `Unit | Integration | System`
- Evidence: Deterministic preview computation plus a filesystem-boundary test proving that source and destination snapshots remain unchanged.

## Change history

- `2026-09-07`: Initial Draft created for the agreed non-mutating first increment.
- `2026-09-07`: Defined preview behavior for unresolved capture times.
