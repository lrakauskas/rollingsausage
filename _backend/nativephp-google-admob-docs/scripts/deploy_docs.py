from __future__ import annotations

import argparse
import json
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

    run([sys.executable, "-m", "mkdocs", "build", "--strict", "--config-file", str(MKDOCS_FILE)])
    run([
        sys.executable,
        "-m",
        "mike",
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
    run([
        sys.executable,
        "-m",
        "mike",
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


def run(command: list[str]) -> None:
    subprocess.run(command, check=True, cwd=ROOT)


if __name__ == "__main__":
    raise SystemExit(main())
