# ADR-004: Capture-time adapter contract

- Status: `Accepted`
- Date: `2026-09-07`
- Decision makers: `Daniel (Architecture Owner)`
- Supersedes: `Not applicable`
- Superseded by: `Not applicable`

## Context

`REQ-METADATA-001` defines product-owned capture-time semantics without exposing
ExifTool details. ADR-003 requires all ExifTool access to remain inside one
read-only infrastructure adapter. The adapter therefore needs a concrete mapping
from technical metadata fields to semantic candidates while preserving enough
precision and provenance for deterministic domain resolution.

## Decision

The ExifTool infrastructure adapter maps technical fields to normalized,
project-owned capture-time candidates as follows:

| Semantic candidate | ExifTool fields | Adapter rule |
|---|---|---|
| Original capture timestamp | `EXIF:DateTimeOriginal`, with `EXIF:SubSecTimeOriginal` and `EXIF:OffsetTimeOriginal` when present | Emit the highest-priority semantic candidate and retain local value, precision, offset, and provenance. |
| Digitization or creation timestamp | `EXIF:CreateDate` (the EXIF `DateTimeDigitized` value), with `EXIF:SubSecTimeDigitized` and `EXIF:OffsetTimeDigitized` when present | Emit a second-priority candidate; the domain may select it only when no valid original-capture candidate exists. |
| Format-specific capture timestamp | Explicitly approved HEIC/HEIF container field mapping | Emit a third-priority candidate only after the exact field's capture semantics and timezone interpretation have been defined and verified for the concrete adapter source. Until then, report it only as diagnostic metadata, not as an eligible fallback. |
| GPS plausibility timestamp | `Composite:GPSDateTime` or its validated source fields | Emit separately for plausibility assessment only; never classify it as a capture-time fallback in the first increment. |

The adapter must request qualified group names and must not merge same-named
fields from different metadata groups without retaining their provenance.
Technical field names, ExifTool group selection, command arguments, raw values,
parsing details, and process failures remain inside the infrastructure boundary.

The normalized contract exposes semantic candidate type, parsed local date and
time, optional subsecond precision, optional explicit UTC offset, source
provenance, and a per-file parse or extraction outcome. Domain and application
logic must not depend on any ExifTool tag name.

Syntactically invalid values and impossible calendar values are rejected per
candidate. No additional calendar plausibility boundary is introduced by this
ADR; `Q-010` must resolve any such boundary before an implementation task relies
on it.

When both compared candidates carry explicit UTC offsets, normalized absolute
instants are available for equality and conflict comparison. When only one
candidate has an offset, the adapter and domain must not assert absolute-time
equality. For matching local date and time, the explicit offset may enrich the
selected normalized value without changing that local value.

The local date and time of the domain-selected candidate remain unchanged for
destination naming and filing. Neither the adapter nor downstream logic converts
them to the executing system's timezone.

## Alternatives considered

### Put ExifTool tags in functional requirements

- Benefit: The complete rule would appear in one document.
- Drawback: It would couple product and domain semantics to the selected backend
  and contradict ADR-003.
- Reason not selected: Functional requirements own observable behavior, while
  this ADR owns the technical mapping.

### Accept any HEIC/HEIF creation field as a fallback

- Benefit: More files would immediately receive a destination path.
- Drawback: Container fields may have different semantics or timezone handling;
  an incorrect fallback could silently misfile a source and later permit deletion.
- Reason not selected: Representative evidence is required before the mapping is
  eligible.

### Use modification or filesystem timestamps

- Benefit: A value is usually available.
- Drawback: These values describe modification or storage behavior, not reliably
  the photographic capture time.
- Reason not selected: `REQ-METADATA-001` explicitly excludes them.

## Consequences

- Positive: Product and domain rules remain backend-independent.
- Positive: Conflicts can be assessed without discarding provenance, precision,
  or explicit offsets.
- Positive: HEIC/HEIF fallback behavior cannot become active without evidence.
- Negative/trade-off: Representative fixtures and explicit mapping verification
  are required before third-priority HEIC/HEIF candidates can be used.
- Prohibited unless this ADR is superseded: Exposing ExifTool fields outside the
  adapter contract; treating unverified HEIC/HEIF container values, GPS time,
  modification time, or filesystem time as capture-time fallbacks.
- Required follow-up: Resolve `Q-010`, establish the minimum ExifTool version,
  and verify the mapping with representative JPEG, HEIC/HEIF, and DNG fixtures.

## Evidence and review

- Affected requirements: `REQ-METADATA-001`, `REQ-PREVIEW-001`,
  `REQ-ORGANIZE-001`, `REQ-ORGANIZE-002`
- Affected invariant: `INV-SAFETY-001`
- Verification criteria: Fixture-based adapter tests show qualified provenance,
  correct parsing, offset preservation, per-file failures, and no source changes;
  domain tests prove priority and conflict behavior independently of ExifTool.
- Revisit when: ExifTool changes relevant output semantics, a new format-specific
  mapping is proposed, or timezone requirements change.
