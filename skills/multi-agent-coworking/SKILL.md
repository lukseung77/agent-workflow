---
name: multi-agent-coworking
description: Use when multiple AI agents collaborate on a project, especially during exploration, review, handoff, or implementation. Applies one-question-at-a-time elicitation, lead/consultant role boundaries, durable source-of-truth updates, consultant feedback reconciliation, and restart discipline.
---

# Multi-Agent Coworking

Use this skill when Codex, Claude, Gemini, or another agent is collaborating with other AI agents on the same project.

## Core Rule

One agent leads each phase. Other agents consult unless the user explicitly reassigns ownership.

## Startup

Follow `workflow/rule-precedence.md`. Load the project collaboration bootstrap, local facts/rules/current-state when present, generated queue, one selected item, and focused source-of-truth files.

Do not ask the user to restate the whole project by default.

## Phase Roles

Use `workflow/role-boundaries.md` for lead, consultant, and user responsibilities. Use `workflow/stages.md` for stage-specific duties.

## Question-At-A-Time Exploration

Use `workflow/question-model.md`. Ask one focused question at a time, include the estimated questions left, and record confirmed answers into project files.

## Source Of Truth

Prefer durable repo files over chat history.

Use the project's existing structure. If none exists, recommend the structure in `workflow/local-project-files.md`, plus `openspec/explorations/` for active exploration and `openspec/changes/` for formal proposals.

## Consultant Feedback

Ask consultant agents to leave feedback in one predictable place.

Require feedback to include:

- issue
- why it matters
- affected file or topic
- whether it is a contradiction, missing detail, wording issue, or future-facing suggestion
- proposed next question, if useful

Reconcile each meaningful suggestion with:

- `Adopted`
- `Partially adopted`
- `Not adopted`

Include a short reason so later agents do not repeat the same review.

## Token And Context Discipline

- Load the restart snapshot, generated queue, selected item, and focused source files before full historical threads.
- Summarize large consultant findings before merging them into source-of-truth files.
- Move durable guidance into short bootstrap files plus focused references.
- Use MarkItDown for bulky non-Markdown inputs before pasting or asking another agent to read them; check `agent-workflow-local/references/reference.md` first and reuse current converted Markdown when available.
- Preserve enough links and file paths that a future agent can reopen the original material when needed.

## Boundaries

- Keep reusable collaboration policy in generic guides or skills.
- Keep product-specific decisions in the product repo.
- Do not let consultant agents overwrite confirmed requirements unless the user explicitly asks them to.
- Do not let multiple agents sync to GitHub independently unless that responsibility is coordinated.
