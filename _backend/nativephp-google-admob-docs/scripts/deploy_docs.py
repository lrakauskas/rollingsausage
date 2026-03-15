from __future__ import annotations

import argparse
import json
import shutil
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MKDOCS_FILE = ROOT / "mkdocs.yml"
DATA_MANIFEST = ROOT / "data" / "current" / "manifest.json"


def main() -> int:
    parser = argparse.ArgumentParser(description="Deploy versioned NativePHP Google AdMob docs")
    parser.add_argument("--push", action="store_true", help="Push main-branch docs updates to origin")
    args = parser.parse_args()

    manifest = json.loads(DATA_MANIFEST.read_text(encoding="utf-8"))
    major_line = manifest["major_line"]
    plugin_version = manifest["plugin_version"]
    mike_command = resolve_mike_command()

    run([sys.executable, "-m", "mkdocs", "build", "--strict", "--config-file", str(MKDOCS_FILE)])
    run(mike_command + [
        "deploy",
        "--config-file",
        str(MKDOCS_FILE),
        "--branch",
        "main",
        "--remote",
        "origin",
        "--title",
        f"{major_line} ({plugin_version})",
        "--update-aliases",
        major_line,
        "latest",
    ] + (["--push"] if args.push else []))
    run(mike_command + [
        "set-default",
        "--config-file",
        str(MKDOCS_FILE),
        "--branch",
        "main",
        "--remote",
        "origin",
        "latest",
    ] + (["--push"] if args.push else []))

    return 0


def resolve_mike_command() -> list[str]:
    for candidate in ["mike", "mike.exe"]:
        mike_path = shutil.which(candidate)
        if mike_path:
            return [mike_path]

    scripts_dir = Path(sys.executable).resolve().parent
    for candidate in [scripts_dir / "mike", scripts_dir / "mike.exe"]:
        if candidate.exists():
            return [str(candidate)]

    raise RuntimeError("Unable to locate the mike CLI executable on PATH.")


def run(command: list[str]) -> None:
    subprocess.run(command, check=True, cwd=ROOT)


if __name__ == "__main__":
    raise SystemExit(main())
