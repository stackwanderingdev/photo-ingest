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
And already imported, within-plan duplicate, name-collision, stale-plan, and
blocking destination-path-conflict outcomes are distinguishable
And no source or destination file is created, changed, moved, or deleted
```

## Edge and error cases

- Missing or invalid capture time and blocking capture-time conflicts must be
  visible as blocking per-file outcomes without a final destination path.
- An existing byte-identical destination must be shown as `Already imported` or
  an unambiguous equivalent, not silently skipped.
- A byte-identical source in the same plan must be distinguishable as a
  within-plan content duplicate while remaining a separate plan item.
- A resolved regular-file name collision must show its suffixed destination and
  a visible non-blocking collision status.
- A non-regular object at the proposed target must show a blocking
  destination-path conflict without being followed or inspected as file content.
- A plan item invalidated after preview must be distinguishable as stale or
  requiring replanning and must not receive a silently changed destination.
- Inaccessible sources, unsupported files, and scan errors remain visible
  per-file outcomes.

## Verification

- Test level: `Unit | Integration | System`
- Evidence: Deterministic preview computation plus a filesystem-boundary test proving that source and destination snapshots remain unchanged.

## Change history

- `2026-09-07`: Initial Draft created for the agreed non-mutating first increment.
- `2026-09-07`: Defined preview behavior for unresolved capture times.
- `2026-09-08`: Defined distinct duplicate, collision, stale-plan, and blocking
  destination-object preview outcomes.
