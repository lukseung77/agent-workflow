#!/usr/bin/env python3
"""Archive resolved collaboration items after a size threshold."""

from __future__ import annotations

import argparse
import re
from pathlib import Path

from collab_common import collaboration_files, parse_items


RESOLVED = {"done", "superseded", "accepted", "partially_accepted", "rejected"}


def next_archive_path(root: Path, source: Path) -> Path:
    archive_dir = root / "docs" / "collaboration-archives"
    agent = source.stem.removeprefix("collaboration-")
    numbers = [
        int(match[1]) for path in archive_dir.glob(f"{agent}-*.md")
        if (match := re.fullmatch(re.escape(agent) + r"-(\d+)\.md", path.name))
    ]
    number = max(numbers, default=0) + 1
    return archive_dir / f"{agent}-{number:03d}.md"


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=Path, default=Path.cwd())
    parser.add_argument("--threshold-bytes", type=int, default=20_000)
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()
    if args.threshold_bytes < 1:
        parser.error("--threshold-bytes must be positive")
    root = args.root.resolve()

    changed = 0
    for source in collaboration_files(root):
        resolved = [item for item in parse_items(source) if item.status in RESOLVED]
        total = sum(len("\n".join(item.raw).encode("utf-8")) for item in resolved)
        if total < args.threshold_bytes or not resolved:
            continue

        archive = next_archive_path(root, source)
        print(f"{source.relative_to(root)} -> {archive.relative_to(root)} ({len(resolved)} items)")
        if args.dry_run:
            continue

        archive.parent.mkdir(parents=True, exist_ok=True)
        lines = source.read_text(encoding="utf-8").splitlines()
        remove_lines: set[int] = set()
        for item in resolved:
            remove_lines.update(range(item.start_line, item.end_line + 1))
        retained = [line for number, line in enumerate(lines, start=1) if number not in remove_lines]
        archived = "\n\n".join("\n".join(item.raw).strip() for item in resolved)
        # Never overwrite an existing archive, even if another process raced us.
        with archive.open("x", encoding="utf-8") as output:
            output.write(f"# Collaboration Archive\n\nSource: `{source.relative_to(root)}`\n\n{archived}\n")
        source.write_text("\n".join(retained).rstrip() + "\n", encoding="utf-8")
        changed += 1

    if not changed and not args.dry_run:
        print("No collaboration file exceeded the resolved-content threshold.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
