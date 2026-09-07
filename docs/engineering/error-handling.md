# Error Handling

## Principles

- Detect errors where enough context exists to handle them.
- Preserve the original cause when translating or propagating an error.
- Keep business rejections, validation errors, technical failures, and defects distinct.
- Partial operations must not leave silent inconsistent state.
- Retry only transient, idempotent operations with explicit limits.
- Give users actionable messages without internal or sensitive details.
- Log technical context and correlation identifiers, never secrets.

## Error categories

| Category | Example | Response | Visibility |
|---|---|---|---|
| Validation | `<INVALID INPUT>` | Reject and explain the field | User + optional metric |
| Business | `<RULE VIOLATION>` | Defined domain outcome | User + audit if needed |
| Transient | `<TIMEOUT>` | Limited retry or abort | Log + metric |
| Permanent technical | `<SCHEMA ERROR>` | Fail safely | Alert + log |
| Programming defect | `<INVARIANT VIOLATION>` | Fail fast at boundary | Alert + diagnostics |

## Contract per system boundary

For API, UI, queue, file, and database boundaries define:

- permitted error forms or status codes: `<DEFINITION>`
- timeout: `<VALUE>`
- retry/backoff: `<STRATEGY OR NO RETRY>`
- idempotency: `<KEY/RULE>`
- transaction/compensation behavior: `<RULE>`
- logging and alerting: `<RULE>`

Empty catch blocks, blanket suppression, and return values without defined error
semantics are prohibited.
