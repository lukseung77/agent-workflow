# Local Project Files

This file defines the generic shape of `agent-workflow-local/`. Keep project-specific facts, rules, current state, and per-agent assignments separate so agents can load only the context they need.

## File Map

- `agent-workflow-local/project-facts.md` - stable local facts: paths, roles, stage tracking, and source-of-truth inventory.
- `agent-workflow-local/rules.md` - project-specific workflow rules and explicit overrides.
- `agent-workflow-local/current-state.md` - compact restart snapshot: current stage, current artifact, next lead action, blockers, and update date.
- `agent-workflow-local/agent-workflow.md` - legacy shared override, read only if an existing project uses it; new shared overrides go in `rules.md`. Existing precedence remains supported.
- `agent-workflow-local/agent-workflow-{agent}.md` - per-agent assignment, current responsibility, and project-specific restrictions.
- `agent-workflow-local/references/reference.md` - external reference registry.
- `agent-workflow-local/references/markitdown/` - converted Markdown outputs for bulky external references.

## Placement Rules

- Keep stable paths, roles, stage tracking, and source-of-truth inventory in `project-facts.md`.
- Keep workflow rules in `rules.md` or focused future local rule files under `agent-workflow-local/`.
- Keep restart state, active blockers, and immediate next action in `current-state.md`.
- Keep collaboration history and traceability in `docs/collaboration-*.md`.
- Keep product decisions in the source-of-truth files listed in `project-facts.md`.

## Ownership Summary

- Shared workflow files: reusable stage, trigger, source-of-truth, review, sync, role, context, and anti-pattern rules.
- Shared per-agent files: generic role strengths, limits, review behavior, and tool-specific cautions.
- Project-local shared rules: project-specific overrides and guardrails.
- Project-local facts: repo paths, role assignments, stage tracking location, source-of-truth inventory, and reference registry location.
- Project-local per-agent files: current responsibility, project-specific restrictions, and local reading-order differences.
- Collaboration files: recommendations, gaps, review findings, reconciliation history, and traceable cross-agent communication.

## Override Style

When a project-local rule overrides a shared rule, state it explicitly:

- `Overrides shared rule: [short name]`
- `Reason: [project-specific need]`
- `Replacement: [the rule to follow here]`

Do not copy shared global rules into a project repository unless self-contained packaging is explicitly needed.
