# Agent Workflow

Shared defaults for all projects using `agent-workflow`.

Project-specific facts, rules, current state, and per-agent assignments belong in `./agent-workflow-local/`; see `workflow/local-project-files.md`.

## Default Model

- One agent leads each phase.
- Other agents may critique, review, and suggest alternatives, but they do not redirect the project unless the user explicitly changes ownership.
- Durable project files are the source of truth, not chat history.
- The lead agent is the default owner of GitHub actions and source-of-truth updates unless the user explicitly delegates those actions elsewhere.
- Role boundaries are defined in `workflow/role-boundaries.md`.

## Trigger Model

- Shared files carry state but do not automatically trigger another agent across tools, terminals, or platforms.
- The practical trigger is still the user explicitly starting or messaging the next agent.
- File-based handoff is the required portable mechanism. Direct CLI, subprocess, API, or authentication-based invocation of another agent must not be required for the workflow to function.
- A project may use reliable orchestration supplied by its environment, but all requests and outcomes must still be recorded in project files.
- The user may identify which agent sessions responded and may direct the lead to wait, consolidate, or proceed. The user should not have to relay prompts, findings, or response content between agents.
- Default minimal handoff: `Session ID: <session_id>. Files updated. Re-read docs/collaboration.md and continue from the next unresolved question.`
- When the user asks an agent to leave a handoff note, include a `session_id` that the same or another agent can cite when asking the user to resume or reference that session.

## Source-Of-Truth Model

- Use project files as the durable source of truth.
- Separate stable rules from current project state.
- Prefer focused files by topic instead of one monolithic document.
- Keep confirmed, deferred, and still-open items distinguishable.
- Treat converted external documents as source material until the lead records confirmed decisions into source-of-truth files.
- Project-local file placement is defined in `workflow/local-project-files.md`.

## Active State Model

- Collaboration files are authoritative for collaboration items and history.
- Active work is derived by recipient and lifecycle status, not by message type.
- Generated queues are the default discovery mechanism when the shared scripts are available. Persistent indexes are a compatibility fallback, not a second source of truth.
- `current-state.md` is a compact restart snapshot, not a task queue or decision history.
- Source-of-truth files own confirmed decisions.

## Cross-Session Lead Resume

- A lead agent starting from another session should rebuild context from files, not from assumptions about prior chat history.
- On resume, the lead agent should re-read the startup path first, then `current-state.md`, then any relevant collaboration files before making new decisions.
- If consultant feedback was posted while the lead agent was away, the lead agent should reconcile it explicitly into source-of-truth files or new collaboration items rather than leaving it implicit.
- A resumed lead agent should leave a traceable status note when it has finished reconciling cross-session feedback.

## Question Model

- Ask one focused question at a time while requirements are still emerging.
- Ask only what is needed for the next real decision.
- Record confirmed answers back into project files promptly.
- Follow `workflow/question-model.md` for remaining-question estimates, decision queues, and user-facing question format.

## Review Model

- Review should be file-based and traceable.
- Consultant feedback should identify the issue, why it matters, where it belongs, and what action or question follows.
- The lead agent should reconcile feedback explicitly rather than silently absorbing it.
- Consultant agents should communicate recommendations, gaps, and suggestions through collaboration files.

## Sync Model

- One agent should be the default Git integrator for a project unless the user explicitly changes that.
- The lead agent should handle GitHub actions and source-of-truth updates by default.
- Consultant agents should not perform GitHub actions or edit source-of-truth files unless the user explicitly authorizes that for the current project.
- If the relevant repositories are already available locally, prefer local files and local repository state over additional Git operations.
- Withhold Git operations by default unless the user explicitly asks for them or there is no reasonable local-only way to complete the task.
- Do not have multiple agents push or sync concurrently unless that is deliberately coordinated.
- Project-local files should state any stronger sync restrictions.

## Large-Rule Handling

- Keep bootstrap files short.
- Split stable rules from current-state files.
- Split large topic areas into reference files and load them only when relevant.
- If a rule file becomes too large for reliable startup reading, move detail into topic-specific references and keep only summary rules in the bootstrap files.

## Context Budget Model

- Default to scan-first orientation: bootstrap, restart snapshot, generated queue, selected item, then focused source files.
- Do not load full collaboration history unless a selected item or source file points to it.
- Use concise handoff summaries after long reviews, broad searches, or multi-agent reconciliation.
- Put reusable lessons into `docs/lessons-learned.md`, then promote stable rules into workflow files or skills.
- See `workflow/context-management.md` for split criteria and restart discipline.

## External Document Model

- Use Markdown as the default agent-readable import format.
- Use MarkItDown for bulky PDFs, office files, HTML exports, emails, archives, and similar inputs when local conversion is appropriate.
- Track external references in `agent-workflow-local/references/reference.md` with content hashes, source paths, conversion status, and converted Markdown paths.
- Store MarkItDown outputs in `agent-workflow-local/references/markitdown/`.
- Before reading an external reference, use an existing current Markdown conversion when the registry shows one.
- If a requested file name is ambiguous, list the plausible matches and ask the user which file they meant.
- Treat files in `_OLD` as obsolete unless the user explicitly asks for old material; keep tracking metadata when practical.
- Keep original documents and converted Markdown separate from confirmed source-of-truth files.
- Summarize decision-relevant content before asking another agent to review it.
- See `workflow/markitdown.md` for install, conversion, and token-discipline guidance.
