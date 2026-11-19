# Rule Precedence

Use the installed `agent-workflow-foundation/` directory, or the explicit
foundation path in project facts, as `<foundation-root>`. Local facts and overrides live in
`agent-workflow-local/`; placement details are in `workflow/local-project-files.md`.
Project-specific maintainer rules belong in the consuming project's own local
configuration; the foundation does not assign upstream authority.
Shared `workflow/`, `scripts/`, `templates/`, `third-party/`, and operational-doc
references resolve from the foundation root. Local configuration and
`docs/collaboration-*.md` resolve from the consuming project root.

## Read Order

Read existing files in order; skip absent optional files:

1. A host entry file supplies the workflow path. Read `docs/collaboration.md` only if an existing project uses that legacy pointer; do not read message history here
2. `<foundation-root>/workflow/rule-precedence.md` and `<foundation-root>/workflow/agent-workflow.md`
3. `agent-workflow-local/project-facts.md`, `rules.md`, and `current-state.md`
4. `<foundation-root>/workflow/agent-workflow-{agent}.md`
5. `agent-workflow-local/agent-workflow.md` only when an existing project uses this compatibility file
6. `agent-workflow-local/agent-workflow-{agent}.md` only for existing agent-specific restrictions; roles come from project facts

Generate active work with `python3 <foundation-root>/scripts/collab_queue.py <agent>`.
Load the selected item and affected source files, then use the routing table below.
Use `--id ITEM-ID` for any live or archived item and `--refs REQUEST-ID` for its
responses, including completed reviews. Persistent indexes are compatibility only.

## Task Routing

This table is the canonical rule map. The focused rule file governs its topic
over generic summaries and agent adapters. Load only rows relevant to the task.

| Task / topic | Read |
|---|---|
| Foundation install, customization, and update | `workflow/foundation-lifecycle.md` |
| Upstream improvement suggestions | `workflow/upstream-feedback.md` |
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

Project roles and authority come from its own local configuration. A copied
foundation grants no write authority to the upstream source. Explicit local
overrides apply from highest to lowest:

1. `agent-workflow-local/agent-workflow-{agent}.md`
2. `agent-workflow-local/rules.md`
3. `agent-workflow-local/agent-workflow.md` (legacy compatibility)
4. `<foundation-root>/workflow/agent-workflow-{agent}.md`
5. `<foundation-root>/workflow/agent-workflow.md`

Use focused topic rules over summaries at the same authority. An accepted
requirement is not superseded by a newer exploration or collaboration note.
Resolve equal-authority conflicts through the lead or human; do not guess.

## Missing Workflow Root

Check the host entry file, project facts, and `agent-workflow-foundation/` first. If unavailable,
use the repository URL when permitted, or report degraded mode and continue with
project-local rules. Never assume missing shared rules grant extra authority.
