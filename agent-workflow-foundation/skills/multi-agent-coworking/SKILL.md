---
name: multi-agent-coworking
description: Use when multiple AI agents collaborate on a project, especially during exploration, review, handoff, implementation, or upstream workflow governance.
---

# Multi-Agent Coworking

Use this skill when Codex, Claude, Gemini, or another agent collaborates with other AI agents through this workflow.

## Startup

Resolve `<foundation-root>` from the host entry file or project facts. Project
state paths are relative to the consuming project, including this source repository.

Follow `<foundation-root>/workflow/rule-precedence.md`. Load the project bootstrap, local facts/rules/current-state when present, generated queue, one selected item, and focused source files. Use task routing there before loading topic rules.

Do not ask the user to restate project context when files can answer it.

## Authority

- Project phase authority: `<foundation-root>/workflow/role-boundaries.md` and `<foundation-root>/workflow/stages.md`
- Foundation installation and updates: `<foundation-root>/workflow/foundation-lifecycle.md`; upstream feedback: `<foundation-root>/workflow/upstream-feedback.md`
- User-question escalation: `<foundation-root>/workflow/decision-protocol.md` and `<foundation-root>/workflow/question-model.md`

One agent leads each phase. Other agents consult unless the user explicitly reassigns ownership.

## Collaboration

- Message schema and queue behavior: `<foundation-root>/workflow/collaboration-format.md`
- Consultant review and lead consolidation: `<foundation-root>/workflow/review-cycle.md`
- Context, handoff, and archive hygiene: `<foundation-root>/workflow/context-management.md`
- External reference conversion: `<foundation-root>/workflow/markitdown.md`

Keep reusable policy in workflow files, project decisions in source-of-truth files, and project-specific overrides in `agent-workflow-local/`.
