#!/usr/bin/env python3
"""Install and review updates to foundation consumers, including this repository."""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import shutil
import subprocess
import tempfile
import zipfile
from contextlib import contextmanager
from datetime import date
from pathlib import Path


STATE = "agent-workflow-local/foundation-state.json"
HOSTS = {"codex": "AGENTS.md", "claude": "CLAUDE.md", "gemini": "GEMINI.md"}
START, END = "<!-- agent-workflow:startup:start -->", "<!-- agent-workflow:startup:end -->"


def digest(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def inside(root: Path, name: str) -> Path:
    path = Path(name)
    if path.is_absolute() or ".." in path.parts or not path.parts:
        raise ValueError(f"Expected a project-relative path: {name}")
    target = root / path
    if not target.resolve().is_relative_to(root.resolve()) or target.is_symlink():
        raise ValueError(f"Path escapes the project or is a symlink: {name}")
    return target


def snapshot(root: Path) -> dict[str, bytes]:
    manifest = json.loads((root / "foundation.json").read_text())
    if manifest.get("name") != "agent-workflow-foundation" or manifest.get("schema_version") != 1:
        raise ValueError("Unsupported foundation manifest")
    files = {}
    distribution = set(manifest["distribution"])
    for path in sorted(root.rglob("*")):
        relative = path.relative_to(root)
        if relative.parts[0] not in distribution:
            continue
        if set(relative.parts) & {".git", "__pycache__"} or path.name == ".DS_Store" or path.suffix == ".pyc":
            continue
        if path.is_symlink():
            raise ValueError(f"Foundation contains a symlink: {relative}")
        if path.is_file():
            files[relative.as_posix()] = path.read_bytes()
    return files


@contextmanager
def source_tree(source: str, relative_to: Path):
    """A repository source exports only its foundation subdirectory."""
    with tempfile.TemporaryDirectory(prefix="foundation-source-") as temporary:
        if source.startswith(("https://", "git@")):
            checkout = Path(temporary) / "checkout"
            subprocess.run(["git", "clone", "--depth", "1", "--", source, str(checkout)], check=True, timeout=180)
            candidate = checkout
        else:
            candidate = Path(source).expanduser()
            if not candidate.is_absolute():
                candidate = relative_to / candidate
            candidate = candidate.resolve()
        if (candidate / "agent-workflow-foundation/foundation.json").is_file():
            candidate /= "agent-workflow-foundation"
        if not (candidate / "foundation.json").is_file():
            raise ValueError("Source must be a foundation directory or a repository containing one")
        yield candidate


def render(text: str, context: dict) -> str:
    for key, value in context.items():
        text = text.replace("{{" + key + "}}", str(value))
    return text


def project_templates(files: dict[str, bytes], context: dict) -> dict[str, str]:
    result = {}
    prefix = "templates/agent-workflow-local/"
    for name, data in files.items():
        if name.startswith(prefix):
            result["agent-workflow-local/" + name[len(prefix):]] = render(data.decode(), context)
    for agent in context["agents"]:
        body = files[f"templates/{agent.upper()}.md"].decode()
        body = render(body, context).replace("[Project Name]", context["project_name"]).replace("<foundation-root>", context["foundation_root"])
        result[HOSTS[agent]] = START + "\n" + body.rstrip() + "\n" + END + "\n"
    return result


def write(path: Path, data: bytes) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.NamedTemporaryFile(dir=path.parent, delete=False) as temporary:
        temporary.write(data)
        temp_path = Path(temporary.name)
    try:
        if path.exists():
            temp_path.chmod(path.stat().st_mode)
        os.replace(temp_path, path)
    finally:
        if temp_path.exists():
            temp_path.unlink()


def merge(base: str, local: str, incoming: str) -> str | None:
    if local == base or local == incoming:
        return incoming
    if incoming == base:
        return local
    if not shutil.which("git"):
        return None
    with tempfile.TemporaryDirectory(prefix="foundation-merge-") as temporary:
        paths = [Path(temporary) / name for name in ("local", "base", "incoming")]
        for path, text in zip(paths, (local, base, incoming)):
            path.write_text(text)
        result = subprocess.run(["git", "merge-file", "-p", *map(str, paths)], capture_output=True, text=True, timeout=30)
        return result.stdout if result.returncode == 0 else None


def state_data(source: str, context: dict, files: dict[str, bytes], templates: dict[str, str]) -> dict:
    hashes = {name: digest(data) for name, data in files.items()}
    return {
        "schema_version": 1,
        "source": source,
        "source_fingerprint": digest(json.dumps(hashes, sort_keys=True).encode()),
        "context": context,
        "foundation_files": hashes,
        "project_bases": templates,
    }


def canonical_source(origin: Path, label: str, destination: Path, context: dict) -> str:
    if label.startswith(("https://", "git@")):
        return label
    return context["foundation_root"] if origin.resolve() == destination.resolve() else str(origin.resolve())


def initialize(project: Path, source: Path, source_label: str, context: dict) -> dict:
    project = project.resolve()
    if (project / STATE).exists():
        return {"status": "already initialized", "state": STATE}
    files = snapshot(source)
    destination = inside(project, context["foundation_root"])
    if destination == project or destination.is_relative_to(project / "agent-workflow-local"):
        raise ValueError("Foundation must have its own directory outside project-local configuration")
    source_label = canonical_source(source, source_label, destination, context)
    templates = project_templates(files, context)
    pending = {}
    for name, data in files.items():
        path = inside(destination, name)
        if path.exists() and path.read_bytes() != data:
            raise ValueError(f"Existing foundation differs: {path}; review it before initialization")
        if not path.exists():
            pending[path] = data
    for name, incoming in templates.items():
        path = inside(project, name)
        if path.exists():
            if name not in HOSTS.values():
                continue
            local = path.read_text()
            if START in local or END in local:
                raise ValueError(f"Existing managed startup block in {name}; adopt or merge it deliberately")
            incoming = local.rstrip() + "\n\n" + incoming
        pending[path] = incoming.encode()
    for agent in context["agents"]:
        path = inside(project, f"docs/collaboration-{agent}.md")
        if not path.exists():
            pending[path] = f"# Collaboration: {agent}\n".encode()
    for path, data in pending.items():
        write(path, data)
    state = state_data(source_label, context, files, templates)
    write(inside(project, STATE), (json.dumps(state, indent=2) + "\n").encode())
    return {"status": "initialized", "foundation": context["foundation_root"], "state": STATE}


def update(project: Path, source: Path, source_label: str, apply: bool = False, keep_local: tuple[str, ...] = ()) -> dict:
    project = project.resolve()
    state = json.loads(inside(project, STATE).read_text())
    if state.get("schema_version") != 1:
        raise ValueError("Unsupported consumer state")
    files = snapshot(source)
    context = state["context"]
    destination = inside(project, context["foundation_root"])
    source_label = canonical_source(source, source_label, destination, context)
    templates = project_templates(files, context)
    actions, conflicts, pending = [], [], {}
    for name in sorted(state["foundation_files"].keys() | files.keys()):
        path = inside(destination, name)
        key = "foundation/" + name
        local = path.read_bytes() if path.exists() else None
        incoming = files.get(name)
        baseline = state["foundation_files"].get(name)
        if local == incoming or (incoming is not None and digest(incoming) == baseline):
            continue
        if key in keep_local:
            actions.append({"path": key, "action": "keep local by explicit selection"})
        elif (local is None and baseline is None) or (local is not None and digest(local) == baseline):
            actions.append({"path": key, "action": "delete" if incoming is None else "replace"})
            pending[path] = incoming
        else:
            conflicts.append(key)
    for name in sorted(state["project_bases"].keys() | templates.keys()):
        path = inside(project, name)
        key = "project/" + name
        local = path.read_text() if path.exists() else None
        incoming, base = templates.get(name), state["project_bases"].get(name)
        if local == incoming or incoming == base:
            continue
        if key in keep_local:
            actions.append({"path": key, "action": "keep local by explicit selection"})
            continue
        merged = merge(base, local, incoming) if None not in (base, local, incoming) else incoming if local == base else None
        if merged is None and not (incoming is None and local == base):
            conflicts.append(key)
        else:
            actions.append({"path": key, "action": "delete" if merged is None else "merge"})
            pending[path] = None if merged is None else merged.encode()
    if apply and not conflicts:
        for path, data in pending.items():
            if data is None:
                path.unlink()
            else:
                write(path, data)
        write(inside(project, STATE), (json.dumps(state_data(source_label, context, files, templates), indent=2) + "\n").encode())
    return {"status": "conflict" if conflicts else "applied" if apply else "review", "actions": actions, "conflicts": conflicts}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest="command", required=True)
    export = commands.add_parser("export", help="Package only the distributable foundation")
    export.add_argument("--source", default=str(Path(__file__).resolve().parents[1]))
    export.add_argument("--output", type=Path, required=True)
    for name in ("init", "update"):
        command = commands.add_parser(name)
        command.add_argument("--project", type=Path, default=Path.cwd())
        command.add_argument("--source", help="Local foundation/repository path or explicit Git URL")
        if name == "init":
            command.add_argument("--project-name")
            command.add_argument("--foundation-path", default="agent-workflow-foundation")
            command.add_argument("--source-root", default="openspec/explorations")
            command.add_argument("--agents", default="codex")
            command.add_argument("--lead", default="codex")
        else:
            command.add_argument("--apply", action="store_true", help="Apply a reviewed conflict-free plan")
            command.add_argument("--keep-local", action="append", default=[], help="Explicitly retain a conflicting path shown in the plan")
    args = parser.parse_args()
    try:
        if args.command == "export":
            with source_tree(args.source, Path.cwd()) as origin:
                if args.output.resolve().is_relative_to(origin.resolve()):
                    raise ValueError("Export destination must be outside the foundation source")
                files = snapshot(origin)
                args.output.parent.mkdir(parents=True, exist_ok=True)
                with zipfile.ZipFile(args.output, "x", compression=zipfile.ZIP_DEFLATED) as archive:
                    for name, data in files.items():
                        archive.writestr("agent-workflow-foundation/" + name, data)
            print(json.dumps({"status": "exported", "output": str(args.output), "files": len(files)}))
            return 0
        project = args.project.resolve()
        if args.command == "init":
            agents = list(dict.fromkeys("gemini" if value.strip() == "agy" else value.strip() for value in args.agents.lower().split(",")))
            if not agents or any(agent not in HOSTS for agent in agents) or args.lead not in agents:
                raise ValueError("Choose codex/claude/gemini agents and a lead from that roster")
            source = args.source or str(Path(__file__).resolve().parents[1])
            inside(project, args.source_root)
            context = {"project_name": args.project_name or project.name, "foundation_root": args.foundation_path, "source_root": args.source_root, "agents": agents, "lead": args.lead, "consultants": ", ".join(agent for agent in agents if agent != args.lead) or "none", "today": date.today().isoformat()}
            with source_tree(source, Path.cwd()) as origin:
                result = initialize(project, origin, source, context)
        else:
            state = json.loads(inside(project, STATE).read_text())
            source = args.source or state["source"]
            with source_tree(source, Path.cwd() if args.source else project) as origin:
                result = update(project, origin, source, args.apply, tuple(args.keep_local))
        print(json.dumps(result, indent=2))
        return 2 if result.get("conflicts") else 0
    except (OSError, ValueError, KeyError, subprocess.SubprocessError) as exc:
        print(f"foundation: {exc}")
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
