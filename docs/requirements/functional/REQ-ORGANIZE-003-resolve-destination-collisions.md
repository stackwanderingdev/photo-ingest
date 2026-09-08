# REQ-ORGANIZE-003 — Resolve destination-name collisions

- Status: `Accepted`
- Priority: `Must`
- Source/goal: `PRD-IMPORT-001`
- Affected journey/UX rule: `UJ-001`, `UX-PROJ-003`

## Behavior

The system must never overwrite an existing destination object. If the base
destination path from `REQ-ORGANIZE-001` and `REQ-ORGANIZE-002` is occupied by a
different regular file, it must deterministically reserve the first available
conflict-free filename in ascending numeric order.

The suffix is inserted before the extension and formatted with a minimum width
of three digits: `_001` through `_999`, followed by `_1000`, `_1001`, and so on.
There is no product-defined upper bound.

Availability checks must consider both objects already present at the
destination and paths already reserved by other items in the same import plan.
Once assigned, a destination reservation remains stable within that plan. A
resolved regular-file name collision is visible in the preview but is not a
blocking business error when a unique conflict-free path can be reserved.

A directory, symbolic link, broken symbolic link, or other non-regular object at
the proposed destination path is a blocking destination-path conflict. The
system must not follow, replace, overwrite, or treat that object as a regular
destination file for content comparison.

## Acceptance examples

```gherkin
Given the base destination contains a different regular file
And suffixes 001 and 002 are occupied or reserved
When the system allocates a destination
Then it reserves the filename with suffix 003
And shows a non-blocking name-collision status
```

```gherkin
Given suffixes 001 through 999 are occupied or reserved
When the system allocates the next destination
Then it uses suffix 1000
```

```gherkin
Given a symbolic link exists at the proposed destination
When the system creates the preview
Then it reports a blocking destination-path conflict
And it neither follows nor replaces the link
```

## Edge and error cases

- Multiple plan items require the same base name -> allocate against existing
  objects and earlier reservations using the deterministic plan order.
- The destination changes after reservation -> do not silently reassign the
  item; apply `REQ-PLAN-001`.
- An occupied suffixed candidate is byte-identical -> behavior remains open
  under `Q-015`.
- The deterministic source ordering and tie-breakers remain open under `Q-014`.

## Verification

- Test level: `Unit | Integration | System`
- Evidence: Table-driven suffix allocation tests across 001, 999, and 1000;
  multi-source reservation tests; filesystem tests for regular and non-regular
  destination objects; preview status tests.

## Change history

- `2026-09-08`: Accepted deterministic unbounded suffixing, reservation
  stability, non-overwrite behavior, and non-regular-object blocking by Daniel.
