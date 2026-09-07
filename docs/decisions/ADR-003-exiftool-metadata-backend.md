# ADR-003: ExifTool metadata backend

- Status: `Accepted`
- Date: `2026-09-07`
- Decision makers: `Daniel (Architecture Owner)`
- Supersedes: `Not applicable`
- Superseded by: `Not applicable`

## Context

The first required photo formats are JPEG, HEIC/HEIF, and DNG. PhotoIngest
needs consistent read-only access to the metadata required for destination
naming and filing without decoding, converting, or rewriting original image
content. Metadata failures must remain attributable to individual source files.

The application is licensed under MIT. pyexiv2 would introduce an in-process
GPLv3 dependency, while Pillow plus pillow-heif does not provide one uniform,
verified metadata solution for the accepted JPEG, HEIC/HEIF, and DNG scope.

## Decision

Use ExifTool as the metadata backend through an encapsulated infrastructure
adapter. Only the adapter may invoke ExifTool. The adapter must use exclusively
read-only operations and must never modify source files.

Domain and application logic receive normalized project-owned metadata values.
They must not know ExifTool tag names, command-line arguments, process details,
or raw output structures.

At runtime and during verification, check ExifTool availability and a minimum
supported version. The exact minimum version remains to be established from the
required fields and representative evidence before the stack profile becomes
Accepted.

Verify actual suitability with representative JPEG, HEIC/HEIF, and DNG test
files. The adapter contract must support per-file outcomes for metadata errors,
timeouts, invalid output, unavailable required metadata, and other technical
failures without losing the original cause.

Pillow and pillow-heif are not part of this metadata decision. They may be
evaluated independently later if decoded visual previews become required.

Bundling ExifTool with a future application distribution is outside this
decision. Its installation, redistribution, packaging, and licensing questions
remain open. Batch evaluation and ExifTool's persistent process mode remain
possible later optimizations and are not part of the first increment.

## Alternatives considered

### Pillow with pillow-heif

- Benefits: In-process Python APIs and potential reuse for visual previews.
- Drawbacks: Couples metadata access to image-format plugins and does not provide one verified solution for JPEG, HEIC/HEIF, and DNG.
- Reason not selected: The accepted scope requires a uniform metadata backend; visual preview decoding is a separate concern.

### pyexiv2

- Benefits: In-process metadata access, Python 3.14 Linux wheels, and broad format support through Exiv2.
- Drawbacks: GPLv3 licensing conflicts with the accepted MIT dependency strategy; the project also documents lack of thread safety.
- Reason not selected: It is unsuitable as the accepted in-process dependency for this MIT-licensed application.

### Exiv2 command-line tool

- Benefits: External process boundary and support for JPEG, DNG, and BMFF formats when enabled.
- Drawbacks: HEIC/HEIF support depends on a build option and must be inspected per installation.
- Reason not selected: ExifTool provides the preferred uniform external metadata interface for the accepted formats.

## Consequences

- Positive: Domain behavior remains independent of vendor-specific tag names and process mechanics.
- Positive: One backend covers the initial formats and leaves room for later format expansion.
- Positive: Read-only metadata extraction is separated from future image-preview decoding.
- Negative/trade-off: ExifTool becomes an external runtime prerequisite unless a later bundling decision changes distribution.
- Negative/trade-off: Process execution, timeouts, output validation, and per-file error mapping require an explicit adapter boundary.
- Prohibited unless this ADR is superseded: Invoking ExifTool outside the infrastructure adapter; exposing ExifTool tags or process structures to domain or application code; using ExifTool write operations; silently adding Pillow or pillow-heif as metadata dependencies.
- Required follow-up: Establish the minimum ExifTool version, normalize capture-time semantics, add representative fixtures, and record executable commands in the stack profile.

## Evidence and review

- Affected requirements: `REQ-FORMAT-001`, `REQ-PREVIEW-001`, `REQ-ORGANIZE-001`, `REQ-ORGANIZE-002`
- Verification criteria: Representative JPEG, HEIC/HEIF, and DNG fixtures yield normalized per-file metadata or a classified per-file failure; source bytes and filesystem metadata remain unchanged.
- Revisit when: A required format or metadata field is unsupported, process overhead violates an accepted NFR, distribution requires bundling, or a licensing constraint changes.
