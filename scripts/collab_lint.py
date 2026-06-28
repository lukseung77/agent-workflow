#!/usr/bin/env python3
"""Read-only validation for collaboration metadata and restart state."""

from __future__ import annotations

import argparse
import json
import re
from datetime import date, datetime
from pathlib import Path

from collab_common import Item, all_items


TYPES = {"status", "question", "gap", "review-request", "review", "suggestion", "response"}
STATUSES = {"open", "active", "done", "superseded"}
LEGACY_STATUSES = {"accepted", "partially_accepted", "rejected"}
REQUIRED_FIELDS = {"date", "from", "to", "type", "status"}
STATE_FIELDS = {"updated", "current_stage", "current_artifact", "next_lead_action", "active_blockers"}
DEFAULT_STAGES = {"Setup", "Exploration", "Proposal", "Implementation", "Complete"}
DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")


def _refs_contain_id(refs_value: str, item_id: str) -> bool:
    """Return True if item_id appears (bare or bracketed) in a refs field value."""
    parts = re.split(r"[,|]", refs_value)
    tokens = {re.sub(r"[\[\]\s]", "", p).lower() for p in parts}
    return item_id.lower() in tokens


def check_formal_completion(
    items: list[Item],
    root: Path,
    errors: list[str],
    warnings: list[str],
) -> None:
    """Validate the ELS-012 completion gate for every formal review-request."""
    formal_requests = [
        item for item in items
        if item.fields.get("type") == "review-request"
        and item.fields.get("formal", "").strip().lower() == "true"
    ]

    for req in formal_requests:
        location = f"{req.source.relative_to(root)}:{req.start_line}"
        req_id = req.item_id

        if req.status in ("open", "active"):
            errors.append(
                f"{location}: formal review-request {req_id} is not done"
            )
            continue

        consolidation = next(
            (
                item for item in items
                if item.fields.get("type") == "status"
                and item.status == "done"
                and _refs_contain_id(item.fields.get("refs", ""), req_id)
            ),
            None,
        )
        if consolidation is None:
            errors.append(
                f"{location}: no consolidation status item found for formal review {req_id}"
            )

        if "all" not in req.recipients:
            for reviewer in sorted(req.recipients - {req.sender}):
                has_response = any(
                    item.fields.get("type") == "review"
                    and item.sender == reviewer
                    and item.status == "done"
                    and _refs_contain_id(item.fields.get("refs", ""), req_id)
                    for item in items
                )
                if not has_response:
                    errors.append(
                        f"{location}: no done review from '{reviewer}' for formal review {req_id}"
                    )


def parse_state(path: Path) -> dict[str, str]:
    values: dict[str, str] = {}
    for line in path.read_text(encoding="utf-8").splitlines():
        match = re.match(r"^- `([^`]+)`:\s*(.*)$", line)
        if match:
            values[match.group(1)] = match.group(2).strip()
    return values


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=Path, default=Path.cwd())
    parser.add_argument("--json", action="store_true")
    parser.add_argument("--verbose-warnings", action="store_true")
    parser.add_argument("--strict-state", action="store_true")
    parser.add_argument(
        "--check-completion",
        action="store_true",
        help="Validate the ELS-012 completion gate for all formal review-requests",
    )
    parser.add_argument(
        "--allowed-stage",
        action="append",
        default=[],
        help="Additional allowed current_stage value; may be repeated",
    )
    args = parser.parse_args()
    root = args.root.resolve()
    errors: list[str] = []
    warnings: list[str] = []
    seen: dict[str, str] = {}

    items = all_items(root)
    for item in items:
        location = f"{item.source.relative_to(root)}:{item.start_line}"
        key = item.item_id.lower()
        if key in seen:
            errors.append(f"{location}: duplicate ID {item.item_id}; first seen at {seen[key]}")
        seen[key] = location

        missing = REQUIRED_FIELDS - item.fields.keys()
        if missing:
            errors.append(f"{location}: missing fields: {', '.join(sorted(missing))}")

        item_type = item.fields.get("type", "")
        if item_type and item_type not in TYPES:
            errors.append(f"{location}: invalid type: {item_type}")

        status = item.status
        if status in LEGACY_STATUSES:
            warnings.append(f"{location}: legacy status '{status}'; use lifecycle status")
        elif status and status not in STATUSES:
            errors.append(f"{location}: invalid status: {status}")

        raw_date = item.fields.get("date", "")
        if raw_date:
            if not DATE_RE.fullmatch(raw_date):
                errors.append(f"{location}: date must be YYYY-MM-DD")
            else:
                try:
                    date.fromisoformat(raw_date)
                except ValueError:
                    errors.append(f"{location}: invalid calendar date: {raw_date}")

        created_at = item.fields.get("created_at")
        if created_at:
            try:
                parsed = datetime.fromisoformat(created_at.replace("Z", "+00:00"))
                if parsed.tzinfo is None:
                    errors.append(f"{location}: created_at must include Z or a UTC offset")
                if raw_date and parsed.date().isoformat() != raw_date:
                    errors.append(f"{location}: created_at date does not match date")
            except ValueError:
                errors.append(f"{location}: invalid ISO 8601 created_at")

    if args.check_completion:
        check_formal_completion(items, root, errors, warnings)

    state_path = root / "agent-workflow-local" / "current-state.md"
    if args.strict_state and state_path.exists():
        state = parse_state(state_path)
        if set(state) != STATE_FIELDS:
            errors.append(
                f"{state_path.relative_to(root)}: expected exactly: {', '.join(sorted(STATE_FIELDS))}"
            )
        updated = state.get("updated", "")
        if updated:
            if not DATE_RE.fullmatch(updated):
                errors.append(f"{state_path.relative_to(root)}: updated must be YYYY-MM-DD")
            else:
                try:
                    date.fromisoformat(updated)
                except ValueError:
                    errors.append(f"{state_path.relative_to(root)}: invalid updated date")
        stage = state.get("current_stage", "")
        allowed_stages = DEFAULT_STAGES | set(args.allowed_stage)
        if stage and stage not in allowed_stages:
            errors.append(
                f"{state_path.relative_to(root)}: current_stage '{stage}' is not allowed"
            )
        artifact = state.get("current_artifact", "")
        if artifact and artifact.lower() != "none":
            artifact_path = Path(artifact)
            candidate = root / artifact_path
            if artifact_path.is_absolute() or not candidate.exists():
                errors.append(
                    f"{state_path.relative_to(root)}: current_artifact must be an existing project-relative path or None"
                )

    payload = {"errors": errors, "warnings": warnings}
    if args.json:
        print(json.dumps(payload, indent=2))
    else:
        for error in errors:
            print(f"ERROR: {error}")
        if args.verbose_warnings:
            for warning in warnings:
                print(f"WARNING: {warning}")
        elif warnings:
            print(f"{len(warnings)} warning(s); rerun with --verbose-warnings for details.")
        print(f"{len(errors)} error(s), {len(warnings)} warning(s).")
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
