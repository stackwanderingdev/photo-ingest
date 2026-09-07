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
| [`REQ-ORGANIZE-001`](functional/REQ-ORGANIZE-001-name-from-exif.md) | Name imported photos from EXIF data | `Draft` | `Must` | `PRD-IMPORT-001` |
| [`REQ-ORGANIZE-002`](functional/REQ-ORGANIZE-002-file-from-exif.md) | File imported photos from EXIF data | `Draft` | `Must` | `PRD-IMPORT-001` |

Do not define requirements in this index. Add exactly one row linking to each
concrete requirement file. Never reuse an identifier for different behavior.
