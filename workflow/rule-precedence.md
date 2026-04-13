# Rule Precedence

This file defines where workflow rules live and what order agents should read them in.

## Shared-Path Model

The global workflow rules live in the shared `agent-workflow` repository.

Projects should not copy those global rules into every project repo by default.

Instead:

- shared global rules live in `../agent-workflow/workflow/`
- project-specific overrides live in `./agent-workflow-local/`

This keeps global workflow changes centralized and avoids repeated Git changes across project repositories.

## Read Order

Agents should read rules in this order:

1. `../agent-workflow/workflow/rule-precedence.md`
2. `../agent-workflow/workflow/agent-workflow.md`
3. `../agent-workflow/workflow/agent-workflow-{agent}.md`
4. `./agent-workflow-local/agent-workflow.md`
5. `./agent-workflow-local/agent-workflow-{agent}.md`
6. `./agent-workflow-local/current-state.md`

Read additional topic files such as `stages.md`, `review-cycle.md`, or other references only when relevant to the current task.

## Conflict Resolution

If two files disagree, the more specific and more local file wins.

Precedence from highest to lowest:

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
