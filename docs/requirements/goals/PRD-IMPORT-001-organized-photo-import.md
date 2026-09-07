# PRD-IMPORT-001 — Organized photo import

- Status: `Draft`
- Owner: `Daniel`
- Priority: `Must`
- Last updated: `2026-09-07`

## Goal

Enable a personal Linux user to transfer photos from an attached device into a
local photo library with consistent EXIF-derived filenames and directory paths.

## Success criterion

For an agreed representative import set, every successfully imported photo is
present in the expected destination path with the expected filename, and every
file that cannot be imported is reported without an unreported partial outcome.
The representative set and exact naming, filing, and failure rules remain to be
approved through the linked requirements.

## Rationale and scope

- Problem addressed: Manual transfer and organization are repetitive and can produce inconsistent library structure.
- Included users/context: A personal user importing photos from a filesystem, MTP, or network source on a local Linux system.
- Exclusions: Photo editing, cloud synchronization, and support for non-Linux platforms in the initial product.

## Change history

- `2026-09-07`: Initial Draft created from the stated project goal; detailed import policy remains open.
