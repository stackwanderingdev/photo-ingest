# Product Requirements

## Document status

- Product: `PhotoIngest`
- Owner: `Project owner (name to be confirmed)`
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

- Platforms other than Linux.
- Editing image content or EXIF metadata.
- Cloud-hosted photo storage or synchronization unless added by a later approved requirement.
- General photo-library browsing, cataloging, or image editing unless added by a later approved requirement.

## Assumptions and constraints

- Assumption: The primary user controls both the attached source device and the local destination library; confirm with the product owner before accepting trust-boundary decisions.
- Constraint: The supported operating system is Linux.
- Constraint: Imported photo naming and destination structure are derived from EXIF data according to rules that still require approval.

## Open questions

| ID | Question | Owner | Due | Status |
|---|---|---|---|---|
| `Q-001` | Which interface should the first increment provide (CLI, desktop GUI, or another interface)? | Product owner | Before architecture acceptance | `Open` |
| `Q-002` | Which connected-device access methods must be supported initially (for example a mounted filesystem, MTP, or both)? | Product owner | Before architecture acceptance | `Open` |
| `Q-003` | What exact EXIF fields, filename pattern, directory pattern, timezone handling, and fallback behavior are required? | Product owner | Before requirement acceptance | `Open` |
| `Q-004` | Should import copy or move source files, and what verification is required before any source deletion? | Product owner | Before requirement acceptance | `Open` |
| `Q-005` | How should duplicates, filename collisions, missing or malformed EXIF data, unsupported files, and interrupted imports be handled? | Product owner | Before requirement acceptance | `Open` |
| `Q-006` | Which language/toolchain, project license, initial version, and accountable decision owner(s) apply? | Project owner | Before bootstrap completion | `Open` |

## Acceptance framework

Describe who accepts product goals, when, and based on which evidence.

The accountable product owner reviews and explicitly accepts product goals and
functional behavior. The owner assignment is still open; until it is confirmed,
new normative artifacts remain Draft.
