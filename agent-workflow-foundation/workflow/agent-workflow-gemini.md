# Agent Workflow - Gemini

Read the role and review lens in `agent-workflow-local/project-facts.md`.
`agent-workflow-local/agent-workflow-gemini.md`, when present, adds restrictions
within that role; it is not a second role assignment.
Shared authority and operating rules follow `workflow/rule-precedence.md`.

## Host Guidance

- Keep `GEMINI.md` as a short bootstrap. Link local skill directories when iterating on shared skills instead of copying prompt blocks.
- Use configured MCP servers and skills when they supply relevant context; report compact findings with source references.
- Follow `workflow/agent-tooling.md` for Gemini/agy and Antigravity integrations, and `workflow/markitdown.md` for bulky references when relevant.
