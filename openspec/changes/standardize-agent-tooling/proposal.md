## Why

`agent-workflow` currently has shared rules, agent adapters, and file-based
project setup, but no common lifecycle for repository intelligence, minimal
implementation discipline, or compact command execution. Adding those
capabilities through the existing workflow makes Codex, Claude Code, and
agy/Antigravity more consistent without making any external tool mandatory.

## What Changes

- Add one shared policy for Ponytail, Graphify, and RTK with phase-specific
  routing and explicit precedence over tool preferences.
- Add a standard-library environment bootstrap and doctor command for detection,
  safe project configuration, Graphify indexing, verification, and warnings.
- Use upstream-supported installation and host-integration commands only behind
  explicit flags; preserve existing instruction files and continue after
  unsupported or failed optional integrations.
- Extend new-project templates, agent adapters, README, operations guidance,
  and tests.

## Capabilities

### New Capabilities

- `agent-tooling-environment`: shared capability policy, idempotent bootstrap,
  diagnostics, Graphify lifecycle, and graceful degradation for optional tools.

### Modified Capabilities

- None. The existing file-based workflow remains the source of truth; this
  change adds a capability rather than changing an existing requirement.

## Impact

Affected areas are `workflow/`, setup templates, agent adapter templates, a
new Python standard-library script, unit tests, operational documentation, and
the new-project OpenSpec change record. The bootstrap may write a marked block
to a downstream project's `AGENTS.md` and may invoke upstream CLIs only when
the user explicitly opts into installation or host-wide configuration.
