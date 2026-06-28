---
name: multi-agent-coworking
description: Use when multiple AI agents collaborate on a project, especially during exploration, review, handoff, or implementation. Applies one-question-at-a-time elicitation, lead/consultant role boundaries, durable source-of-truth updates, consultant feedback reconciliation, and restart discipline.
---

# Multi-Agent Coworking

Use this skill when Codex, Claude, Gemini, or another agent is collaborating with other AI agents on the same project.

## Core Rule

One agent leads each phase. Other agents consult unless the user explicitly reassigns ownership.

## Startup

1. Read the project collaboration bootstrap.
2. Read the current-state file.
3. Generate the active recipient queue when the shared script is available.
4. Load one selected collaboration item.
5. Read only the focused source-of-truth files needed for that action.

Do not ask the user to restate the whole project by default.

## Phase Roles

- Exploration lead:
  - synthesizes user decisions
  - asks the next focused question
  - records confirmed requirements
  - reconciles consultant feedback
- Consultant agents:
  - find contradictions
  - identify missed edge cases
  - suggest better wording or structure
  - propose focused follow-up questions
- Implementation lead:
  - integrates code and docs
  - verifies changes
  - prevents conflicting edits

## Question-At-A-Time Exploration

When requirements are still emerging:

- ask one focused question at a time
- avoid combining unrelated decisions
- include only the context needed to answer
- do not reopen settled decisions unless there is a contradiction
- update the project source of truth after meaningful clarification
- keep a pending-question list for later

If the project already uses rough remaining-question counts, continue that convention.

## Source Of Truth

Prefer durable repo files over chat history.

Use the project's existing structure. If none exists, recommend:

- `docs/collaboration.md` for project-specific agent coordination
- `agent-workflow-local/current-state.md` for the five-field restart snapshot
- `openspec/explorations/` for active exploration
- `openspec/changes/` for formal proposals
- GitHub issues or PRs once the project is ready for tracked work

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
