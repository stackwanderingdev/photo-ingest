# REQ-SAFETY-001 — Protect associated media from silent loss

- Status: `Accepted`
- Priority: `Must`
- Source/goal: `PRD-IMPORT-001`
- Affected journey/UX rule: `UJ-001`, `UX-003`, `UX-005`, `UX-006`, `UX-007`, `UX-012`

## Behavior

When PhotoIngest recognizes a file as an associated media component that is not
yet supported for import, it must identify that component visibly, exclude it
from deletion, and prevent any import outcome that could silently discard it.

The future treatment of Live Photos or other associated media as importable
logical groups remains undecided and is not implied by this safety requirement.

## Acceptance examples

```gherkin
Given a supported photo with a recognized but unsupported companion file
When the user requests an import preview
Then the companion is shown as not currently supported
And no deletion is planned for the companion
And the preview does not claim that the complete associated media set will be imported
```

## Edge and error cases

- Association is uncertain -> report the ambiguity and plan no deletion for the possible companion.
- Companion metadata cannot be read -> report the error and plan no deletion.
- No known companion is present -> do not infer that a companion was lost.

## Verification

- Test level: `Unit | Integration | System`
- Evidence: Paired and ambiguous media fixtures showing visible classification and absence of delete plans.

## Change history

- `2026-09-07`: Accepted the no-silent-loss rule without committing to future Live Photo import behavior.
