# Functional Requirements

This document is the index and usage guide for observable system behavior.
Libraries, classes, database tables, and implementation techniques belong
elsewhere.

## Convention

Identifier: `REQ-<AREA>-NNN`. Create every requirement as a separate file under
`functional/` using `functional/REQ-template.md`. Use a lowercase hyphenated
title after the identifier, for example `REQ-AUTH-001-sign-in.md`.

## Requirement index

| Requirement | Title | Status | Priority | Goal |
|---|---|---|---|---|
| [`REQ-IMPORT-001`](functional/REQ-IMPORT-001-transfer-photos.md) | Transfer photos to the local library | `Draft` | `Must` | `PRD-IMPORT-001` |
| [`REQ-PREVIEW-001`](functional/REQ-PREVIEW-001-preview-import.md) | Preview an import without changing files | `Draft` | `Must` | `PRD-IMPORT-001` |
| [`REQ-FORMAT-001`](functional/REQ-FORMAT-001-supported-original-formats.md) | Support the initial original photo formats | `Accepted` | `Must` | `PRD-IMPORT-001` |
| [`REQ-SAFETY-001`](functional/REQ-SAFETY-001-protect-associated-media.md) | Protect associated media from silent loss | `Accepted` | `Must` | `PRD-IMPORT-001` |
| [`REQ-METADATA-001`](functional/REQ-METADATA-001-resolve-capture-time.md) | Resolve the authoritative capture time | `Accepted` | `Must` | `PRD-IMPORT-001` |
| [`REQ-DUPLICATE-001`](functional/REQ-DUPLICATE-001-detect-content-duplicates.md) | Detect complete-content duplicates | `Accepted` | `Must` | `PRD-IMPORT-001` |
| [`REQ-ORGANIZE-001`](functional/REQ-ORGANIZE-001-name-from-exif.md) | Name imported photos from EXIF data | `Draft` | `Must` | `PRD-IMPORT-001` |
| [`REQ-ORGANIZE-002`](functional/REQ-ORGANIZE-002-file-from-exif.md) | File imported photos from EXIF data | `Draft` | `Must` | `PRD-IMPORT-001` |
| [`REQ-ORGANIZE-003`](functional/REQ-ORGANIZE-003-resolve-destination-collisions.md) | Resolve destination-name collisions | `Accepted` | `Must` | `PRD-IMPORT-001` |
| [`REQ-PLAN-001`](functional/REQ-PLAN-001-revalidate-import-plan.md) | Revalidate an import plan before mutation | `Accepted` | `Must` | `PRD-IMPORT-001` |
| [`REQ-SAFETY-002`](functional/REQ-SAFETY-002-control-source-deletion.md) | Control source deletion eligibility and execution | `Accepted` | `Must` | `PRD-IMPORT-001` |

Do not define requirements in this index. Add exactly one row linking to each
concrete requirement file. Never reuse an identifier for different behavior.
