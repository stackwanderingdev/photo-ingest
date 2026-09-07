# ADR-002: Source access boundaries

- Status: `Accepted`
- Date: `2026-09-07`
- Decision makers: `Daniel (Product and Architecture Owner)`
- Supersedes: `Not applicable`
- Superseded by: `Not applicable`

## Context

PhotoIngest must eventually import from local filesystems, network paths, and
MTP devices while allowing selection of a subdirectory. These source types have
different access, capability, identity, error, and deletion semantics. The first
increment is a non-mutating preview and must remain small enough to verify the
core EXIF-derived destination behavior.

## Decision

Initially support network locations only when the Linux system has already
mounted them as accessible filesystem paths. Process local and mounted network
paths through filesystem access. PhotoIngest initially does not establish
direct network connections or manage network credentials. Direct network-source
management remains a possible later extension, but requires its own product and
architecture decision; it is not prohibited for an entire release series.

Keep MTP conceptually distinct, with its own capabilities and error semantics.
Do not assume that it is a POSIX filesystem. Select the concrete MTP technology
only after a bounded feasibility comparison of GIO/GVfs and direct libmtp
access.

Limit the first non-mutating preview increment to local or already mounted
filesystem paths. It must not depend on MTP.

## Alternatives considered

### Application-managed network connections now

- Benefits: In-application discovery, connection setup, credentials, and protocol-specific diagnostics.
- Drawbacks: Adds protocol, credential, security, timeout, and connection-lifecycle scope before the core import behavior is established.
- Reason not selected: Mounted paths provide the accepted initial network-source behavior with a smaller system boundary.

### Treat every source as a POSIX path

- Benefits: One apparently uniform implementation model.
- Drawbacks: Hides MTP capability and failure differences and could make later destructive behavior unsafe.
- Reason not selected: MTP requires explicit capability and error semantics.

### Select GIO/GVfs or libmtp immediately

- Benefits: Resolves the implementation dependency early.
- Drawbacks: No project-specific feasibility evidence yet compares integration, device behavior, packaging, and testing.
- Reason not selected: Daniel requires a bounded technical comparison before accepting the MTP technology.

## Consequences

- Positive: The first increment can verify useful preview behavior through a deterministic filesystem boundary.
- Positive: Mounted network paths do not require PhotoIngest to store credentials or implement network protocols.
- Negative/trade-off: Users must mount network sources before selecting them in PhotoIngest.
- Negative/trade-off: MTP implementation and packaging remain unresolved until the feasibility comparison.
- Prohibited unless this ADR is superseded: Treating MTP as necessarily POSIX-compatible; adding direct network connection or credential management incidentally; coupling the first increment to MTP.
- Required follow-up: Define the MTP feasibility task before MTP implementation; create a separate decision if direct network-source management is proposed.

## Evidence and review

- Affected requirements: `REQ-PREVIEW-001`, `REQ-IMPORT-001`
- Verification criteria: The first preview works for local and mounted filesystem paths without MTP dependencies; later MTP evidence covers capability and error differences.
- Revisit when: Direct network connection management is proposed, the mounted-path model fails an accepted requirement, or MTP feasibility evidence is available.
