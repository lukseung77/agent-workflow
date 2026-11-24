# Project Stages And Gates

The core defines communication and decision recording, not a universal project
process. Resolve the selected workflow from
`agent-workflow-local/project-template.json`; its `workflow` path is relative to
the project root. Follow that template's stages, acceptance criteria, reviewer
requirements, and transition approvals, subject to explicit local overrides.
`Setup` and `Complete` are administrative bookends shared by all templates.

Communicate readiness, questions, review requests, decisions, and handoffs using
the core collaboration format. Record actual transitions and their evidence in
collaboration files and update the restart snapshot. Do not infer concurrence,
approval, capability availability, or completion from silence or file transfer.
Use `workflow/review-cycle.md` when a template or project calls for review; that
protocol does not impose the SW template's gates on other project types.

For an existing consumer without a selected template, retain its local process
and gates. `workflow/legacy-stages.md` preserves the former defaults only for
such consumers. Updating the foundation does not select a project type, reset
the current stage, or authorize migration to another workflow. New setup must
ask for a project type and a template before initialization.
