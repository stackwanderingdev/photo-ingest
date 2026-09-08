# REQ-PLAN-001 — Revalidate an import plan before mutation

- Status: `Accepted`
- Priority: `Must`
- Source/goal: `PRD-IMPORT-001`
- Affected journey/UX rule: `UJ-001`, `UX-PROJ-003`, `UX-PROJ-004`

## Behavior

An import plan is a snapshot of the source, destination, metadata, content, and
path-allocation assumptions observed while creating its preview. Before any
mutating execution, the system must revalidate every assumption relevant to the
affected plan item.

If a reserved destination has become occupied or a relevant source or
destination object has changed, the system must not silently allocate a new
path and must not execute that item using the stale plan. It must mark the item
as stale or requiring replanning. An updated import plan, including any changed
destination, must be shown to the user and explicitly confirmed again before a
mutating execution.

## Acceptance examples

```gherkin
Given a preview reserves an available destination path
And that path becomes occupied before import
When the user requests the import
Then the affected item is not executed
And it is shown as stale and requiring a new preview
And no replacement path is silently assigned
```

```gherkin
Given a source changes after its preview
When the user requests a mutating execution
Then the affected plan item is not executed from the stale plan
And an updated plan must be displayed and confirmed before mutation
```

## Edge and error cases

- Only one plan item becomes stale -> block that item's mutation and report its
  state without silently changing unaffected reservations.
- Revalidation cannot determine whether an assumption still holds -> treat the
  item as stale rather than executing optimistically.
- Replanning yields the same path and outcome -> it is still a new visible plan
  requiring confirmation before mutation.

## Verification

- Test level: `Unit | Integration | System`
- Evidence: State-transition tests and controlled filesystem scenarios changing
  a source, destination, and reservation between preview and execution.

## Change history

- `2026-09-08`: Accepted snapshot, revalidation, stale-plan, and renewed
  confirmation behavior by Daniel.
