# ADR-005: Conclusive content verification boundary

- Status: `Accepted`
- Date: `2026-09-08`
- Decision makers: `Daniel (Product and Architecture Owner)`
- Supersedes: `Not applicable`
- Superseded by: `Not applicable`

## Context

`REQ-DUPLICATE-001` defines content identity as equality of the complete file
bytes. `REQ-SAFETY-002` and `INV-SAFETY-002` require conclusive identity evidence
before a source can become eligible for deletion. PhotoIngest will eventually
operate across filesystem and MTP sources with different identity, reading,
change-detection, and deletion capabilities under ADR-002.

The architecture must distinguish conclusive content evidence from optional
performance optimizations without prematurely selecting POSIX-only mechanisms
for all source types.

## Decision

The conclusive identity decision is the result of comparing the complete byte
content of both objects. Equal size, metadata, names, timestamps, or hashes are
not independently conclusive evidence of equality. Size and a selected hash may
be used as rejection filters, candidate selection, caching, or acceleration, but
a match must still be followed by a complete bytewise comparison before the
system reports content identity or grants deletion eligibility.

Content reading, object observation, and deletion are capability-specific
infrastructure responsibilities behind project-owned contracts. Domain and
application behavior receives normalized identity evidence and observation
outcomes; it must not assume that every source is a POSIX path or exposes file
descriptors, inode data, filesystem timestamps, atomic rename, or identical
deletion semantics.

The actual destination used for an `Already imported` result or completed copy
must be the destination against which conclusive verification is performed. Each
source requires its own verification evidence even when multiple byte-identical
sources refer to the same destination.

This decision does not select a hash algorithm, chunk size, streaming API,
file-handle strategy, change token, TOCTOU mitigation, atomic copy/publication
sequence, retry policy, or deletion mechanism. Those mechanisms must be decided
with source-specific capability evidence before the mutating import increment.
The first read-only filesystem preview may use only the subset needed to produce
its non-mutating outcomes, without claiming deletion safety.

## Alternatives considered

### Treat matching hashes as conclusive identity

- Benefits: Avoids a second complete read after hashing and is operationally
  common.
- Drawbacks: It does not implement the accepted exact full-content identity rule
  and would make deletion eligibility depend on the selected algorithm.
- Reason not selected: Hash matches are permitted only as non-conclusive
  acceleration evidence.

### Use size, metadata, or capture time

- Benefits: Cheap and often already available during preview.
- Drawbacks: Different content can share every one of these properties.
- Reason not selected: They cannot establish complete-content equality.

### Define one POSIX file-handle and deletion algorithm for every source

- Benefits: One concrete implementation strategy.
- Drawbacks: It would contradict ADR-002 and could be invalid or unsafe for MTP
  devices.
- Reason not selected: Mechanisms must follow explicit source capabilities and
  feasibility evidence.

## Consequences

- Positive: Duplicate classification and deletion eligibility share one exact,
  backend-independent meaning.
- Positive: Performance optimizations cannot silently weaken the safety rule.
- Positive: Future MTP support can use different mechanisms while preserving the
  same domain outcome.
- Negative/trade-off: Conclusive equality may require reading both complete
  contents even after an optional hash match.
- Prohibited unless this ADR is superseded: Treating size or a hash match alone
  as conclusive equality; granting one source deletion eligibility from another
  source's evidence; embedding POSIX-only assumptions in domain policy.
- Required follow-up: Resolve `Q-011` with representative filesystem evidence
  before the mutating import increment and extend that decision with MTP
  feasibility evidence before MTP mutation is supported.

## Evidence and review

- Affected requirements: `REQ-DUPLICATE-001`, `REQ-IMPORT-001`,
  `REQ-PLAN-001`, `REQ-SAFETY-002`
- Affected invariants: `INV-PLAN-001`, `INV-SAFETY-002`
- Verification criteria: Controlled files that match and differ at the
  beginning, middle, and end produce correct normalized outcomes; hash matches
  alone never produce conclusive evidence; source-specific contract tests prove
  safe failure when stable verification is unavailable.
- Revisit when: The product identity definition changes, performance evidence
  requires another comparison contract, or a source type cannot provide the
  capabilities needed to satisfy the accepted safety invariant.
