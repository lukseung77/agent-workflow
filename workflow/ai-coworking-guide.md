# AI Coworking Guide

This optional overview links to canonical rules; it does not define another
startup sequence or operating agreement. Project-specific facts belong in
`agent-workflow-local/project-facts.md`.

Start with `workflow/rule-precedence.md`, then `workflow/agent-workflow.md`.
Use their task routing to read only the rules needed for the current work:

- Authority and roles: `workflow/role-boundaries.md`.
- Durable decisions and file placement: `workflow/local-project-files.md`.
- Stage readiness and transitions: `workflow/stages.md`.
- Decision classification: `workflow/decision-protocol.md`.
- User questions: `workflow/question-model.md`.
- Consultant review and reconciliation: `workflow/review-cycle.md`.
- Restart and focused context: `workflow/context-management.md`.

Shared files carry work and decisions but do not automatically start other
agents. The human starts or resumes an agent session; that agent reads its
active queue and selected request. Do not assume an agent has seen a file update
until it responds. A short session trigger can be: "Read your active queue and
continue the addressed request."
