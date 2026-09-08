# INV-PLAN-001 — Never execute a stale plan item

- Status: `Accepted`
- Rationale: A preview is a snapshot, so mutation based on changed source,
  destination, metadata, content, or path assumptions could import or delete the
  wrong object.
- Scope: Import-plan lifecycle and every mutating operation.

## Rule

No mutating operation may execute for a plan item until all assumptions relevant
to that operation have been revalidated. If an assumption changed or cannot be
revalidated, that item is stale and remains non-executable until an updated plan
has been shown and explicitly confirmed.

## Allowed transitions

- `Previewed` -> relevant assumptions revalidated unchanged -> `Executable`
- `Previewed` -> relevant assumption changed or indeterminate -> `Stale`
- `Stale` -> updated plan shown and confirmed -> `Previewed`

## Prohibited states or actions

- Executing a stale plan item.
- Silently changing a reserved path during pre-execution revalidation.
- Treating an inability to revalidate as evidence that the plan is current.

## Enforcement and evidence

- Implementation boundary: Application import-plan coordinator using
  capability-specific source and destination observations.
- Evidence: State-transition tests and adapter integration tests that alter or
  make source and destination observations unavailable between preview and
  mutation.
- Requirements covered: `REQ-PLAN-001`, `REQ-PREVIEW-001`, `REQ-IMPORT-001`,
  `REQ-SAFETY-002`

## Change history

- `2026-09-08`: Accepted by Daniel to prevent mutation from outdated previews.
