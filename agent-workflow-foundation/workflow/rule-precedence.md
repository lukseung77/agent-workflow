# Rule Precedence

Use the installed `agent-workflow-foundation/` directory, or the explicit
foundation path in project facts, as `<foundation-root>`. Local facts and overrides live in
`agent-workflow-local/`; placement details are in `workflow/local-project-files.md`.
Project-specific maintainer rules belong in the consuming project's own local
configuration; the foundation does not assign upstream authority.
Product `workflow/`, `guides/`, `scripts/`, `templates/`, and `third-party/`
paths resolve from the foundation root. `docs/` always resolves from the consuming
project root. Local configuration resolves from that same project root.

## Read Order

1. Read the host entry and this file plus `workflow/agent-workflow.md`.
2. Read local `project-facts.md`, `rules.md`, and `current-state.md`.
3. Read optional `agent-workflow-local/agent-workflow-{agent}.md` restrictions.
4. Run `scripts/collab_queue.py <agent> --startup`, select work, and load only
   affected source files and routed topic rules.

If installation state is absent **and** old workflow pointers/override files are
present, this is an existing legacy layout: read `workflow/migration.md` before
other work. A fresh empty project without state is new setup, not legacy.

Use `--id ITEM-ID` for any live/archived item and `--refs REQUEST-ID` for responses.

## Task Routing

This table is the canonical rule map. The focused rule file governs its topic
over generic summaries and agent adapters. Load only rows relevant to the task.

| Task / topic | Read |
|---|---|
| Foundation install, customization, and update | `workflow/foundation-lifecycle.md` |
| Existing project on a pre-foundation layout | `workflow/migration.md` |
| Host-specific guidance when needed | `workflow/agent-workflow-{agent}.md` |
| Upstream improvement suggestions | `workflow/upstream-feedback.md` |
| Project setup | `templates/new-project-setup.md`, `workflow/local-project-files.md` |
| Local files, overrides, source-of-truth placement | `workflow/local-project-files.md` |
| Roles, review lenses, capability mapping | `workflow/role-boundaries.md` |
| Collaboration schema, recipients, IDs, queues | `workflow/collaboration-format.md` |
| Stage gates and transitions | `workflow/stages.md`, `workflow/role-boundaries.md` |
| Decision classification and conflicts | `workflow/decision-protocol.md` |
| User questions and assumption interviews | `workflow/question-model.md`, `workflow/decision-protocol.md` |
| Grill Me installation or explicitly requested grilling interview | `workflow/grill-me.md`; interview pacing in `workflow/question-model.md` |
| Tool freshness on OpenSpec/stage transition or manual request | `workflow/tooling-review.md` |
| Reviews, critical evaluation, consolidation | `workflow/review-cycle.md`, `workflow/collaboration-format.md` |
| Defined domain-term formatting | `workflow/defined-terms.md` |
| Context, restart, handoff, archives | `workflow/context-management.md` |
| External references and conversion | `workflow/markitdown.md` |
| Diagrams | `workflow/diagrams.md` |
| Select or use product skills, browser/design/security tools, MCP services, or host automations | `workflow/tooling.md`; sole catalog in `third-party/origins.json` |
| Repository discovery, implementation, validation, verbose commands | `workflow/tooling.md`; operational commands in `guides/tooling-operations.md` |

## Conflict Resolution

Project roles and authority come from its own local configuration. A copied
foundation grants no write authority to the upstream source. Explicit local
overrides apply from highest to lowest:

1. `agent-workflow-local/agent-workflow-{agent}.md`
2. `agent-workflow-local/rules.md`
3. `<foundation-root>/workflow/agent-workflow-{agent}.md` (when relevant)
4. `<foundation-root>/workflow/agent-workflow.md`

Use focused topic rules over summaries at the same authority. An accepted
requirement is not superseded by a newer exploration or collaboration note.
Resolve equal-authority conflicts through the lead or human; do not guess.

## Missing Workflow Root

Check the host entry file, project facts, and `agent-workflow-foundation/` first. If unavailable,
use the repository URL when permitted, or report degraded mode and continue with
project-local rules. Never assume missing shared rules grant extra authority.
