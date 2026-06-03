# Context Management

Use this file when a project, document set, or agent session is getting large enough that startup or review context becomes expensive.

## Default Read Order

1. Project bootstrap: `docs/collaboration.md`
2. Project queue: `agent-workflow-local/current-state.md`
3. Shared rule summary: `workflow/agent-workflow.md`
4. Agent-specific summary: `workflow/agent-workflow-[agent].md`
5. Collaboration indexes before full collaboration threads
6. Focused source-of-truth files for the current task only

Read full historical collaboration threads only when an index item, current-state entry, or source file points to them.

## File Shape

- Keep bootstrap files short enough to read every session.
- Put durable policy in shared workflow files.
- Put current project state in `current-state.md`.
- Put stable project decisions in source-of-truth files.
- Put large examples, lessons, and source notes in references.
- Prefer topic files over one giant product document.

## Handoff Summaries

A useful handoff summary includes:

- current stage
- lead agent and consultants
- source-of-truth path
- next unresolved question or blocker
- recently reconciled feedback
- exact files changed since the last handoff

Avoid restating entire specs. Link to the relevant source files instead.

## Collaboration Thread Hygiene

- Use index files for scan-first orientation.
- Keep open items near the top.
- Move resolved items to closed sections instead of deleting them.
- Summarize long review threads before asking another agent to act on them.
- Reconcile consultant feedback in one place so later agents do not repeat the same review.

## When To Split Files

Split a file when:

- startup requires reading many sections unrelated to the current task
- unrelated decisions are repeatedly edited together
- consultant feedback often says "this belongs somewhere else"
- agents paste long excerpts instead of linking focused source files

Do not split when the result would create many tiny files with no stable ownership.
