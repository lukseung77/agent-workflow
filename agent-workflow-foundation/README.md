# Agent Workflow Foundation

This directory is the distributable product. It contains reusable workflow
rules, project-local templates, first-party scripts and skills, and third-party
origin references. It contains no consuming project's operational state or
collaboration history and no vendored third-party implementations.

## Start

Use `templates/new-project-setup.md` for guided setup and
`workflow/foundation-lifecycle.md` for install, customization, and update review.
Normal startup and focused rules are routed by `workflow/rule-precedence.md`.
A project uses its own `agent-workflow-local/`, host entry files, and `docs/`.

Python 3.9+ is required. Git supports remote sources and three-way merges.
Use the linked setup and lifecycle guides for commands. Existing consumers
upgrading from the old layout follow `workflow/migration.md`; new projects use
only the current setup.

## Third Parties

`third-party/origins.json` is the capability catalog. `workflow/tooling.md` owns
selection and lifecycle policy and routes the focused adapters in `guides/`.
Freshness review timing and evidence are defined in `workflow/tooling-review.md`.
No third-party implementation or consuming project's installation evidence is
bundled.
