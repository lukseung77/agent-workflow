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

## Avoid

- silently overriding project-local rules with generic defaults
- treating consultant suggestions as accepted decisions without reconciliation
- expanding scope during implementation without a project-level decision path
