# REQ-SAFETY-002 — Control source deletion eligibility and execution

- Status: `Accepted`
- Priority: `Must`
- Source/goal: `PRD-IMPORT-001`
- Affected journey/UX rule: `UX-005`, `UX-006`, `UX-007`, `UX-012`,
  `UX-PROJ-004`

## Behavior

`Deletion eligible` and `Deleted` are separate per-source states. Successful
copying or content verification must not automatically delete a source.

A source may become deletion eligible only when:

- its concrete final destination path is established;
- a regular file exists at that destination;
- source and the actual destination have been conclusively verified as having
  identical complete contents after copying, or reverified against the existing
  destination for an `Already imported` outcome;
- no relevant change to the source or destination has been detected since that
  verification; and
- no unresolved metadata, destination-path, duplicate, stale-plan, or other
  safety conflict remains.

Equal size, a successful copy operation, a hash match without conclusive
complete-content verification, or a previously calculated plan is insufficient.
Eligibility is determined independently for every source, including
byte-identical sources that share one destination.

After import, deletion-eligible sources must be shown together. They are deleted
only through a separate, explicit user action. Before actual deletion, the
system must technically re-establish that deletion remains safe. A relevant
change to the source or verified destination invalidates eligibility and blocks
deletion until the source independently satisfies the rules again.

The exact confirmation interaction and source-specific technical protection
against changes during verification and deletion remain open until before the
mutating import increment.

## Acceptance examples

```gherkin
Given a source has been copied and conclusively verified against its actual destination
And no relevant object has changed
And no safety conflict remains
When the import completes
Then the source is shown as deletion eligible
And it is not deleted automatically
```

```gherkin
Given two byte-identical sources share one verified destination
When only the first source has independently satisfied every deletion condition
Then only the first source is deletion eligible
```

```gherkin
Given a source was deletion eligible
And the source or its verified destination has relevantly changed
When the user requests deletion
Then the eligibility is revoked
And the source is not deleted
```

## Edge and error cases

- Destination is absent or not a regular file -> block deletion eligibility.
- Complete-content verification cannot finish -> block deletion eligibility and
  report the per-source reason.
- Associated media is recognized or uncertain -> additionally apply
  `REQ-SAFETY-001`; no companion is deletion eligible merely because its photo
  qualifies.
- Source-specific deletion capabilities or revalidation guarantees are
  insufficient -> block deletion rather than applying filesystem assumptions.

## Verification

- Test level: `Unit | Integration | System | Manual`
- Evidence: Per-source state-transition tests, new-copy and already-imported
  verification scenarios, shared-destination tests, changed-object tests, and an
  owner walkthrough of the later explicit deletion action.

## Change history

- `2026-09-08`: Accepted independent deletion eligibility, deferred explicit
  deletion, and mandatory revalidation by Daniel.
