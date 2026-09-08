---
name: multi-agent-coworking
description: Use when multiple AI agents collaborate on a project, especially during exploration, review, handoff, implementation, or upstream workflow governance.
---

# Multi-Agent Coworking

Use this skill when Codex, Claude, Gemini, or another agent collaborates with other AI agents through this workflow.

## Startup

Follow `workflow/rule-precedence.md`. Load the project bootstrap, local facts/rules/current-state when present, generated queue, one selected item, and focused source files.

Do not ask the user to restate project context when files can answer it.

## Authority

- Project phase authority: `workflow/role-boundaries.md` and `workflow/stages.md`
- Canonical upstream authority and user-agent suggestions: `workflow/master-governance.md`
- User-question escalation: `workflow/decision-protocol.md` and `workflow/question-model.md`

One agent leads each phase. Other agents consult unless the user explicitly reassigns ownership.

## Collaboration

- Message schema and queue behavior: `workflow/collaboration-format.md`
- Consultant review and lead consolidation: `workflow/review-cycle.md`
- Context, handoff, and archive hygiene: `workflow/context-management.md`
- External reference conversion: `workflow/markitdown.md`

Keep reusable policy in workflow files, project decisions in source-of-truth files, and project-specific overrides in `agent-workflow-local/`.
