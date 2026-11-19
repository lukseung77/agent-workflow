# Codex Collaboration

### [CX-010] Reconciled CL-006 And Added Evidence-Based Critique
- `date`: 2026-11-19
- `session_id`: codex-2026-11-19-agent-workflow-cl006-reconciliation
- `from`: codex
- `to`: codex
- `type`: status
- `status`: done
- `scope`: critical review guidance, CL-006 conflicts and context recommendations, setup, governance, and historical collaboration lookup
- `why`: The human approved the critical-review recommendation and requested checking and incorporating Claude's latest suggestions.
- `request`: Implementation and reconciliation complete; pending stage policy is tracked by CX-011.
- `refs`: CL-006, CX-011, docs/change-log.md, workflow/agent-workflow.md, workflow/review-cycle.md, workflow/question-model.md

Human instruction: "1. I'll take your recommendation above. 2. claude made
suggestions for update. please check and incorporate it."

This item is the canonical disposition record for this update. Critical review
is evidence-based and proportionate: use intent matching normally and select
counterarguments, pre-mortems, disconfirming evidence, or Socratic questions when
useful. No flaw quota, adversarial persona, mandatory interview, or extra approval
gate was added. Original consultant records and historical decision evidence are
preserved.

| CL-006 row | Disposition | Result / rationale |
|---|---|---|
| C01 | adopted | Authority governs before recency; lower-authority notes cannot supersede accepted requirements. |
| C02 | adopted | The lead assesses and posts stage readiness. |
| C03 | awaiting human decision | CX-011 tracks the question about explicit user waivers of missing consultant concurrence; existing stage gates remain in force pending an answer. |
| C04 | adopted | Initial scope is created during checklist section 6; existing source roots remain valid and OpenSpec is the default. |
| C05 | adopted | Setup installs common and participating host entry files; Codex gets an AGENTS.md pointer without overwriting user instructions. |
| C06 | adopted | Local rules template contains only project-specific override scaffolding. |
| C07 | adopted within existing human authority | Explicit human consultant assessment requests are valid when origin/scope/date are recorded in the own file; write restrictions remain unchanged. |
| C08 | adopted | Setup and Complete are ungated administrative bookends, not extra workflow stages. |
| C09 | adopted | One concise canonical-startup pointer leads to master governance; duplicate startup paragraphs removed. |
| U01 | partially adopted | New projects use rules.md only; existing agent-workflow.md remains an optional compatibility read at its existing precedence. No forced migration. |
| U02 | adopted with compatibility | Project facts own the roster; collaboration-format template is a small pointer with no duplicate table. |
| U03 | partially adopted | README uses the single router; overview becomes a compatibility pointer. Keep the existing 31-line skill entry and its focused topic links rather than removing useful discovery paths. |
| U04 | adopted with compatibility | Role-template paths become short pointers to canonical role boundaries and local assignments. |
| U05 | adopted | Activation instructions are owned by the operating model; review cycle keeps one pointer and stage-readiness guidance. |
| U06 | adopted | Setup requires only its three entry documents; task routing supplies other rules. |
| U07 | partially adopted | Operational tooling commands live in docs/agent-tooling.md; README and setup point there. Semantic tooling policy stays canonical in workflow/agent-tooling.md. |
| U08 | adopted | Alias meaning is canonical in collaboration-format.md; redundant alias definitions removed. Host adapter command examples may still name agy. |
| U09 | adopted | Consultant onboarding uses relative paths and selected-request scope, not a dated refactor description. |
| U10 | partially adopted | Registry shrinks to eight columns and rules move to canonical guidance. Keep both content hashes; converted Markdown can change independently. Wider existing registries remain valid. |
| U11 | adopted | Removed repeated collaboration goals/operating pattern, duplicate conversion caution, parser-boundary copy, and manual item-position guidance. |
| U12 | deferred policy choice | Preserve defined-term formatting; no separate human choice to remove the color span has been recorded. |
| U13 | partially adopted | This consolidation owns current dispositions; other current records link here. Retain historical evidence and distinct OpenSpec requirements/design/tasks rather than erasing them. |
| M01 | adopted | One routing table replaces two; startup/precedence are compact and placement details stay in their topic file. |
| M02 | adopted | Suggestion submission/evaluation/status procedures moved to an on-demand intake file; authority and a routing pointer remain in master governance. |
| M03 | adopted | --id retrieves any uniquely identified live/archive item; --refs lists exact referencing items including completed reviews. Default queues stay active and recipient-filtered. |
| M04 | adopted | Default archival threshold is 20,000 bytes; focused reviews link supporting detail without a mandatory body cap. Live consultant files were not archived by this task. |
| M05 | adopted through preceding changes | Four startup files total about 15.2 KB versus 26.7 KB before this update, about 43% less source text; this is not measured model-token usage or performance. |
| M06 | deferred enforcement | No unvalidated universal context budget or broad path-failure gate. Measured startup size and manually checked literal active-guidance paths; planned downstream/generated paths are not broken repository links. |

Validation: `python3 -B scripts/validate.py --require-openspec` passed with 43
unit tests, zero collaboration lint errors/warnings, and both OpenSpec changes
valid. `git diff --check` passed. Direct CLI checks retrieved completed CL-004
and the review/consolidation items referencing CX-006. A literal-path scan of
38 active guidance files found only seven expected downstream/generated paths,
not unexpected missing repository files. CI and real host integrations were not
run remotely. The archived-lookup and threshold cases use temporary fixtures.

Pre-update rollback snapshot:
`/private/tmp/agent-workflow-before-cl006-0tkik0ww.tgz`; restore selectively to
preserve later user edits and consultant input. No GitHub publication or older
downstream suggestion-status decision is part of this update.

### [CX-011] Question — Explicit Stage Concurrence Waivers
- `date`: 2026-11-19
- `from`: codex
- `to`: user
- `type`: question
- `status`: open
- `scope`: workflow/stages.md, missing consultant concurrence
- `why`: CL-006 C03 proposes a policy choice that the prior prompt cleanup deliberately left open.
- `request`: Decide whether the lead may proceed after an explicit user waiver of an unavailable consultant's concurrence, recording the waiver and remaining risk.
- `refs`: CL-006, CX-010, workflow/stages.md

The same question was presented to the human during this update. No answer is
recorded yet. Default concurrence and user stage confirmation remain required.
CL-006 U12's defined-term formatting change is also deferred; ask that separate
policy question after this one rather than bundling approvals.

### [CX-009] Simplified Workflow Prompts
- `date`: 2026-11-19
- `session_id`: codex-2026-11-19-agent-workflow-prompt-simplification
- `from`: codex
- `to`: all
- `type`: status
- `status`: done
- `scope`: shared agent prompts, project instruction templates, collaboration template, setup flow, and question rules
- `why`: The human requested applying the unnecessary-prompt assessment.
- `refs`: docs/change-log.md, docs/project-evaluation.md, templates/, workflow/question-model.md, workflow/agent-workflow-codex.md, workflow/agent-workflow-claude.md, workflow/agent-workflow-gemini.md

Removed repeated model-strength guidance, startup routing, message schemas, and
stage/constraint copies. Agent templates now point to actual local assignments.
Interview counts are optional, source reading follows affected dependencies, and
environment constraints are reported when they affect work. Consultants report
cleanup findings rather than treating obvious fixes as write authorization.
Defined-term formatting and stage-concurrence policy remain separate decisions.

Checks: collaboration lint reported zero errors/warnings; `git diff --check`
passed. A search of active prompts found none of the removed mandatory count,
model-strength, duplicate stage/constraint, or unrestricted-cleanup instructions.
The three agent instruction templates shrank from 152 to 55 lines combined.

### [CX-008] Combined Evaluation And Workflow Integrity Refactor
- `date`: 2026-11-19
- `session_id`: codex-2026-11-19-agent-workflow-integrity-refactor
- `from`: codex
- `to`: codex
- `type`: status
- `status`: done
- `scope`: whole-project consistency, collaboration tooling, optional-tool diagnostics, tests, CI, and maintenance records
- `why`: The human requested implementation of Codex and Claude's evaluation followed by an assumption review and refactor.
- `request`: Finish validation and record the implemented dispositions and downstream compatibility notes.
- `refs`: CL-005, CX-007, docs/project-evaluation.md, openspec/changes/harden-workflow-integrity/, docs/change-log.md

Human instruction: "please update current project with your and claude's evaluation.
then utilize grill-me kind of skill. then refactor whole project."

`docs/project-evaluation.md` records each CL-005 disposition and eight additional
Codex findings. The project retains its standard-library tools, existing entry
points, manual activation, and authority rules. No installed grill-me skill was
found; a question-driven assumption review was used. The optional scope question
has no recorded answer; preserving existing workflow contracts is a lead assumption.

The previously untracked CX-007 wording follow-up is implemented in
`workflow/agent-tooling.md`. Optional diagnostic/test improvements were incorporated
where supported. Default package pins, branch publication, and deferred suggestion
decisions retain their separate status. Claude's original CL-005 and earlier
consultant evidence are preserved; this record reconciles them without editing
another agent's lifecycle metadata.

Validation: `python3 -B scripts/validate.py --require-openspec` passed with 39
unit tests, zero collaboration lint errors/warnings, and two valid OpenSpec
changes. `git diff --check` passed. Optional installations and host integrations
were tested with fakes; the new GitHub CI workflow has not run remotely.

The refactor is implemented locally. Migration and remaining decisions are in
`docs/project-evaluation.md`; rollback orientation is in `docs/change-log.md`.

### [CX-006] Review Standard Agent Tooling Integration
- `date`: 2026-09-18
- `created_at`: 2026-09-18T20:07:21+09:00
- `from`: codex
- `to`: claude, gemini
- `type`: review-request
- `status`: done
- `formal`: false
- `scope`: newly added Ponytail, Graphify, and RTK rules, bootstrap, agent adapters, OpenSpec artifacts, tests, and documentation
- `why`: The human requested independent confirmation that the new tooling integration is valid, contradiction-free, non-blocking, and minimally designed.
- `request`: Review the current working tree independently and record a completed assessment in your own collaboration file, explicitly stating any contradiction, blocker, unsupported assumption, or missing test, then list refactoring suggestions separately from required corrections.
- `refs`: workflow/agent-tooling.md, scripts/agent_workflow_env.py, openspec/changes/standardize-agent-tooling/, templates/project-init.md, templates/new-project-setup.md, docs/agent-tooling.md

- Claude lens: check rule precedence, authority boundaries, security/safety, agent compatibility claims, contradiction with existing workflow, and whether any behavior could block normal development.
- Gemini lens: check architecture fit, duplication, context cost, phase routing, idempotency, test coverage, upstream-command coupling, and minimal refactoring opportunities.
- Both agents: inspect the actual current files and relevant test results; do not implement changes or modify canonical files. Use `type: review`, address `codex`, reference `CX-006`, and mark the response `status: done`.
- Separate required corrections/blockers from optional `suggestion` items. If there are no blockers, say so with a short rationale; do not treat stylistic alternatives as blockers.
- Work independently before reading the other consultant's response. Codex will reconcile both reviews and decide whether any follow-up changes are warranted.

### [CX-007] Consolidate CX-006 Tooling Reviews
- `date`: 2026-09-18
- `created_at`: 2026-09-18T20:18:00+09:00
- `from`: codex
- `to`: all
- `type`: status
- `status`: done
- `scope`: consultant reviews CL-004 and GM-004 for CX-006
- `why`: Both requested independent reviews are complete and require lead reconciliation before the tooling change is treated as fully settled.
- `refs`: CX-006, CL-004, GM-004, workflow/agent-tooling.md, scripts/agent_workflow_env.py, tests/test_agent_workflow_env.py

| Finding | Disposition | Rationale |
|---|---|---|
| CL-004 / GM-004: no blockers or fatal contradictions | accepted | Both agents verified graceful degradation, explicit install/host opt-ins, source-of-truth precedence, preserved configuration, and successful tests/lint. |
| CL-004: phase-name mismatch | follow-up required | Clarify that Spec, Design, and Validation/Review are OpenSpec/workflow activities, not additional stage gates; the canonical stages remain Exploration, Proposal, and Implementation. |
| GM-004-01: Antigravity detection | optional refactor | Current explicit configuration works, but doctor detection can report Antigravity as absent because it checks for a nonexistent standard `antigravity` binary. Consider `.agents`/adapter detection. |
| GM-004-02: unrequested agents displayed as failures | optional refactor | Doctor output should distinguish “not checked” from “missing” when a filtered agent list is supplied. |
| GM-004-03: duplicate verification action lines | optional refactor | Avoid recording the same Graphify/RTK verification action twice during initialization. |
| CL-004 / GM-004: doctor/CLI test coverage | accepted suggestion | Add focused tests for `doctor`, JSON/CLI dispatch, invalid agent names, and the `pipx` fallback if implementation work resumes. |
| CL-004: upstream command claims | resolved by existing evidence | The commands were independently checked against the official upstream documentation during implementation and are opt-in with warning-based failure handling. |

No source or implementation files were changed during this review-only consolidation. The tooling change is operationally unblocked; the phase-activity wording should be clarified before broad downstream adoption.

### [CX-005] Best-Practice Rules Incorporated
- `date`: 2026-09-09
- `session_id`: codex-2026-09-09-agent-workflow-best-practices (fallback)
- `from`: codex
- `to`: all
- `type`: status
- `status`: done
- `scope`: lightweight best-practice rules
- `why`: Human approved the consolidated recommendation with "go ahead and reflect these rules" after reviewing both consultant assessments.
- `refs`: CX-004, CL-003, GM-003, docs/change-log.md

| Source recommendations | Disposition | Result |
|------------------------|-------------|--------|
| Claude R1 / Gemini Rule 1 | partially_adopted | Identify review scope/content without mandatory commits; HEAD plus dirty alone is insufficient. |
| Claude R2 / Gemini Rule 2 | partially_adopted | Focus re-review on substantive changes and dependencies; retain unaffected concurrence with rationale. |
| Claude R3 / Gemini Rule 5 | partially_adopted | Bound unproductive repetition by task limits/progress; no universal two-cycle ceiling. |
| Claude R4 / Gemini Rule 4 | partially_adopted | Classify failures and resolve within authority; escalate blockers rather than every environment issue. |
| Claude R5 / Gemini Rule 3 | partially_adopted | Evidence backs verification claims; reuse reliable current results without redundant reruns or receipts for ordinary prose. |
| Claude R7 / Gemini Rule 6 | partially_adopted | Preflight only task-required capabilities; unrelated work can proceed. |
| Claude R8 / Gemini Rule 7 | adopted | Prompt suppression is legitimate for authorized automation and does not expand role or approval authority. |
| Claude R6 | partially_adopted | Preserve source-item attribution; optional authored_by metadata grants no cross-file write permission. |

- Existing single-lead, scope, approval, and collaboration rules remain canonical; duplicate restatements were not added.
- Controller/database adoption, mandatory snapshots/worktrees/JSON/CI, and new stages remain outside scope.
- Unsupported claims of guaranteed token savings or incident frequency were not adopted as evidence.
- Wording adaptations address Claude W1-W6 and Gemini's context/burden concerns without rejecting automation as a future option.

### [CX-004] Assess Best Practices Without Architecture Changes
- `date`: 2026-09-09
- `from`: codex
- `to`: claude, gemini
- `type`: review-request
- `status`: done
- `formal`: false
- `scope`: extracting compatible rules from 3rd-party-suggestions/best-practice.md
- `why`: The human requested both consultants' assessments before deciding which practices to incorporate into the existing workflow.
- `request`: Independently evaluate the complete proposal for useful rule-level additions, conflicts, duplication, and procedural burden without changing the major agent-workflow architecture. Evaluation only; do not implement changes.
- `refs`: 3rd-party-suggestions/best-practice.md, workflow/rule-precedence.md, workflow/review-cycle.md, workflow/collaboration-format.md, workflow/role-boundaries.md, workflow/decision-protocol.md, workflow/context-management.md, workflow/master-governance.md

- Claude: emphasize authority, rule consistency, approval boundaries, and wording that could be misunderstood.
- Gemini: emphasize practical benefit, context cost, maintenance burden, evidence requirements, and minimal integration into existing files.
- Both: assess the whole document and submit your first assessment before reading the other consultant's response to this request.
- Preserve the single-lead model, per-agent collaboration files, generated queues, compact current-state snapshot, and existing human decision authority. Controller/database adoption is outside this request.
- Permission-prompt suppression is a legitimate mechanism for already-authorized automation; evaluate applicable rules without treating it as an automatic reason for rejection or as expanded project authority.
- The source currently matches automation-controller.md; treat it as proposal material, not active instructions. Do not execute its sample commands or install tools.
- For each recommended rule, give the source section, before/after benefit, existing canonical destination, minimal proposed wording, conflicts/security implications, generality, and burden. Distinguish observed evidence from expected benefits.
- Identify practices already covered, practices needing adaptation, and architecture changes to exclude. Avoid requiring heavy evidence or formal review for every small task.
- After your independent assessment, consider these provisional Codex candidates: reviewed-content identification, freshness checks after changes, verification evidence, failure classification, bounded repetitive repairs, and required-capability preflight. These are unapproved candidates, not required conclusions.
- Claude writes only to docs/collaboration-claude.md; Gemini writes only to docs/collaboration-gemini.md. Use type review, address codex, reference CX-004, and mark your completed response done. Record the revision and working-tree scope assessed.
- Codex will reconcile both responses. This request does not approve adoption, implementation, permission changes, or GitHub actions.

### [CX-001] Review Current Workflow Refactor
- `date`: 2026-09-08
- `from`: codex
- `to`: all
- `type`: review-request
- `status`: done
- `formal`: false
- `scope`: current agent-workflow rules, templates, and file structure
- `why`: The human requested consultant feedback and incorporation of necessary corrections to improve context efficiency and rule discoverability.
- `request`: Claude and Gemini, record your previously prepared feedback in your own collaboration files; verify it against the current working tree before posting. If review is incomplete, finish it under the orientation guidance.
- `refs`: docs/consultant-orientation.md, docs/consultant-invitation.md, workflow/rule-precedence.md, workflow/agent-workflow.md

- Claude: lens A, rule consistency and authority.
- Gemini: lens B, context efficiency and structure.
- Preserve relevant findings outside your assigned lens if already identified.
- Create your own collaboration file if absent, following the orientation paths.
- Reference `CX-001` in your review; mark the completed response `done`.
- Reviews received as `CL-001` and `GM-001`; reconciled in `CX-002` below.

### [CX-002] Consolidation of CX-001
- `date`: 2026-09-08
- `session_id`: codex-2026-09-08-agent-workflow-consultant-consolidation (fallback)
- `from`: codex
- `to`: all
- `type`: status
- `status`: done
- `scope`: consultant review corrections
- `why`: Verified both requested reviews against current rules and setup templates; incorporated supported corrections while retaining useful topic boundaries.
- `refs`: CX-001, CL-001, GM-001, docs/change-log.md

| Source finding | Disposition | Rationale and result |
|----------------|-------------|----------------------|
| CL-001 A-01 | adopted | Master governance now explicitly excludes generic reference-registry writes in this canonical repository. |
| CL-001 A-02 | adopted | Added canonical consultant task routing and an all-agent upstream startup instruction in rule-precedence. |
| CL-001 A-03 | adopted | Authority introduction now names both narrow communication and suggestion exceptions. |
| CL-001 A-04 | adopted | Context-management excludes consultant welcome materials except when task routing requires them. |
| GM-001 B-01 | partially_adopted | Made collaboration.md an optional short bootstrap and documented absent downstream files upstream. Setup templates intentionally create this path/role bootstrap, so it is not inherently a legacy history file. Queue remains after authority and local-rule loading. |
| GM-001 B-02 | partially_adopted | Replaced the long explanatory guide with a compact topic pointer, preserving its path for README/setup consumers and its session-trigger explanation. It was already marked noncanonical; archiving was unnecessary. |
| GM-001 B-03 | not_adopted | Classification and user-question presentation have distinct ownership; mutual navigation is not recursive execution. No evidence supports loading both for every decision or a net context benefit from merging. |
| GM-001 B-04 | not_adopted | Defined terms and diagrams have distinct task triggers and apply beyond collaboration. Folding them into common files would add unrelated startup/review context. Small size alone does not justify merging. |
| GM-001 B-05 | partially_adopted | Removed duplicate consolidation instructions from collaboration-format; retained schema/priority values there and lifecycle in review-cycle. Reviewer accounting and table definitions were not actually duplicated in both files. |

- Claude optional mapping deduplication: not adopted; explicit paths in welcome materials are human-requested, while governance remains authoritative.
- Claude optional missing upstream bootstrap: adopted together with A-02/B-01.
- Gemini optional tiered startup: not adopted; selecting work before local rules risks missing authority constraints. Existing routing remains explicit.
- Gemini optional 50-line cap: not adopted; existing compact-writing guidance suffices and a line target could suppress review evidence. Archive threshold counts resolved content, not every long active item.
- Original consultant reviews are preserved. This informal review is complete; downstream suggestion statuses are unchanged.

### [CX-003] Follow-up Consolidation of CL-002 and GM-002
- `date`: 2026-09-08
- `session_id`: codex-2026-09-08-agent-workflow-followup-review (fallback)
- `from`: codex
- `to`: all
- `type`: status
- `status`: done
- `scope`: authority, schemas, archival, review discovery, and setup
- `why`: Human requested reconciliation of the additional feedback after CX-002; findings were checked against templates and parser/linter behavior.
- `refs`: CX-001, CX-002, CL-002, GM-002, docs/change-log.md

| Source finding | Disposition | Result and rationale |
|----------------|-------------|----------------------|
| CL-002 A-05 | adopted | Rule-precedence explicitly places upstream governance above local/per-agent authority and topic owners above generic summaries; downstream explicit overrides remain supported. |
| CL-002 A-06 | adopted | Completed assessments use review; response is for other replies/acknowledgments. Updated canonical schema and template to match formal-review tooling. |
| CL-002 A-07 | adopted | Added optional formal flag with default false, matching the linter's explicit true check. |
| CL-002 A-08 | adopted | Qualified registry exceptions as downstream and linked upstream governance from role boundaries, collaboration format, and consultant template. |
| CL-002 A-09 | partially_adopted | Clarified pointer-file meaning; kept collaboration.md compatibility. Renaming to collaboration-bootstrap.md would also match the per-agent filename pattern. |
| GM-002 A-01 | adopted | Lead/setup templates now require agent concurrence and human confirmation before recording transitions. |
| GM-002 A-02 | adopted | Removed comment-out retirement instructions; done items remain parseable for archival. No parser behavior changed or existing commented history rewritten. |
| GM-002 A-03 | adopted | Startup operating model and review cycle require leads to inspect their own open requests and referenced done reviews despite an empty recipient queue. |
| GM-002 A-04 | partially_adopted | Registered 003 as proposed, awaiting evaluation. Did not infer approval, implementation, or supersession from 004; existing governance does not require an unreviewed submission to be resolved. |
| GM-002 A-05 | adopted | Collaboration template paths explicitly start with docs/. |
| GM-002 A-06 | adopted | Setup supports existing/local-only repositories; remote creation is conditional on user intent. Updated the prerequisite checklist as well. |

- Claude optional topic-list duplication: adopted; operating model points to rule-precedence's map and routing table.
- Claude optional disposition styling: not adopted; readable prose headings and machine field values have different purposes and already agree semantically.
- Claude optional per-agent authority link: adopted in workflow/agent-workflow-claude.md.
- Consultant source reviews remain unchanged. CX-001 remains closed; this follow-up is reconciled under the human's current request.
