# Rule Precedence

This file defines where workflow rules live, what order to read them in, and how conflicts are resolved.

## Layout

- Shared workflow rules live in `../agent-workflow/workflow/`
- Project-specific overrides live in `./agent-workflow-local/`
- Projects should not copy the shared global rules into each repository by default

## Read Order

Read these files in order:

1. `./docs/collaboration.md`
2. `../agent-workflow/workflow/rule-precedence.md`
3. `../agent-workflow/workflow/agent-workflow.md`
4. `./agent-workflow-local/current-state.md`
5. `../agent-workflow/workflow/agent-workflow-{agent}.md`
6. `./agent-workflow-local/agent-workflow.md`
7. `./agent-workflow-local/agent-workflow-{agent}.md`

Read topic files such as `context-management.md`, `markitdown.md`, `stages.md`, or `review-cycle.md` only when relevant to the current task.

After the startup path, generate the current agent queue when the shared scripts are available:

```sh
python3 ../agent-workflow/scripts/collab_queue.py <agent>
```

Read the selected collaboration item and focused source files only. Use persistent collaboration indexes only as a compatibility fallback.

## Canonical Rule Map

| Topic | Canonical file |
|-------|----------------|
| Rule location and precedence | `workflow/rule-precedence.md` |
| Shared operating model | `workflow/agent-workflow.md` |
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
2. `./agent-workflow-local/agent-workflow.md`
3. `../agent-workflow/workflow/agent-workflow-{agent}.md`
4. `../agent-workflow/workflow/agent-workflow.md`

If two files at the same level appear to conflict, do not guess. Treat that as a workflow gap and ask the user or the designated lead agent to resolve it.

## What Belongs Where

Global shared rules:

- stage model
- trigger model
- source-of-truth model
- review and consolidation model
- generic sync policy
- generic anti-patterns

Global per-agent rules:

- role strengths
- role limits
- role-specific review behavior
- tool-specific cautions

Project-local shared rules:

- repo paths
- project-wide role assignments
- source-of-truth file order for this project
- project-specific overrides
- project-specific guardrails

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

If `../agent-workflow` is missing:

1. Look for a project bootstrap file that provides an alternate path.
2. If no local shared path is available, use the GitHub repo URL if the environment allows it.
3. If neither is available, continue in degraded mode using only project-local files and record that the shared workflow repo was unavailable.

## Override Style

When a project-local rule overrides a global rule, state it explicitly:

- `Overrides global rule: [short name]`
- `Reason: [project-specific need]`
- `Replacement: [the rule to follow here]`

Do not silently restate global rules in slightly different wording.
