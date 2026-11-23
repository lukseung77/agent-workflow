"""Conservative existing-project migration; preserve content needing semantic review."""

from __future__ import annotations

import json
from pathlib import Path
import re

import foundation


RECEIPT = "agent-workflow-local/migration.json"
MARKER = "<!-- agent-workflow:migrated-shared-rules -->"
POINTER = re.compile(r"^\s*(?:[-*]\s*)?(?:follow|read|see|@)\s*.*(?:agent-common\.md|CODEX\.md|docs/collaboration\.md|agent-workflow/workflow/)", re.I)


def migrate(project: Path, source: Path, source_label: str, context: dict, apply: bool = False) -> dict:
    project = project.resolve()
    receipt = foundation.inside(project, RECEIPT)
    if receipt.exists():
        return {"status": "already migrated", "receipt": RECEIPT}
    candidates = ["docs/collaboration.md", "docs/collaboration-format.md", "agent-common.md", "CODEX.md",
                  "agent-workflow-local/agent-workflow.md"]
    candidates += [str(p.relative_to(project)) for p in sorted((project / "docs").glob("collaboration-index-*.md"))]
    candidates += [str(p.relative_to(project)) for p in sorted((project / "agent-workflow-local").glob("agent-workflow-*.md"))]
    existing = [name for name in candidates if foundation.inside(project, name).is_file()]
    host_edits = {}
    for name in foundation.HOSTS.values():
        path = foundation.inside(project, name)
        if not path.exists():
            continue
        original = path.read_text()
        lines, removed = [], []
        in_fence = False
        for line in original.splitlines(keepends=True):
            if line.lstrip().startswith(("```", "~~~")):
                in_fence = not in_fence
            if not in_fence and POINTER.search(line):
                removed.append(line.rstrip())
            else:
                lines.append(line)
        if removed:
            host_edits[name] = {"text": "".join(lines), "removed": removed}
    if not existing and not host_edits:
        raise ValueError("No legacy markers found; use init for a new project")
    pending = {"status": "review", "legacy_files": existing,
               "host_pointer_changes": {name: edit["removed"] for name, edit in host_edits.items()},
               "preserved": ["stage", "accepted specs", "collaboration IDs/history/archives", "references", "installed tools"],
               "manual_review": ["Reconcile role/review-lens text into project-facts; retain per-agent restrictions only.",
                                 "Review preserved shared overrides against current rules.",
                                 "Review remaining legacy wrappers/indexes and vendored copies before archival/removal.",
                                 "Inspect existing tooling blocks and regenerate only their managed adapter when needed."],
               "receipt": RECEIPT}
    if not apply:
        return pending
    # Validate all target paths before initialization writes any files.
    originals = {name: foundation.inside(project, name).read_bytes() for name in existing}
    originals.update({name: foundation.inside(project, name).read_bytes() for name in host_edits})
    for name in list(foundation.HOSTS.values()) + ["agent-workflow-local/rules.md", "agent-workflow-local/project-facts.md"]:
        path = foundation.inside(project, name)
        if path.is_file():
            originals[name] = path.read_bytes()
    for name in originals:
        foundation.inside(project, "agent-workflow-local/migration-backup/" + name)
    rules = foundation.inside(project, "agent-workflow-local/rules.md")
    # init preserves existing text and the generated template merge base.
    foundation.initialize(project, source, source_label, context)
    for name, contents in originals.items():
        foundation.write(foundation.inside(project, "agent-workflow-local/migration-backup/" + name), contents)
    for name, edit in host_edits.items():
        path = foundation.inside(project, name)
        current = path.read_text()
        # init may have appended a managed startup block; remove only the exact
        # old pointer lines outside that newly generated block.
        for line in edit["removed"]:
            current = current.replace(line + "\n", "", 1)
        foundation.write(path, current.encode())
    shared = project / "agent-workflow-local/agent-workflow.md"
    if shared.is_file() and MARKER not in rules.read_text():
        incoming = rules.read_text().rstrip() + "\n\n" + MARKER + "\n## Preserved Existing Shared Overrides\n\n"
        incoming += "Existing project rules migrated verbatim; reconcile against current foundation rules before dependent work.\n\n" + shared.read_text() + "\n"
        foundation.write(rules, incoming.encode())
    pending["status"] = "mechanical migration applied; semantic review required"
    pending["foundation_fingerprint"] = json.loads((project / foundation.STATE).read_text())["source_fingerprint"]
    foundation.write(receipt, (json.dumps(pending, indent=2) + "\n").encode())
    return pending
