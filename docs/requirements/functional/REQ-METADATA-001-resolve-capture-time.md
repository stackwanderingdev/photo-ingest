# REQ-METADATA-001 — Resolve the authoritative capture time

- Status: `Accepted`
- Priority: `Must`
- Source/goal: `PRD-IMPORT-001`
- Affected journey/UX rule: `UJ-001`, `UX-003`, `UX-006`, `UX-007`, `UX-010`, `UX-012`

## Behavior

For each supported photo, the system must select the valid capture-time
candidate from the highest available semantic priority:

1. the original capture timestamp, including associated subsecond precision and
   an explicitly stored UTC offset;
2. the digitization or creation timestamp, only when no valid first-priority
   candidate exists;
3. a format-specific capture timestamp, only when no valid higher-priority
   candidate exists and the adapter has unambiguously defined and verified its
   semantics and timezone interpretation for that source.

Lower-priority values are fallbacks. A lower-priority value that differs from a
valid selected higher-priority value does not by itself constitute a conflict.
GPS time is used only for plausibility assessment in the first increment and is
not a capture-time fallback. Modification timestamps and filesystem timestamps
are not capture-time candidates.

The selected value retains its local date and time, available subsecond
precision, explicit UTC offset, semantic provenance, and timezone-known status.
Its local date and time remain authoritative for destination naming and filing;
the system must not convert them to the executing system's timezone.

## Acceptance examples

```gherkin
Given a valid original capture timestamp and a different valid digitization timestamp
When the system resolves the photo's capture time
Then it selects the original capture timestamp
And it does not report a conflict solely because the fallback differs
```

```gherkin
Given no valid original capture timestamp
And a valid digitization timestamp
When the system resolves the photo's capture time
Then it selects the digitization timestamp
```

```gherkin
Given two semantically equivalent candidates with identical local date and time
And only one candidate includes subsecond precision or an explicit UTC offset
When the system resolves the photo's capture time
Then it treats the additional value as a compatible precision refinement
```

```gherkin
Given two semantically equal candidates with explicit UTC offsets
And their normalized absolute times differ
When the system resolves the photo's capture time
Then it reports a blocking capture-time conflict
```

```gherkin
Given a valid local capture timestamp without a UTC offset
When the system resolves the photo's capture time
Then it selects that timestamp
And marks its timezone as unknown
```

## Edge and error cases

- Multiple semantically equal or equivalent candidates resolve to different
  capture times -> report a blocking conflict.
- Matching local date and time with additional subsecond precision or an
  explicit UTC offset -> accept the additional value as compatible precision.
- Only one of two matching local values has an explicit UTC offset -> the offset
  may enrich the selected value, but the system must not claim that the two
  inputs denote the same absolute instant.
- Both compared values have explicit offsets -> normalize them for conflict
  comparison without changing the selected local value used for naming and
  filing.
- Missing UTC offset -> retain the otherwise valid local timestamp and mark its
  timezone as unknown.
- Syntactically invalid or impossible calendar date or time -> reject that
  candidate as invalid.
- Additional plausibility limits, including treatment of dates far in the
  future, remain open under `Q-010`; no unspecified limit may be applied.
- Missing or invalid capture time, or a blocking conflict -> do not produce a
  final destination path and block import and deletion release as required by
  `INV-SAFETY-001`.

## Verification

- Test level: `Unit | Integration`
- Evidence: Table-driven domain tests for priority, precision, offset comparison,
  invalid calendar values, missing values, and conflicts; adapter integration
  tests with representative JPEG, HEIC/HEIF, and DNG files under `ADR-004`.

## Change history

- `2026-09-07`: Accepted capture-time priority, comparison, timezone, and
  blocking-error behavior by Daniel.
