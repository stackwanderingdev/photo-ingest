# INV-SAFETY-001 — Unresolved capture time blocks transfer

- Status: `Accepted`
- Rationale: A photo without one authoritative capture time has no trustworthy
  final destination and must never be imported or released for source deletion
  under an invented or ambiguous path.
- Scope: Preview planning, import eligibility, destination planning, and source
  deletion eligibility for photos and recognized associated media.

## Rule

A supported photo may receive a final destination path, become eligible for
import, or become eligible for later source deletion only after
`REQ-METADATA-001` has produced one valid, non-conflicting selected capture time.
Missing or invalid capture times and blocking capture-time conflicts keep all
three outcomes unavailable. Recognized associated media remain ineligible for
deletion whenever their photo has such an unresolved outcome.

## Allowed transitions

- `Capture time unresolved` -> resolve one valid, non-conflicting capture time ->
  `Destination planning permitted`
- `Destination verified after permitted import` -> apply the separately accepted
  deletion rules -> `Source deletion may become eligible`

## Prohibited states or actions

- A final destination path exists while capture time is missing, invalid, or in
  blocking conflict.
- Import begins for a file whose capture time is unresolved.
- A photo or recognized associated media component is released for deletion
  while the photo's capture time is unresolved.
- A technical fallback, modification time, or filesystem time silently bypasses
  the capture-time requirement.

## Enforcement and evidence

- Implementation boundary: Domain destination planning and application import
  eligibility; adapters may report candidates and failures but may not override
  this rule.
- Evidence: Domain state-transition tests and application-level preview/import
  tests covering missing, invalid, and conflicting capture times plus associated
  media.
- Requirements covered: `REQ-METADATA-001`, `REQ-PREVIEW-001`,
  `REQ-ORGANIZE-001`, `REQ-ORGANIZE-002`, `REQ-IMPORT-001`, `REQ-SAFETY-001`

## Change history

- `2026-09-07`: Accepted by Daniel as the safety boundary for unresolved capture
  times and associated media.
