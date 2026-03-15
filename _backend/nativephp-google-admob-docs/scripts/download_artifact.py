from __future__ import annotations

import argparse
import json
import os
import sys
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen


def main() -> int:
    parser = argparse.ArgumentParser(description="Download private release asset from GitHub")
    parser.add_argument("--repo", required=True, help="Private repo slug, for example owner/repo")
    parser.add_argument("--tag", required=True, help="Release tag, for example v1.2.3")
    parser.add_argument("--asset-name", required=True, help="Asset file name to download")
    parser.add_argument("--output", required=True, type=Path, help="Destination path")
    args = parser.parse_args()

    token = os.environ.get("PRIVATE_DOCS_SOURCE_TOKEN")
    if not token:
        print("ERROR: PRIVATE_DOCS_SOURCE_TOKEN is required.", file=sys.stderr)
        return 1

    headers = {
        "Authorization": f"Bearer {token}",
        "Accept": "application/vnd.github+json",
        "X-GitHub-Api-Version": "2022-11-28",
        "User-Agent": "nativephp-google-admob-docs-sync",
    }

    release_url = f"https://api.github.com/repos/{args.repo}/releases/tags/{args.tag}"
    release_payload = request_json(release_url, headers)
    assets = release_payload.get("assets", [])
    asset = next((item for item in assets if item.get("name") == args.asset_name), None)

    if asset is None:
        print(f"ERROR: asset {args.asset_name} not found on release {args.tag}", file=sys.stderr)
        return 1

    download_url = asset["url"]
    download_headers = dict(headers)
    download_headers["Accept"] = "application/octet-stream"
    body = request_bytes(download_url, download_headers)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_bytes(body)
    return 0


def request_json(url: str, headers: dict[str, str]) -> dict:
    request = Request(url, headers=headers)
    try:
        with urlopen(request) as response:
            return json.loads(response.read().decode("utf-8"))
    except HTTPError as exc:
        raise SystemExit(f"GitHub API error {exc.code}: {exc.read().decode('utf-8', errors='ignore')}")
    except URLError as exc:
        raise SystemExit(f"Network error: {exc}")


def request_bytes(url: str, headers: dict[str, str]) -> bytes:
    request = Request(url, headers=headers)
    try:
        with urlopen(request) as response:
            return response.read()
    except HTTPError as exc:
        raise SystemExit(f"GitHub download error {exc.code}: {exc.read().decode('utf-8', errors='ignore')}")
    except URLError as exc:
        raise SystemExit(f"Network error: {exc}")


if __name__ == "__main__":
    raise SystemExit(main())
