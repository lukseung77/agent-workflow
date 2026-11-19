# [Project Name] — Codex Instructions

Read `agent-common.md` when present. Follow startup and task routing in `<workflow-root>/workflow/rule-precedence.md`.
`<workflow-root>` is usually `../agent-workflow` or `./agent-workflow`.

## Assignment

- Role and current responsibility: `agent-workflow-local/agent-workflow-codex.md`
- Agent roster, review lens, and source-of-truth inventory: `agent-workflow-local/project-facts.md`
- Collaboration file: `docs/collaboration-codex.md`
- Queue: `python3 <workflow-root>/scripts/collab_queue.py codex`
- Message prefix: `CX` (for example, `CX-001`)

## Project State And Rules

Read `agent-workflow-local/current-state.md` for the active stage and next action.
Project constraints belong in `agent-workflow-local/rules.md`; Codex-specific
assignments or restrictions belong in its local assignment file above.
