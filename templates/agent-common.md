# Agent Common Rules

Shared bootstrap for every project agent. Keep this file short; detailed reusable rules belong in `<workflow-root>/workflow/`.

## Startup

1. Follow `<workflow-root>/workflow/rule-precedence.md`.
2. Generate your active queue when scripts are available.
3. Load one selected item and its focused source files.
4. Use the task-routing table in `<workflow-root>/workflow/rule-precedence.md` to load only the topic rules the task needs.

Do not act from stale chat context when current project files are available.

## Operating Rules

- Use durable project files as source of truth.
- Touch only files your role authorizes under `<workflow-root>/workflow/role-boundaries.md`.
- Keep accepted product decisions in the source-of-truth inventory recorded in `agent-workflow-local/project-facts.md`.
- Keep current restart state limited to `agent-workflow-local/current-state.md`.
- Classify missing information under `<workflow-root>/workflow/decision-protocol.md` before asking the user.
- Ask user questions one at a time under `<workflow-root>/workflow/question-model.md`.

## Routing

- Collaboration schema and queues: `<workflow-root>/workflow/collaboration-format.md`
- Review consolidation: `<workflow-root>/workflow/review-cycle.md`
- Stage gates: `<workflow-root>/workflow/stages.md`
- Context and handoff: `<workflow-root>/workflow/context-management.md`
- External references: `<workflow-root>/workflow/markitdown.md`
- Local placement rules: `<workflow-root>/workflow/local-project-files.md`
- Defined terms: `<workflow-root>/workflow/defined-terms.md`

Project-specific constraints belong in `agent-workflow-local/rules.md` or `agent-workflow-local/agent-workflow-[agent].md`.
