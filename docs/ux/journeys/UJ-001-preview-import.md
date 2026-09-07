# UJ-001 — Preview a planned photo import

- Status: `Draft`
- Primary user: `USR-001`
- User goal: Understand where photos would be imported before any file changes occur.
- Requirements: `REQ-PREVIEW-001`, `REQ-ORGANIZE-001`, `REQ-ORGANIZE-002`
- UX rules: `UX-002`, `UX-003`, `UX-005`, `UX-006`, `UX-007`, `UX-010`, `UX-012`
- Entry: The graphical desktop application is open.
- Success: The user sees planned destination paths and file-specific problems, while source and destination remain unchanged.

## Main flow

| Step | User intent/action | System response | Visible status |
|---|---|---|---|
| 1 | Choose a source type and accessible source location. | Offer filesystem, MTP, and network sources supported by the current environment. | Selected source and access state |
| 2 | Select a subdirectory within the source. | Validate access and retain the selected source scope. | Selected source path |
| 3 | Select the configurable destination root. | Validate whether the destination can be inspected. | Selected destination root |
| 4 | Request a preview. | Discover photos, read required EXIF data, and derive planned paths without mutating files. | Progress where the total is known; otherwise current activity and cancellation |
| 5 | Review the plan and problems. | Show each source, planned `YYYY/MM/YYYYMMDD_HHMMSS.ext` destination, and outcome classification. | Preview summary and item-level details |

## Alternatives and interruptions

| Trigger | Behavior | Resume/recovery |
|---|---|---|
| Source or destination is inaccessible | Explain which location failed and preserve other selections. | Retry access or choose another location. |
| Scan or EXIF reading fails for one file | Keep the item in the result with an actionable problem classification. | Review the item; policy remains open under Q-005. |
| User cancels scanning | Stop safely without changing files and show that the preview is incomplete. | Restart the preview. |
| Source disconnects | Stop dependent scanning, report the disconnection, and retain completed preview results as incomplete. | Reconnect and restart or select another source. |

## State matrix

| State | Presentation/output | Available actions | Accessibility note |
|---|---|---|---|
| Loading | Current scan activity, progress where available, and explicit non-mutating status | Cancel | Status is programmatically exposed and does not rely on animation alone. |
| Empty | No supported photos were found in the selected scope | Change source or subdirectory; rescan | Explanation and next actions receive logical focus. |
| Error | Location or item-level cause plus what remained unchanged | Retry, change selection, or inspect details | Error is textual and associated with the affected control or row. |
| Success | Count and planned paths, with warnings separated from importable items | Review or change selections | Summary and table are keyboard navigable. |

## Open design questions

| ID | Question | Options | Decision criterion | Status |
|---|---|---|---|---|
| `UXQ-001` | How should filesystem, MTP, and network source selection be presented consistently? | Unified chooser; source-type selector with specialized chooser | Successful selection with clear permission and connection feedback | `Open` |
| `UXQ-002` | Which preview columns and grouping are required for the first increment? | Minimal source/destination/status; extended EXIF details | Understandability without unnecessary complexity | `Open` |
