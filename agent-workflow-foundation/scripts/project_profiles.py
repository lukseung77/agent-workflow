"""Resolve project templates without installing tools or changing workflow state."""

from __future__ import annotations

import json
from pathlib import PurePosixPath


CATALOG = "templates/project-types.json"
SELECTION = "agent-workflow-local/project-template.json"
LEGACY_STAGES = ["Exploration", "Proposal", "Implementation"]


def catalog(files: dict[str, bytes]) -> dict:
    data = json.loads(files[CATALOG])
    if data.get("schema_version") != 1 or not data.get("project_types"):
        raise ValueError("Unsupported or empty project type catalog")
    registry = json.loads(files["third-party/origins.json"])["tools"]
    for project_type in data["project_types"].values():
        if not project_type.get("templates"):
            raise ValueError("Every project type needs at least one template")
        for template in project_type["templates"].values():
            workflow = template["workflow"]
            source = PurePosixPath(template["source_root"])
            stages = template["stages"]
            if workflow not in files or source.is_absolute() or ".." in source.parts or not source.parts:
                raise ValueError("Template workflow or source root is invalid")
            if not stages or any(not isinstance(stage, str) or not stage.strip() for stage in stages) or len(stages) != len(set(stages)):
                raise ValueError("Template needs distinct nonempty stages")
            if any(tool not in registry for tool in data["core_tools"] + template["required_tools"]):
                raise ValueError("Template references a tool without an origin")
    return data


def selection(files: dict[str, bytes], context: dict) -> dict:
    data = catalog(files)
    project_type, template_id = context.get("project_type"), context.get("template_id")
    if not project_type and not template_id:
        # Existing consumers retain their process; update never chooses a new type.
        return {
            "schema_version": 1, "status": "legacy-unselected",
            "project_type": None, "template_id": None,
            "workflow": context["foundation_root"] + "/workflow/legacy-stages.md",
            "source_root": context["source_root"], "stages": LEGACY_STAGES,
            "required_tools": data["core_tools"], "manual_requirements": [],
            "handoff": "existing-project", "stage_tooling_review": True,
            "installation": "guided", "capability_status": "not-verified",
        }
    try:
        kind = data["project_types"][project_type]
        template = kind["templates"][template_id]
    except KeyError:
        raise ValueError("Choose a valid project type and a template belonging to it") from None
    return {
        **template, "schema_version": 1, "status": "selected",
        "project_type": project_type, "project_type_name": kind["name"],
        "template_id": template_id,
        "workflow": context["foundation_root"] + "/" + template["workflow"],
        "source_root": context.get("source_root") or template["source_root"],
        "required_tools": list(dict.fromkeys(data["core_tools"] + template["required_tools"])),
        "installation": "guided", "capability_status": "not-verified",
    }
