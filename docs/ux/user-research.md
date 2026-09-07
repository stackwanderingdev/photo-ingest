# User Research

This document records evidence, assumptions, and insights. Do not invent
personas. Store personal raw data only in designated protected locations.

For `Minimal` UX effort, a short self-assessment may replace formal research.
State why the users and context are sufficiently understood.

## Research frame

- UX effort: `Proposed: Minimal; approval pending UX profile review`
- Research question: `Can the intended personal user reliably import and organize photos on their Linux system?`
- Method: `Initial project statement; self-assessment and walkthrough still required`
- Period: `2026-09-07`
- Sample and selection: `Daniel, the intended personal user and decision owner`
- Limitations/bias: `No observed workflow or representative device and photo set has yet been evaluated.`
- Consent and privacy: `Not applicable for the initial project statement; no personal research data was collected.`

## User group USR-001 — Personal Linux user

- Goals: Transfer photos from an attached device and obtain a consistently named and structured local library.
- Tasks: Connect a source device, initiate an import, understand its progress and outcome, and recover from import problems.
- Context: The user's own Linux system, local photo library, and attached device such as a smartphone.
- Capabilities and constraints: Uses a graphical Linux desktop application; sources may be filesystem, MTP, or network paths and require subdirectory selection.
- Existing tools/workarounds: Manual transfer and organization are inferred from the problem statement and must be confirmed.
- Frequency: `UNKNOWN`; confirm during the initial walkthrough.

## Evidence and assumptions

| ID | Statement | Type | Source | Confidence | Validation |
|---|---|---|---|---|---|
| `INS-001` | The product is intended for a personal Linux workflow. | `Evidence` | Current project statement | `High` | Product-owner review |
| `INS-002` | Consistent EXIF-derived naming and filing are the core intended outcome. | `Evidence` | Current project statement | `High` | Product-owner review and representative examples |
| `INS-003` | Manual import is currently repetitive and inconsistent. | `Assumption` | Inferred problem framing | `Medium` | Confirm in self-assessment walkthrough |

## Derived changes

| Insight | Affected goals/requirements | Decision/task |
|---|---|---|
| `INS-001` | `PRD-IMPORT-001`, `NFR-PORT-001` (planned) | Constrain the product to Linux after explicit acceptance |
| `INS-002` | `REQ-ORGANIZE-001`, `REQ-ORGANIZE-002` | Obtain concrete EXIF mapping examples before acceptance |
