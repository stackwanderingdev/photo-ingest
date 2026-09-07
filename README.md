# PhotoIngest

PhotoIngest is a graphical desktop application for previewing and later
transferring photos from filesystem, MTP, and network sources into an organized
local photo library.

## Status

- Version: `0.1.0`
- Status: Pre-alpha; project bootstrap in progress
- License: `MIT`; see `LICENSE`
- Originating template: `software-project-template` version `1.0.0`; see `template-manifest.yml`

## Planned capabilities

- Select a source and a contained subdirectory.
- Preview photo destinations without changing source or destination files.
- Support JPEG, HEIC/HEIF, and DNG as the first required original formats.
- Preserve supported originals without automatic conversion or extraction from multi-image HEIF containers.
- Detect known associated media without silently deleting an unsupported companion.
- Derive destination paths in the form `[configured root]/YYYY/MM/YYYYMMDD_HHMMSS.ext` from photo metadata.
- Transfer and verify photos before deleting their source files.
- Support local and mounted network filesystems through filesystem access.
- Add MTP as a distinct source with technology selected after a GIO/GVfs versus libmtp feasibility comparison.
- Permit later direct network-source support only through a separate product and architecture decision.

## Requirements

- Linux is the initial supported operating system.
- Exact runtime installation and verification requirements will be binding in `docs/engineering/stack-profile.md` after bootstrap completes.

## Installation and usage

Not yet available. Production implementation has not started.

## Development

Binding quality, test, build, and start commands are defined only in
`docs/engineering/stack-profile.md` once its remaining format and dependency
decisions are resolved.

The development process and normative artifacts are described under `docs/`.

## License

PhotoIngest is licensed under the MIT License. See `LICENSE`.
