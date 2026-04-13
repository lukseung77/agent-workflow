# Rule Precedence

This file defines where workflow rules live, what order to read them in, and how conflicts are resolved.

## Layout

- Shared workflow rules live in `../agent-workflow/workflow/`
- Project-specific overrides live in `./agent-workflow-local/`
- Projects should not copy the shared global rules into each repository by default

## Read Order

Read these files in order:

1. `../agent-workflow/workflow/rule-precedence.md`
2. `../agent-workflow/workflow/agent-workflow.md`
3. `../agent-workflow/workflow/agent-workflow-{agent}.md`
4. `./agent-workflow-local/agent-workflow.md`
5. `./agent-workflow-local/agent-workflow-{agent}.md`
6. `./agent-workflow-local/current-state.md`

Read topic files such as `stages.md` or `review-cycle.md` only when relevant to the current task.

If the project uses collaboration files, read those after the startup path above and only as needed for agent-specific recommendations, gaps, review notes, or reconciliation history.

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
- current source-of-truth files
- pending questions
- active constraints
- environment facts that matter right now
- the canonical open-question queue for the project

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
