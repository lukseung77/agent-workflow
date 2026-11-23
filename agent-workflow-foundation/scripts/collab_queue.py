#!/usr/bin/env python3
"""Generate active queues and retrieve live or archived collaboration evidence."""

from __future__ import annotations

import argparse
import json
import re
from datetime import datetime, timezone
from pathlib import Path

from collab_common import Item, addressed_to, all_items, normalize_agent, refs_contain_id


ACTIVE_STATUSES = {"open", "active"}


def startup(root: Path, agent: str) -> dict:
    agent = normalize_agent(agent)
    live = all_items(root)
    own = [item for item in live if item.status in ACTIVE_STATUSES and addressed_to(item, agent)]
    facts = root / "agent-workflow-local/project-facts.md"
    text = facts.read_text() if facts.exists() else ""
    match = re.search(r"^- Lead:\s*([^\s`]+)", text, re.MULTILINE)
    lead = bool(match and normalize_agent(match.group(1)) == agent)
    result = {"queue": [serialize(item, root) for item in sorted(own, key=sort_key, reverse=True)]}
    if not lead:
        return result
    result["user"] = [serialize(item, root) for item in live
                      if item.status in ACTIVE_STATUSES and "user" in item.recipients]
    requests = [item for item in live if item.sender == agent and item.status in ACTIVE_STATUSES
                and item.fields.get("type") == "review-request"]
    evidence = all_items(root, include_archives=True) if requests else []
    result["responses"] = {request.item_id: [serialize(item, root) for item in evidence
                                           if refs_contain_id(item.fields.get("refs", ""), request.item_id)]
                           for request in requests}
    path = root / "agent-workflow-local/tooling-reviews.json"
    try:
        reviews = json.loads(path.read_text()).get("reviews", []) if path.exists() else []
        result["tooling"] = ("Last recorded review: " + str(reviews[-1].get("status", "unknown"))) if reviews else "No review recorded"
    except (OSError, ValueError, TypeError, AttributeError, IndexError):
        result["tooling"] = "Review record unreadable; inspect when relevant"
    return result


def sort_key(item: Item) -> tuple[datetime, str, str]:
    created_at = item.fields.get("created_at", "")
    date = item.fields.get("date", "")
    try:
        instant = datetime.fromisoformat(created_at.replace("Z", "+00:00"))
        if instant.tzinfo is None:
            raise ValueError("timestamp has no timezone")
    except ValueError:
        try:
            instant = datetime.fromisoformat(date).replace(tzinfo=timezone.utc)
        except ValueError:
            instant = datetime.min.replace(tzinfo=timezone.utc)
    return instant.astimezone(timezone.utc), date, item.item_id.lower()


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
    parser.add_argument("agent", help="Recipient for the default queue; not a filter for --id or --refs")
    parser.add_argument("--root", type=Path, default=Path.cwd())
    group = parser.add_mutually_exclusive_group()
    group.add_argument("--full", action="store_true")
    group.add_argument("--id", dest="item_id", help="Retrieve any live or archived item by ID")
    group.add_argument("--refs", dest="reference_id", help="List any live or archived items referencing this ID")
    group.add_argument("--startup", action="store_true", help="Combine queue, lead user decisions, and review responses without online checks")
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()

    root = args.root.resolve()
    if args.startup:
        data = startup(root, args.agent)
        if args.json:
            print(json.dumps(data, indent=2))
        else:
            for key in ("queue", "user"):
                if key in data:
                    print(f"{key}: " + (", ".join(f"{item['id']} ({item['status']}): {item['title']}" for item in data[key]) or "none"))
            for request, responses in data.get("responses", {}).items():
                print(f"{request} responses: " + (", ".join(item["id"] for item in responses) or "none"))
            if "tooling" in data:
                print("tooling: " + data["tooling"] + "; no online check performed")
        return 0
    items = all_items(root, include_archives=bool(args.item_id or args.reference_id))
    queue = [
        item
        for item in items
        if item.status in ACTIVE_STATUSES and addressed_to(item, args.agent)
    ]
    if args.reference_id:
        queue = [item for item in items if refs_contain_id(item.fields.get("refs", ""), args.reference_id)]
    queue.sort(key=sort_key, reverse=True)

    if args.item_id:
        matches = [item for item in items if item.item_id.lower() == args.item_id.lower()]
        if len(matches) != 1:
            parser.error(f"expected one item for ID {args.item_id}; found {len(matches)}")
        item = matches[0]
        print(json.dumps(serialize(item, root), indent=2) if args.json else render_detail(item, root))
        return 0

    if args.json:
        print(json.dumps([serialize(item, root) for item in queue], indent=2))
        return 0

    if not queue:
        print("No referencing items." if args.reference_id else "No active addressed items.")
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

