# Project Facts

Stable project-local facts for agents. Current task state belongs in `current-state.md`; durable product decisions belong in source-of-truth files.

## Paths

- Shared workflow repo: `../agent-workflow`
- Source-of-truth root: `[path]`
- Reference registry: `agent-workflow-local/references/reference.md`
- Collaboration bootstrap: `docs/collaboration.md`
- Collaboration format: `docs/collaboration-format.md`

## Roles

- Lead: `[agent]`
- Consultants: `[agent, agent]`
- Agent aliases: `agy` means `gemini` when Gemini is present in the project

## Stage Tracking

- Active stage is tracked in `agent-workflow-local/current-state.md`.
- Stage transitions follow `../agent-workflow/workflow/stages.md` unless a local rule explicitly overrides that gate.

## Source-Of-Truth Inventory

Active while `current-state.md` says the project is in `[stage]`:

- `[path/to/source-of-truth-file.md]`
