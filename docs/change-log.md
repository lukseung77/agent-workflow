# Change Log

The master-agent records canonical `agent-workflow` updates here when they are not already fully tracked in `user-agent-suggestions/status.md`.

Keep entries compact. Use this file for rollback orientation and downstream update notes, not detailed design discussion.

## 2026-11-23 - Foundation GitHub Publication

- `request`: sync the foundation to GitHub and establish it as the basis of the agent-workflow repository
- `summary`: publish the accumulated foundation integrations, tooling-review refinements, Claude follow-up, migration support, and this repository's development evidence; README explicitly identifies foundation as the delivered product
- `target`: lukseung77/agent-workflow default master; fast-forward from the existing working branch, preserving remote history; synchronize the working branch too
- `validation`: 71 tests, three main specifications, clean collaboration lint, and boundary/self-consumer validation passed before publication; publication result and remote CI are verified after the publishing commit
- `boundary`: third-party installed skill directories remain ignored; consumer export still includes only foundation product source, excluding this project's local state and history
- `rollback`: use a reviewed revert of the publishing change on master; do not force-push or reset shared history

## 2026-11-23 - Claude CL-010 / CL-011 Follow-Up

- `request`: review and accept Claude's suggestions, including its recorded human decisions about existing-project legacy support and stage/manual tooling-review triggers
- `summary`: consolidated tooling and registry defaults; renamed reusable docs to guides; unified setup and lead startup; isolated migration with read-only preview/apply; removed dead wrappers; corrected gates, review labels, deferral format, and duplication
- `decisions`: `docs/evaluations/claude-follow-up-2026-11-23.md` dispositions all findings; retained safe template merge bases and conservative semantic migration review rather than adopting destructive or lossy interpretations
- `validation`: 71 tests, three main specs, zero lint errors/warnings, 53-file boundary/self-consumer check; literal paths, supported registry pointers, fresh export/install, and exported migration CLI preview/apply/lint verified
- `consumer impact`: product docs paths now use guides; tooling policy is workflow/tooling.md; setup is templates/new-project-setup.md; tooling review accepts manual/stage-change only. This instance applied the shared update without conflicts. Historic evidence and installed tools are preserved
- `rollback`: selectively restore this follow-up's paths/policy/scripts/tests from a reviewed prior snapshot and apply the shared lifecycle update; do not revert unrelated uncommitted work or later consumer history. No GitHub sync performed

## 2026-11-23 - Setup And Stage Tooling Freshness Reviews

- `request`: check current tools/plugins/skills during new-project setup and automatically invoke the same process on OpenSpec stage changes
- `summary`: added the agent-run upstream/discovery review procedure, read-only due checker and evidence recorder, local review-history scaffold, setup/transition invocation, and resume recovery; recommendations remain separate from installations
- `decisions and evidence`: `docs/collaboration-codex.md` CX-018; `agent-workflow-foundation/workflow/tooling-review.md`; actual local findings in `agent-workflow-local/tooling-reviews.json`
- `validation`: 65 tests including six tooling-review cases, three specs, clean collaboration lint, 61-file self-consumer/boundary validation, and exported fresh-consumer setup review check passed
- `initial findings`: Grill Me revision matches current upstream; GitHub stable OpenSpec v2.1.1 is newer than installed/CI-pinned 1.3.1, retained pending focused compatibility review. No upgrade performed
- `distribution and rollback`: only the empty review-history template is distributed; agent sessions perform online checks, not a background daemon. Revert CX-018 source/process changes and review/apply the lifecycle update if retiring the feature; preserve actual review evidence and installed tools

## 2026-11-23 - Supported Foundation Tool Integrations

- `request`: incorporate all listed optional tools into master/foundation except SEO/voice and visual assets/animation
- `summary`: added a capability router and eight focused setup/use adapters for engineering, efficiency, references, UI, browser, security, host automation, and workspaces; 29 total registry entries now have supported integration pointers including the existing Grill Me and OpenSpec integrations
- `decisions and evidence`: `docs/collaboration-codex.md` CX-017; `agent-workflow-foundation/workflow/tool-integrations.md`
- `validation`: 59 tests, three specs, clean collaboration lint, 58-file boundary/self-consumer validation, complete integration-pointer/exclusion checks, and export-to-fresh-consumer smoke check passed
- `distribution`: origins and first-party adapters only; consumer installation stays selective. Six excluded entries remain catalog-only. No third-party installation, live provider calls, global host changes, external deployment, or GitHub publication was performed
- `rollback`: selectively revert CX-017 product adapters, routing, and registry fields, then review/apply the foundation lifecycle update; preserve consumer installations and unrelated earlier changes

## 2026-11-23 - Foundation Grill Me Integration

- `request`: incorporate Grill Me into the master/foundation as well as this local consumer
- `summary`: added a shared Grill Me setup/invocation adapter, promoted its catalog recommendation, routed interviews to it, and included it in new-project setup guidance; replaced the local duplicate with the shared integration
- `decisions and evidence`: `docs/collaboration-codex.md` CX-016; `agent-workflow-foundation/workflow/grill-me.md`
- `validation`: 59 tests, three specs, clean collaboration lint, 49-file boundary/self-consumer validation, and fresh-consumer setup smoke check passed
- `distribution`: foundation delivers first-party integration and official origin/dependency guidance; consumers install both upstream skills separately. No third-party prompts bundled, automatic downloads, or GitHub publication added
- `rollback`: revert the CX-016 integration edits and review/apply the foundation lifecycle update; retain this consumer's installed upstream pair and provenance unless separately retired

## 2026-11-23 - Project-Local Grill Me Installation

- `request`: human requested having the Grill Me skill available
- `summary`: used skill-installer to install mattpocock/skills Grill Me and its grilling dependency at revision abeeaf95660ba9e8b7c753eb38f441ca707a8823 into this consumer's .agents/skills; preserved upstream files and recorded local question-pacing/authority adaptations
- `decisions and evidence`: `docs/collaboration-codex.md` CX-015; file hashes, provenance, and lifecycle instructions in `agent-workflow-local/tooling.json`
- `distribution`: installed files are Git-ignored and outside foundation; no global host settings or foundation default installation changed
- `rollback`: remove the selected local integration rules/inventory and installed directories after checking for edits and other users of grilling; retain history and upstream origin catalog

## 2026-11-23 - Product Capability Selection Catalog

- `request`: evaluate 28 named tools/plugins/skills, incorporate useful capabilities, and prepare others for future product needs
- `summary`: added a routed product-selection guide and 30 optional origin entries covering all requests and alternatives; setup selects by product need, keeps tools inactive until chosen, and records actual consumer installation/verification rather than vendoring third parties
- `decisions and evidence`: `docs/collaboration-codex.md` CX-014; detailed evaluations and primary-source links in `agent-workflow-foundation/docs/tool-selection.md`
- `validation`: 59 tests, three OpenSpec specs, clean collaboration lint, 48-file distribution/self-consumer check, and catalog coverage/inactive-default checks passed
- `downstream note`: this instance applied the shared lifecycle update with no actions/conflicts; new catalog entries do not add automatic installers or enable tools. OpenSEO/VoiceStudio candidate identities need confirmation. No third-party package or host/service configuration was installed or runtime-certified
- `rollback`: selectively revert the CX-014 product and documentation changes, then review/apply the shared foundation update to refresh this instance's baseline; preserve unrelated consumer customizations

## 2026-11-19 - Foundation Product And Self-Consumer Structure

- `request`: implement the agreed foundation product model, self-consuming local scaffold, official third-party origin references, then sync GitHub
- `summary`: moved reusable content under agent-workflow-foundation; created this project's own local instance and host entries through the common installer; added distribution/export, local/Git source acquisition, update review/apply, customization merges, stable release resolution, and local tool inventory
- `decisions and evidence`: `docs/collaboration-codex.md` CX-013; accepted requirements in `openspec/specs/foundation-consumers/spec.md`, change history under `openspec/changes/archive/2026-11-19-separate-foundation-and-consumer/`
- `validation`: 59 tests passed, clean collaboration lint, 47-file product boundary/self-consumer check, both main specs and change valid, and standalone consumer install from the exported package verified
- `migration`: new product paths start at agent-workflow-foundation; local-template sources are templates/agent-workflow-local inside it; root scripts/validate.py remains maintenance-only. Historical reviewed paths remain in archives as evidence; existing downstream copies migrate deliberately rather than being overwritten
- `rollback`: selective restore from `/private/tmp/agent-workflow-before-foundation-r1e1p2b6.tgz` or the prior tracked baseline while preserving later user edits; publication is separately authorized by the human in this session

## 2026-11-19 - Final Claude Follow-Up And Queue Cleanup

- `request`: follow up Claude's evaluation and clear remaining collaboration queues; CL-009 records approval to combine review/gate concurrence, defer scaffolding, and the already completed local commit
- `decisions`: `docs/collaboration-archives/codex-001.md` CX-012 is the full disposition record for CL-007, CL-008, CL-009 and the retired unanswered question; retrieve it with `collab_queue.py codex --id CX-012`
- `summary`: combined review/concurrence rounds, one host entry file per agent, authoritative roles in project facts, consolidated message/session rules, direct intake links, fewer verification probes, PR-only branch validation with npm caching, promoted main OpenSpec specs, and archived resolved collaboration records
- `downstream note`: preserve existing wrappers; new Codex setup installs CODEX template content directly into AGENTS.md; role restrictions do not override roster assignments; no setup scaffold or missing-concurrence waiver was introduced
- `rollback`: restore only this follow-up's changes from commit `130975cd76daf06c908f434c362b7d8f94b722db`, preserving subsequent user edits; OpenSpec and collaboration history remain in their archive directories

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
