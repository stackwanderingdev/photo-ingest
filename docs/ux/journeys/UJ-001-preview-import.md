# UJ-001 — Preview a planned photo import

- Status: `Draft`
- Primary user: `USR-001`
- User goal: Understand where photos would be imported before any file changes occur.
- Requirements: `REQ-PREVIEW-001`, `REQ-DUPLICATE-001`,
  `REQ-ORGANIZE-001`, `REQ-ORGANIZE-002`, `REQ-ORGANIZE-003`,
  `REQ-PLAN-001`
- UX rules: `UX-002`, `UX-003`, `UX-005`, `UX-006`, `UX-007`, `UX-010`,
  `UX-012`, `UX-PROJ-001`, `UX-PROJ-003`
- Entry: The graphical desktop application is open.
- Success: The user sees planned destination paths and file-specific problems, while source and destination remain unchanged.

## Main flow

| Step | User intent/action | System response | Visible status |
|---|---|---|---|
| 1 | Choose an accessible local or already mounted filesystem location. | Provide filesystem selection without offering MTP or application-managed network connections in this increment. | Selected source and access state |
| 2 | Select a subdirectory within the filesystem source. | Validate access and retain the selected source scope. | Selected source path |
| 3 | Select the configurable destination root. | Validate whether the destination can be inspected. | Selected destination root |
| 4 | Request a preview. | Discover photos, read required EXIF data, and derive planned paths without mutating files. | Progress where the total is known; otherwise current activity and cancellation |
| 5 | Review the plan and problems. | Show each source, its reserved destination where available, and a distinguishable outcome classification. | Preview summary and item-level details, including already imported, within-plan duplicate, name collision, and blocking conflict states |

## Alternatives and interruptions

| Trigger | Behavior | Resume/recovery |
|---|---|---|
| Source or destination is inaccessible | Explain which location failed and preserve other selections. | Retry access or choose another location. |
| Scan or metadata reading fails for one file | Keep the item in the result with an actionable blocking classification and no unsupported final path. | Review the item, correct the source where possible, and create a new preview. |
| Existing destination is byte-identical | Keep the source visible, refer to the existing destination, and label it already imported without planning another copy. | Review the non-copy outcome. |
| Sources in the plan are byte-identical | Keep every source as a separate item, label later occurrences as within-plan duplicates, and show their shared destination. | Review each independent item state. |
| Different regular file occupies a derived name | Reserve the deterministic suffixed path and show a non-blocking name collision. | Review the adjusted destination. |
| Non-regular object occupies a proposed path | Show a blocking destination-path conflict without following or replacing the object. | Remove the conflict or choose another destination and create a new preview. |
| A relevant assumption changes after preview | Mark the affected item stale; do not silently reassign or execute it. | Create and explicitly confirm an updated preview. |
| User cancels scanning | Stop safely without changing files and show that the preview is incomplete. | Restart the preview. |
| Source disconnects | Stop dependent scanning, report the disconnection, and retain completed preview results as incomplete. | Reconnect and restart or select another source. |

## State matrix

| State | Presentation/output | Available actions | Accessibility note |
|---|---|---|---|
| Loading | Current scan activity, progress where available, and explicit non-mutating status | Cancel | Status is programmatically exposed and does not rely on animation alone. |
| Empty | No supported photos were found in the selected scope | Change source or subdirectory; rescan | Explanation and next actions receive logical focus. |
| Error | Location or item-level cause plus what remained unchanged | Retry, change selection, or inspect details | Error is textual and associated with the affected control or row. |
| Success | Count and planned paths, with warnings separated from importable items | Review or change selections | Summary and table are keyboard navigable. |
| Already imported | Existing byte-identical destination and no planned copy | Review source and destination | Text identifies the state independently of color. |
| Within-plan duplicate | Separate source item and shared planned destination | Review every affected source | The relationship and independent item states are programmatically exposed. |
| Name collision | Reserved suffixed destination and non-blocking explanation | Review the adjusted path | Original and adjusted names are available as text. |
| Stale plan | Changed assumption and absence of executable current plan | Create a new preview | The required next action is explicit and receives logical focus. |
| Blocking destination-path conflict | Object type and affected proposed path without content inspection | Resolve conflict or choose another destination | The state is textual and distinguished from a resolvable name collision. |

## Open design questions

| ID | Question | Options | Decision criterion | Status |
|---|---|---|---|---|
| `UXQ-001` | How should future MTP selection coexist with filesystem selection? | Unified chooser; source-type selector with specialized chooser | Successful selection with clear capability, permission, and connection feedback | `Deferred until the MTP feasibility comparison` |
| `UXQ-002` | Which preview columns and grouping are required for the first increment? | Minimal source/destination/status plus accessible detail for the accepted outcome states; extended metadata details | Understandability without unnecessary complexity | `Open` |
