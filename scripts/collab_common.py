#!/usr/bin/env python3
"""Shared parser utilities for collaboration workflow scripts."""

from __future__ import annotations

import re
from dataclasses import dataclass, field
from pathlib import Path


ITEM_RE = re.compile(r"^### \[([A-Za-z0-9_-]+)\]\s*(.*)$")
FIELD_RE = re.compile(r"^- `([^`]+)`:\s*(.*)$")


@dataclass
class Item:
    item_id: str
    title: str
    source: Path
    start_line: int
    end_line: int = 0
    fields: dict[str, str] = field(default_factory=dict)
    body: list[str] = field(default_factory=list)
    raw: list[str] = field(default_factory=list)

    @property
    def status(self) -> str:
        return self.fields.get("status", "").strip().lower()

    @property
    def sender(self) -> str:
        return self.fields.get("from", "").strip().lower()

    @property
    def recipients(self) -> set[str]:
        value = self.fields.get("to", "")
        return {
            part.strip().lower()
            for part in re.split(r"[,|]", value)
            if part.strip()
        }


def collaboration_files(root: Path) -> list[Path]:
    docs = root / "docs"
    if not docs.exists():
        return []
    return sorted(
        path
        for path in docs.glob("collaboration-*.md")
        if not path.name.startswith("collaboration-index-")
        and path.name != "collaboration-format.md"
    )


def parse_items(path: Path) -> list[Item]:
    lines = path.read_text(encoding="utf-8").splitlines()
    items: list[Item] = []
    current: Item | None = None
    in_comment = False

    for number, line in enumerate(lines, start=1):
        if "<!--" in line:
            in_comment = True

        match = None if in_comment else ITEM_RE.match(line)
        if match:
            if current:
                current.end_line = number - 1
                items.append(current)
            current = Item(
                item_id=match.group(1),
                title=match.group(2).strip(),
                source=path,
                start_line=number,
                raw=[line],
            )
        elif current:
            current.raw.append(line)
            field_match = FIELD_RE.match(line)
            if field_match:
                current.fields[field_match.group(1).strip()] = field_match.group(2).strip()
            else:
                current.body.append(line)

        if "-->" in line:
            in_comment = False

    if current:
        current.end_line = len(lines)
        items.append(current)
    return items


def all_items(root: Path) -> list[Item]:
    result: list[Item] = []
    for path in collaboration_files(root):
        result.extend(parse_items(path))
    return result


def addressed_to(item: Item, agent: str) -> bool:
    agent = agent.lower()
    recipients = item.recipients
    return agent in recipients or ("all" in recipients and item.sender != agent)

