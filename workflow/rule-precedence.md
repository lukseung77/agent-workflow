# Rule Precedence

This file defines where workflow rules live, what order to read them in, and how conflicts are resolved.

## Layout

- Shared workflow rules live in the workflow root, normally `../agent-workflow/workflow/` for a sibling checkout or `./agent-workflow/workflow/` for a project-vendored copy.
- Project-specific overrides live in `./agent-workflow-local/`
- Projects may use a shared sibling checkout or a project-local vendored copy. User-agents may customize only their downstream local copy unless acting under `workflow/master-governance.md` in the canonical upstream repository.
- Projects should not copy shared global rules into `agent-workflow-local/`; local files should contain facts, overrides, and project-specific rules only.

## Read Order

Read these files in order for normal startup:

1. `./docs/collaboration.md` when present, as a short path/role bootstrap (pointer file, not a message file);
   do not load collaboration history here
2. `<workflow-root>/workflow/rule-precedence.md`
3. `<workflow-root>/workflow/agent-workflow.md`
4. `./agent-workflow-local/project-facts.md` when present
5. `./agent-workflow-local/rules.md` when present
6. `./agent-workflow-local/current-state.md`
7. `<workflow-root>/workflow/agent-workflow-{agent}.md`
8. `./agent-workflow-local/agent-workflow.md`
9. `./agent-workflow-local/agent-workflow-{agent}.md`

For downstream projects, `<workflow-root>` is the available `agent-workflow` copy, usually `../agent-workflow` or `./agent-workflow`.

When operating in the canonical upstream `agent-workflow` repository as master-agent, also read `workflow/master-governance.md` before updating workflow files, templates, scripts, skills, docs, suggestion status, or GitHub state.

Read topic files only when relevant to the current task. Use the task-routing table below to avoid missing required rules.

For all agents operating on the canonical repository itself, `<workflow-root>`
is this repository. Read `workflow/master-governance.md` before acting; consultants
also read `docs/consultant-orientation.md`. Skip absent downstream bootstrap and
`agent-workflow-local/` files here. Consultation requests live in
`docs/collaboration-codex.md` and are selected through the queue below.

After the startup path, generate the current agent queue when the shared scripts are available:

```sh
python3 <workflow-root>/scripts/collab_queue.py <agent>
```

Read the selected collaboration item and focused source files only. Use persistent collaboration indexes only as a compatibility fallback.

## Canonical Rule Map

| Topic | Canonical file |
|-------|----------------|
| Rule location and precedence | `workflow/rule-precedence.md` |
| Canonical upstream maintenance and suggestion governance | `workflow/master-governance.md` |
| Shared operating model | `workflow/agent-workflow.md` |
| Project-local file map and placement rules | `workflow/local-project-files.md` |
| Lead, consultant, and user boundaries | `workflow/role-boundaries.md` |
| User question flow and decision queues | `workflow/question-model.md` |
| Optional diagram defaults | `workflow/diagrams.md` |
| Collaboration schema and recipient semantics | `workflow/collaboration-format.md` |
| Defined domain-term formatting | `workflow/defined-terms.md` |
| Review and finding consolidation | `workflow/review-cycle.md` |
| Decision classification and escalation | `workflow/decision-protocol.md` |
| Stage gates | `workflow/stages.md` |
| Startup context, restart state, and archives | `workflow/context-management.md` |
| External reference conversion | `workflow/markitdown.md` |
| Optional agent tooling and phase routing | `workflow/agent-tooling.md` |

Other files should link to these canonical rules instead of restating detailed schemas or procedures.

## Task Routing

Load these topic files only when the task matches:

| Task | Read |
|------|------|
| Canonical upstream update, suggestion evaluation, GitHub sync for this repo | `workflow/master-governance.md`, then focused files named by the task |
| Consultant review of the canonical agent-workflow repository itself | `workflow/master-governance.md`, `docs/consultant-orientation.md` |
| Project setup | `templates/project-init.md`, `templates/new-project-setup.md`, `workflow/local-project-files.md` |
| Collaboration item writing, queue use, message IDs, lifecycle status | `workflow/collaboration-format.md` |
| Source-of-truth placement, local overrides, project-local facts | `workflow/local-project-files.md` |
| Role authority, consultant review lenses, capability mapping | `workflow/role-boundaries.md` |
| Stage readiness or phase transition | `workflow/stages.md`, `workflow/role-boundaries.md` |
| User question, decision escalation, conflict classification | `workflow/decision-protocol.md`, `workflow/question-model.md` |
| Consultant review, formal findings, consolidation | `workflow/review-cycle.md`, `workflow/collaboration-format.md` |
| Defined domain terms in project docs | `workflow/defined-terms.md` |
| Large context, handoff, restart, archive, file split | `workflow/context-management.md` |
| Bulky external documents or converted references | `workflow/markitdown.md` |
| Diagrams | `workflow/diagrams.md` |
| Repository discovery, implementation, validation, or verbose CLI execution | `workflow/agent-tooling.md` |

## Conflict Resolution

For canonical repository operations, `workflow/master-governance.md` governs
repository authority and cannot be overridden by per-agent or project-local
files. For each topic, the canonical file named in the rule map governs over
summaries in generic or per-agent workflow files. Explicit downstream overrides
still follow the ladder below, but cannot grant canonical upstream authority.

For downstream overrides, the more specific and more local file wins.

Highest to lowest:

1. `./agent-workflow-local/agent-workflow-{agent}.md`
2. `./agent-workflow-local/rules.md`
3. `./agent-workflow-local/agent-workflow.md`
4. `<workflow-root>/workflow/agent-workflow-{agent}.md`
5. `<workflow-root>/workflow/agent-workflow.md`

Project-local overrides affect only the downstream project. They do not authorize changes to the canonical upstream `agent-workflow` repository.

If two files at the same level appear to conflict, do not guess. Treat that as a workflow gap and ask the user or the designated lead agent to resolve it.

## Placement Summary

Detailed placement rules live in `workflow/local-project-files.md`. In short: reusable policy belongs in focused workflow files, project facts and overrides belong in `agent-workflow-local/`, collaboration history belongs in `docs/collaboration-*.md`, and confirmed product decisions belong in source-of-truth files.

## Missing Shared Repo

If the expected workflow root is missing:

1. Look for a project bootstrap file that provides an alternate path.
2. Check both common locations: `../agent-workflow` and `./agent-workflow`.
3. If no local shared path is available, use the GitHub repo URL if the environment allows it.
4. If neither is available, continue in degraded mode using only project-local files and record that the shared workflow repo was unavailable.

## Override Style

Use `workflow/local-project-files.md` for local override style. Do not silently restate global rules in slightly different wording.
