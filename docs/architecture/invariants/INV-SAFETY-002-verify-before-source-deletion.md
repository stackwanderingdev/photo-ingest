# INV-SAFETY-002 — Verify independently before source deletion

- Status: `Accepted`
- Rationale: Source deletion is irreversible and must depend on current evidence
  about that exact source and its actual destination, never on copy completion,
  another source's result, or stale planning evidence.
- Scope: Content verification, deletion eligibility, and actual source deletion.

## Rule

Every source has independent deletion eligibility. Eligibility requires one
concrete destination that is currently a regular file, conclusive equality of
the complete source and destination contents established against that actual
destination after copying or for an `Already imported` result, and absence of
unresolved safety conflicts. A relevant change after the governing verification
revokes eligibility.

Actual deletion is a separate explicit user action and requires a fresh
technical safety check. The check and deletion mechanism must honor the
capabilities and identity semantics of the source type; this invariant does not
assume POSIX paths, handles, timestamps, or deletion operations for MTP.

## Allowed transitions

- `Not eligible` -> exact source and actual destination conclusively verified ->
  `Deletion eligible`
- `Deletion eligible` -> relevant change detected or safety cannot be
  re-established -> `Not eligible`
- `Deletion eligible` -> user explicitly requests deletion and the technical
  safety check succeeds -> `Deleted`

## Prohibited states or actions

- Copy success, size equality, a hash result alone, or an earlier plan grants
  deletion eligibility.
- One source inherits verification or deletion eligibility from another source,
  including when both share a destination.
- Verification automatically deletes a source.
- A source is deleted when safety cannot be re-established for its source type.

## Enforcement and evidence

- Implementation boundary: Domain eligibility state and application deletion
  coordinator over capability-specific source and destination ports.
- Evidence: State-transition tests, full-content verification tests, changed
  source/destination tests, shared-destination tests, and later capability tests
  for every supported source type.
- Requirements covered: `REQ-DUPLICATE-001`, `REQ-IMPORT-001`,
  `REQ-PLAN-001`, `REQ-SAFETY-001`, `REQ-SAFETY-002`

## Change history

- `2026-09-08`: Accepted by Daniel as the per-source deletion safety boundary
  without selecting a filesystem- or MTP-specific mechanism.
