#!/usr/bin/env python3
"""Shared parser utilities for collaboration workflow scripts."""

from __future__ import annotations

import re
from collections.abc import Iterator
from dataclasses import dataclass, field
from pathlib import Path


ITEM_RE = re.compile(r"^### \[([A-Za-z0-9_-]+)\]\s*(.*)$")
FIELD_RE = re.compile(r"^- `([^`]+)`:\s*(.*)$")
HEADING_RE = re.compile(r"^ {0,3}#{1,3}(?:\s|$)")
FENCE_RE = re.compile(r"^ {0,3}(`{3,}|~{3,})(.*)$")


def visible_lines(lines: list[str]) -> Iterator[tuple[int, str]]:
    """Yield original line numbers and syntax outside fences and HTML comments.

    This deliberately supports the collaboration format's Markdown subset,
    rather than interpreting arbitrary Markdown as workflow metadata.
    """
    in_comment = False
    fence = ""
    for number, line in enumerate(lines, start=1):
        if fence:
            closing = FENCE_RE.match(line)
            if closing and closing[1][0] == fence[0] and len(closing[1]) >= len(fence) and not closing[2].strip():
                fence = ""
            yield number, ""
            continue

        # Comment delimiters in code fences are literal code.
        match = None if in_comment else FENCE_RE.match(line)
        if match and not (match[1][0] == "`" and "`" in match[2]):
            fence = match[1]
            yield number, ""
            continue

        visible = ""
        remaining = line
        while remaining:
            if in_comment:
                _, end, remaining = remaining.partition("-->")
                if not end:
                    break
                in_comment = False
            else:
                prefix, start, remaining = remaining.partition("<!--")
                visible += prefix
                if not start:
                    break
                in_comment = True
        yield number, visible


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
        return normalize_agent(self.fields.get("from", ""))

    @property
    def recipients(self) -> set[str]:
        value = self.fields.get("to", "")
        return {
            normalize_agent(part)
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
    metadata_open = False
    fields_started = False

    for number, visible in visible_lines(lines):
        line = lines[number - 1]
        match = ITEM_RE.match(visible)
        if HEADING_RE.match(visible):
            if current is not None:
                current.end_line = number - 1
                items.append(current)
                current = None
        if match:
            current = Item(
                item_id=match.group(1),
                title=match.group(2).strip(),
                source=path,
                start_line=number,
                raw=[line],
            )
            metadata_open = True
            fields_started = False
        elif current:
            current.raw.append(line)
            field_match = FIELD_RE.match(visible) if metadata_open else None
            if field_match:
                current.fields[field_match.group(1).strip()] = field_match.group(2).strip()
                fields_started = True
            else:
                current.body.append(line)
                if visible.strip() or fields_started or FENCE_RE.match(line):
                    metadata_open = False

    if current:
        current.end_line = len(lines)
        items.append(current)
    return items


def all_items(root: Path, include_archives: bool = False) -> list[Item]:
    result: list[Item] = []
    paths = collaboration_files(root)
    if include_archives:
        paths += sorted(
            path for path in (root / "docs" / "collaboration-archives").glob("*.md")
            if re.fullmatch(r".+-\d+\.md", path.name)
        )
    for path in paths:
        result.extend(parse_items(path))
    return result


def addressed_to(item: Item, agent: str) -> bool:
    agent = normalize_agent(agent)
    recipients = item.recipients
    return agent in recipients or ("all" in recipients and item.sender != agent)


def normalize_agent(agent: str) -> str:
    value = agent.strip().lower()
    return "gemini" if value == "agy" else value


def refs_contain_id(refs_value: str, item_id: str) -> bool:
    """Match a complete item ID in comma/pipe-separated references."""
    tokens = {re.sub(r"[\[\]`\s]", "", part).lower() for part in re.split(r"[,|]", refs_value)}
    return item_id.lower() in tokens

