# Rule Precedence

This file defines where workflow rules live, what order to read them in, and how conflicts are resolved.

## Layout

- Shared workflow rules live in the workflow root, normally `../agent-workflow/workflow/` for a sibling checkout or `./agent-workflow/workflow/` for a project-vendored copy.
- Project-specific overrides live in `./agent-workflow-local/`
- Projects may use a shared sibling checkout or a project-local vendored copy. User-agents may customize only their downstream local copy unless acting under `workflow/master-governance.md` in the canonical upstream repository.
- Projects should not copy shared global rules into `agent-workflow-local/`; local files should contain facts, overrides, and project-specific rules only.

## Read Order

Read these files in order:

1. `./docs/collaboration.md`
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

Read topic files such as `local-project-files.md`, `question-model.md`, `role-boundaries.md`, `diagrams.md`, `context-management.md`, `markitdown.md`, `stages.md`, or `review-cycle.md` only when relevant to the current task.

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
| Review and finding consolidation | `workflow/review-cycle.md` |
| Decision classification and escalation | `workflow/decision-protocol.md` |
| Stage gates | `workflow/stages.md` |
| Startup context, restart state, and archives | `workflow/context-management.md` |
| External reference conversion | `workflow/markitdown.md` |

Other files should link to these canonical rules instead of restating detailed schemas or procedures.

## Conflict Resolution

If two files disagree, the more specific and more local file wins.

Highest to lowest:

1. `./agent-workflow-local/agent-workflow-{agent}.md`
2. `./agent-workflow-local/rules.md`
3. `./agent-workflow-local/agent-workflow.md`
4. `<workflow-root>/workflow/agent-workflow-{agent}.md`
5. `<workflow-root>/workflow/agent-workflow.md`

Project-local overrides affect only the downstream project. They do not authorize changes to the canonical upstream `agent-workflow` repository.

If two files at the same level appear to conflict, do not guess. Treat that as a workflow gap and ask the user or the designated lead agent to resolve it.

## What Belongs Where

Global shared rules:

- stage model
- trigger model
- source-of-truth model
- review and consolidation model
- generic sync policy
- generic anti-patterns

See the canonical rule map before adding new shared rules. Prefer updating a focused topic file over expanding bootstrap files.

Global per-agent rules:

- role strengths
- role limits
- role-specific review behavior
- tool-specific cautions

Project-local shared rules:

- project-specific overrides
- project-specific guardrails

Project-local facts:

- repo paths
- project-wide role assignments
- stage tracking location
- source-of-truth file order for this project
- external reference registry location

Project-local per-agent rules:

- project role for that agent
- project-specific responsibilities
- project-specific prohibitions
- project-specific reading order differences

Current-state file:

- current stage
- current artifact
- next lead action
- active blockers
- last updated date

Collaboration files:

- agent-specific recommendations
- gaps
- review findings
- reconciliation history
- traceable cross-agent communication

## Missing Shared Repo

If the expected workflow root is missing:

1. Look for a project bootstrap file that provides an alternate path.
2. Check both common locations: `../agent-workflow` and `./agent-workflow`.
3. If no local shared path is available, use the GitHub repo URL if the environment allows it.
4. If neither is available, continue in degraded mode using only project-local files and record that the shared workflow repo was unavailable.

## Override Style

Use `workflow/local-project-files.md` for local override style. Do not silently restate global rules in slightly different wording.
