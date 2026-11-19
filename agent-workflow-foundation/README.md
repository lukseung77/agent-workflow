# Agent Workflow Foundation

This directory is the distributable product. It contains reusable workflow
rules, project-local templates, first-party scripts and skills, and third-party
origin references. It contains no consuming project's operational state or
collaboration history and no vendored third-party implementations.

## Start

Use `templates/project-init.md` for guided setup and
`workflow/foundation-lifecycle.md` for install, customization, and update review.
Normal startup and focused rules are routed by `workflow/rule-precedence.md`.
A project uses its own `agent-workflow-local/`, host entry files, and `docs/`.

```sh
python3 scripts/foundation.py init --project PROJECT_PATH --source SOURCE --project-name NAME --agents codex --lead codex
python3 scripts/foundation.py update --project PROJECT_PATH --source SOURCE
python3 scripts/foundation.py update --project PROJECT_PATH --source SOURCE --apply
```

Commands above are invoked from this directory; from elsewhere use the actual
foundation script path. Python 3.9+ is required. Git is needed for Git sources
and automatic three-way merging; without it conflicting local edits stay
blocked for manual review. The foundation repository consumes these same tools.

## Third Parties

`third-party/origins.json` identifies optional capabilities and official sources.
Install only selected tools from current upstream instructions, then record the
actual versions and configuration in the consuming project's local inventory.
First-party workflow rules and scripts remain part of the foundation product.
