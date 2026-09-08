# Local Rules

Project-specific workflow rules. These rules supplement the shared workflow in `<workflow-root>/workflow/`, where `<workflow-root>` is recorded in `agent-workflow-local/project-facts.md`.

## Source-Of-Truth Hygiene

- Keep product decisions in the files listed in `project-facts.md`.
- Keep workflow rules in `rules.md` or focused future rule files under `agent-workflow-local/`.
- Keep restart state, active blockers, and immediate next action in `current-state.md`.
- Keep collaboration history and traceability in `docs/collaboration-*.md`.

## Optional Local Overrides

Add only project-specific rules here. When a local rule overrides a shared rule, state the shared rule name, the project-specific reason, and the replacement rule.
