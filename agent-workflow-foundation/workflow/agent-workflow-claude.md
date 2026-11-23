# Agent Workflow - Claude

Read the role and review lens in `agent-workflow-local/project-facts.md`.
`agent-workflow-local/agent-workflow-claude.md`, when present, adds restrictions
within that role; it is not a second role assignment.
Shared authority and operating rules follow `workflow/rule-precedence.md`.

## Host Guidance

- Keep `CLAUDE.md` as a short bootstrap; use skills for reusable procedures and project files for decisions.
- Use foreground subagents for dependent work and background subagents for independent work when delegation is authorized; request compact findings with file references.
- Keep hook, plugin, and subagent behavior visible in project-local settings when it affects collaboration or verification. Their output remains input for lead reconciliation.
- Follow `workflow/tooling.md` for configured Graphify, Ponytail, and RTK integrations.
- For bulky references, follow `workflow/markitdown.md`; use direct PDF/image inspection when conversion omits decision-relevant content.
