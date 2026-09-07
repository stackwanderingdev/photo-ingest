# Software Project Template

This repository template provides a controlled, traceable engineering process
for software developed by people and AI agents. It is technology-independent:
language, framework, build system, and quality tools are selected when a new
project is initialized.

## Template identity

- Name: `software-project-template`
- Version: `1.0.0`
- Status: `stable`
- Language: English
- License: [MIT](LICENSE)
- Source: [github.com/stackwanderingdev/software-development-template](https://github.com/stackwanderingdev/software-development-template)
- Machine-readable metadata: [`template-manifest.yml`](template-manifest.yml)
- Release history: [`CHANGELOG.md`](CHANGELOG.md)
- Governance and upgrades: [`docs/template-governance.md`](docs/template-governance.md)

The template follows Semantic Versioning:

- `PATCH` clarifies guidance without changing its intended workflow or contracts.
- `MINOR` adds backward-compatible documents, rules, or optional capabilities.
- `MAJOR` changes authority, identifiers, required artifacts, or workflow contracts incompatibly.

The detailed compatibility, deprecation, release, and derived-project upgrade
policy is defined in `docs/template-governance.md`.

A derived project keeps `template-manifest.yml` as provenance. While
`derived_project.name` still equals `<PROJECT_NAME>`, the repository is in its
uninitialized template state. Follow [`docs/project-bootstrap/bootstrap.md`](docs/project-bootstrap/bootstrap.md)
to personalize the repository, replace the template README, changelog, and CI
workflow, and complete the required project artifacts before implementation.
Do not update `template.version` merely because the derived project itself
changes; it records the template version originally used or deliberately adopted
through a documented template upgrade.

## Start a new project

1. Create a repository from this template or copy it.
2. Read `AGENTS.md` and `template-manifest.yml`.
3. If `derived_project.name` is still `<PROJECT_NAME>`, follow the complete [project bootstrap](docs/project-bootstrap/bootstrap.md).
4. Follow the [development workflow](docs/development-workflow.md), beginning with the product idea.
5. Complete the [product overview](docs/requirements/product-requirements.md), then create separate product goal, functional requirement, and quality requirement files through their linked indexes and templates.
6. Define target users, usage context, and the UX profile in [`docs/ux/`](docs/ux/README.md).
7. Complete the [stack profile](docs/engineering/stack-profile.md).
8. Define the architecture, system invariants, and dependency rules.
9. Select applicable standards in the [architecture standards](docs/architecture/architecture-standards.md).
10. Record significant technical decisions as ADRs.
11. Derive the first small work item from `docs/tasks/TASK-template.md`.
12. Only then add production code under `src/`.

Mark sections that do not apply explicitly as `Not applicable` with a reason;
do not leave them silently blank.

## Information model

| Area | Primary question | Normative? |
|---|---|---|
| `docs/requirements/` | What must the product achieve? | Yes |
| `docs/ux/` | For whom, in what context, and how will it be usable? | Partly; see document status |
| `docs/architecture/` | Which boundaries and invariants apply? | Yes |
| `docs/decisions/` | Why was a technical option selected? | Yes, when accepted |
| `docs/engineering/` | How is quality produced and verified? | Yes |
| `docs/tasks/` | What may change in this increment? | Within higher-authority rules |
| `tests/` | Which rules are technically verified? | Evidence, not a requirement source |
| `src/` | How is behavior implemented? | Descriptive |

When sources conflict, do not guess, silently change a source, or begin a
semantic redesign. Report the conflict with exact references.

## Identifiers and traceability

- Product goals: `PRD-<AREA>-NNN`
- Functional requirements: `REQ-<AREA>-NNN`
- Quality requirements: `NFR-<AREA>-NNN`
- UX rules: `UX-<AREA>-NNN`
- System invariants: `INV-<AREA>-NNN`
- Architecture decisions: `ADR-NNN`
- Work items: `TASK-NNN`

```text
Requirement -> Task -> Test -> Implementation -> Verification
```

## Directory structure

```text
.
├── AGENTS.md
├── README.md
├── docs/
│   ├── project-bootstrap/
│   ├── requirements/
│   │   ├── goals/
│   │   ├── functional/
│   │   └── quality/
│   ├── ux/
│   │   └── journeys/
│   ├── architecture/
│   │   ├── diagrams/
│   │   └── invariants/
│   ├── decisions/
│   ├── engineering/
│   └── tasks/
├── src/
└── tests/
```

`README.md` is the human entry point. `AGENTS.md` contains binding instructions
for coding agents. Executable installation, start, and verification commands
live only in the active stack profile; the README may link there but must not
create a second command source.

Concrete `PRD-*`, `REQ-*`, `NFR-*`, `INV-*`, `UJ-*`, `ADR-*`, and `TASK-*`
artifacts each live in their own file. Their parent documents are concise
indexes, not accumulating definition files. Filenames start with the stable
identifier followed by a lowercase hyphenated title.

## Multiple technology stacks

The cross-cutting rules remain independent of language and framework. Technical
details for a concrete project are centralized in the
[stack profile](docs/engineering/stack-profile.md), so agents do not infer the
runtime, package manager, or quality tools from incidental files.

A project has exactly one active stack profile. A monorepo may define separate
component profiles, but each component must state its working directory and
commands unambiguously.

## Standards in this template

The [coding guidelines](docs/engineering/coding-guidelines.md) define mandatory,
technology-independent minimum standards. Stack-specific conventions supplement
them without silently lowering the quality baseline.

The [architecture standards](docs/architecture/architecture-standards.md) require
a traceable architecture description, measurable quality goals, explicit system
boundaries, and documented decisions. External standards are activated only
when appropriate to the project type and risk, with version and scope fixed.

The [UX standards](docs/ux/ux-guidelines.md) define the
technology-independent baseline for usable, predictable, accessible, and
trustworthy interaction. The active UX effort level scales required research
and evaluation to the project's audience, uncertainty, and risk. The accepted
accessibility profile and interaction contracts are normative; user research
and usability evaluations provide evidence rather than independent standards.

## Template maintenance

The template has a dependency-free validator requiring Python 3.11 or newer:

```text
python tools/validate_template.py --mode template
```

It checks required files and headings, local Markdown links, balanced code
fences, English-language consistency, unique base-rule definitions, manifest
identity, and rule-sequence completeness. External URLs are intentionally not
requested during validation.

After deriving and completing a project, use the stricter mode:

```text
python tools/validate_template.py --mode project
```

Project mode performs the same checks and rejects unresolved angle-bracket
placeholders in project-specific documents. Reusable ADR/task skeletons and
files that document placeholder syntax are exempt. Projects may adapt the
validator when they deliberately remove template-only documents, but such
changes must be explicit.

GitHub Actions runs template-mode validation on every push and pull request.

## License

This template is available under the [MIT License](LICENSE). Derived projects
may retain this license or deliberately choose another license appropriate to
their own code, dependencies, distribution model, and legal requirements.
