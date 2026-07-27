# Role Boundaries

This file defines generic lead, consultant, and user boundaries. Project-specific assignments belong in `agent-workflow-local/project-facts.md` and per-agent local files.

## Lead Agent

- Owns source-of-truth file updates unless the user explicitly delegates a specific action.
- Integrates accepted decisions from consultant agents.
- Reconciles consultant disagreements and logs the rationale.
- Owns GitHub sync actions by default.
- Declares stage readiness and records stage transitions after user confirmation.
- Keeps `agent-workflow-local/project-facts.md` and `agent-workflow-local/current-state.md` accurate enough for another lead session to resume from files.

## Consultant Agents

- Write only to their own `docs/collaboration-[agent].md`, except for allowed external-reference registry updates.
- Surface gaps, conflicts, risks, review findings, and non-blocking suggestions.
- Request source-of-truth or GitHub changes from the lead through collaboration files.
- Do not edit source-of-truth files, run GitHub sync commands, declare stage transitions, or edit another agent's collaboration file unless the user explicitly authorizes that specific action.

## User

- Resolves product and scope decisions that agents cannot determine from source-of-truth files.
- Receives one question at a time under `workflow/question-model.md`.
- Confirms stage transitions after the lead agent declares readiness.

## Operational Notes

- A consultant may challenge a lead decision by logging a `gap` item, but the challenge is not a stage or source-of-truth change by itself.
- A user may temporarily authorize a consultant for a specific write or GitHub action. Record that authorization in collaboration files.
- Do not let decisions remain only in collaboration files; accepted decisions must flow into source-of-truth files.
