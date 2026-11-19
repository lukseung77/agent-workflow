#!/usr/bin/env python3
"""Run repository checks without installing packages or configuring agent hosts."""

from __future__ import annotations

import argparse
import shutil
import subprocess
import sys
from pathlib import Path


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--require-openspec", action="store_true", help="fail if the optional OpenSpec CLI is unavailable")
    args = parser.parse_args()
    root = Path(__file__).resolve().parents[1]
    checks = [
        ("Unit tests", [sys.executable, "-B", "-m", "unittest", "discover", "-s", "tests"]),
        ("Collaboration lint", [sys.executable, "-B", "scripts/collab_lint.py", "--root", ".", "--strict-state", "--check-completion", "--verbose-warnings"]),
    ]
    openspec = shutil.which("openspec")
    if openspec:
        checks.append(("OpenSpec", [openspec, "validate", "--all"]))
    failed = False
    for label, command in checks:
        print(f"Running {label}", flush=True)
        try:
            result = subprocess.run(command, cwd=root, check=False)
            failed |= result.returncode != 0
        except OSError as exc:
            print(f"{label}: failed ({exc})", file=sys.stderr)
            failed = True
    if not openspec:
        print("OpenSpec: unavailable" + (" (required)" if args.require_openspec else " (skipped; optional locally)"), flush=True)
        failed |= args.require_openspec
    return int(failed)


if __name__ == "__main__":
    raise SystemExit(main())
