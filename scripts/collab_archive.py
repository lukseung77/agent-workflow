#!/usr/bin/env python3
"""Archive resolved collaboration items after a size threshold."""

from __future__ import annotations

import argparse
from pathlib import Path

from collab_common import collaboration_files, parse_items


RESOLVED = {"done", "superseded", "accepted", "partially_accepted", "rejected"}


def next_archive_path(root: Path, source: Path) -> Path:
    archive_dir = root / "docs" / "collaboration-archives"
    agent = source.stem.removeprefix("collaboration-")
    existing = sorted(archive_dir.glob(f"{agent}-*.md"))
    number = int(existing[-1].stem.rsplit("-", 1)[1]) + 1 if existing else 1
    return archive_dir / f"{agent}-{number:03d}.md"


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=Path, default=Path.cwd())
    parser.add_argument("--threshold-bytes", type=int, default=50_000)
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()
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
        archive.write_text(
            f"# Collaboration Archive\n\nSource: `{source.relative_to(root)}`\n\n{archived}\n",
            encoding="utf-8",
        )
        source.write_text("\n".join(retained).rstrip() + "\n", encoding="utf-8")
        changed += 1

    if not changed and not args.dry_run:
        print("No collaboration file exceeded the resolved-content threshold.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
