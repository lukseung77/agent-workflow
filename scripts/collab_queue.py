#!/usr/bin/env python3
"""Generate an agent's active queue from authoritative collaboration files."""

from __future__ import annotations

import argparse
import json
from datetime import datetime
from pathlib import Path

from collab_common import Item, addressed_to, all_items


ACTIVE_STATUSES = {"open", "active"}


def sort_key(item: Item) -> tuple[str, str, str]:
    created_at = item.fields.get("created_at", "")
    date = item.fields.get("date", "")
    return created_at or f"{date}T00:00:00+00:00", date, item.item_id.lower()


def serialize(item: Item, root: Path) -> dict[str, object]:
    return {
        "id": item.item_id,
        "status": item.status,
        "title": item.title,
        "source": f"{item.source.relative_to(root)}:{item.start_line}",
        "fields": item.fields,
        "body": "\n".join(item.body).strip(),
    }


def render_detail(item: Item, root: Path) -> str:
    data = serialize(item, root)
    lines = [f"## [{item.item_id}] {item.title}"]
    for key, value in item.fields.items():
        lines.append(f"- `{key}`: {value}")
    lines.append(f"- `source`: {data['source']}")
    body = str(data["body"])
    if body:
        lines.extend(["", body])
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("agent", help="Recipient agent name")
    parser.add_argument("--root", type=Path, default=Path.cwd())
    group = parser.add_mutually_exclusive_group()
    group.add_argument("--full", action="store_true")
    group.add_argument("--id", dest="item_id")
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()

    root = args.root.resolve()
    queue = [
        item
        for item in all_items(root)
        if item.status in ACTIVE_STATUSES and addressed_to(item, args.agent)
    ]
    queue.sort(key=sort_key, reverse=True)

    if args.item_id:
        matches = [item for item in queue if item.item_id.lower() == args.item_id.lower()]
        if len(matches) != 1:
            parser.error(f"active addressed item not found: {args.item_id}")
        item = matches[0]
        print(json.dumps(serialize(item, root), indent=2) if args.json else render_detail(item, root))
        return 0

    if args.json:
        print(json.dumps([serialize(item, root) for item in queue], indent=2))
        return 0

    if not queue:
        print("No active addressed items.")
        return 0

    if args.full:
        print("\n\n".join(render_detail(item, root) for item in queue))
        return 0

    print("| ID | Status | Title | Source |")
    print("|----|--------|-------|--------|")
    for item in queue:
        source = f"{item.source.relative_to(root)}:{item.start_line}"
        print(f"| {item.item_id} | {item.status} | {item.title} | {source} |")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

