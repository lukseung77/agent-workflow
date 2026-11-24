# Project Facts

## Identity And Paths

- Project: {{project_name}}
- Project type: {{project_type}}
- Project template: `{{template_id}}`
- Selected workflow and requirements: `agent-workflow-local/project-template.json`
- Foundation root: `{{foundation_root}}`
- Source-of-truth root: `{{source_root}}`
- Reference registry: `agent-workflow-local/references/reference.md`
- Foundation installation and template baselines: `agent-workflow-local/foundation-state.json` (operational metadata, not a startup read)
- Third-party inventory: `agent-workflow-local/tooling.json`

## Roles

- Lead: {{lead}}
- Consultants: {{consultants}}
- Review lenses: none assigned; record actual assignments here when needed.

## Stage Tracking

Use `agent-workflow-local/current-state.md` for the active stage and next action.
Resolve template-specific stages and gates through
`{{foundation_root}}/workflow/stages.md` and the selected workflow record.
Local rules may explicitly override a gate.

## Source-Of-Truth Inventory

- `{{source_root}}`
