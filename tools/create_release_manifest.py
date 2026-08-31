#!/usr/bin/env python3
"""Create the deterministic manifest and checksums for setup-host ZIP files."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
from pathlib import Path


VERSION_RE = re.compile(r"^v[0-9]+\.[0-9]+\.[0-9]+$")


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--release", required=True)
    parser.add_argument("--dist", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--checksums", type=Path, required=True)
    args = parser.parse_args()

    if not VERSION_RE.fullmatch(args.release):
        parser.error("--release must use vX.Y.Z")

    archives = sorted(args.dist.glob("mortal-kombat-4-recomp-*.zip"))
    if not archives:
        parser.error("the distribution directory contains no title ZIP files")

    packages = [
        {
            "file": archive.name,
            "size": archive.stat().st_size,
            "sha256": sha256(archive),
        }
        for archive in archives
    ]
    manifest = {
        "schema": 2,
        "release": args.release,
        "package_count": len(packages),
        "packages": packages,
    }
    args.output.write_text(
        json.dumps(manifest, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
        newline="\n",
    )

    checksum_lines = [
        f"{package['sha256']}  {package['file']}" for package in packages
    ]
    checksum_lines.append(f"{sha256(args.output)}  {args.output.name}")
    args.checksums.write_text(
        "\n".join(checksum_lines) + "\n",
        encoding="ascii",
        newline="\n",
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
