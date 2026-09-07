# Project Bootstrap

Use this procedure once when deriving a project from this template. It defines the controlled transition from the untouched template state to an initialized project repository.

The bootstrap is required while `template-manifest.yml` still contains `derived_project.name: <PROJECT_NAME>`. Replacing that sentinel with the real project name marks the project identity as initialized. It does not by itself complete the bootstrap; all other required bootstrap steps must still be completed before implementation begins.

## 1. Read before writing

1. Read root `AGENTS.md` completely.
2. Read `template-manifest.yml` completely.
3. Read this bootstrap document completely.
4. Inspect the existing repository structure and the artifact map in `template-manifest.yml` before creating or moving documentation.
5. Treat existing template-defined artifacts as the default destinations for project information.

Do not start product implementation while the project-name sentinel remains unresolved.

## 2. Personalize the template

- [ ] Replace `derived_project.name: <PROJECT_NAME>` with the project name.
- [ ] Fill `derived_project.version`, `derived_project.license`, `derived_project.initialized_at`, and `derived_project.initialized_by`.
- [ ] Preserve the originating template name, version, schema version, and source as provenance.
- [ ] Replace root `README.md` with a project README based on `docs/project-bootstrap/README-template.md`.
- [ ] Replace root `CHANGELOG.md` with a project changelog based on `docs/project-bootstrap/CHANGELOG-template.md`.
- [ ] Replace `.github/workflows/validate-template.yml` with project CI based on `docs/project-bootstrap/project-ci.yml` and the accepted stack profile.
- [ ] Verify repository metadata and default branch configuration.
- [ ] Set repository description, product ownership, license, contribution rules, and security contact where required.
- [ ] Remove unused examples and resolve project-specific placeholders.
- [ ] Remove `docs/project-bootstrap/` and template-only governance documents after their project replacements are complete.
- [ ] Review `CHANGELOG.md` and `docs/template-governance.md` when deliberately upgrading an existing project.

## 3. Product and requirements

- [ ] Read `docs/development-workflow.md` and assign decision ownership.
- [ ] Document the problem, target users, measurable goals, and non-goals in the existing requirement artifacts.
- [ ] Assign stable `REQ-*` identifiers to initial functional requirements.
- [ ] Assign measurable `NFR-*` identifiers to relevant quality goals.
- [ ] Store each `PRD-*`, `REQ-*`, and `NFR-*` entity in its own file and update its index.
- [ ] Give open questions owners and ensure they do not block the first increment.

## 4. Architecture and decisions

- [ ] Describe the system boundary, building blocks, and responsibilities.
- [ ] Document critical invariants as `INV-*`.
- [ ] Store each invariant and user journey in its own indexed file.
- [ ] Make dependency rules concrete and preferably automated.
- [ ] Clarify data, security, and operational boundaries.
- [ ] Record significant stack and persistence decisions as accepted ADRs.
- [ ] Select the active architecture profile and applicable external standards.
- [ ] Document stakeholder concerns and measurable quality scenarios.

## 5. UX and accessibility

- [ ] Document target users, usage context, user goals, and critical journeys.
- [ ] State applicable interface profiles and `UX-*` rules.
- [ ] Define accessibility target, standard, version, and scope.
- [ ] Describe critical interactions including loading, empty, error, and permission states.
- [ ] Define appropriate formative and final usability evaluation.

## 6. Stack profile

- [ ] Set `docs/engineering/stack-profile.md` to `Accepted`.
- [ ] Pin reproducible runtime and tool versions.
- [ ] Document manifests and lock-file strategy.
- [ ] Make every binding command executable from its stated directory.
- [ ] Explain non-applicable checks rather than leaving them blank.

## 7. Quality and automation

- [ ] Run `python tools/validate_template.py --mode project` after resolving project placeholders and removing template-only files.
- [ ] Configure formatting, linting, type checking, tests, and build.
- [ ] Cover coding standards with tools or explicit review rules.
- [ ] Add at least one smoke test proving that test execution works.
- [ ] Run required checks in CI.
- [ ] Confirm that CI uses project mode, the supported runner/runtime, and every binding verification category.
- [ ] Prevent secrets and local configuration from being committed.
- [ ] Define security profile, dependency checks, and threat model when applicable.
- [ ] Review the project-specific Definition of Done.

## 8. First task

- [ ] Reference requirements, invariants, UX rules, and relevant ADRs.
- [ ] State allowed scope and prohibited changes.
- [ ] Define acceptance criteria and verification commands before implementation.
- [ ] Keep the task small enough for one coherent, verifiable change.

## Completion criteria

Bootstrap is complete only when all required checklist items are complete or explicitly marked `Not applicable` with a reason, project-mode validation passes, and the first implementation task is ready.

- Initialized by: `<NAME>`
- Date: `<YYYY-MM-DD>`
- Remaining constraints: `<NONE OR LIST>`
- First task: `<TASK-NNN>`
