# Agent Workflow

Shared startup-safe defaults for projects using `agent-workflow`.

Use `workflow/rule-precedence.md` for read order, conflict precedence, and task-specific topic routing.

## Core Model

- One agent leads each phase; other agents consult unless the user explicitly changes ownership.
- Durable project files are the source of truth, not chat history.
- Project-specific facts, rules, current state, and per-agent assignments belong in `agent-workflow-local/`.
- Collaboration files carry communication and review history; accepted decisions must flow into source-of-truth files.
- The lead agent owns source-of-truth updates and GitHub sync by default unless project-local rules or the user explicitly delegate a specific downstream action.

## Trigger Model

- Files carry state but do not automatically trigger other tools, terminals, or agent sessions.
- The practical trigger is the user starting or messaging the next agent session.
- Default collaboration uses files: write the request, verify the queue when useful, and wait for the target agent to respond in its own collaboration file.
- Direct CLI, subprocess, API, browser, or authentication-based invocation of another agent is optional orchestration, not a workflow requirement. Use it only when the user explicitly asks or project-local rules allow it.
- The user may identify which sessions responded and direct wait, consolidate, or proceed; the lead still reads the files directly.

## State Model

- Generate active work from collaboration files by recipient and lifecycle status when scripts are available.
- Treat persistent collaboration indexes as compatibility fallbacks only.
- Keep `agent-workflow-local/current-state.md` as a compact restart snapshot, not a task queue.
- On resume, rebuild context from files: startup path, current state, generated queue, selected item, and focused source files.

## Review And Decision Model

- Evaluate proposals against their goals, constraints, and evidence. Identify material unsupported assumptions, contradictions, and plausible failure modes; distinguish demonstrated defects from uncertainty and preference. Explain disagreement and suggest a proportionate correction. Do not invent objections to appear critical; say when no material issue is found.
- Consultant feedback should identify the issue, why it matters, where it belongs, and the requested action or question.
- On resume, the lead checks its own open review requests for referenced consultant responses, including `done` reviews omitted from active recipient queues.
- The lead reconciles consultant feedback explicitly and writes accepted outcomes into source-of-truth files.
- Ask the user one focused question at a time only after agent-resolvable and lead-resolvable decisions are handled.

## Sync And Scope Model

- Prefer local repository state before extra Git operations when files are already available.
- Withhold GitHub sync unless the user asks, project rules require it, or no reasonable local-only path completes the task.
- Do not let multiple agents push or sync concurrently unless deliberately coordinated.
- During Implementation, scope changes go through a mini-proposal cycle before changing accepted specs.

## Topic Rules

Use the Canonical Rule Map and Task Routing in `workflow/rule-precedence.md`
for focused rules; load only topics relevant to the current task.
