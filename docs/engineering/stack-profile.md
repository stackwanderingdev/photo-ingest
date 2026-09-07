# Active Technology Stack Profile

This is the single source for runtimes, tools, working directories, and commands.
Complete it when initializing a project. Product and architecture decisions still
belong in requirements and ADRs.

## Status

- Profile status: `Unconfigured | Draft | Accepted`
- Profile name: `<SHORT NAME, E.G. python-desktop>`
- Owner: `<NAME/ROLE>`
- Last reviewed: `<YYYY-MM-DD>`
- Supported platforms: `<WINDOWS | LINUX | MACOS | CONTAINER | ...>`

While status is `Unconfigured`, or a required placeholder remains, no
implementation task may be considered fully verified.

## Components

Use one row for a single application. In a monorepo, add one row per independently
buildable or deployable component.

| Component | Type | Source path | Test path | Working directory |
|---|---|---|---|---|
| `<NAME>` | `<APP | LIBRARY | SERVICE | UI | ...>` | `<PATH>` | `<PATH>` | `<PATH>` |

## Runtimes and SDKs

| Purpose | Technology | Supported version | Version file | Verification |
|---|---|---|---|---|
| Language/runtime | `<NAME>` | `<EXACT OR RANGE>` | `<PATH>` | `<VERSION COMMAND>` |

Versions should be reproducible through a committed file or build configuration.
`Latest` is not an adequate version constraint.

## Dependencies and reproducibility

- Package manager: `<NAME AND VERSION>`
- Manifest(s): `<PATH>`
- Lock file(s): `<PATH>`
- Lock file committed: `Yes | No, because <REASON>`
- CI installation mode: `<FROZEN/LOCKED COMMAND>`
- Sources/registries: `<SOURCES; NO SECRETS>`

New runtime dependencies require explicit task authorization. Changing runtime,
package manager, framework, or lock strategy normally requires an ADR.

## Binding commands

Commands must run non-interactively from the stated directory. State options,
environment variables, and prerequisites explicitly. Do not rely on shell aliases
or IDE-only actions.

| Operation | Working directory | Command | Expected result |
|---|---|---|---|
| Check runtime | `<PATH>` | `<COMMAND>` | `<VERSION>` |
| Install | `<PATH>` | `<COMMAND>` | Dependencies match lock file |
| Check formatting | `<PATH>` | `<COMMAND>` | No differences |
| Apply formatting | `<PATH>` | `<COMMAND>` | Formatting changes only |
| Lint | `<PATH>` | `<COMMAND>` | No errors |
| Type check | `<PATH>` | `<COMMAND OR NOT APPLICABLE + REASON>` | No errors |
| Targeted tests | `<PATH>` | `<COMMAND WITH TEST-PATH PLACEHOLDER>` | Selected tests pass |
| Unit tests | `<PATH>` | `<COMMAND>` | Suite passes |
| Integration tests | `<PATH>` | `<COMMAND>` | Suite passes |
| All tests | `<PATH>` | `<COMMAND>` | Regression passes |
| Build | `<PATH>` | `<COMMAND>` | Reproducible artifact |
| Check dependencies | `<PATH>` | `<COMMAND>` | No unaccepted risks |
| Secret scan | `<PATH>` | `<COMMAND>` | No secrets found |
| Start | `<PATH>` | `<COMMAND>` | Application is locally usable |

## Stack conventions

- Entry points: `<PATH>`
- Configuration files: `<PATHS>`
- Build output: `<PATH>`
- Generated code: `<PATH AND GENERATION COMMAND OR NOT APPLICABLE>`
- Migrations: `<PATH AND COMMAND OR NOT APPLICABLE>`
- Local environment variables: `<DOCUMENTATION/EXAMPLE FILE>`
- Secret management: `<MECHANISM; NO VALUES>`
- Security/dependency scanners: `<TOOLS AND CONFIGURATION>`

## CI mapping

| Local check | CI job | Blocks merge/release? |
|---|---|---|
| `<OPERATION>` | `<JOB NAME>` | `Yes | No, because <REASON>` |

Local and CI commands should use the same tools and configuration.

## Multiple-stack component profiles

Repeat this section for each component that uses a different stack:

### `<COMPONENT>`

- Runtime/SDK: `<NAME AND VERSION>`
- Package manager: `<NAME AND VERSION>`
- Working directory: `<PATH>`
- Manifest/lock file: `<PATHS>`
- Quality and build commands: `<TABLE REFERENCES OR COMPONENT TABLE>`
- Interfaces to other components: `<CONTRACTS/SCHEMAS>`

A cross-component task must name all affected profiles and their required checks.
