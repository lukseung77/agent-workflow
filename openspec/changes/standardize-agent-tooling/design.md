## Context

The project is a file-based multi-agent workflow. Shared policy belongs in
`workflow/`, agent-specific files are thin adapters, and new projects are
initialized from templates. There is no existing executable setup or doctor
command. The three requested tools have different upstream interfaces: Ponytail
is primarily a rules/plugin distribution, Graphify is a Python CLI with
project-scoped skills and a repository graph, and RTK is a Rust CLI with
agent-specific hooks or instruction adapters.

## Goals / Non-Goals

**Goals:**

- Keep one semantic rule source and map it onto the current three-stage
  workflow plus validation/review activities.
- Make project initialization safe, repeatable, diagnosable, and useful when
  any optional tool or agent is absent.
- Preserve existing user instructions and avoid network access in unit tests.
- Use official upstream commands rather than invented installers.

**Non-Goals:**

- Replacing the existing collaboration queue, stage gates, or role model.
- Making external tools hard requirements for normal development.
- Maintaining a second persistent tool-configuration database.
- Silently changing global agent hooks, plugins, or user package installations.

## Decisions

1. **One shared policy with thin adapters.** `workflow/agent-tooling.md` owns
   capability semantics, precedence, phase routing, refresh behavior, and
   fallback behavior. Codex, Claude, and Gemini/agy files only describe host
   differences. This follows the existing rule-precedence architecture and
   avoids semantic drift.

2. **A standard-library Python command owns lifecycle orchestration.**
   `scripts/agent_workflow_env.py` detects tools with `PATH` and lightweight
   verification commands, writes one marked `AGENTS.md` pointer, invokes
   project-scoped upstream adapters, initializes or incrementally updates
   Graphify, and prints a doctor report. A small command runner seam makes
   external operations mockable in tests.

3. **Installation and host-wide configuration are explicit.** Plain `init`
   performs safe project setup and reports manual/global actions. `--install-missing`
   enables `uv`/`pipx`/Cargo installation, while `--configure-hosts` enables
   native agent hooks/plugins. No remote script is piped into a shell.

4. **Graphify owns its graph files and adapters.** The bootstrap calls
   `graphify .` only when no known index exists, then `graphify update .` on
   later runs. Generated skills, hooks, and index files are not reimplemented
   by agent-workflow.

5. **RTK verification uses `rtk gain`.** The name collision with another
   `rtk` package makes version-only detection insufficient. Failed verification
   remains a warning and normal commands remain available.

6. **Ponytail has an instruction fallback.** Native Codex/Claude/Gemini
   integration is delegated to upstream commands where automation is supported.
   Antigravity and unsupported hosts receive the shared `AGENTS.md` pointer;
   the equivalent minimalism policy remains active without a plugin.

## Risks / Trade-offs

- [Upstream CLIs change their generated paths or flags] → Keep commands and
  compatibility notes in one script/docs location, treat failed optional steps
  as warnings, and verify expected Graphify/RTK artifacts.
- [A user mistakes a wrong `rtk` package for Rust Token Killer] → Require
  `rtk gain` verification and explain the collision in troubleshooting.
- [A managed pointer conflicts with project instructions] → Append only a
  clearly marked block and never replace existing `AGENTS.md` content.
- [Graph index is stale] → Declare source authoritative, expose `graphify
  update .`, and allow normal targeted inspection when Graphify is unavailable.
- [Global hook setup affects unrelated projects] → Require the separate
  `--configure-hosts` opt-in and report the exact unsupported/manual cases.

## Migration Plan

Existing downstream projects need no migration. On the next setup run, the
environment command adds the marked adapter only if absent. Users can run the
doctor command to inspect availability, then explicitly opt into installation
or host configuration. Removing the marked adapter and upstream-generated
files is the rollback path; normal workflow files remain usable without them.

## Open Questions

None for this implementation. Native host behavior remains subject to the
upstream tools' current commands and is reported when a host cannot be
automated.
