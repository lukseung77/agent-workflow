#!/usr/bin/env python3
"""Initialize and inspect optional agent-workflow tooling.

The command intentionally uses only the Python standard library. Package
installation and host-wide configuration are opt-in because both can change
user-owned state. Tool-specific files and hooks remain owned by the upstream
tool; this script only calls documented commands and maintains one small,
marked repository adapter block.
"""

from __future__ import annotations

import argparse
import json
import re
import shutil
import subprocess
import sys
from datetime import datetime, timezone
from dataclasses import dataclass, field
from pathlib import Path
from typing import Callable, Iterable, Sequence


ORIGINS = json.loads((Path(__file__).resolve().parents[1] / "third-party/origins.json").read_text())["tools"]
PONYTAIL_URL = ORIGINS["ponytail"]["origin"]
PONYTAIL_REPO = PONYTAIL_URL.removeprefix("https://github.com/")
GRAPHIFY_PACKAGE = ORIGINS["graphify"]["package"]
RTK_REPO = ORIGINS["rtk"]["origin"]
COMMAND_TIMEOUT_SECONDS = 300
ADAPTER_START = "<!-- agent-workflow:tooling:start -->"
ADAPTER_END = "<!-- agent-workflow:tooling:end -->"

KNOWN_AGENTS = ("codex", "claude", "agy", "antigravity")
AGENT_LABELS = {
    "codex": "Codex",
    "claude": "Claude Code",
    "agy": "agy / Gemini",
    "antigravity": "Antigravity",
}


@dataclass
class CommandResult:
    returncode: int
    stdout: str = ""
    stderr: str = ""


class SubprocessRunner:
    def run(self, command: Sequence[str], cwd: Path) -> CommandResult:
        result = subprocess.run(
            list(command),
            cwd=str(cwd),
            text=True,
            capture_output=True,
            check=False,
            timeout=COMMAND_TIMEOUT_SECONDS,
        )
        return CommandResult(result.returncode, result.stdout, result.stderr)


@dataclass
class EnvironmentReport:
    agents: dict[str, bool] = field(default_factory=dict)
    tools: dict[str, bool] = field(default_factory=dict)
    graph_index: bool = False
    warnings: list[str] = field(default_factory=list)
    actions: list[str] = field(default_factory=list)
    versions: dict[str, str] = field(default_factory=dict)
    _command_attempts: int = field(default=0, init=False, repr=False)

    def as_dict(self) -> dict[str, object]:
        return {
            "agents": self.agents,
            "tools": self.tools,
            "graph_index": self.graph_index,
            "warnings": self.warnings,
            "actions": self.actions,
            "versions": self.versions,
        }


def _run(
    runner: SubprocessRunner,
    command: Sequence[str],
    root: Path,
    report: EnvironmentReport,
    description: str,
    version_key: str | None = None,
) -> bool:
    report._command_attempts += 1
    try:
        result = runner.run(command, root)
    except (OSError, subprocess.TimeoutExpired) as exc:
        report.warnings.append(f"{description} failed ({exc})")
        return False
    if result.returncode == 0:
        if version_key and result.stdout.strip():
            report.versions[version_key] = result.stdout.strip()
        action = f"{description}: ok"
        if action not in report.actions:
            report.actions.append(action)
        return True
    detail = result.stderr.strip() or result.stdout.strip()
    suffix = f" ({detail[-240:]})" if detail else ""
    report.warnings.append(f"{description} failed{suffix}")
    return False


def _command_available(name: str, which: Callable[[str], str | None]) -> bool:
    return which(name) is not None


def _agent_detected(
    agent: str,
    root: Path,
    which: Callable[[str], str | None],
) -> bool:
    if agent == "codex":
        return _command_available("codex", which) or (root / ".codex").exists()
    if agent == "claude":
        return _command_available("claude", which) or (root / ".claude").exists()
    if agent == "agy":
        return (
            _command_available("agy", which)
            or _command_available("gemini", which)
            or (root / ".gemini").exists()
        )
    return _command_available("antigravity", which)


def normalize_agents(
    requested: str | None,
    root: Path,
    which: Callable[[str], str | None],
) -> list[str]:
    if requested and requested.lower() not in {"auto", "detect"}:
        values = [value.strip().lower() for value in requested.split(",")]
        result: list[str] = []
        for value in values:
            if value == "gemini":
                value = "agy"
            if value not in KNOWN_AGENTS:
                raise ValueError(
                    f"unknown agent '{value}'; choose from {', '.join(KNOWN_AGENTS)}"
                )
            if value not in result:
                result.append(value)
        return result

    detected: list[str] = []
    if _agent_detected("codex", root, which):
        detected.append("codex")
    if _agent_detected("claude", root, which):
        detected.append("claude")
    if _agent_detected("agy", root, which):
        detected.append("agy")
    # Antigravity has no required CLI. Its project adapter is selected
    # explicitly, so an existing .agents directory is not mistaken for the
    # application itself.
    return detected


def _graph_index_exists(root: Path) -> bool:
    return any(
        (root / candidate).is_file()
        for candidate in ("graphify-out/graph.json", "graph.json")
    )


def _graphify_adapter_exists(root: Path, agent: str) -> bool:
    candidates = {
        "codex": (root / ".codex/skills/graphify/SKILL.md",),
        "claude": (root / ".claude/skills/graphify/SKILL.md",),
        "agy": (
            root / ".gemini/skills/graphify/SKILL.md",
            root / ".gemini/commands/graphify.toml",
        ),
        "antigravity": (
            root / ".agents/skills/graphify/SKILL.md",
            root / ".agents/rules/graphify.md",
        ),
    }
    return any(path.is_file() for path in candidates.get(agent, ()))


def _rtk_adapter_exists(root: Path, agent: str) -> bool:
    # A local RTK.md does not prove that agent-wide hooks are configured.
    return agent == "antigravity" and (root / ".agents/rules/antigravity-rtk-rules.md").is_file()


def _adapter_span(content: str) -> tuple[int, int] | None:
    if ADAPTER_START not in content and ADAPTER_END not in content:
        return None
    if content.count(ADAPTER_START) != 1 or content.count(ADAPTER_END) != 1:
        raise ValueError("AGENTS.md has malformed tooling markers; repair the managed block first")
    start = content.index(ADAPTER_START)
    end = content.index(ADAPTER_END) + len(ADAPTER_END)
    if end < start:
        raise ValueError("AGENTS.md has reversed tooling markers")
    return start, end


def ensure_repository_adapter(root: Path, workflow_root: str) -> bool:
    """Add the shared-rule pointer once without overwriting AGENTS.md."""

    path = root / "AGENTS.md"
    if path.exists():
        content = path.read_text(encoding="utf-8")
    else:
        content = ""
    block = f"""{ADAPTER_START}
## Agent Workflow Tooling

Read `{workflow_root}/workflow/tooling.md` when repository discovery,
implementation, validation, or verbose CLI execution needs tool guidance.
This is a thin adapter; the selected template, explicit project requirements, correctness,
security, and tests take precedence.
{ADAPTER_END}
"""
    span = _adapter_span(content)
    if span is not None:
        start, end = span
        updated = content[:start] + block.rstrip("\n") + content[end:]
        if updated == content:
            return False
        path.write_text(updated, encoding="utf-8")
        return True
    separator = "\n" if content and not content.endswith("\n") else ""
    path.write_text(content + separator + ("\n" if content else "") + block, encoding="utf-8")
    return True


def verify_tools(
    root: Path,
    runner: SubprocessRunner,
    which: Callable[[str], str | None],
    report: EnvironmentReport,
) -> None:
    agents_file = root / "AGENTS.md"
    content = agents_file.read_text(encoding="utf-8") if agents_file.is_file() else ""
    try:
        report.tools["ponytail"] = _adapter_span(content) is not None
    except ValueError as exc:
        report.tools["ponytail"] = False
        report.warnings.append(str(exc))

    graphify_ok = _command_available("graphify", which)
    if graphify_ok:
        graphify_ok = _run(runner, ["graphify", "--version"], root, report, "Graphify version check", version_key="graphify")
    report.tools["graphify"] = graphify_ok
    report.graph_index = _graph_index_exists(root)

    rtk_ok = _command_available("rtk", which)
    if rtk_ok:
        rtk_ok = _run(runner, ["rtk", "gain"], root, report, "RTK verification")
    report.tools["rtk"] = rtk_ok


def install_missing_tools(
    root: Path,
    runner: SubprocessRunner,
    which: Callable[[str], str | None],
    report: EnvironmentReport,
    graphify_version: str | None = None,
    rtk_revision: str | None = None,
) -> None:
    """Install only with explicit --install-missing approval.

    The commands are the upstream package/repository mechanisms. No remote
    shell script is piped into a shell.
    """

    graphify_package = f"{GRAPHIFY_PACKAGE}=={graphify_version}" if graphify_version else GRAPHIFY_PACKAGE
    if not report.tools.get("graphify", False):
        if _command_available("uv", which):
            installed = _run(runner, ["uv", "tool", "install", graphify_package], root, report, "Graphify installation")
            report.tools["graphify"] = installed and _command_available("graphify", which)
        elif _command_available("pipx", which):
            installed = _run(runner, ["pipx", "install", graphify_package], root, report, "Graphify installation")
            report.tools["graphify"] = installed and _command_available("graphify", which)
        else:
            report.warnings.append(
                "Graphify is missing; install graphifyy with uv or pipx, then rerun initialization"
            )

    if not report.tools.get("rtk", False):
        if _command_available("cargo", which):
            command = ["cargo", "install", "--git", RTK_REPO]
            if rtk_revision:
                command += ["--rev", rtk_revision]
            else:
                try:
                    tags = runner.run(["git", "ls-remote", "--tags", "--refs", RTK_REPO], root)
                    stable = []
                    for line in tags.stdout.splitlines() if tags.returncode == 0 else []:
                        match = re.search(r"refs/tags/(v?(\d+)\.(\d+)\.(\d+))$", line)
                        if match:
                            stable.append((tuple(map(int, match.groups()[1:])), match[1]))
                    if not stable:
                        report.warnings.append("RTK stable release could not be resolved; review its official origin or pass --rtk-revision")
                        return
                    tag = max(stable)[1]
                    command += ["--tag", tag]
                    report.actions.append(f"RTK selected stable release: {tag}")
                except (OSError, subprocess.TimeoutExpired) as exc:
                    report.warnings.append(f"RTK release lookup failed ({exc}); review its official origin")
                    return
            installed = _run(runner, command, root, report, "RTK installation")
            report.tools["rtk"] = installed and _command_available("rtk", which)
        else:
            report.warnings.append(
                "RTK is missing and cargo is unavailable; install Rust/cargo, then rerun initialization"
            )


def configure_graphify(
    root: Path,
    agents: Iterable[str],
    runner: SubprocessRunner,
    report: EnvironmentReport,
) -> None:
    for agent in agents:
        if _graphify_adapter_exists(root, agent):
            continue
        if agent == "claude":
            command = ["graphify", "install", "--project"]
        elif agent == "codex":
            command = ["graphify", "install", "--project", "--platform", "codex"]
        elif agent == "agy":
            command = ["graphify", "install", "--project", "--platform", "gemini"]
        else:
            command = ["graphify", "antigravity", "install"]
        _run(runner, command, root, report, f"Graphify {AGENT_LABELS[agent]} adapter")


def initialize_graph(
    root: Path,
    runner: SubprocessRunner,
    report: EnvironmentReport,
) -> None:
    if not report.tools.get("graphify", False):
        report.warnings.append("Graphify unavailable; using targeted source inspection")
        return
    command = ["graphify", "update", "."] if report.graph_index else ["graphify", "."]
    if _run(runner, command, root, report, "Graphify repository index"):
        report.graph_index = _graph_index_exists(root)
        if not report.graph_index:
            report.warnings.append(
                "Graphify command succeeded but graphify-out/graph.json was not found; verify the CLI output"
            )


def configure_ponytail(
    root: Path,
    agents: Iterable[str],
    runner: SubprocessRunner,
    report: EnvironmentReport,
    configure_hosts: bool,
) -> None:
    if not configure_hosts:
        for agent in agents:
            if agent == "claude":
                report.warnings.append(
                    "Ponytail Claude Code plugin not changed; run its two official /plugin commands if desired"
                )
            elif agent == "codex":
                report.warnings.append(
                    "Ponytail Codex plugin not changed; rerun with --configure-hosts to use the official plugin commands"
                )
            elif agent == "agy":
                report.warnings.append(
                    "Ponytail Gemini/agy extension not changed; rerun with --configure-hosts if desired"
                )
        return

    for agent in agents:
        if agent == "codex":
            _run(
                runner,
                ["codex", "plugin", "marketplace", "add", PONYTAIL_REPO],
                root,
                report,
                "Ponytail Codex marketplace",
            )
            _run(
                runner,
                ["codex", "plugin", "add", "ponytail@ponytail"],
                root,
                report,
                "Ponytail Codex plugin",
            )
        elif agent == "agy":
            _run(
                runner,
                ["gemini", "extensions", "install", PONYTAIL_URL],
                root,
                report,
                "Ponytail Gemini extension",
            )
        elif agent == "claude":
            report.warnings.append(
                "Ponytail Claude Code requires the official interactive /plugin marketplace and install prompts"
            )
        elif agent == "antigravity":
            report.actions.append("Ponytail Antigravity adapter: shared AGENTS.md rules")


def configure_rtk(
    root: Path,
    agents: Iterable[str],
    runner: SubprocessRunner,
    report: EnvironmentReport,
    configure_hosts: bool,
) -> None:
    if not report.tools.get("rtk", False):
        report.warnings.append("RTK unavailable; normal CLI execution remains enabled")
        return
    if not configure_hosts:
        report.warnings.append(
            "RTK host hooks were not changed; rerun with --configure-hosts to use official agent adapters"
        )
        return

    for agent in agents:
        if agent == "claude":
            command = ["rtk", "init", "--global"]
        elif agent == "codex":
            command = ["rtk", "init", "--global", "--codex"]
        elif agent == "agy":
            command = ["rtk", "init", "--global", "--gemini"]
        else:
            command = ["rtk", "init", "--agent", "antigravity"]
        if _rtk_adapter_exists(root, agent):
            continue
        _run(runner, command, root, report, f"RTK {AGENT_LABELS[agent]} adapter")


def initialize(
    root: Path,
    workflow_root: str,
    agents: list[str],
    install_missing: bool = False,
    configure_hosts: bool = False,
    runner: SubprocessRunner | None = None,
    which: Callable[[str], str | None] = shutil.which,
    graphify_version: str | None = None,
    rtk_revision: str | None = None,
) -> EnvironmentReport:
    runner = runner or SubprocessRunner()
    report = EnvironmentReport(
        agents={agent: _agent_detected(agent, root, which) for agent in agents}
    )

    if ensure_repository_adapter(root, workflow_root):
        report.actions.append("shared AGENTS.md adapter: created or updated")
    else:
        report.actions.append("shared AGENTS.md adapter: already present")

    verify_tools(root, runner, which, report)
    verified_attempts = report._command_attempts
    if install_missing:
        install_missing_tools(root, runner, which, report, graphify_version, rtk_revision)

    if report.tools.get("graphify", False):
        configure_graphify(root, agents, runner, report)
    else:
        report.warnings.append("Graphify adapters skipped because the CLI is unavailable")
    configure_ponytail(root, agents, runner, report, configure_hosts)
    initialize_graph(root, runner, report)
    configure_rtk(root, agents, runner, report, configure_hosts)
    # Only re-probe after an install, adapter, or indexing command actually ran.
    if report._command_attempts > verified_attempts:
        verify_tools(root, runner, which, report)
    record_inventory(root, runner, report)
    return report


def record_inventory(root: Path, runner: SubprocessRunner, report: EnvironmentReport) -> None:
    """Keep verified tool provenance in the consumer, never in product source."""
    path = root / "agent-workflow-local/tooling.json"
    try:
        if not path.resolve().is_relative_to(root.resolve()):
            raise ValueError("Tool inventory must stay inside the consuming project")
        inventory = json.loads(path.read_text()) if path.exists() else {"tools": {}}
        tools = inventory.setdefault("tools", {})
        if report.tools.get("rtk"):
            _run(runner, ORIGINS["rtk"]["verification"], root, report, "RTK installed version", version_key="rtk")
        for name in ("graphify", "rtk"):
            entry = tools.setdefault(name, {})
            entry.update({"origin": ORIGINS[name]["origin"], "available": report.tools.get(name, False), "checked_at": datetime.now(timezone.utc).isoformat()})
            entry.setdefault("version", None)
            if name in report.versions:
                entry["version"] = report.versions[name]
        entry = tools.setdefault("ponytail", {})
        entry.update({"origin": PONYTAIL_URL, "shared_adapter": report.tools.get("ponytail", False)})
        entry.setdefault("native_state", "unknown")
        entry.setdefault("version", None)
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(json.dumps(inventory, indent=2) + "\n")
    except (OSError, ValueError, TypeError, AttributeError) as exc:
        report.warnings.append(f"Tool inventory not updated: {exc}")


def doctor(
    root: Path,
    agents: list[str],
    runner: SubprocessRunner | None = None,
    which: Callable[[str], str | None] = shutil.which,
) -> EnvironmentReport:
    runner = runner or SubprocessRunner()
    report = EnvironmentReport(
        agents={agent: _agent_detected(agent, root, which) for agent in agents}
    )
    verify_tools(root, runner, which, report)
    return report


def print_report(report: EnvironmentReport) -> None:
    def mark(value: bool) -> str:
        return "✓" if value else "!"

    print("Agent Workflow Environment")
    for agent in KNOWN_AGENTS:
        state = mark(report.agents[agent]) if agent in report.agents else "not checked"
        print(f"  {AGENT_LABELS[agent]:<16} {state}")
    print(f"  {'Shared adapter':<16} {mark(report.tools.get('ponytail', False))}")
    print("  Ponytail plugin  unknown (not inspected)")
    print(f"  {'Graphify':<16} {mark(report.tools.get('graphify', False))}")
    print(f"  {'Graphify index':<16} {mark(report.graph_index)}")
    print(f"  {'RTK':<16} {mark(report.tools.get('rtk', False))}")
    for action in report.actions:
        print(f"  action: {action}")
    for warning in report.warnings:
        print(f"  warning: {warning}", file=sys.stderr)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    subparsers = parser.add_subparsers(dest="command", required=True)

    init = subparsers.add_parser("init", help="detect, configure, index, and verify")
    init.add_argument("--root", type=Path, default=Path.cwd())
    init.add_argument("--foundation-root", "--workflow-root", dest="workflow_root", default="./agent-workflow-foundation")
    init.add_argument("--agents", default="auto", help="comma-separated: codex,claude,agy,antigravity")
    init.add_argument(
        "--install-missing",
        action="store_true",
        help="explicitly permit official package/repository installation",
    )
    init.add_argument(
        "--configure-hosts",
        action="store_true",
        help="explicitly permit agent-wide hooks/plugins; project adapters remain safe by default",
    )
    init.add_argument("--json", action="store_true")
    init.add_argument("--graphify-version", help="Graphify version used only with --install-missing")
    init.add_argument("--rtk-revision", help="RTK Git revision used only with --install-missing")

    check = subparsers.add_parser("doctor", help="verify the environment without writing")
    check.add_argument("--root", type=Path, default=Path.cwd())
    check.add_argument("--agents", default="auto")
    check.add_argument("--json", action="store_true")
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    root = args.root.resolve()
    try:
        agents = normalize_agents(args.agents, root, shutil.which)
        if args.command == "init":
            report = initialize(
                root,
                args.workflow_root,
                agents,
                install_missing=args.install_missing,
                configure_hosts=args.configure_hosts,
                which=shutil.which,
                graphify_version=args.graphify_version,
                rtk_revision=args.rtk_revision,
            )
        else:
            report = doctor(root, agents, which=shutil.which)
    except (OSError, ValueError) as exc:
        print(f"agent-workflow environment error: {exc}", file=sys.stderr)
        return 2

    if args.json:
        print(json.dumps(report.as_dict(), indent=2, sort_keys=True))
    else:
        print_report(report)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
