# Agent Common Rules

Shared bootstrap for every project agent. Keep this file short; detailed reusable rules belong in `<workflow-root>/workflow/`.

## Startup

Follow the read order and task routing in
`<workflow-root>/workflow/rule-precedence.md` for local context, active queues,
and focused source files.

Do not act from stale chat context when current project files are available.

## Operating Rules

- Use durable project files as source of truth.
- Touch only files your role authorizes under `<workflow-root>/workflow/role-boundaries.md`.
- As a consultant, report cleanup findings to the lead; an obvious fix does not grant write authority.
- Keep accepted product decisions in the source-of-truth files listed in `agent-workflow-local/project-facts.md`.
- Keep current restart state limited to `agent-workflow-local/current-state.md`.
- Classify missing information under `<workflow-root>/workflow/decision-protocol.md` before asking the user.
- Ask user questions one at a time under `<workflow-root>/workflow/question-model.md`.

Project-specific constraints belong in `agent-workflow-local/rules.md` or `agent-workflow-local/agent-workflow-[agent].md`.
