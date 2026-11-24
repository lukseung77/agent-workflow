# Core And Project Template Structural Update

## Accepted Design And Evaluation

The human asked for evaluation and clarification before editing the foundation.
CX-021 preserves the original instructions and follow-up answers verbatim.
Confirmed scope is communication between agents and the user in the core,
including Grill-Me; one or more templates per project type; explicit type then
template selection during setup; template-owned stages/gates; guided installation;
and the two initial types below. The final stage-ownership answer was "yes pls".

This is a coherent separation: the communication protocol is reusable across
deliverables, while a development lifecycle and its integrations need not govern
proposal presentation work. Existing tooling already supported selective
installation, but installer source paths and lint stage names assumed SW work.
Changing only documentation would have left those executable assumptions intact.

Risks and responses:

- Selecting a template could be mistaken for installing or verifying tools:
  selection records requirements as unverified; actual evidence remains in the
  separate local tooling inventory. Initialization performs no third-party setup.
- A growing template catalog could duplicate the tool registry: template entries
  select tool IDs; origins and installation adapters stay in the existing registry.
- Template updates could switch existing workflows: old contexts remain explicitly
  `legacy-unselected`, preserve source roots/stages/history, and retain prior gates.
  Selected contexts keep their IDs and merge local customization with new defaults.
- Claude plugin identity and production details are not settled: the template
  records a manual prerequisite, requires identifying the actual host plugin,
  and allows independent planning without claiming slide-production readiness.
- Manual handoffs could use stale instructions: slide briefs identify revision,
  approval, stable slide IDs, sources, expected output, deviations, and return notes.

## Implemented Structure

- `workflow/project-templates.md` defines the core/template boundary and selection
  lifecycle; `templates/project-types.json` is the extensible catalog.
- SW Development / `openspec-github`: OpenSpec overall process, GitHub repository,
  development stages/gates, and additional capabilities selected for actual needs.
- Proposal PT Making / `chatgpt-claude-manual`: MarkItDown RFP/supporting-data
  extraction, ChatGPT analysis and TOC/per-slide planning, manual transfer to the
  user's Claude PowerPoint plugin, returned-deck review, and final acceptance.
  The reusable handoff includes slide titles, key messages, contents, and
  drawing/layout prompts as requested.
- `foundation.py templates` lists choices; fresh CLI initialization requires a
  valid type/template pair. The setup agent asks the questions; the CLI records
  explicit choices rather than running a second terminal interview.
- Local `project-template.json` records selected workflow, stages, requirements,
  and handoff mode. Collaboration lint validates that template's stages, preventing
  accidental acceptance of SW-only stages in a proposal project.
- Core stage/role/review/tooling guidance dispatches to the chosen process.
  SW stage definitions moved under its template. Existing consumers retain those
  former defaults through a narrow compatibility route, without selecting SW tools.
- Stage-triggered tooling reviews are template-owned: retained for SW and existing
  consumers; the initial proposal template uses explicit requests only. No online
  tooling review, stage transition, or upgrade was triggered by this change.

## Validation And Limits

`python3 -B scripts/validate.py --require-openspec` passed: 78 unit tests, three
accepted specifications, collaboration lint with zero errors/warnings, and the
61-file foundation boundary/self-consumer check. Seven additional tests cover
selection failures without writes, both initial templates, process-specific
stages, pre-template updates, multiple templates/source-root overrides, selection
merge conflicts, and template-owned tooling-review triggers.

Exported-package smoke checks also passed for both templates: initialize using a
custom foundation directory, run strict-state lint, and verify a no-op update.
The ordinary reviewed lifecycle update applied this repository's scaffold changes
without conflicts, preserving its source root, stage, role lenses, and local rules.
`git diff --check` passed. No external plugin execution or finished-deck quality
is claimed; this change delivers the workflow/template structure and installer.

## Review And Rollback

CX-022 records implementation; CX-023 requests focused consultant review of the
working tree. Independent consultant concurrence and product publication are not
claimed. This implementation is not a project-stage transition.

To roll back, restore this update's product paths and accepted requirements from
a reviewed prior snapshot and review/apply the foundation lifecycle update. Keep
consumer installation metadata consistent with that snapshot; preserve user
artifacts, collaboration history, and actual tooling evidence. Do not rerun init
or discard unrelated local configuration to undo a template change.
