# INV-DATA-001 — Never overwrite a destination object

- Status: `Accepted`
- Rationale: Existing library content and non-regular filesystem objects must not
  be destroyed or traversed as an incidental result of importing a photo.
- Scope: Destination inspection, path reservation, import planning, and mutation.

## Rule

PhotoIngest never overwrites, replaces, or removes an existing destination
object. A different regular file requires a unique path under
`REQ-ORGANIZE-003`. A directory, symbolic link, broken symbolic link, or other
non-regular object at a proposed path blocks that plan item and is neither
followed nor treated as regular file content.

## Allowed transitions

- `Base path occupied by different regular file` -> reserve first available
  deterministic suffix -> `Unique path reserved`
- `Calculated path contains byte-identical regular file` -> classify under
  `REQ-DUPLICATE-001` -> `Already imported candidate`

## Prohibited states or actions

- Copying to an occupied destination path with overwrite or replacement
  semantics.
- Following a symbolic link to inspect or mutate its referent as the planned
  destination.
- Treating a non-regular object as an eligible destination file.

## Enforcement and evidence

- Implementation boundary: Destination-access adapter, plan construction, and
  import coordination.
- Evidence: Filesystem integration tests for different and identical regular
  files, directories, symbolic links, broken links, and other representable
  non-regular objects.
- Requirements covered: `REQ-DUPLICATE-001`, `REQ-ORGANIZE-003`,
  `REQ-PREVIEW-001`, `REQ-IMPORT-001`

## Change history

- `2026-09-08`: Accepted by Daniel to protect all existing destination objects.
