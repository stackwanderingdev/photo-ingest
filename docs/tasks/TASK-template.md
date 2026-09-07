# TASK-NNN: `<SHORT TITLE>`

- Status: `Ready | In Progress | Blocked | Done`
- Owner: `<NAME/AGENT>`
- Created: `<YYYY-MM-DD>`

## Goal

A small, verifiable outcome that ideally fits one commit:

`<GOAL>`

## Context and requirements

- Implements: `<REQ-...>, <NFR-...>`
- Affected UX rules/journeys: `<UX-... OR NOT APPLICABLE + REASON>`
- Protects: `<INV-...>`
- Relevant ADRs: `<ADR-NNN>`
- Dependencies: `<TASK-NNN OR NONE>`

## Current behavior

`<EVIDENCE-BASED CURRENT BEHAVIOR>`

## Required behavior

`<REQUIRED OBSERVABLE BEHAVIOR>`

## Allowed change scope

Only the following files or modules may change:

- `<PATH>`

## Prohibited changes

- `<UNAFFECTED LAYER/INTERFACE/FORMAT/DEPENDENCY>`
- No additional refactoring or opportunistic fixes.

## Acceptance criteria

```gherkin
Given <INITIAL STATE>
When <ACTION>
Then <OUTCOME>
And <ADDITIONAL CONDITION>
```

### Edge and error cases

- `<CASE>` -> `<EXPECTED OUTCOME>`

### Affected user states

- Loading: `<BEHAVIOR OR NOT APPLICABLE>`
- Empty: `<BEHAVIOR OR NOT APPLICABLE>`
- Error/offline: `<BEHAVIOR OR NOT APPLICABLE>`
- Permission: `<BEHAVIOR OR NOT APPLICABLE>`
- Keyboard/assistive technology: `<EVIDENCE OR NOT APPLICABLE>`

## Implementation plan

1. `<SMALL STEP>`
2. `<SMALL STEP>`

## Verification

```text
Targeted tests:   <COMMAND>
Regression:       <COMMAND>
Lint/types:       <COMMAND>
Build:            <COMMAND>
UX/accessibility: <TEST, REVIEW, OR NOT APPLICABLE + REASON>
```

## Completion report

- Changed files: `<LIST>`
- Checks executed and results: `<LIST>`
- Checks not executed and reasons: `<LIST OR NONE>`
- Remaining risks/open issues: `<LIST OR NONE>`
