# UX Standards and Active UX Profile

These rules form the technology-independent minimum. They apply to graphical
interfaces, CLIs, APIs, and other human-system interfaces where relevant.

## Status and profile

- Status: `Accepted`
- UX effort: `Minimal`
- Owner: `Daniel`
- Last reviewed: `2026-09-07`
- Interface types: `Desktop`
- Primary users: `USR-001 in user-research.md`
- Critical journeys: `UJ-001`

### Effort levels

| Level | Typical use | Minimum evidence |
|---|---|---|
| Minimal | Personal script or low-risk internal tool | User, primary task, context, key risk, and walkthrough |
| Standard | Team tool or product with a bounded audience | User groups, journeys, states, and informal evaluation |
| Extended | Public product or diverse audience | Research, prototypes, and structured usability tests |
| Critical | High-impact, regulated, or safety-relevant system | Formal research, accessibility evidence, and repeated evaluation |

Research methods are risk-based. User understanding is always required; formal
interviews or studies are not mandatory for a small, well-understood tool.

## Binding baseline

### UX-001 — Users and context

Base decisions on named user groups, goals, capabilities, devices, and contexts.
Mark unsupported assumptions and define how they will be validated.

### UX-002 — Task orientation

Support actual user goals and vocabulary. Align information architecture with
users' mental models and workflows, not internal technical structure.

### UX-003 — Visible system status

Provide timely, understandable feedback about actions, progress, persistence,
connectivity, and completion. Avoid indefinite waits and ambiguous intermediate states.

### UX-004 — Consistency and platform conventions

Make equivalent terms and interactions behave consistently. Follow target
platform conventions unless evidence supports a deviation.

### UX-005 — User control and reversibility

Allow appropriate cancellation, exit, and correction. Name destructive or
irreversible actions clearly, protect them from accidental activation, and make
them reversible where practical.

### UX-006 — Error prevention and recovery

Prevent foreseeable errors. Explain what happened, what remained unchanged, and
how to recover. Preserve input where security and privacy permit.

### UX-007 — Complete state design

Design applicable normal, loading, empty, success, error, offline, permission,
and partial states.

### UX-008 — Progressive disclosure

Keep frequent information and actions discoverable. Reveal rare or complex
options contextually without hiding core functionality or overwhelming users.

### UX-009 — Accessibility and inclusion

Do not make operation or information depend solely on vision, color, hearing,
precise pointer control, or complex gestures. Define targets in `accessibility.md`.

### UX-010 — Understandable content

Use precise, concise, actionable language appropriate to the audience. Keep
terminology, abbreviations, date, number, and unit formats consistent. Do not
block localization through concatenated interface strings.

### UX-011 — Efficiency and learnability

Make first use possible without unnecessary prior knowledge. Let returning users
complete frequent work efficiently without harming learnability or accessibility.

### UX-012 — Trust, privacy, and fair interaction

Explain data use, permissions, cost, and consequences before commitment. Dark
patterns, hidden consent, artificial pressure, and deceptive design are prohibited.

### UX-013 — Responsive and robust interaction

Support defined viewports, input methods, languages, zoom levels, and network
conditions. Do not expose technical limitations as unexplained UX behavior.

### UX-014 — Evidence and evaluation

Support UX decisions with user research, usability tests, accessible prototypes,
usage evidence, or explicitly documented assumptions. Respect privacy and do not
equate measurement with user value.

## Interface-specific profiles

| Profile | Additional concerns | Active? |
|---|---|---|
| Web | Responsive layout, browser behavior, URL/navigation, WCAG, keyboard | `No` |
| Mobile | Touch targets, orientation, platform conventions, interruptions | `No` |
| Desktop | Windows, keyboard, focus, platform integration, scaling | `Yes` |
| CLI | Help, examples, exit codes, pipes, non-interactive use | `No user-facing CLI planned` |
| API | Consistent concepts, discoverability, contracts, errors, examples | `No public API planned` |

## Project-specific UX rules

| ID | Rule | User/journey | Evidence | Status |
|---|---|---|---|---|
| `UX-PROJ-001` | A preview must state clearly that it will not change source or destination files. | `USR-001` / `UJ-001` | GUI system test and owner walkthrough | `Accepted` |
| `UX-PROJ-002` | Source selection must expose filesystem, MTP, and network locations and allow selecting a contained subdirectory. | `USR-001` / `UJ-001` | Owner walkthrough with representative sources | `Accepted` |

## Official foundations

- [ISO 9241-210:2019 — Human-centred design](https://www.iso.org/standard/77520.html)
- [WCAG 2.2](https://www.w3.org/TR/WCAG22/)
