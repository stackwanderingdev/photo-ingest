# REQ-FORMAT-001 — Support the initial original photo formats

- Status: `Accepted`
- Priority: `Must`
- Source/goal: `PRD-IMPORT-001`
- Affected journey/UX rule: `UJ-001`, `UX-003`, `UX-006`, `UX-007`, `UX-010`, `UX-012`

## Behavior

When PhotoIngest discovers a JPEG (`.jpg`, `.jpeg`), HEIC/HEIF (`.heic`,
`.heif`), or DNG (`.dng`) photo, it must treat the file as an initially
supported original format and derive import metadata without converting or
rewriting the original.

A multi-image HEIF file is one source file and one unchanged container.
PhotoIngest must not automatically extract its contained images.

PNG, WebP, TIFF, AVIF, and vendor-specific RAW formats are outside the required
initial format set, but are not prohibited from later support through an
explicit requirement change.

## Acceptance examples

```gherkin
Given representative JPEG, HEIC, HEIF, and DNG source files
When the user requests an import preview
Then every file is classified as a supported original format
And its planned operation preserves the original bytes and container
And no converted or extracted derivative is planned
```

## Edge and error cases

- A supported extension whose content cannot be recognized or read -> report a file-specific error and do not plan deletion.
- A multi-image HEIF container -> treat it as one file and do not create plans for extracted images.
- A format outside the required initial set -> report it as not currently supported without implying permanent exclusion.

## Verification

- Test level: `Unit | Integration`
- Evidence: Representative fixtures for every accepted extension and a byte-for-byte unchanged source snapshot.

## Change history

- `2026-09-07`: Accepted JPEG, HEIC/HEIF, and DNG as the first required format set with unchanged originals.
