# Local Project Files

The source templates are in `templates/agent-workflow-local/`. This file defines the generic shape of `agent-workflow-local/`. Keep project-specific facts, rules, current state, and per-agent assignments separate so agents can load only the context they need.

## File Map

- `agent-workflow-local/project-facts.md` - stable local facts: paths, authoritative roles/review lenses, stage tracking, and source-of-truth inventory.
- `agent-workflow-local/rules.md` - project-specific workflow rules and explicit overrides.
- `agent-workflow-local/current-state.md` - compact restart snapshot: current stage, current artifact, next lead action, blockers, and update date.
- `agent-workflow-local/agent-workflow-{agent}.md` - optional agent-specific restrictions; roles and review lenses remain in `project-facts.md`.
- `agent-workflow-local/references/reference.md` - external reference registry.
- `agent-workflow-local/references/markitdown/` - converted Markdown outputs for bulky external references.

## Placement Rules

- Keep stable paths, roles, stage tracking, and source-of-truth inventory in `project-facts.md`.
- Keep workflow rules in `rules.md` or focused future local rule files under `agent-workflow-local/`.
- Keep restart state, active blockers, and immediate next action in `current-state.md`.
- Keep collaboration history and traceability in `docs/collaboration-*.md`.
- Keep product decisions in the source-of-truth files listed in `project-facts.md`.

## Override Style

When a project-local rule overrides a shared rule, state it explicitly:

- `Overrides shared rule: [short name]`
- `Reason: [project-specific need]`
- `Replacement: [the rule to follow here]`

Do not copy shared global rules into a project repository unless self-contained packaging is explicitly needed.

## Foundation And Instance

The foundation is product source; this local directory is a consuming instance.
Use `workflow/foundation-lifecycle.md` to review and merge foundation/template
updates. Preserve local customizations. Keep installation baselines and tool
inventory out of normal startup reads; they are operational metadata.
