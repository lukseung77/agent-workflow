#!/usr/bin/env python3
"""Run repository checks without installing packages or configuring agent hosts."""

from __future__ import annotations

import argparse
import shutil
import subprocess
import sys
from pathlib import Path


def check_foundation(root: Path) -> bool:
    foundation = root / "agent-workflow-foundation"
    sys.path.insert(0, str(foundation / "scripts"))
    try:
        import foundation as lifecycle
        files = lifecycle.snapshot(foundation)
        denied = {"agent-workflow-local", "openspec", "tests", "user-agent-suggestions", "3rd-party-suggestions"}
        if any(Path(name).parts[0] in denied or name.startswith("docs/collaboration-") for name in files):
            raise ValueError("Consumer or maintenance state entered the product distribution")
        if set(path.name for path in (foundation / "third-party").iterdir()) != {"origins.json"}:
            raise ValueError("Third-party distribution must contain origins only")
        import json
        state = json.loads((root / lifecycle.STATE).read_text())
        if (root / state["context"]["foundation_root"]).resolve() != foundation.resolve():
            raise ValueError("This project must consume its foundation directory")
        expected = lifecycle.state_data(state["source"], state["context"], files, lifecycle.project_templates(files, state["context"]))
        if expected["source_fingerprint"] != state["source_fingerprint"]:
            raise ValueError("Review and apply this project's foundation update before final validation")
        plan = lifecycle.update(root, foundation, state["source"])
        if plan["conflicts"] or plan["actions"]:
            raise ValueError("This consumer has unapplied foundation template changes")
        print(f"Foundation boundary and self-consumer: ok ({len(files)} product files)", flush=True)
        return True
    except (OSError, ValueError, KeyError) as exc:
        print(f"Foundation boundary: failed ({exc})", file=sys.stderr)
        return False


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--require-openspec", action="store_true", help="fail if the optional OpenSpec CLI is unavailable")
    args = parser.parse_args()
    root = Path(__file__).resolve().parents[1]
    checks = [
        ("Unit tests", [sys.executable, "-B", "-m", "unittest", "discover", "-s", "tests"]),
        ("Collaboration lint", [sys.executable, "-B", "agent-workflow-foundation/scripts/collab_lint.py", "--root", ".", "--strict-state", "--check-completion", "--verbose-warnings"]),
    ]
    openspec = shutil.which("openspec")
    if openspec:
        checks.append(("OpenSpec", [openspec, "validate", "--all"]))
    failed = not check_foundation(root)
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
