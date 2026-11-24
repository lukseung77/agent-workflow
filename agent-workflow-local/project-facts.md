# Project Facts

## Identity And Paths

- Project: agent-workflow
- Project type: Existing project (type not selected)
- Project template: `legacy-unselected`
- Selected workflow and requirements: `agent-workflow-local/project-template.json`
- Foundation root: `agent-workflow-foundation`
- Source-of-truth root: `agent-workflow-foundation`
- Reference registry: `agent-workflow-local/references/reference.md`
- Foundation installation and template baselines: `agent-workflow-local/foundation-state.json` (operational metadata, not a startup read)
- Third-party inventory: `agent-workflow-local/tooling.json`

## Roles

- Lead: codex
- Consultants: claude, gemini
- Review lenses: Claude checks rule consistency and authority; Gemini checks architecture, context efficiency, and implementation feasibility.

## Stage Tracking

Use `agent-workflow-local/current-state.md` for the active stage and next action.
Resolve template-specific stages and gates through
`agent-workflow-foundation/workflow/stages.md` and the selected workflow record.
Local rules may explicitly override a gate.

## Source-Of-Truth Inventory

- `agent-workflow-foundation/` — delivered product source
- `openspec/specs/` — accepted product requirements
- `docs/change-log.md` — maintenance and rollback records
