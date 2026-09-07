#!/usr/bin/env python3
"""Validate the repository template using only the Python standard library."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

REQUIRED_FILES = (
    "README.md",
    "AGENTS.md",
    "CHANGELOG.md",
    "LICENSE",
    "template-manifest.yml",
    "docs/development-workflow.md",
    "docs/requirements/product-requirements.md",
    "docs/requirements/goals/README.md",
    "docs/requirements/goals/PRD-template.md",
    "docs/requirements/functional-requirements.md",
    "docs/requirements/functional/README.md",
    "docs/requirements/functional/REQ-template.md",
    "docs/requirements/non-functional-requirements.md",
    "docs/requirements/quality/README.md",
    "docs/requirements/quality/NFR-template.md",
    "docs/ux/ux-guidelines.md",
    "docs/ux/journeys/README.md",
    "docs/ux/journeys/UJ-template.md",
    "docs/architecture/architecture.md",
    "docs/architecture/architecture-standards.md",
    "docs/architecture/system-contracts.md",
    "docs/architecture/invariants/README.md",
    "docs/architecture/invariants/INV-template.md",
    "docs/architecture/dependency-rules.md",
    "docs/decisions/ADR-template.md",
    "docs/engineering/coding-guidelines.md",
    "docs/engineering/definition-of-done.md",
    "docs/engineering/stack-profile.md",
    "docs/tasks/TASK-template.md",
)

TEMPLATE_ONLY_FILES = (
    "docs/template-governance.md",
    "docs/project-bootstrap/bootstrap.md",
    "docs/project-bootstrap/README-template.md",
    "docs/project-bootstrap/CHANGELOG-template.md",
    "docs/project-bootstrap/project-ci.yml",
)

REQUIRED_HEADINGS = {
    "CHANGELOG.md": (
        "# Changelog",
        "## [Unreleased]",
    ),
    "docs/template-governance.md": (
        "# Template Governance and Release Policy",
        "## Semantic versioning policy",
        "## Release process",
        "## Upgrading a derived project",
    ),
    "docs/development-workflow.md": (
        "# Development Workflow",
        "## Core model",
        "## Artifact states",
        "## Phase 5 — Cut a ready task",
        "## Phase 7 — Feed evidence back",
    ),
    "docs/tasks/TASK-template.md": (
        "## Goal",
        "## Allowed change scope",
        "## Acceptance criteria",
        "## Verification",
    ),
    "docs/engineering/stack-profile.md": (
        "## Status",
        "## Binding commands",
        "## CI mapping",
    ),
}

EXPECTED_RULES = {
    "docs/engineering/coding-guidelines.md": ("CODE", 14),
    "docs/architecture/architecture-standards.md": ("ARCH", 12),
    "docs/ux/ux-guidelines.md": ("UX", 14),
}

EXPECTED_ARTIFACT_PATHS = {
    "product_requirements": "docs/requirements/product-requirements.md",
    "functional_requirements": "docs/requirements/functional-requirements.md",
    "non_functional_requirements": "docs/requirements/non-functional-requirements.md",
    "ux": "docs/ux/ux-guidelines.md",
    "architecture": "docs/architecture/architecture.md",
    "system_contracts": "docs/architecture/system-contracts.md",
    "dependency_rules": "docs/architecture/dependency-rules.md",
    "decisions": "docs/decisions",
    "engineering": "docs/engineering",
    "tasks": "docs/tasks",
    "development_workflow": "docs/development-workflow.md",
}

PROJECT_PLACEHOLDER_EXEMPT = {
    "README.md",  # documents placeholder syntax and identifier patterns
    "AGENTS.md",  # documents the command-placeholder contract
    "docs/decisions/ADR-template.md",
    "docs/tasks/TASK-template.md",
    "docs/requirements/goals/PRD-template.md",
    "docs/requirements/functional/REQ-template.md",
    "docs/requirements/quality/NFR-template.md",
    "docs/architecture/invariants/INV-template.md",
    "docs/ux/journeys/UJ-template.md",
}

GERMAN_MARKERS = re.compile(
    r"[äöüÄÖÜß]|\b(?:und|oder|für|nicht|wird|werden|muss|soll|eine|einer|"
    r"diese|beschreibung|prüfung|fehler|änderung|begründung|benutzer)\b",
    re.IGNORECASE,
)
PLACEHOLDER = re.compile(r"<[^<>\n]+>")
MARKDOWN_LINK = re.compile(r"\[[^\]]+\]\(([^)]+)\)")
RULE_DEFINITION = re.compile(r"^#{2,6}\s+((?:CODE|ARCH|UX)-\d{3})\b", re.MULTILINE)
ARTIFACT_DEFINITION = re.compile(
    r"^#\s+((?:PRD|REQ|NFR|INV)-[A-Z0-9]+-\d{3}|(?:UJ|ADR|TASK)-\d{3})\b",
    re.MULTILINE,
)
ARTIFACT_DIRECTORIES = {
    "PRD": "docs/requirements/goals",
    "REQ": "docs/requirements/functional",
    "NFR": "docs/requirements/quality",
    "INV": "docs/architecture/invariants",
    "UJ": "docs/ux/journeys",
    "ADR": "docs/decisions",
    "TASK": "docs/tasks",
}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--mode",
        choices=("template", "project"),
        default="template",
        help="Template mode permits placeholders; project mode rejects them.",
    )
    parser.add_argument(
        "--root",
        type=Path,
        default=Path(__file__).resolve().parents[1],
        help="Repository root; defaults to the parent of tools/.",
    )
    return parser.parse_args()


def relative(path: Path, root: Path) -> str:
    return path.relative_to(root).as_posix()


def markdown_files(root: Path) -> list[Path]:
    return sorted(path for path in root.rglob("*.md") if ".git" not in path.parts)


def validate_required_files(root: Path, mode: str, errors: list[str]) -> None:
    required = REQUIRED_FILES + (TEMPLATE_ONLY_FILES if mode == "template" else ())
    for name in required:
        path = root / name
        if not path.is_file():
            errors.append(f"missing required file: {name}")
        elif not path.read_text(encoding="utf-8").strip():
            errors.append(f"required file is empty: {name}")
    if mode == "project":
        for name in TEMPLATE_ONLY_FILES:
            if (root / name).exists():
                errors.append(f"template-only bootstrap/governance file remains in project: {name}")


def validate_markdown(root: Path, files: list[Path], errors: list[str]) -> None:
    for path in files:
        name = relative(path, root)
        text = path.read_text(encoding="utf-8")
        lines = text.splitlines()

        if not text.strip():
            errors.append(f"empty Markdown file: {name}")
            continue
        if not next((line for line in lines if line.strip()), "").startswith("# "):
            errors.append(f"first content line is not an H1 heading: {name}")
        if sum(1 for line in lines if line.strip().startswith("```")) % 2:
            errors.append(f"unbalanced fenced code block: {name}")
        if GERMAN_MARKERS.search(text):
            errors.append(f"possible German-language content: {name}")

        for target in MARKDOWN_LINK.findall(text):
            clean_target = target.split("#", 1)[0].strip()
            if not clean_target or re.match(r"^[a-z][a-z0-9+.-]*:", clean_target, re.I):
                continue
            decoded = clean_target.replace("%20", " ")
            resolved = (path.parent / decoded).resolve()
            try:
                resolved.relative_to(root)
            except ValueError:
                errors.append(f"local link escapes repository: {name} -> {target}")
                continue
            if not resolved.exists():
                errors.append(f"broken local link: {name} -> {target}")


def validate_headings(root: Path, errors: list[str]) -> None:
    for name, headings in REQUIRED_HEADINGS.items():
        path = root / name
        if not path.is_file():
            continue
        existing = set(path.read_text(encoding="utf-8").splitlines())
        for heading in headings:
            if heading not in existing:
                errors.append(f"missing heading in {name}: {heading}")


def validate_rule_definitions(root: Path, files: list[Path], errors: list[str]) -> None:
    definitions: dict[str, str] = {}
    for path in files:
        name = relative(path, root)
        for identifier in RULE_DEFINITION.findall(path.read_text(encoding="utf-8")):
            previous = definitions.get(identifier)
            if previous:
                errors.append(f"duplicate rule definition {identifier}: {previous}, {name}")
            else:
                definitions[identifier] = name

    for name, (prefix, count) in EXPECTED_RULES.items():
        path = root / name
        if not path.is_file():
            continue
        text = path.read_text(encoding="utf-8")
        expected = {f"{prefix}-{number:03d}" for number in range(1, count + 1)}
        actual = set(RULE_DEFINITION.findall(text))
        missing = sorted(expected - actual)
        if missing:
            errors.append(f"missing base rules in {name}: {', '.join(missing)}")


def validate_artifact_files(root: Path, files: list[Path], errors: list[str]) -> None:
    for path in files:
        name = relative(path, root)
        identifiers = ARTIFACT_DEFINITION.findall(path.read_text(encoding="utf-8"))
        if len(identifiers) > 1:
            errors.append(f"multiple concrete artifacts in one file: {name}")
        for identifier in identifiers:
            prefix = identifier.split("-", 1)[0]
            expected_directory = ARTIFACT_DIRECTORIES[prefix]
            if path.parent != root / expected_directory:
                errors.append(
                    f"artifact {identifier} must be stored in {expected_directory}: {name}"
                )
            if not path.name.startswith(f"{identifier}-"):
                errors.append(f"artifact filename must start with {identifier}-: {name}")


def validate_artifact_map(root: Path, text: str, errors: list[str]) -> None:
    match = re.search(r"^artifacts:\s*$([\s\S]*)", text, re.MULTILINE)
    if not match:
        errors.append("manifest missing artifacts map")
        return

    entries: dict[str, dict[str, str]] = {}
    current: str | None = None
    for line in match.group(1).splitlines():
        entry_match = re.match(r"^  ([a-z0-9_]+):\s*$", line)
        if entry_match:
            current = entry_match.group(1)
            entries[current] = {}
            continue
        field_match = re.match(r"^    (path|entity_directory|template):\s*(\S+)\s*$", line)
        if current and field_match:
            entries[current][field_match.group(1)] = field_match.group(2)

    for name, expected_path in EXPECTED_ARTIFACT_PATHS.items():
        fields = entries.get(name)
        if fields is None:
            errors.append(f"manifest artifacts map missing entry: {name}")
            continue
        if fields.get("path") != expected_path:
            errors.append(
                f"manifest artifact {name}.path must be {expected_path}"
            )

    for name, fields in entries.items():
        if "path" not in fields:
            errors.append(f"manifest artifact {name} missing path")
        for field in ("path", "entity_directory", "template"):
            target = fields.get(field)
            if target and not (root / target).exists():
                errors.append(
                    f"manifest artifact {name}.{field} references missing path: {target}"
                )


def validate_manifest(root: Path, mode: str, errors: list[str]) -> None:
    path = root / "template-manifest.yml"
    if not path.is_file():
        return
    text = path.read_text(encoding="utf-8")
    expected = (
        "schema_version: 1",
        "name: software-project-template",
        "language: en",
        "license: MIT",
        "source: https://github.com/stackwanderingdev/software-development-template.git",
    )
    normalized = "\n".join(line.strip() for line in text.splitlines())
    for entry in expected:
        if entry not in normalized:
            errors.append(f"manifest missing or changed entry: {entry}")

    validate_artifact_map(root, text, errors)

    if mode == "template":
        license_text = (
            (root / "LICENSE").read_text(encoding="utf-8") if (root / "LICENSE").is_file() else ""
        )
        if not license_text.startswith("MIT License\n"):
            errors.append("LICENSE does not contain the MIT License heading")
        if "Copyright (c) 2026 stackwanderingdev" not in license_text:
            errors.append("LICENSE does not contain the expected copyright notice")
        if "- License: [MIT](LICENSE)" not in (root / "README.md").read_text(encoding="utf-8"):
            errors.append("README does not identify the MIT license")

    version_match = re.search(r"^\s*version:\s*([^\s#]+)", text, re.MULTILINE)
    semver = r"(?:0|[1-9]\d*)\.(?:0|[1-9]\d*)\.(?:0|[1-9]\d*)(?:-[0-9A-Za-z.-]+)?"
    if not version_match or not re.fullmatch(semver, version_match.group(1)):
        errors.append("manifest template.version must be a valid semantic version")
    elif mode == "template":
        readme = (root / "README.md").read_text(encoding="utf-8")
        if f"- Version: `{version_match.group(1)}`" not in readme:
            errors.append("README template version does not match the manifest")
        changelog = (root / "CHANGELOG.md").read_text(encoding="utf-8")
        if f"## [{version_match.group(1)}]" not in changelog:
            errors.append("CHANGELOG has no entry for the manifest version")

    status_match = re.search(r"^\s*status:\s*([^\s#]+)", text, re.MULTILINE)
    allowed_statuses = {"development", "release-candidate", "stable", "deprecated"}
    if not status_match or status_match.group(1) not in allowed_statuses:
        errors.append(
            f"manifest template.status must be one of: {', '.join(sorted(allowed_statuses))}"
        )
    elif mode == "template" and f"- Status: `{status_match.group(1)}`" not in (
        root / "README.md"
    ).read_text(encoding="utf-8"):
        errors.append("README template status does not match the manifest")

    if mode == "template":
        for marker in (
            "name: <PROJECT_NAME>",
            "version: <PROJECT_VERSION>",
            "license: <SPDX_IDENTIFIER>",
            "initialized_at: <YYYY-MM-DD>",
            "initialized_by: <NAME_OR_AUTOMATION>",
        ):
            if marker not in normalized:
                errors.append(f"template manifest must retain placeholder: {marker}")
    else:
        derived_match = re.search(r"^derived_project:\s*$([\s\S]+)", text, re.MULTILINE)
        derived = derived_match.group(1) if derived_match else ""
        for field in ("name", "version", "license", "initialized_at", "initialized_by"):
            if not re.search(rf"^\s{{2}}{field}:\s*\S+", derived, re.MULTILINE):
                errors.append(f"derived_project.{field} must be populated")
        derived_version = re.search(r"^\s{2}version:\s*([^\s#]+)", derived, re.MULTILINE)
        if derived_version and not re.fullmatch(semver, derived_version.group(1)):
            errors.append("derived_project.version must be a valid semantic version")


def validate_project_placeholders(root: Path, mode: str, errors: list[str]) -> None:
    if mode != "project":
        return
    for path in sorted(root.rglob("*")):
        if (
            not path.is_file()
            or ".git" in path.parts
            or path.suffix not in {".md", ".yml", ".yaml"}
        ):
            continue
        if relative(path, root) in PROJECT_PLACEHOLDER_EXEMPT:
            continue
        text = path.read_text(encoding="utf-8")
        matches = PLACEHOLDER.findall(text)
        if matches:
            preview = ", ".join(sorted(set(matches))[:3])
            errors.append(f"unresolved placeholders in {relative(path, root)}: {preview}")


def main() -> int:
    args = parse_args()
    root = args.root.resolve()
    errors: list[str] = []

    if not root.is_dir():
        print(f"ERROR: repository root does not exist: {root}", file=sys.stderr)
        return 2

    files = markdown_files(root)
    validate_required_files(root, args.mode, errors)
    validate_markdown(root, files, errors)
    validate_headings(root, errors)
    validate_rule_definitions(root, files, errors)
    validate_artifact_files(root, files, errors)
    validate_manifest(root, args.mode, errors)
    validate_project_placeholders(root, args.mode, errors)

    if errors:
        print(f"Validation failed with {len(errors)} error(s):", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1

    print(f"Validation passed ({args.mode} mode, {len(files)} Markdown files).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
