# UX Documentation

This area connects product understanding, requirements, and interaction design.
UX is not only visual design; it addresses whether defined users can achieve
their goals effectively, efficiently, understandably, and accessibly in their
actual context.

## Documents

| Document | Purpose | Character |
|---|---|---|
| `user-research.md` | Users, context, needs, and evidence | Descriptive; source for requirements |
| `ux-guidelines.md` | Binding UX baseline and active profile | Normative when `Accepted` |
| `interaction-design.md` and `journeys/` | Journey index and one interaction contract per file | Normative when `Accepted` |
| `accessibility.md` | Accessibility target, standards, and evidence | Normative when `Accepted` |
| `usability-evaluation.md` | Research/evaluation plan and results | Verification and decision evidence |

## Workflow

```text
Understand users and context
    -> define problems and user goals
    -> derive REQ-/NFR-/UX rules
    -> design interactions and states
    -> prototype or implement
    -> evaluate with suitable users and checks
    -> feed evidence back through controlled changes
```

Research findings do not silently change accepted requirements or designs. They
produce a traceable change with source, rationale, and affected identifiers.

## Scaling

Scale effort by risk and user exposure. An internal CLI needs no visual design
system but still needs understandable commands, help, output, and errors. A
public web or mobile application commonly needs formal accessibility goals,
multiple device contexts, and user testing.

Select an effort level in `ux-guidelines.md`. At `Minimal`, documented user
understanding and a walkthrough may be sufficient; formal research is optional.
