# Rule Precedence

Use the selected workflow copy (`../agent-workflow`, `./agent-workflow`, or the
explicit project path) as `<workflow-root>`. Local facts and overrides live in
`agent-workflow-local/`; placement details are in `workflow/local-project-files.md`.
For this canonical repository, first read `workflow/master-governance.md` for
startup exceptions and upstream authority.

## Read Order

Read existing files in order; skip absent optional files:

1. `docs/collaboration.md`: workflow path/role bootstrap only, not message history
2. `<workflow-root>/workflow/rule-precedence.md` and `<workflow-root>/workflow/agent-workflow.md`
3. `agent-workflow-local/project-facts.md`, `rules.md`, and `current-state.md`
4. `<workflow-root>/workflow/agent-workflow-{agent}.md`
5. `agent-workflow-local/agent-workflow.md` only when an existing project uses this compatibility file
6. `agent-workflow-local/agent-workflow-{agent}.md`

Generate active work with `python3 <workflow-root>/scripts/collab_queue.py <agent>`.
Load the selected item and affected source files, then use the routing table below.
Use `--id ITEM-ID` for any live or archived item and `--refs REQUEST-ID` for its
responses, including completed reviews. Persistent indexes are compatibility only.

## Task Routing

This table is the canonical rule map. The focused rule file governs its topic
over generic summaries and agent adapters. Load only rows relevant to the task.

| Task / topic | Read |
|---|---|
| Canonical repository maintenance and authority | `workflow/master-governance.md` |
| Canonical consultant onboarding | `docs/consultant-orientation.md` after master governance |
| Human-requested downstream suggestion intake or evaluation | `workflow/suggestion-intake.md` after master governance |
| Project setup | `templates/project-init.md`, `templates/new-project-setup.md`, `workflow/local-project-files.md` |
| Local files, overrides, source-of-truth placement | `workflow/local-project-files.md` |
| Roles, review lenses, capability mapping | `workflow/role-boundaries.md` |
| Collaboration schema, recipients, IDs, queues | `workflow/collaboration-format.md` |
| Stage gates and transitions | `workflow/stages.md`, `workflow/role-boundaries.md` |
| Decision classification and conflicts | `workflow/decision-protocol.md` |
| User questions and assumption interviews | `workflow/question-model.md`, `workflow/decision-protocol.md` |
| Reviews, critical evaluation, consolidation | `workflow/review-cycle.md`, `workflow/collaboration-format.md` |
| Defined domain-term formatting | `workflow/defined-terms.md` |
| Context, restart, handoff, archives | `workflow/context-management.md` |
| External references and conversion | `workflow/markitdown.md` |
| Diagrams | `workflow/diagrams.md` |
| Repository discovery, implementation, validation, verbose commands | `workflow/agent-tooling.md`; operational commands in `docs/agent-tooling.md` |

## Conflict Resolution

For canonical operations, master governance controls upstream authority; local
or per-agent files cannot grant upstream write permissions. For downstream
projects, explicit local overrides apply from highest to lowest:

1. `agent-workflow-local/agent-workflow-{agent}.md`
2. `agent-workflow-local/rules.md`
3. `agent-workflow-local/agent-workflow.md` (legacy compatibility)
4. `<workflow-root>/workflow/agent-workflow-{agent}.md`
5. `<workflow-root>/workflow/agent-workflow.md`

Use focused topic rules over summaries at the same authority. An accepted
requirement is not superseded by a newer exploration or collaboration note.
Resolve equal-authority conflicts through the lead or human; do not guess.

## Missing Workflow Root

Check the project bootstrap and both common workflow paths first. If unavailable,
use the repository URL when permitted, or report degraded mode and continue with
project-local rules. Never assume missing shared rules grant extra authority.
