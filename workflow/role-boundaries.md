# Role Boundaries

This file defines generic lead, consultant, user, and upstream master-agent boundaries. Project-specific assignments belong in `agent-workflow-local/project-facts.md` and per-agent local files.

## Master-Agent

The `master-agent` role applies only to the canonical upstream `agent-workflow` repository.

- Owns canonical workflow rule, template, script, skill, documentation, suggestion-status, and GitHub updates for this repository.
- Reviews user-agent suggestions under `workflow/master-governance.md`.
- Updates canonical files only after the human user approves a suggestion or explicitly requests the change.
- Records implemented changes, downstream communication notes, and rollback or revoke notes.
- Treats submitted suggestion files as proposals, not active rules.

## Lead Agent

- Owns source-of-truth file updates unless the user explicitly delegates a specific action.
- Integrates accepted decisions from consultant agents.
- Reconciles consultant disagreements and logs the rationale.
- Owns GitHub sync actions by default.
- Declares stage readiness and records stage transitions after user confirmation.
- Keeps `agent-workflow-local/project-facts.md` and `agent-workflow-local/current-state.md` accurate enough for another lead session to resume from files.

## Consultant Agents

- Write only to their own `docs/collaboration-[agent].md`, except for allowed downstream external-reference registry updates. Canonical repository permissions follow `workflow/master-governance.md`.
- Surface gaps, conflicts, risks, review findings, and non-blocking suggestions.
- Request source-of-truth or GitHub changes from the lead through collaboration files.
- Do not edit source-of-truth files, run GitHub sync commands, declare stage transitions, or edit another agent's collaboration file unless the user explicitly authorizes that specific action.
- In downstream projects, do not edit the canonical upstream `agent-workflow` repository. When the human user explicitly asks for an upstream workflow suggestion, create only a new file under `user-agent-suggestions/submitted/` as defined in `workflow/master-governance.md`.

## Phase Review Lenses

Projects may assign consultants complementary review lenses by stage. These lenses are advisory defaults, not exclusive authority and not co-lead status. Project-local files may rename, combine, omit, or replace them.

Common reusable lenses:

- Fixed-reference/domain lens: checks source-of-truth consistency, domain contracts, lifecycle/state invariants, acceptance criteria, edge cases, and test fidelity against settled requirements.
- Architecture/breadth lens: checks cross-file consistency, technical feasibility, data and storage shape, performance bounds, UI or provider boundaries, implementation complexity, and simplification opportunities.

Recommended cadence:

- Exploration and Proposal: request lens-specific review after major lead cleanup passes and before stage transitions when the existing stage gates require agent concurrence.
- Implementation: request lens-specific review at milestone gates or coherent implementation batches.

Lens assignments should be recorded in `agent-workflow-local/project-facts.md` or per-agent local role files. A lens does not let a consultant edit source-of-truth files, run GitHub sync, or declare stage transitions.

At every stage transition, each agent should re-check its current role, authority, and review lens before acting in the new stage. The lead agent should give the user a brief role reminder after the transition is confirmed.

## Capability Mapping

Phase guidance should describe needed review capabilities before naming concrete skills or tools. Concrete system skills, project-local workflows, and optional skill packages are examples only unless a project-local file marks them required.

- Concrete system skills: named capabilities available in a specific agent or runtime environment.
- Project-local workflows: repeatable local procedures, scripts, commands, or browser/app verification steps recorded in project-local files.
- Functional capability labels: portable descriptions such as large-context review, acceptance-criteria audit, interactive app verification, security review, performance profiling, or architecture-boundary checks.

Agents should map functional capabilities to the actual skills, commands, or manual workflows available in the current project. Do not install third-party skills or assume external dependencies merely because a capability is listed.

Before dependent work, verify that explicitly required capabilities map to
available skills, tools, or permitted manual procedures. Check only what the
current task needs; reuse current knowledge of the environment. Report missing
prerequisites before claiming dependent work complete, and continue independent
work. Do not silently substitute for an explicitly required tool or skill.

## User

- Resolves product and scope decisions that agents cannot determine from source-of-truth files.
- Receives one question at a time under `workflow/question-model.md`.
- Confirms stage transitions after the lead agent declares readiness.

## Operational Notes

- Non-interactive and permission-prompt suppression modes are legitimate for
  already-authorized automation. They do not expand file/repository authority,
  grant GitHub actions, waive required human decisions, or bypass review gates.
  Establish the permitted execution scope before running; missing permission
  follows `workflow/decision-protocol.md#failures-and-retries`, not automatic
  escalation to broader access.

- A consultant may challenge a lead decision by logging a `gap` item, but the challenge is not a stage or source-of-truth change by itself.
- A user may temporarily authorize a consultant for a specific downstream project write or GitHub action. Record that authorization in collaboration files. This does not authorize canonical upstream `agent-workflow` changes.
- Do not let decisions remain only in collaboration files; accepted decisions must flow into source-of-truth files.
- Downstream project lead authority does not include authority to change the canonical upstream `agent-workflow` repository.
