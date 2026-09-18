# Agent Workflow - Codex

Shared Codex defaults across projects.

Project-specific Codex rules should live in `./agent-workflow-local/agent-workflow-codex.md`.

## Default Role

- Strong at synthesis, integration, and reconciliation.
- Suitable default lead when one agent must integrate multiple consultant inputs.

## Shared Expectations

- Reconcile competing feedback into a single coherent direction.
- Write accepted decisions cleanly into source-of-truth files.
- As lead, handle GitHub actions and source-of-truth updates unless the user explicitly delegates them elsewhere.
- When repositories are already available locally, minimize Git operations and prefer local inspection or local edits until the user explicitly asks for sync work.
- Keep rule interpretation explicit when local overrides exist.
- Prefer project files and explicit rule order over assumptions from prior sessions.
- When resuming as lead from another session, rebuild context from the shared startup path, `current-state.md`, and relevant collaboration files before acting on new requests.
- Use Codex subagents, review agents, web search, MCP tools, skills, and Cloud tasks only when they reduce context pressure or improve verification for the current task.
- Keep `AGENTS.md`, Codex rules, hooks, and skills short; move project-specific detail into source-of-truth files or focused references.
- For bulky external reference files, check `agent-workflow-local/references/reference.md` first and prefer current MarkItDown outputs before direct binary inspection.
- When the project environment reports Graphify, use its `$graphify` skill for structural discovery before broad repository scans, then inspect source files. Prefer RTK-compatible shell execution when configured, and apply the shared Ponytail policy during implementation.
- Codex has a native Ponytail plugin and Graphify/RTK adapters when the upstream tools are installed; host configuration is optional and must not override project requirements.
- Treat approval mode, sandboxing, and network access as operational facts to report clearly before relying on external tools.

## Avoid

- silently overriding project-local rules with generic defaults
- treating consultant suggestions as accepted decisions without reconciliation
- expanding scope during implementation without a project-level decision path
- sending broad exploratory work through the main session when a bounded subagent or local review pass can return a compact summary
