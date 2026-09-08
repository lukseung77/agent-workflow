# External Lead Agent Suggestions

Legacy note: this file preserves historical suggestion records and adoption decisions. It is not the active suggestion submission queue.

New upstream suggestions should be submitted as one file per suggestion under `user-agent-suggestions/submitted/` using `user-agent-suggestions/suggestion-form.md`. The master-agent tracks new suggestion decisions in `user-agent-suggestions/status.md`; see `workflow/master-governance.md`.

This file previously collected improvement suggestions from lead agents working in other projects that use `agent-workflow`.

Suggestions recorded here are proposals, not active workflow rules. The current workflow maintainer or designated lead must review each suggestion and explicitly adopt it into the appropriate canonical workflow file before agents follow it.

## Submission Rules

- Add one suggestion per entry.
- Describe observed project behavior rather than making assumptions about other projects.
- Include enough project context to explain why the suggestion may be reusable.
- Identify the canonical workflow file that would change, when known.
- State expected benefits, costs, risks, and compatibility concerns.
- Do not edit canonical workflow rules as part of submitting a suggestion.
- Do not include confidential project content; summarize or link only material that may be shared.

## Statuses

- `proposed`: submitted and awaiting review
- `under-review`: being evaluated against current workflow rules
- `adopted`: accepted and incorporated into canonical workflow files
- `partially-adopted`: only part of the suggestion was incorporated
- `rejected`: not accepted, with a recorded reason
- `superseded`: replaced by a later suggestion or workflow change

## Suggestion Format

```md
### [ELS-NNN] Short title
- `date`: YYYY-MM-DD
- `status`: proposed
- `from-project`: project name or non-confidential identifier
- `from-lead`: lead agent name or tool
- `workflow-version`: commit, tag, or date reviewed
- `observed-problem`: concise description of what happened
- `evidence`: file paths, metrics, repeated failure pattern, or summarized example
- `suggested-change`: specific proposed workflow change
- `target`: canonical workflow file or topic
- `expected-benefit`: what should improve
- `costs-and-risks`: context cost, complexity, compatibility, or migration concerns
- `scope`: projects or situations where the suggestion should apply

Additional notes, if needed.
```

## Suggestions

<!-- Add new proposed suggestions below this line. -->

## Generalization Review: 2026-06-07

| ID | Disposition | Generalized outcome |
|----|-------------|---------------------|
| ELS-001 | Partially adopted | File-based handoff is mandatory and portable; reliable environment-provided orchestration remains allowed. |
| ELS-002 | Adopted | Queue discovery uses recipient plus lifecycle status; type controls handling. |
| ELS-003 | Superseded | Replaced by generated queues in ELS-004. |
| ELS-004 | Adopted | Collaboration files are authoritative; generated queues are default with compatibility indexes as fallback. |
| ELS-005 | Adopted | Users may identify responders and direct wait/consolidate/proceed without relaying content. |
| ELS-006 | Adopted | Resolved content uses threshold-based numbered archives. |
| ELS-007 | Adopted | Lifecycle status is separate from lead-owned finding disposition. |
| ELS-008 | Adopted | Stable finding rows apply to formal reviews; informal reviews remain lightweight. |
| ELS-009 | Adopted | Formal finding deduplication and canonical IDs are lead-owned. |
| ELS-010 | Adopted | Canonical priority is assigned by the lead after deduplication. |
| ELS-011 | Adopted | A read-only generic collaboration linter was added. |
| ELS-012 | Partially adopted | Formal completion gate is canonical; exact mapping is currently a lead check rather than fully linted. |
| ELS-013 | Adopted | Canonical rule ownership is mapped in `workflow/rule-precedence.md`. |
| ELS-014 | Adopted | Current state is restricted to five restart fields. |
| ELS-015 | Adopted | Strict restart validation is available through the existing linter. |
| ELS-016 | Adopted | Generated queues are compact by default. |
| ELS-017 | Adopted | `to: all` excludes the sender unless explicitly self-addressed. |
| ELS-018 | Adopted | Queue detail can be selected case-insensitively by ID. |
| ELS-019 | Adopted | Selected-item output includes complete fields, body, references, and source. |
| ELS-020 | Adopted | Queue presentation is newest-first without expiring unresolved work. |
| ELS-021 | Adopted | Default lint output summarizes warnings; verbose and JSON retain detail. |
| ELS-022 | Partially adopted | Optional timestamps are supported, but must include `Z` or a UTC offset for cross-timezone safety. |

### [ELS-001] Use session-trigger-only cross-agent collaboration
- `date`: 2026-06-07
- `status`: partially-adopted
- `from-project`: proposal-document-workflow pilot
- `from-lead`: Codex
- `workflow-version`: 2026-06-07 project-local workflow
- `observed-problem`: Direct invocation of another agent through CLI, subprocess, API, or authentication flows did not reliably produce a response and incorrectly shifted operational work to the user.
- `evidence`: Repeated invocation attempts failed; collaboration succeeded after requests and responses were stored in files and the user started or resumed the target session.
- `suggested-change`: Prohibit direct cross-agent invocation. The user triggers sessions but never relays prompts, context, findings, or responses.
- `target`: `workflow/agent-workflow.md` and `workflow/review-cycle.md`
- `expected-benefit`: Reliable cross-tool collaboration, lower token duplication, and durable handoffs.
- `costs-and-risks`: The user remains the session trigger; files must contain enough context for the target agent to self-direct.
- `scope`: Agents operating in separate tools, accounts, terminals, or sessions.

### [ELS-002] Discover work by recipient and lifecycle status
- `date`: 2026-06-07
- `status`: adopted
- `from-project`: proposal-document-workflow pilot
- `from-lead`: Codex
- `workflow-version`: 2026-06-07 project-local workflow
- `observed-problem`: Requiring an exact message type allowed a minor metadata error to hide an otherwise clear open task.
- `evidence`: An addressed open review item could be skipped when its `type` did not match the expected discovery filter.
- `suggested-change`: Discover work from `status: open|active` and `to: <agent>|all`; use `type` to control handling, not visibility.
- `target`: `workflow/collaboration-format.md`, `workflow/review-cycle.md`, and consultant startup guidance
- `expected-benefit`: Fewer silently missed requests and simpler queue discovery.
- `costs-and-risks`: Agents must inspect type after discovery to choose the correct handling procedure.
- `scope`: All file-based collaboration queues.

### [ELS-003] Keep collaboration threads authoritative and indexes active-only
- `date`: 2026-06-07
- `status`: superseded
- `from-project`: proposal-document-workflow pilot
- `from-lead`: Codex
- `workflow-version`: 2026-06-07 project-local workflow
- `observed-problem`: Historical state duplicated across collaboration files and manually maintained indexes, allowing stale rows.
- `evidence`: Resolved items remained in both locations and required parallel maintenance.
- `suggested-change`: Treat collaboration files as authoritative and keep any index limited to `open` and `active` items.
- `target`: `workflow/collaboration-format.md`
- `expected-benefit`: Reduced duplication and clearer history ownership.
- `costs-and-risks`: Manual active-only indexes can still become stale.
- `scope`: Historical intermediate proposal; superseded by ELS-004 generated queues.

### [ELS-004] Generate active queues instead of maintaining indexes
- `date`: 2026-06-07
- `status`: adopted
- `from-project`: proposal-document-workflow pilot
- `from-lead`: Codex
- `workflow-version`: 2026-06-07 project-local workflow
- `observed-problem`: Persistent queue indexes required maintenance and consumed startup context.
- `evidence`: A read-only queue generator successfully derived active work from authoritative collaboration files and allowed legacy indexes to be deprecated.
- `suggested-change`: Generate each agent's queue from collaboration files; do not maintain persistent queue indexes.
- `target`: `scripts/collab_queue.py`, startup guidance, and `workflow/collaboration-format.md`
- `expected-benefit`: No index drift, lower maintenance, and reproducible queue state.
- `costs-and-risks`: Requires a small local script and valid collaboration metadata.
- `scope`: Projects with more than one collaboration file.

### [ELS-005] Allow user responder signals without content relay
- `date`: 2026-06-07
- `status`: adopted
- `from-project`: proposal-document-workflow pilot
- `from-lead`: Codex
- `workflow-version`: 2026-06-07 project-local workflow
- `observed-problem`: Defining the user only as a session trigger was too narrow because the user also knows which consultant sessions responded and may direct consolidation behavior.
- `evidence`: The normal operating pattern included the user telling the lead which agents responded and whether to merge, wait, or proceed.
- `suggested-change`: Permit the user to identify responders and direct consolidation, while prohibiting manual relay of consultant content.
- `target`: `workflow/agent-workflow.md` and `workflow/review-cycle.md`
- `expected-benefit`: Matches real session control without turning the user into a messenger.
- `costs-and-risks`: The lead must still read consultant files and verify the named responses.
- `scope`: User-triggered multi-agent reviews.

### [ELS-006] Use size-based collaboration archives
- `date`: 2026-06-07
- `status`: adopted
- `from-project`: proposal-document-workflow pilot
- `from-lead`: Codex
- `workflow-version`: 2026-06-07 project-local workflow
- `observed-problem`: Weekly or yearly archives create file churn when little content is resolved, while large live threads consume context.
- `evidence`: A 50 KB resolved-content threshold kept the pilot live file intact while it remained below the limit and provided deterministic archival when tested on fixtures.
- `suggested-change`: Archive resolved items only after a size threshold, using numbered per-agent archive files.
- `target`: `scripts/collab_archive.py`, `workflow/collaboration-format.md`, and `workflow/context-management.md`
- `expected-benefit`: Smaller live files without calendar-driven maintenance.
- `costs-and-risks`: Threshold selection is approximate; archive files must remain readable when explicitly referenced.
- `scope`: Long-running projects retaining collaboration history.

### [ELS-007] Separate lifecycle status from finding disposition
- `date`: 2026-06-07
- `status`: adopted
- `from-project`: proposal-document-workflow pilot
- `from-lead`: Codex
- `workflow-version`: 2026-06-07 project-local workflow
- `observed-problem`: Response statuses such as accepted or rejected mixed work completion with lead-owned adoption decisions.
- `evidence`: Consultant work completion and lead consolidation required different semantics during a multi-reviewer document review.
- `suggested-change`: Use only lifecycle statuses for messages. Consultants complete responses as `done`; the lead records `adopted`, `partially_adopted`, or `not_adopted` as finding disposition.
- `target`: `workflow/collaboration-format.md`, `workflow/review-cycle.md`, and role templates
- `expected-benefit`: Clear ownership and less ambiguous review state.
- `costs-and-risks`: Historical statuses require warning-only compatibility.
- `scope`: Workflows with consultant feedback and lead consolidation.

### [ELS-008] Standardize compact formal finding rows
- `date`: 2026-06-07
- `status`: adopted
- `from-project`: proposal-document-workflow pilot
- `from-lead`: Codex
- `workflow-version`: 2026-06-07 project-local workflow
- `observed-problem`: Free-form review findings required repeated interpretation and manual matching.
- `evidence`: Consolidating document findings became simpler after each issue used a stable finding ID and fixed fields.
- `suggested-change`: Use `finding_id | location | category | what | why`, with optional `correction`, and require lead disposition by finding ID.
- `target`: `workflow/review-cycle.md`, `workflow/collaboration-format.md`, and reviewer role templates
- `expected-benefit`: Compact feedback, deterministic mapping, and less repeated prose.
- `costs-and-risks`: Reviewers must create sequential IDs and keep one issue per row.
- `scope`: Formal document, specification, design, compliance, or code reviews.

### [ELS-009] Make canonical finding deduplication lead-only
- `date`: 2026-06-07
- `status`: adopted
- `from-project`: proposal-document-workflow pilot
- `from-lead`: Codex
- `workflow-version`: 2026-06-07 project-local workflow
- `observed-problem`: Multiple consultants reported overlapping findings, causing duplicate prose while provenance still needed preservation.
- `evidence`: A merged human-review artifact needed both deduplication and traceability to every consultant finding.
- `suggested-change`: Only the lead may merge the same issue at the same location into a `canonical_id`; preserve every `source_finding_id` and keep similar but distinct issues separate.
- `target`: `workflow/review-cycle.md` and lead role guidance
- `expected-benefit`: Consistent consolidation without loss of provenance.
- `costs-and-risks`: The lead must make careful equivalence decisions and avoid over-merging.
- `scope`: Multi-reviewer formal reviews.

### [ELS-010] Assign canonical priority only after deduplication
- `date`: 2026-06-07
- `status`: adopted
- `from-project`: proposal-document-workflow pilot
- `from-lead`: Codex
- `workflow-version`: 2026-06-07 project-local workflow
- `observed-problem`: Consultant priorities can conflict before duplicate findings are reconciled.
- `evidence`: Reviewers expressed impact differently for overlapping issues, requiring a single post-deduplication priority.
- `suggested-change`: The lead assigns `P0` correctness/compliance/delivery blockers, `P1` pre-submission fixes, and `P2` optional improvements. Consultants describe impact only in `why`.
- `target`: `workflow/review-cycle.md` and lead/consultant role templates
- `expected-benefit`: One consistent priority per canonical issue.
- `costs-and-risks`: Priority remains a lead judgment and needs clear criteria.
- `scope`: Reviews that produce an actionable remediation list.

### [ELS-011] Add a read-only collaboration schema linter
- `date`: 2026-06-07
- `status`: adopted
- `from-project`: proposal-document-workflow pilot
- `from-lead`: Codex
- `workflow-version`: 2026-06-07 project-local workflow
- `observed-problem`: IDs, fields, statuses, review tables, priorities, dispositions, and references could drift silently.
- `evidence`: The pilot linter validates collaboration and review schemas and completed with zero errors across 47 items.
- `suggested-change`: Run a read-only linter after collaboration changes and before archival; fail on errors and retain legacy compatibility as warnings.
- `target`: `scripts/collab_lint.py`, setup guidance, and `workflow/collaboration-format.md`
- `expected-benefit`: Earlier schema-drift detection and safer automation.
- `costs-and-risks`: The linter and tests must evolve with canonical schemas.
- `scope`: Projects using structured collaboration metadata.

### [ELS-012] Require an explicit formal review completion gate
- `date`: 2026-06-07
- `status`: partially-adopted
- `from-project`: proposal-document-workflow pilot
- `from-lead`: Codex
- `workflow-version`: 2026-06-07 project-local workflow
- `observed-problem`: Review requests could be closed without complete reviewer accounting or finding disposition.
- `evidence`: Multi-consultant review required confirmation of responders, skipped reviewers, finding mapping, and machine validation.
- `suggested-change`: Close formal review only after requested reviewers are processed or explicitly skipped by user direction, all processed findings map exactly once, and lint reports zero errors.
- `target`: `workflow/review-cycle.md` and lint completion-gate validation
- `expected-benefit`: Prevents silent omissions and premature closure.
- `costs-and-risks`: Adds metadata and is too heavy for informal suggestions.
- `scope`: Explicit formal review requests.

### [ELS-013] Keep detailed workflow rules in canonical files only
- `date`: 2026-06-07
- `status`: adopted
- `from-project`: proposal-document-workflow pilot
- `from-lead`: Codex
- `workflow-version`: 2026-06-07 project-local workflow
- `observed-problem`: Repeated schemas and procedures across overlays, roles, skills, templates, and README files increased drift and token use.
- `evidence`: Conflicting current-state and review descriptions were found in canonical files and local copies during the pilot audit.
- `suggested-change`: Give each detailed rule one canonical owner. Other files contain links, local paths, assignments, orientation, and explicit exceptions only.
- `target`: `workflow/rule-precedence.md`, canonical workflow files, templates, skills, and README structure
- `expected-benefit`: Less drift, lower maintenance, and smaller startup context.
- `costs-and-risks`: Canonical dependencies must remain discoverable; self-contained packaging needs an explicit exception.
- `scope`: Reusable workflows distributed across projects and agent platforms.

### [ELS-014] Restrict current state to five restart fields
- `date`: 2026-06-07
- `status`: adopted
- `from-project`: proposal-document-workflow pilot
- `from-lead`: Codex
- `workflow-version`: 2026-06-07 project-local workflow
- `observed-problem`: The current-state file accumulated stale questions, environment facts, decisions, source indexes, and task history.
- `evidence`: The pilot state still reported an early stage after proposal artifacts existed and duplicated information owned elsewhere.
- `suggested-change`: Keep only `updated`, `current_stage`, `current_artifact`, `next_lead_action`, and `active_blockers`. Generated queues own tasks; source-of-truth files own decisions.
- `target`: `workflow/context-management.md`, `workflow/agent-workflow.md`, and setup templates
- `expected-benefit`: Faster restart and clearer state ownership.
- `costs-and-risks`: The lead must update the snapshot when one of the five fields changes.
- `scope`: Long-running projects with session handoffs.

### [ELS-015] Validate the restart snapshot with the existing linter
- `date`: 2026-06-07
- `status`: adopted
- `from-project`: proposal-document-workflow pilot
- `from-lead`: Codex
- `workflow-version`: 2026-06-07 project-local workflow
- `observed-problem`: Documentation alone could not prevent agents from reintroducing stale history or invalid values into current state.
- `evidence`: Automated tests verify exact fields, ISO date, workflow stage, project-relative artifact path, missing files, and `None` before an artifact exists.
- `suggested-change`: Extend the collaboration linter to enforce the five-field state schema and validate its date, stage, and artifact path.
- `target`: `scripts/collab_lint.py` and `workflow/context-management.md`
- `expected-benefit`: Prevents restart-state drift without another command.
- `costs-and-risks`: Projects with different stage names need a configurable or extended allowed-stage set.
- `scope`: Projects adopting the five-field restart snapshot.

### [ELS-016] Make generated queues compact by default
- `date`: 2026-06-07
- `status`: adopted
- `from-project`: proposal-document-workflow pilot
- `from-lead`: Codex
- `workflow-version`: 2026-06-07 project-local workflow
- `observed-problem`: Reprinting full request descriptions for every active item consumed context before work selection.
- `evidence`: Compact output reduced a live queue from 1,328 bytes to 477 bytes, about 64 percent.
- `suggested-change`: Default queue output to ID, status, title, and source. Retain `--full` for whole-queue detail.
- `target`: `scripts/collab_queue.py` and context/startup guidance
- `expected-benefit`: Lower session-start token use and faster scanning.
- `costs-and-risks`: Agents need a follow-up detail command for selected items.
- `scope`: Queues containing long requests or multiple active items.

### [ELS-017] Exclude the sender from `to: all`
- `date`: 2026-06-07
- `status`: adopted
- `from-project`: proposal-document-workflow pilot
- `from-lead`: Codex
- `workflow-version`: 2026-06-07 project-local workflow
- `observed-problem`: An agent's own broadcast item appeared in its generated queue even though it had authored the item.
- `evidence`: A live Gemini broadcast was redundantly returned to Gemini before sender-aware filtering.
- `suggested-change`: Interpret `to: all` as every agent except the sender; explicitly naming the sender preserves intentional self-addressing.
- `target`: `scripts/collab_queue.py` and recipient semantics
- `expected-benefit`: Removes redundant self-work without eliminating deliberate reminders.
- `costs-and-risks`: Changes existing broadcast semantics and requires documentation.
- `scope`: Generated queues with broadcast recipients.

### [ELS-018] Add selected-item queue detail by ID
- `date`: 2026-06-07
- `status`: adopted
- `from-project`: proposal-document-workflow pilot
- `from-lead`: Codex
- `workflow-version`: 2026-06-07 project-local workflow
- `observed-problem`: Whole-queue detail expanded every item when only one request needed inspection.
- `evidence`: `--id ITEM-ID` returned one active addressed item and clearly rejected unknown, closed, or unaddressed IDs.
- `suggested-change`: Add case-insensitive `--id ITEM-ID`; imply one-item detail and return one object with `--json`.
- `target`: `scripts/collab_queue.py` and startup guidance
- `expected-benefit`: Loads only the context needed for the selected task.
- `costs-and-risks`: Adds CLI surface and requires duplicate-ID error handling.
- `scope`: Compact queues where agents act on one item at a time.

### [ELS-019] Give selected items a complete readable detail view
- `date`: 2026-06-07
- `status`: adopted
- `from-project`: proposal-document-workflow pilot
- `from-lead`: Codex
- `workflow-version`: 2026-06-07 project-local workflow
- `observed-problem`: A one-row selected-item table omitted references and made long requests hard to read.
- `evidence`: The dedicated pilot view includes metadata, complete request or action, references, and exact source without another file read.
- `suggested-change`: Render selected Markdown items as a heading-and-fields block; keep whole-queue `--full` and JSON behavior separate.
- `target`: `scripts/collab_queue.py`
- `expected-benefit`: Better readability and fewer immediate source-file reads.
- `costs-and-risks`: Markdown and JSON presentations differ intentionally.
- `scope`: Queue items with long text or multiple reference paths.

### [ELS-020] Sort queues newest-first without expiring old work
- `date`: 2026-06-07
- `status`: adopted
- `from-project`: proposal-document-workflow pilot
- `from-lead`: Codex
- `workflow-version`: 2026-06-07 project-local workflow
- `observed-problem`: Oldest-first display put long-lived reminders before newer actionable work.
- `evidence`: Regression tests confirm newest-first presentation while every older unresolved item remains visible.
- `suggested-change`: Sort by newest date first with deterministic fallback. Treat recency only as display order; never close, hide, or lower the validity of older unresolved items.
- `target`: `scripts/collab_queue.py` and `workflow/context-management.md`
- `expected-benefit`: New work is encountered first without losing durable reminders.
- `costs-and-risks`: Date-only records cannot establish exact cross-agent same-day order.
- `scope`: Active queues mixing durable reminders and new requests.

### [ELS-021] Summarize recurring warnings in default lint output
- `date`: 2026-06-07
- `status`: adopted
- `from-project`: proposal-document-workflow pilot
- `from-lead`: Codex
- `workflow-version`: 2026-06-07 project-local workflow
- `observed-problem`: The same historical warning lines printed on every run and obscured new problems.
- `evidence`: Default pilot output became two concise lines while `--verbose-warnings` and JSON retained all five historical warnings.
- `suggested-change`: Always print error details, show only warning count by default, add `--verbose-warnings`, and keep full JSON issue data.
- `target`: `scripts/collab_lint.py` and lint documentation
- `expected-benefit`: Better signal-to-noise without information loss.
- `costs-and-risks`: Users must request verbose output when auditing warnings.
- `scope`: Projects with preserved legacy records or recurring non-blocking warnings.

### [ELS-022] Add optional creation timestamps and strict metadata validation
- `date`: 2026-06-07
- `status`: partially-adopted
- `from-project`: proposal-document-workflow pilot
- `from-lead`: Codex
- `workflow-version`: 2026-06-07 project-local workflow
- `observed-problem`: Day-only dates could not order same-day cross-agent work, and ambiguous date formats or contradictory queue flags could be accepted.
- `evidence`: The final pilot suite contains 28 passing tests. Queue and lint verify timestamp ordering, exact date formats, date agreement, legacy fallback, and mutually exclusive detail flags.
- `suggested-change`: Allow optional local `created_at: YYYY-MM-DDTHH:MM`; sort timestamped same-day items by it and use date/item-number fallback for legacy records. Require `created_at` to match `date`, enforce exact `YYYY-MM-DD`, and reject `--id` with `--full`.
- `target`: `scripts/collab_queue.py`, `scripts/collab_lint.py`, `workflow/collaboration-format.md`, and collaboration templates
- `expected-benefit`: More accurate recent-first ordering and earlier rejection of ambiguous input.
- `costs-and-risks`: Timestamps are local and timezone-free; cross-timezone projects may need an offset-bearing format instead.
- `scope`: Multi-agent projects creating multiple items on the same day.
