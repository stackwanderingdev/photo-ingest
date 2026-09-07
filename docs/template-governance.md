# Template Governance and Release Policy

This document governs the template itself. A derived project may adopt its own
release process, but retains `template-manifest.yml` as provenance.

## Goals

- Keep the template coherent, technology-independent, and usable at different scales.
- Make every release identifiable and reproducible.
- Prevent silent changes to authority, identifiers, or workflow contracts.
- Let derived projects evaluate upgrades instead of copying changes blindly.
- Preserve useful history without accumulating obsolete rules indefinitely.

## Sources of truth

- `template-manifest.yml` defines current template identity, version, status, language, license, and source.
- `CHANGELOG.md` describes notable changes between released versions.
- This document defines compatibility and the release process.
- Git tags identify immutable released states using `vMAJOR.MINOR.PATCH`.

The manifest, README, changelog, and Git tag must agree for a release.

## Semantic versioning policy

### PATCH

Use a patch release for backward-compatible corrections that do not alter the
intended workflow or document contracts, for example:

- wording and spelling corrections,
- clarified examples,
- fixed links,
- validator bug fixes that enforce an already documented rule.

### MINOR

Use a minor release for backward-compatible capabilities, for example:

- a new optional document or profile,
- additional guidance or checks with an explicit adoption path,
- a new optional automation,
- a new rule that does not invalidate previously conforming derived projects.

### MAJOR

Use a major release for incompatible changes, including:

- changed authority order or conflict semantics,
- removed or redefined identifiers,
- newly mandatory artifacts or lifecycle gates,
- incompatible status meanings or task contracts,
- renamed/moved files that break established references,
- validator changes that make previously valid projects invalid without an opt-in path.

Before `1.0.0`, incompatible changes may occur in minor versions, but they must
be explicit in the changelog. After `1.0.0`, the policy above is binding.

## Change proposal and review

Every material template change must state:

- the problem and intended outcome,
- affected files, identifiers, and workflow phases,
- whether it is normative, descriptive, or tooling-only,
- compatibility impact on derived projects,
- migration guidance when existing projects may be affected,
- verification performed.

Changes to authority, mandatory standards, lifecycle gates, manifest schema, or
validator behavior require explicit maintainer approval. Editorial corrections
may use a lighter review but still pass template validation.

## Compatibility contract

A release is backward compatible when a project valid under the previous release
can remain valid without changing accepted product behavior, architecture
decisions, public contracts, or completed task evidence.

Adding an optional artifact is compatible. Making it mandatory is potentially
incompatible. Clarifying an existing rule is compatible only when it does not
change reasonable prior interpretations.

## Deprecation and removal

Before removing a public template artifact, identifier, status, or workflow rule:

1. mark it deprecated in a minor release,
2. explain the replacement and migration path,
3. retain it for at least one minor release unless security or correctness requires faster removal,
4. remove it only in a major release after `1.0.0`.

Emergency removal must be called out prominently in the changelog with impact
and remediation.

## Release process

1. Ensure the working tree contains only intended release changes.
2. Review unresolved `[Unreleased]` changelog entries and classify compatibility.
3. Choose the next semantic version.
4. Update `template.version` and `template.status` in `template-manifest.yml`.
5. Update matching version and status in `README.md`.
6. Confirm that `LICENSE`, manifest metadata, and the README agree.
7. Move released changelog entries under `## [VERSION] - YYYY-MM-DD`.
8. Update changelog comparison links.
9. Run `python tools/validate_template.py --mode template`.
10. Review all normative changes and migration notes.
11. Commit the release with a clear message.
12. Create an annotated Git tag `vVERSION` from that commit.
13. Publish release notes derived from the changelog.

Do not tag a release from an uncommitted or failing state. A release tag is
immutable; correct mistakes with a new version rather than moving a published tag.

## Release readiness for 1.0.0

Version `1.0.0` requires:

- completed template identity, workflow, governance, and validation,
- a documented license decision,
- no unresolved release-blocking template placeholders,
- a successful end-to-end pilot project,
- all template-mode validation checks passing,
- an initial committed baseline and annotated `v1.0.0` tag.

## Upgrading a derived project

Template upgrades are deliberate migrations, not automatic merges. In a derived
project:

1. record the current template version from `template-manifest.yml`,
2. read every intervening changelog entry and migration note,
3. compare template files without overwriting project-specific decisions,
4. classify changes as adopted, adapted, or not applicable,
5. review effects on requirements, UX, architecture, ADRs, tasks, tests, and tooling,
6. run project and template-derived validation,
7. update `template.version` only after the upgrade is accepted,
8. record the upgrade date, decision, and local deviations.

Never replace a derived project's accepted normative documents wholesale with
new blank templates.

## Local deviations

A derived project may intentionally diverge from the template. Record material
deviations in its architecture/engineering documentation or an ADR, including:

- originating template rule or artifact,
- local replacement,
- rationale and scope,
- effect on future template upgrades.

Local divergence does not change the upstream template version.

## Support window

Until `1.0.0`, only the latest release candidate is maintained. Starting with
`1.0.0`, document any broader support promise explicitly; without one, only the
latest minor release of the current major version receives routine fixes.
