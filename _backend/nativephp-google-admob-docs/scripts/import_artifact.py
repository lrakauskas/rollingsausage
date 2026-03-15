from __future__ import annotations

import argparse
import json
import re
import shutil
import subprocess
import sys
import tempfile
import zipfile
from dataclasses import dataclass
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS_DIR = ROOT / "docs"
DATA_DIR = ROOT / "data" / "current"
EXPECTED_PACKAGE = "lrakauskas/nativephp-google-admob"
EXPECTED_POLICY = "public-facades-events-config-only"
SUPPORTED_SCHEMA = 1


class ImportErrorWithContext(RuntimeError):
    pass


@dataclass
class Artifact:
    manifest: dict[str, Any]
    api: dict[str, Any]


def main() -> int:
    parser = argparse.ArgumentParser(description="Import NativePHP Google AdMob docs artifact")
    parser.add_argument("artifact", type=Path, help="Path to docs artifact zip/json")
    parser.add_argument("--source-repo", type=str, default="", help="Private repo slug for download metadata")
    parser.add_argument("--tag", type=str, default="", help="Plugin tag used for this artifact")
    parser.add_argument("--asset-name", type=str, default="", help="Artifact asset name")
    args = parser.parse_args()

    artifact = load_artifact(args.artifact)
    validate_artifact(artifact)

    DATA_DIR.mkdir(parents=True, exist_ok=True)
    write_json(DATA_DIR / "manifest.json", artifact.manifest)
    write_json(DATA_DIR / "api.json", artifact.api)

    generated_targets = {
        DOCS_DIR / "events.md": {
            "events_table": render_events_table(artifact.api["events"]),
            "events_payloads": render_events_payloads(artifact.api["events"]),
        },
        DOCS_DIR / "configuration.md": {
            "config_table": render_config_table(artifact.api["config"]),
        },
        DOCS_DIR / "api-reference" / "config.md": {
            "config_table": render_config_table(artifact.api["config"]),
        },
        DOCS_DIR / "api-reference" / "facades.md": {
            "facades_methods": render_facades(artifact.api["facades"]),
        },
        DOCS_DIR / "api-reference" / "enums.md": {
            "enums_table": render_enums(artifact.api["enums"]),
        },
        DOCS_DIR / "index.md": {
            "release_meta": render_release_meta(artifact.manifest, args.source_repo, args.asset_name),
        },
    }

    for file_path, replacements in generated_targets.items():
        update_markers(file_path, replacements)

    return 0


def load_artifact(path: Path) -> Artifact:
    if not path.exists():
        raise ImportErrorWithContext(f"Artifact not found: {path}")

    if path.suffix.lower() == ".zip":
        with tempfile.TemporaryDirectory(prefix="admob-docs-") as temp_dir:
            temp_path = Path(temp_dir)
            with zipfile.ZipFile(path) as archive:
                archive.extractall(temp_path)

            manifest = json.loads((temp_path / "manifest.json").read_text(encoding="utf-8"))
            api = json.loads((temp_path / "api.json").read_text(encoding="utf-8"))

            return Artifact(manifest=manifest, api=api)

    payload = json.loads(path.read_text(encoding="utf-8"))
    if "manifest" not in payload or "api" not in payload:
        raise ImportErrorWithContext("JSON artifact must contain top-level 'manifest' and 'api' keys.")

    return Artifact(manifest=payload["manifest"], api=payload["api"])


def validate_artifact(artifact: Artifact) -> None:
    manifest = artifact.manifest
    api = artifact.api

    if manifest.get("schema_version") != SUPPORTED_SCHEMA:
        raise ImportErrorWithContext("Unsupported schema_version in artifact.")

    if manifest.get("package_name") != EXPECTED_PACKAGE:
        raise ImportErrorWithContext("Artifact package_name does not match expected package.")

    if manifest.get("visibility_policy") != EXPECTED_POLICY:
        raise ImportErrorWithContext("Artifact visibility policy is not allowed.")

    version = str(manifest.get("plugin_version", ""))
    major_line = str(manifest.get("major_line", ""))
    match = re.match(r"^(\d+)\.", version)
    if match is None:
        raise ImportErrorWithContext("plugin_version must be semver-like.")

    if major_line != f"v{match.group(1)}":
        raise ImportErrorWithContext("major_line does not match plugin_version major.")

    required_sections = {"facades", "events", "enums", "config"}
    if set(api.keys()) != required_sections:
        raise ImportErrorWithContext("Artifact api sections do not match expected public sections exactly.")

    forbidden_fragments = ["resources/android", "src/Commands", "Services\\", "Services/"]
    payload = json.dumps(artifact.api)
    for fragment in forbidden_fragments:
        if fragment in payload:
            raise ImportErrorWithContext(f"Forbidden fragment detected in artifact payload: {fragment}")


def update_markers(file_path: Path, replacements: dict[str, str]) -> None:
    content = file_path.read_text(encoding="utf-8")

    for block_id, replacement in replacements.items():
        start = f"<!-- GENERATED:{block_id}:start -->"
        end = f"<!-- GENERATED:{block_id}:end -->"

        if start not in content or end not in content:
            raise ImportErrorWithContext(f"Missing required marker {block_id} in {file_path}")

        pattern = re.compile(re.escape(start) + r".*?" + re.escape(end), re.DOTALL)
        replacement_block = f"{start}\n{replacement.rstrip()}\n{end}"
        content, count = pattern.subn(replacement_block, content, count=1)

        if count != 1:
            raise ImportErrorWithContext(f"Expected exactly one replacement for {block_id} in {file_path}")

    file_path.write_text(content + ("" if content.endswith("\n") else "\n"), encoding="utf-8")


def render_release_meta(manifest: dict[str, Any], source_repo: str, asset_name: str) -> str:
    parts = [
        f"- Current imported release: `{manifest['plugin_tag']}`",
        f"- Major docs line: `{manifest['major_line']}`",
        f"- Source commit: `{manifest['source_commit']}`",
        f"- Generated at: `{manifest['generated_at']}`",
    ]

    if source_repo and asset_name:
        parts.append(f"- Artifact source: `{source_repo}` release asset `{asset_name}`")

    return "\n".join(parts)


def render_events_table(events: list[dict[str, Any]]) -> str:
    lines = [
        "| Event | Description | Trigger |",
        "| --- | --- | --- |",
    ]

    for event in events:
        lines.append(
            f"| `{event['name']}` | {escape_pipes(event['description'])} | {escape_pipes(event['trigger'])} |"
        )

    return "\n".join(lines)


def render_events_payloads(events: list[dict[str, Any]]) -> str:
    blocks: list[str] = []

    for event in events:
        blocks.append(f"### `{event['name']}`")
        blocks.append("")
        blocks.append(event["description"])
        blocks.append("")

        payload = event.get("payload", [])
        if not payload:
            blocks.append("This event does not expose a public payload.")
            blocks.append("")
            continue

        blocks.extend([
            "| Field | Type | Required | Default | Notes |",
            "| --- | --- | --- | --- | --- |",
        ])

        for field in payload:
            default = field.get("default") or "-"
            required = "yes" if field.get("required") else "no"
            blocks.append(
                f"| `{field['name']}` | `{field['type']}` | {required} | {escape_pipes(default)} | {escape_pipes(field.get('notes', ''))} |"
            )

        blocks.append("")

    return "\n".join(blocks).rstrip()


def render_facades(facades: list[dict[str, Any]]) -> str:
    blocks: list[str] = []

    for facade in facades:
        blocks.append(f"## `{facade['name']}`")
        blocks.append("")
        summary = facade.get("summary") or "Public facade for plugin consumers."
        blocks.append(summary)
        blocks.append("")
        blocks.append("| Method | Parameters | Returns | Description |")
        blocks.append("| --- | --- | --- | --- |")

        for method in facade.get("methods", []):
            blocks.append(
                f"| `{method['name']}` | `{method['parameters']}` | `{method['returns']}` | {escape_pipes(method.get('description', ''))} |"
            )

        blocks.append("")

    return "\n".join(blocks).rstrip()


def render_config_table(config_rows: list[dict[str, Any]]) -> str:
    lines = [
        "| Key | Type | Default | Required | Description |",
        "| --- | --- | --- | --- | --- |",
    ]

    for row in config_rows:
        lines.append(
            f"| `{row['key']}` | `{row['type']}` | {escape_pipes(row['default'])} | {escape_pipes(row['required'])} | {escape_pipes(row['description'])} |"
        )

    return "\n".join(lines)


def render_enums(enums: list[dict[str, Any]]) -> str:
    blocks: list[str] = []

    for enum in enums:
        blocks.append(f"## `{enum['name']}`")
        blocks.append("")
        blocks.append(enum.get("description", ""))
        blocks.append("")
        blocks.append("| Case | Value | Description |")
        blocks.append("| --- | --- | --- |")

        for case in enum.get("cases", []):
            blocks.append(
                f"| `{case['name']}` | `{case['value']}` | {escape_pipes(case.get('description', ''))} |"
            )

        blocks.append("")

    return "\n".join(blocks).rstrip()


def escape_pipes(value: Any) -> str:
    text = str(value)
    return text.replace("|", "\\|").replace("\n", "<br>")


def write_json(path: Path, payload: dict[str, Any]) -> None:
    path.write_text(json.dumps(payload, indent=2, ensure_ascii=True) + "\n", encoding="utf-8")


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except ImportErrorWithContext as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        raise SystemExit(1)
