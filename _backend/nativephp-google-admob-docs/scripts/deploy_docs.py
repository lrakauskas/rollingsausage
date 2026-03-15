from __future__ import annotations

import argparse
import json
import shutil
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
REPO_ROOT = ROOT.parents[1]
MKDOCS_FILE = ROOT / "mkdocs.yml"
DATA_MANIFEST = ROOT / "data" / "current" / "manifest.json"
PUBLISH_SUBPATH = Path("nativephp-admob") / "docs"
TEMP_DEPLOY_BRANCH = "nativephp-google-admob-docs-build"


def main() -> int:
    parser = argparse.ArgumentParser(description="Prepare versioned NativePHP Google AdMob docs for publication")
    parser.add_argument("--deploy-branch", default=TEMP_DEPLOY_BRANCH, help="Temporary local branch used by mike")
    parser.add_argument("--keep-deploy-branch", action="store_true", help="Keep the temporary local deployment branch after generation")
    args = parser.parse_args()

    manifest = json.loads(DATA_MANIFEST.read_text(encoding="utf-8"))
    major_line = manifest["major_line"]
    plugin_version = manifest["plugin_version"]

    delete_local_branch(args.deploy_branch)
    run([sys.executable, "-m", "mkdocs", "build", "--strict", "--config-file", str(MKDOCS_FILE)])
    run_mike([
        "deploy",
        "--config-file",
        str(MKDOCS_FILE),
        "--branch",
        args.deploy_branch,
        "--title",
        f"{major_line} ({plugin_version})",
        "--update-aliases",
        major_line,
        "latest",
    ])
    run_mike([
        "set-default",
        "--config-file",
        str(MKDOCS_FILE),
        "--branch",
        args.deploy_branch,
        "latest",
    ])
    checkout_publish_tree(args.deploy_branch)

    if not args.keep_deploy_branch:
        delete_local_branch(args.deploy_branch)

    return 0


def run_mike(arguments: list[str]) -> None:
    command = [
        sys.executable,
        "-c",
        (
            "import sys; "
            "import mike.driver; "
            "sys.argv = ['mike'] + sys.argv[1:]; "
            "raise SystemExit(mike.driver.main())"
        ),
        *arguments,
    ]

    run(command)


def checkout_publish_tree(branch: str) -> None:
    publish_root = REPO_ROOT / PUBLISH_SUBPATH.parent
    publish_path = REPO_ROOT / PUBLISH_SUBPATH

    publish_root.mkdir(parents=True, exist_ok=True)

    if publish_path.exists():
        shutil.rmtree(publish_path)

    run([
        "git",
        "checkout",
        branch,
        "--",
        str(PUBLISH_SUBPATH).replace("\\", "/"),
    ], cwd=REPO_ROOT)


def delete_local_branch(branch: str) -> None:
    subprocess.run(
        ["git", "branch", "-D", branch],
        check=False,
        cwd=REPO_ROOT,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    )


def run(command: list[str], cwd: Path = ROOT) -> None:
    subprocess.run(command, check=True, cwd=cwd)


if __name__ == "__main__":
    raise SystemExit(main())
