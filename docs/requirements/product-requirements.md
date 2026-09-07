# Product Requirements

## Document status

- Product: `PhotoIngest`
- Owner: `Daniel (Product Owner)`
- Status: `Draft`
- Last updated: `2026-09-07`

## Problem and context

Describe the concrete problem, affected users, and environment without assuming
a solution.

Photos stored on connected devices such as smartphones need to be transferred
to a local photo library on a Linux system. Manual transfer, naming, and filing
make the resulting library inconsistent and require repeated effort. PhotoIngest
is intended to perform that transfer and organize imported photos using their
EXIF metadata.

## Target users

| User group | Need | Usage context |
|---|---|---|
| Personal Linux user (`USR-001`) | Import photos from connected devices into a consistently organized local library | On the user's own Linux system with a source device attached |

Detailed evidence and assumptions belong in `docs/ux/user-research.md`.
Requirements may reference research insights without making raw notes normative.

## Product goals

Store each goal as a separate file under `goals/`, created from
`goals/PRD-template.md`. Maintain a concise index in `goals/README.md`; do not
append goal definitions to this overview.

## Non-goals

- Support for operating systems other than Linux in the initial product.
- Editing image content or EXIF metadata.
- Cloud-hosted photo storage or synchronization unless added by a later approved requirement.
- General photo-library browsing, cataloging, or image editing unless added by a later approved requirement.

## Assumptions and constraints

- Assumption: The primary user controls both the attached source device and the local destination library; validate during the first workflow walkthrough.
- Constraint: The initial supported operating system is Linux; future platform support is not prohibited.
- Constraint: The product provides a graphical desktop interface.
- Constraint: Sources include filesystem paths, MTP-accessible devices, and network paths, with selection of a contained subdirectory.
- Constraint: A completed import deletes its source file only after successful destination verification.
- Constraint: Imported photo naming and destination structure are derived from EXIF data according to rules that still require approval.

## Open questions

| ID | Question | Owner | Due | Status |
|---|---|---|---|---|
| `Q-001` | Which interface should the first increment provide (CLI, desktop GUI, or another interface)? | Daniel | 2026-09-07 | `Resolved: graphical desktop application` |
| `Q-002` | Which connected-device access methods must be supported initially? | Daniel | 2026-09-07 | `Resolved: filesystem, MTP, and network paths; selectable subdirectories` |
| `Q-003` | What exact EXIF fields, filename pattern, directory pattern, timezone handling, and fallback behavior are required? | Product owner | Before requirement acceptance | `Open` |
| `Q-004` | Should import copy or move source files, and what verification is required before any source deletion? | Daniel | Before requirement acceptance | `Partly resolved: delete source after verification; verification definition remains open` |
| `Q-005` | How should duplicates, filename collisions, missing or malformed EXIF data, unsupported files, and interrupted imports be handled? | Product owner | Before requirement acceptance | `Open` |
| `Q-006` | Which language/toolchain, project license, and initial version apply? | Daniel | 2026-09-07 | `Resolved: accepted foundation recorded in ADR-001; metadata library remains open pending format scope` |
| `Q-007` | Which photo formats are initially supported, including HEIC/HEIF behavior, and which metadata solution satisfies that scope? | Daniel | 2026-09-07 | `Resolved: JPEG, HEIC/HEIF, and DNG with ExifTool per ADR-003` |
| `Q-009` | Which minimum ExifTool version is required? | Daniel | Before stack-profile acceptance | `Open; determine from required tags, JSON behavior, and representative fixtures` |
| `Q-008` | How are network and MTP sources integrated? | Daniel | 2026-09-07 | `Resolved by ADR-002: mounted network paths use filesystem access; MTP remains distinct and its technology requires a feasibility comparison` |

## Acceptance framework

Describe who accepts product goals, when, and based on which evidence.

Daniel holds the Product, UX, Architecture, Security/Risk, and Task Owner roles
for this personal project. Daniel reviews and explicitly accepts normative
artifacts and task completion.
