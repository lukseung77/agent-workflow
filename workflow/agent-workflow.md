# Agent Workflow

This file contains the shared workflow defaults for all projects using the `agent-workflow` repository.

Project repositories should override these rules only in `./agent-workflow-local/`.

## Default Model

- One agent leads each phase.
- Other agents may critique, review, and suggest alternatives, but they do not redirect the project unless the user explicitly changes ownership.
- Durable project files are the source of truth, not chat history.
- Generic workflow rules live in the shared `agent-workflow` repo, not duplicated inside every project.
- The lead agent is the default owner of GitHub actions and source-of-truth updates unless the user explicitly delegates those actions elsewhere.

## Trigger Model

- Shared files carry state but do not automatically trigger another agent across tools, terminals, or platforms.
- The practical trigger is still the user explicitly starting or messaging the next agent.
- Default minimal handoff:
  - `Files updated. Re-read docs/collaboration.md and continue from the next unresolved question.`

## Source-Of-Truth Model

- Use project files as the durable source of truth.
- Separate stable rules from current project state.
- Prefer focused files by topic instead of one monolithic document.
- Keep confirmed, deferred, and still-open items distinguishable.

## Question Model

- Ask one focused question at a time while requirements are still emerging.
- Ask only what is needed for the next real decision.
- Record confirmed answers back into project files promptly.
- Keep a pending-question list for later rather than batching questions at the user.

## Review Model

- Review should be file-based and traceable.
- Consultant feedback should identify the issue, why it matters, where it belongs, and what action or question follows.
- The lead agent should reconcile feedback explicitly rather than silently absorbing it.
- Consultant agents should communicate recommendations, gaps, and suggestions through their collaboration files so traceability is preserved.

## Sync Model

- One agent should be the default Git integrator for a project unless the user explicitly changes that.
- The lead agent should handle GitHub actions and source-of-truth updates by default.
- Consultant agents should not perform GitHub actions or edit source-of-truth files unless the user explicitly authorizes that for the current project.
- Do not have multiple agents push or sync concurrently unless that is deliberately coordinated.
- Project-local files should state any stronger sync restrictions.

## Large-Rule Handling

- Keep bootstrap files short.
- Split stable rules from current-state files.
- Split large topic areas into reference files and load them only when relevant.
- If a rule file becomes too large for reliable startup reading, move detail into topic-specific references and keep only summary rules in the bootstrap files.
