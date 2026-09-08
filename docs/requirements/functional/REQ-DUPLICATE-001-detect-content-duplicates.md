# REQ-DUPLICATE-001 — Detect complete-content duplicates

- Status: `Accepted`
- Priority: `Must`
- Source/goal: `PRD-IMPORT-001`
- Affected journey/UX rule: `UJ-001`, `UX-PROJ-003`

## Behavior

Two files are content duplicates in the initial scope if and only if their
complete file contents are byte-identical. Equal size, filename, capture time,
metadata, or visual appearance alone is insufficient. Files with identical
depicted image content but different metadata or encoding are not content
duplicates unless their complete bytes are identical.

The initial duplicate search scope is limited to:

- the object at the destination path currently calculated or reserved for a
  plan item; and
- source files within the same current import plan.

PhotoIngest does not search the rest of the photo library for content duplicates
in the initial scope. Library-wide duplicate discovery remains a possible later
product feature.

When the calculated destination already contains a byte-identical regular file,
the system must not copy the source again. The plan item must visibly report
`Already imported` or an equivalent unambiguous status and refer to the actual
existing destination. It may become eligible for source deletion only through
the separate per-source rules in `REQ-SAFETY-002`.

When multiple source files in one plan are byte-identical, their content is
copied at most once and every affected plan item visibly refers to the same
destination object. Each source remains an independent plan item with its own
outcome, verification state, and deletion eligibility. Success or deletion
eligibility for one source must not be inherited by another.

## Acceptance examples

```gherkin
Given a source and the regular file at its calculated destination are byte-identical
When the system creates the preview
Then the item is shown as already imported
And no copy is planned for that source
```

```gherkin
Given two byte-identical source files in one import plan
When the system creates the preview
Then both remain visible as separate plan items
And both refer to the same destination object
And their outcome, verification, and deletion states remain independent
```

```gherkin
Given two photos have equal size and capture time but different complete bytes
When the system evaluates content identity
Then it does not classify them as content duplicates
```

## Edge and error cases

- A destination cannot be read completely -> do not classify it as already
  imported; report a blocking per-file problem.
- Candidate files have matching hashes or sizes but have not passed conclusive
  complete-content verification -> do not classify them as content duplicates.
- An identical file exists elsewhere in the library but outside the current
  search scope -> do not discover or use it automatically.
- An occupied suffixed candidate is byte-identical -> behavior remains open
  under `Q-015`.

## Verification

- Test level: `Unit | Integration | System`
- Evidence: Fixtures that distinguish byte-identical files from equal-size,
  same-metadata, visually equal, and differently encoded files; plan tests with
  an existing destination and multiple identical sources.

## Change history

- `2026-09-08`: Accepted complete-byte identity, bounded search scope, existing
  destination behavior, and independent plan-item state by Daniel.
