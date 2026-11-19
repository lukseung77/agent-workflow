# Change Log

The master-agent records canonical `agent-workflow` updates here when they are not already fully tracked in `user-agent-suggestions/status.md`.

Keep entries compact. Use this file for rollback orientation and downstream update notes, not detailed design discussion.

## 2026-11-19 - Critical Review And CL-006 Reconciliation

- `request`: human approved evidence-based critique guidance and asked to check and incorporate Claude's latest suggestions
- `summary`: added proportionate critical-review methods; corrected rule authority and setup contradictions; reduced startup duplication; split suggestion intake; preserved compatibility pointers; added historical item/reference lookup and a 20 KB archive threshold
- `decisions`: `docs/collaboration-codex.md` CX-010 owns all CL-006 dispositions, measured context changes, pending policy decisions, and verification outcomes
- `downstream note`: default active queues and existing override precedence remain compatible; setup installs actual host entry files, keeps roles in project facts, and uses canonical message examples; the compact reference registry retains both hashes
- `rollback`: selectively restore from `/private/tmp/agent-workflow-before-cl006-0tkik0ww.tgz`, preserving later edits and consultant input; `workflow/suggestion-intake.md` is the new routed procedure file

## 2026-11-19 - Prompt Simplification

- `request`: human approved applying the unnecessary-prompt assessment
- `summary`: shortened agent templates and shared agent prompts to assignment pointers and host guidance; removed model-strength prescriptions, duplicated message schemas/routing, and duplicate stage/constraint fields; made interview progress counts optional; narrowed joining-project reads to affected files and dependencies; made environment reporting conditional on impact; directed consultants to report cleanup within their write authority
- `changed`: `templates/{CODEX,CLAUDE,GEMINI,agent-common,project-init,new-project-setup}.md`, `templates/docs/collaboration-format.md`, `workflow/agent-workflow-{codex,claude,gemini}.md`, `workflow/question-model.md`
- `downstream note`: roles and review lenses come from project facts and per-agent assignments; stage and constraints come from existing local state/rules; use canonical collaboration examples rather than copying schemas; defined-term formatting, stage approval, ownership, and review-evidence rules remain in force
- `validation`: collaboration lint passed with zero errors/warnings; diff whitespace check passed; searched active prompts for the removed mandatory counts, model-strength sections, duplicated stage/constraint sections, and unrestricted cleanup instructions
- `rollback`: restore the three agent templates, three shared agent prompts, common template, and project-init from baseline `04ea42048d38b50d166b03fad8fd609fc368ba6b`; reverse only prompt-simplification hunks in the collaboration template, setup checklist, and question model to preserve the preceding integrity fixes

## 2026-11-19 - Evaluation And Workflow Integrity Refactor

- `request`: human requested incorporating Claude and Codex's evaluations, a grill-me-style assumption review, and a whole-project refactor
- `summary`: hardened shared Markdown parsing and archive boundaries, corrected queue chronology and aliases, preserved archived review evidence, improved recipient/state checks and optional-tool diagnostics, refreshed managed adapters, isolated optional command failures, and added installation version selectors
- `changed`: collaboration/environment scripts and regression tests; canonical collaboration, review, context, question, and tooling rules; setup templates; README and operational docs; external-proposal labels; `.gitignore`; `scripts/validate.py`; `.github/workflows/validate.yml`; `openspec/changes/harden-workflow-integrity/`
- `decisions`: `docs/project-evaluation.md` records every CL-005 disposition, eight independent findings, the question-driven assumption review, and remaining limitations; `docs/collaboration-codex.md` CX-008 records completion
- `validation`: 39 tests passed; collaboration lint reported zero errors/warnings; both OpenSpec changes validated; diff whitespace check passed; CI is configured but has not run remotely
- `downstream note`: commands and paths remain stable; keep metadata in the initial contiguous field block and use level 4–6 item subheadings; `tools.ponytail` retains its shared-adapter meaning, while text diagnostics identify unrequested agents and unknown native plugin state; package version selectors apply only to missing tools
- `rollback`: restore only these maintenance changes from baseline `04ea42048d38b50d166b03fad8fd609fc368ba6b` and remove newly added validation/change-record files, preserving consultant input and unrelated user edits; no host configuration, installation, merge, or publication occurred

## 2026-09-18 - Standard Optional Agent Tooling

- `request`: human-requested Ponytail, Graphify, and RTK integration
- `summary`: added shared capability policy, safe/idempotent environment bootstrap and doctor, OpenSpec change artifacts, phase routing, agent adapters, compatibility/troubleshooting docs, and mocked lifecycle tests
- `changed`: `workflow/agent-tooling.md`, rule routing and agent defaults, setup/templates, `scripts/agent_workflow_env.py`, tests, README/docs, `openspec/changes/standardize-agent-tooling/`
- `downstream note`: optional tools remain non-blocking; package installation and host-wide hooks require explicit flags; existing `AGENTS.md` content is preserved
- `rollback`: remove the marked downstream adapter and upstream-generated tool files, then revert this entry and the related change files; normal workflow files remain usable without optional tooling

## 2026-09-09 - Lightweight Best-Practice Rules

- `request`: human approval of consolidated CL-003 and GM-003 recommendations
- `summary`: added review-content identification/freshness, verification evidence, failure classification, progress-aware retry bounds, task-specific capability checks, permission-suppression authority clarification, and optional source authorship attribution
- `changed`: `workflow/review-cycle.md`, `workflow/collaboration-format.md`, `workflow/decision-protocol.md`, `workflow/role-boundaries.md`, `docs/collaboration-codex.md`
- `decisions`: CX-005 records consultant dispositions; CX-004 is complete
- `downstream note`: no new infrastructure or required schema fields; claims need appropriate evidence, but ordinary tasks do not require formal audits, mandatory commits, or fixed two-cycle limits
- `rollback`: revert these topic additions and record a superseding disposition for CX-005; preserve original consultant records

## 2026-09-09 - Review Request And Activation Clarification

- `request`: human-requested clarification of ambiguous review-cycle activation directives
- `summary`: distinguished file-based requests from session activation, made manual activation a default rather than a fixed agent-launch sequence, and clarified parallel reviews, session reuse, authorized orchestration, and completion requirements
- `changed`: `workflow/review-cycle.md`
- `downstream note`: file updates do not activate agents; orchestration still requires existing authorization and preserves file records, role boundaries, and human stage approval
- `rollback`: revert this review-cycle clarification and record any replacement guidance; no tools or schemas changed

## 2026-09-08 - Follow-up Consultant Corrections

- `request`: human-requested reconciliation of CL-002 and GM-002
- `summary`: clarified precedence and review schemas, aligned stage authority, preserved parseable completed items for archival, documented done-review discovery, and supported local-only project setup
- `changed`: `workflow/rule-precedence.md`, `workflow/collaboration-format.md`, `workflow/decision-protocol.md`, `workflow/role-boundaries.md`, `workflow/review-cycle.md`, `workflow/agent-workflow.md`, `workflow/agent-workflow-claude.md`, lead/consultant role templates, project-init/setup templates, collaboration-format template, suggestion status ledger, `docs/collaboration-codex.md`
- `decisions`: CX-003 records all eleven findings and optional recommendations; suggestion 003 is registered as proposed without an acceptance decision
- `downstream note`: keep completed items uncommented for automatic archival; leads must check responses to their own open review requests; stage transitions still require concurrence and human confirmation
- `rollback`: revert the changes associated with CX-003 and record any changed dispositions in a follow-up; preserve consultant records and suggestion intake history

## 2026-09-08 - Consultant Review Corrections

- `request`: human-requested reconciliation of Claude CL-001 and Gemini GM-001
- `summary`: clarified upstream authority exceptions, routed canonical consultants at startup, made the downstream bootstrap conditional, excluded on-demand welcome docs, shortened the explanatory guide, and removed repeated consolidation instructions
- `changed`: `workflow/master-governance.md`, `workflow/rule-precedence.md`, `workflow/context-management.md`, `workflow/ai-coworking-guide.md`, `workflow/collaboration-format.md`, `docs/collaboration-codex.md`
- `decisions`: `docs/collaboration-codex.md` item `CX-002` records all nine findings and optional recommendations
- `downstream note`: retain short collaboration.md bootstrap files where present; topic-file paths and collaboration schema remain compatible
- `rollback`: revert the changes associated with CX-002, retaining consultant reviews and recording a superseding consolidation if decisions are withdrawn

## 2026-09-08 - Consultant Invitation And Orientation

- `request`: human-requested invitation and orientation materials for consultant agents
- `summary`: added invitation and orientation; updated by human direction to designate Codex as maintainer and use collaboration files exclusively for consultation requests and responses
- `changed`: `docs/consultant-invitation.md`, `docs/consultant-orientation.md`, `docs/collaboration-codex.md` (request `CX-001` for existing consultant feedback), `workflow/master-governance.md`, `README.md`
- `downstream note`: canonical consultants may create and update only their own collaboration file under `docs/`; Codex maintains all other project files. Downstream suggestion intake is unchanged.
- `rollback`: remove the two consultant documents, their README pointer, and the canonical consultant channel governance section; preserve collaboration history and mark any withdrawn request superseded

## 2026-09-08 - Master Governance And Context Refactor

- `request`: human-requested canonical governance update and context-efficiency cleanup
- `summary`: added master-agent governance, one-file-per-suggestion intake, compact suggestion status ledger, downstream vendored workflow-root support, and lower-context startup orientation
- `backup`: `/private/tmp/agent-workflow-backup-20260908-135043.tgz`
- `changed`: `workflow/master-governance.md`, `workflow/rule-precedence.md`, `workflow/role-boundaries.md`, `workflow/context-management.md`, `workflow/collaboration-format.md`, `README.md`, `skills/multi-agent-coworking/SKILL.md`, setup templates, `user-agent-suggestions/`, `docs/external-lead-suggestions.md`, `docs/legacy/external-lead-suggestions.md`
- `downstream note`: downstream agents may customize local `agent-workflow/` copies but submit reusable upstream changes only through `user-agent-suggestions/submitted/` when explicitly asked by the human user
- `rollback`: restore from the backup archive or revert the commit that includes this entry

## 2026-09-08 - Stage Role Reminder

- `request`: human-requested rule for agents to check roles at OpenSpec phase changes and remind the user of active roles
- `summary`: added stage-transition role recheck and compact user role reminder rules
- `changed`: `workflow/stages.md`, `workflow/role-boundaries.md`, `templates/roles/lead-agent.md`, `templates/roles/consultant-agent.md`
- `downstream note`: after Exploration, Proposal, or Implementation transitions, agents re-check project-local role files and the lead gives the user a one-line role summary
- `rollback`: revert this entry and the related stage/role-template changes

## 2026-09-08 - Skill Recommendation Channel

- `request`: human-approved advisory channel for identifying job areas where specialized skills would be beneficial
- `summary`: added a non-binding skill recommendation channel with initial reusable capability areas
- `changed`: `docs/skill-recommendations.md`, `README.md`, `workflow/context-management.md`
- `downstream note`: projects do not need to install anything; use the channel as planning input and map concrete skills locally
- `rollback`: remove `docs/skill-recommendations.md` and related README/context references

## 2026-09-08 - Rule Routing And Defined-Term Split

- `request`: human-requested assessment and refactor to improve memory efficiency and reduce missed rules
- `summary`: added task-specific rule routing, moved placement detail out of mandatory startup, shortened the always-loaded operating model, and split defined-term formatting into a focused topic file
- `changed`: `workflow/rule-precedence.md`, `workflow/agent-workflow.md`, `workflow/local-project-files.md`, `workflow/defined-terms.md`, `workflow/collaboration-format.md`, `templates/docs/collaboration-format.md`, `templates/agent-common.md`, `templates/project-init.md`, `templates/new-project-setup.md`, `skills/multi-agent-coworking/SKILL.md`, `README.md`, `workflow/context-management.md`
- `downstream note`: agents should load topic files according to the task-routing table instead of reading every workflow rule
- `rollback`: remove `workflow/defined-terms.md`, restore defined-term text in collaboration-format files, and revert the rule-precedence routing changes
