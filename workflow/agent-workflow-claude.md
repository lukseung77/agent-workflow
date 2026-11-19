# Agent Workflow - Claude

Read the role, responsibility, and review lens in
`agent-workflow-local/agent-workflow-claude.md` and
`agent-workflow-local/project-facts.md` when present.
Shared authority and operating rules follow `workflow/rule-precedence.md`.
In the canonical repository, `workflow/master-governance.md` governs writes.

## Host Guidance

- Keep `CLAUDE.md` as a short bootstrap; use skills for reusable procedures and project files for decisions.
- Use foreground subagents for dependent work and background subagents for independent work when delegation is authorized; request compact findings with file references.
- Keep hook, plugin, and subagent behavior visible in project-local settings when it affects collaboration or verification. Their output remains input for lead reconciliation.
- Follow `workflow/agent-tooling.md` for configured Graphify, Ponytail, and RTK integrations.
- For bulky references, follow `workflow/markitdown.md`; use direct PDF/image inspection when conversion omits decision-relevant content.
