#!/usr/bin/env python3
"""Plan or record an agent-run upstream tooling review; never install or fetch tools."""

from __future__ import annotations

import argparse
from datetime import datetime, timezone
import json
from pathlib import Path
import re

import foundation


RECORD = "agent-workflow-local/tooling-reviews.json"


def context(root: Path, stage: str | None = None) -> dict:
    text = (root / "agent-workflow-local/current-state.md").read_text()
    def field(name):
        match = re.search(r"^- `" + name + r"`:\s*(.+)$", text, re.MULTILINE)
        if not match:
            raise ValueError(f"Missing current-state field: {name}")
        return match.group(1).strip()
    return {"stage": stage or field("current_stage"), "artifact": field("current_artifact")}


def load_record(root: Path) -> dict:
    path = foundation.inside(root, RECORD)
    data = json.loads(path.read_text()) if path.exists() else {"schema_version": 1, "reviews": []}
    if data.get("schema_version") != 1 or not isinstance(data.get("reviews"), list):
        raise ValueError("Unsupported tooling review record")
    return data


def plan(root: Path, origin: Path, event: str, stage: str | None = None,
         transition_id: str | None = None, tools: tuple[str, ...] = ()) -> dict:
    if event not in {"manual", "stage-change"}:
        raise ValueError("Use a manual request or stage-change event")
    if event == "stage-change" and not transition_id:
        raise ValueError("Stage changes need the transition collaboration ID")
    current = context(root, stage)
    data = load_record(root)
    latest = data["reviews"][-1] if data["reviews"] else None
    same = bool(event == "stage-change" and latest and latest.get("context") == current)
    if event == "stage-change":
        same = same and latest.get("transition_id") == transition_id
    registry = json.loads((origin / "third-party/origins.json").read_text())["tools"]
    inventory_path = root / "agent-workflow-local/tooling.json"
    inventory = json.loads(inventory_path.read_text()).get("tools", {}) if inventory_path.exists() else {}
    selected = set(tools) | {key for key, value in inventory.items()
                             if value.get("selected") or value.get("installed") or value.get("available")}
    # Retain the last review's explicit selections when an installed tool has
    # not yet been added to the separate actual-installation inventory.
    if latest:
        selected.update(latest.get("tools", {}).keys())
    unknown = selected - registry.keys()
    if unknown:
        raise ValueError("Register official origins before review: " + ", ".join(sorted(unknown)))
    excluded = {key for key in selected if registry[key].get("integration_status") == "catalog-only"}
    selected -= excluded
    if same and not selected.issubset(latest.get("tools", {})):
        same = False
    return {"status": "event-recorded" if same else "review-required", "event": event,
            "context": current, "transition_id": transition_id,
            "tools": {key: {"origin": registry[key]["origin"],
                            "installed": inventory.get(key, {}),
                            "integration": registry[key].get("integration")}
                      for key in sorted(selected)},
            "excluded": sorted(excluded),
            "discovery": "Check primary sources for product-relevant additions and replacements; preserve excluded categories.",
            "previous_status": latest.get("status") if same else None,
            "procedure": "workflow/tooling-review.md"}


def record(root: Path, request: dict, report: dict) -> None:
    if report.get("context") != request["context"]:
        raise ValueError("Report context must match the current review plan")
    if report.get("transition_id") != request["transition_id"]:
        raise ValueError("Report transition ID must match the review plan")
    checked = report.get("checked_at", "")
    stamp = datetime.fromisoformat(checked.replace("Z", "+00:00"))
    if stamp.tzinfo is None:
        raise ValueError("checked_at needs a timezone")
    results = report.get("tools")
    if not isinstance(results, dict) or set(results) != set(request["tools"]):
        raise ValueError("Report must account for every selected tool exactly once")
    degraded = False
    for key, result in results.items():
        status = result.get("status")
        if status not in {"current", "update-available", "unavailable", "not-applicable"}:
            raise ValueError(f"Invalid check status for {key}")
        if not result.get("decision") or not result.get("summary"):
            raise ValueError(f"Record the decision and evidence/limitation summary for {key}")
        if status == "unavailable":
            degraded = True
        elif status != "not-applicable" and not (result.get("source", "").startswith("https://") and result.get("observed")):
            raise ValueError(f"Checked tool {key} needs a primary-source URL and observed version/revision/service change")
    discovery = report.get("discovery", {})
    if discovery.get("status") not in {"checked", "unavailable"} or not discovery.get("summary"):
        raise ValueError("Record new-tool discovery evidence or its unavailability")
    if discovery["status"] == "checked" and not discovery.get("sources"):
        raise ValueError("Discovery needs primary-source URLs")
    if any(not isinstance(url, str) or not url.startswith("https://") for url in discovery.get("sources", [])):
        raise ValueError("Discovery sources must be HTTPS URLs")
    degraded |= discovery["status"] == "unavailable"
    entry = {**report, "event": request["event"], "status": "degraded" if degraded else "completed",
             "recorded_at": datetime.now(timezone.utc).isoformat()}
    data = load_record(root)
    data["reviews"].append(entry)
    foundation.write(foundation.inside(root, RECORD), (json.dumps(data, indent=2) + "\n").encode())


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path.cwd())
    parser.add_argument("--event", choices=["manual", "stage-change"], required=True)
    parser.add_argument("--stage", help="Confirmed destination stage, if not yet saved")
    parser.add_argument("--transition-id", help="Unique stage transition collaboration ID")
    parser.add_argument("--tools", nargs="*", default=[], help="Additional selected registry IDs")
    parser.add_argument("--json", action="store_true", help="Print the full plan even for a recorded event")
    parser.add_argument("--record", type=Path, help="Record the agent's evidence report; does not perform online checks")
    args = parser.parse_args()
    try:
        root = args.root.resolve()
        request = plan(root, Path(__file__).resolve().parents[1], args.event, args.stage,
                       args.transition_id, tuple(args.tools))
        if args.record:
            record(root, request, json.loads(args.record.read_text()))
            request["status"] = "recorded"
        if args.json or request["status"] == "review-required":
            print(json.dumps(request, indent=2))
        else:
            print(f"Tooling review: {request['status']} ({request.get('previous_status') or 'evidence saved'}).")
        return 0
    except (OSError, ValueError, KeyError, TypeError, AttributeError) as exc:
        print(f"tooling review: {exc}")
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
