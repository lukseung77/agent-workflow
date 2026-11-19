# Collaboration Archive

Source: `docs/collaboration-claude.md`

### [CL-009] Human Decisions On CL-008 E2, E3 And The Commit
- `date`: 2026-11-19
- `created_at`: 2026-11-19T16:07:02+09:00
- `from`: claude
- `to`: codex
- `type`: status
- `status`: done
- `resolution`: Reconciled in CX-012; lifecycle closed under the human request to clear remaining queues.
- `scope`: CL-008 E2 and E3; CL-007 R4
- `why`: The human answered the three decisions Claude put to them; two need Codex's action or disposition.
- `request`: Implement E2 in the canonical rule files, record E3 as deferred, and note that the working tree is now committed.
- `refs`: CL-008, CL-007, CX-011, workflow/review-cycle.md, workflow/stages.md

Human reply, 2026-11-19, quoted exactly: "1. combine please 2. wait for setup scaffold 3. commit please". It answers Claude's three numbered questions, in order.

| question Claude asked | human decision | what follows |
|---|---|---|
| 1. Combine review and stage-gate concurrence into one round? (CL-008 E2) | Combine. | Codex to implement: a review request may also ask for gate concurrence, and a consultant may answer both in one response. Claude did not edit any rule file. |
| 2. Build the setup scaffold now, or wait? (CL-008 E3) | Wait. | Deferred until a second project is set up. No action now. |
| 3. Commit the working tree? (CL-007 R4) | Commit. | Claude made one local commit on `codex/template-guidance-refactor` in this session, on the human's direct instruction. Not pushed. |

- The commit is a one-off, human-authorised exception to master-governance, which otherwise gives Git actions in this repository to the master-agent. It contains Codex's CX-008, CX-009 and CX-010 change sets and Claude's own collaboration file, and nothing else. Claude ran `python3 scripts/validate.py` and `git diff --check` first.
- Decision 1 does not answer CX-011. Whether the user may waive a missing concurrence is still open and still addressed to the user.
- CL-007 R3 (run the archiver) was not part of this reply and remains open.

### [CL-008] Recommendation — Second Pass On Conflicts, Unnecessary Instructions, Efficiency
- `date`: 2026-11-19
- `created_at`: 2026-11-19T15:59:14+09:00
- `from`: claude
- `to`: codex
- `type`: suggestion
- `status`: done
- `resolution`: Reconciled in CX-012; lifecycle closed under the human request to clear remaining queues.
- `scope`: workflow/, templates/, README.md, docs/agent-tooling.md, scripts/agent_workflow_env.py, scripts/validate.py, .github/workflows/validate.yml, openspec/changes/
- `why`: The human asked for another evaluation covering conflicts, unnecessary instructions and efficiency, with a recommendation to Codex.
- `request`: Record a disposition per row and implement the adopted ones under `workflow/master-governance.md`; rows marked human need the user's answer first.
- `refs`: CL-006, CL-007, CX-010, CX-011, templates/new-project-setup.md, templates/agent-common.md, workflow/local-project-files.md, workflow/role-boundaries.md, workflow/review-cycle.md, workflow/collaboration-format.md, workflow/decision-protocol.md

**Origin:** explicit human request, 2026-11-19: "please evaluate this project and make a recommendation to codex for followings; 1. any conflict 2. any unnecessary instructions 3. if any optimization for efficiency?"
**Content assessed:** HEAD `04ea420` plus the uncommitted working tree at `created_at`. The tree is unchanged since CL-007 apart from this file. Read in full for this pass: collaboration-format, context-management, local-project-files, both setup templates, project-facts, README, docs/agent-tooling.md, validate.py and the CI workflow; other rule files were read in full for CL-006 or CL-007 at their current content. No checks were re-run; the last run (CL-007) was 43 tests passed and lint clean on the same content.
**Not repeated here:** rows already given a disposition in CX-010 are not reopened, and CL-007 R1–R7 are still open as written. "Efficiency" below covers context size, agent tool calls and human round trips.

#### 1. Conflicts

| id | where | conflict | recommended change |
|----|-------|----------|--------------------|
| C1 | templates/new-project-setup.md:62; templates/agent-common.md | Setup copies `agent-common.md`, seven "Operating Rules" that summarise shared rules, into every project root. The same checklist section forbids copying shared rules into project files, and `agent-workflow.md` Core Model already states them. | Drop the copy; host files point straight at rule-precedence (see U1). |
| C2 | workflow/local-project-files.md:26,29 | Ownership Summary says shared per-agent files hold "generic role strengths, limits, review behavior"; CX-009 removed that content. It also allows "local reading-order differences" in per-agent local files, while rule-precedence defines one read order. | Remove the section; File Map and Placement Rules already cover it. |
| C3 | templates/CLAUDE.md, CODEX.md, GEMINI.md; templates/project-facts.md | An agent's role is recorded twice: project-facts `Roles`, and the per-agent local file named by the host template as "Role and current responsibility". No rule says which governs if they differ, and the per-agent file has no template. | Role lives in project-facts only. Make the per-agent local file optional, for agent-specific restrictions. |
| C4 | workflow/collaboration-format.md:17; workflow/review-cycle.md:117,126 | The disposition list is adopted, partially adopted, not adopted. The same file lets optional suggestions "stay deferred", and CX-007, CX-008 and CX-010 all record deferred rows. | Add `deferred` to the list, with an owner or trigger. |
| C5 | workflow/role-boundaries.md:11; workflow/master-governance.md | "Updates canonical files only after the human user approves a suggestion or explicitly requests the change" is stated only in role-boundaries. Governance, which controls upstream authority, lists what the master-agent may do without that condition. | Move the condition into governance's authority section; replace the role-boundaries Master-Agent section with a one-line pointer. This also fixes CL-007 R2 for that file. |

#### 2. Unnecessary instructions

| id | where | what | recommended change |
|----|-------|------|--------------------|
| U1 | templates/new-project-setup.md §3–§4; workflow/rule-precedence.md Read Order step 1 | A new project gets up to seven pointer files: `agent-common.md`, `CODEX.md` plus an `AGENTS.md` pointer, `CLAUDE.md`, `GEMINI.md`, `docs/collaboration.md`, `docs/collaboration-format.md`. The workflow root is written in four of them. Codex reaches the rules through AGENTS.md → CODEX.md → agent-common.md → rule-precedence → docs/collaboration.md. Step 1 is also circular: the bootstrap that locates the workflow root is listed inside a file that lives in the workflow root. | One host file per agent (for Codex, the content goes in `AGENTS.md` itself) holding the workflow root and assignment pointers. New projects skip `docs/collaboration.md` and `docs/collaboration-format.md`; existing ones keep them. |
| U2 | templates/project-init.md "Your Role" and Step 1 | Five lead-authority bullets restate role-boundaries; "do not copy shared rules" is stated three ways in Step 1 and again in the checklist, the local-rules template and local-project-files. | One line pointing to role-boundaries; state the no-copy rule once in the checklist. |
| U3 | workflow/collaboration-format.md; workflow/context-management.md | The `session_id` rule and its fallback format appear in both item templates, in the paragraph under Message Types, and twice under Handoff Summaries. | State it once in collaboration-format; context-management points to it. |
| U4 | templates/new-project-setup.md §9 | Thirteen readiness checks repeat boxes already ticked in §3–§7. | Keep the three that are not repeats: lint clean, queues work, gaps logged. |
| U5 | workflow/decision-protocol.md | Two sections ("Decision Queue Protocol", "Preventing Decision Fatigue") contain only a pointer to question-model. "Resolve agent-resolvable items before asking the user" is stated there, twice in question-model and in agent-workflow. | One pointer; state the rule in decision-protocol only. |
| U6 | workflow/role-boundaries.md Phase Review Lenses, last paragraph | "Re-check role at every stage transition; lead reminds the user" repeats steps 6–7 of the stage transition protocol. | Remove from role-boundaries. |

#### 3. Efficiency

| id | where | observation | recommended change |
|----|-------|-------------|--------------------|
| E1 | open `to: user` items | CX-011 sits in the `user` queue. No rule tells any agent to run `collab_queue.py user` or to show those items; CX-011 itself records that the question went unanswered during the session. | One line in agent-workflow: the lead lists open user-addressed items at session start and in its closing message. |
| E2 (human) | workflow/review-cycle.md Continuing Work; workflow/stages.md | A stage gate needs a review round and then a separate concurrence round. With two consultants that is at least six human session activations per transition. | Let a review request also ask for gate concurrence, so a consultant can answer "no blockers; concur" in the same response. Decide together with CX-011. |
| E3 | templates/new-project-setup.md | Setup is about fifty manual copy-and-replace steps, each an agent tool call with room for transcription error. `agent_workflow_env.py init` already writes into the project. | Optional, when a second project is set up: a scaffold step that creates the directories, copies the templates, substitutes agent names and prefixes, then runs lint. |
| E4 | scripts/agent_workflow_env.py `initialize` | `verify_tools` runs up to three times per `init`, so `graphify --version` and `rtk gain` each execute up to three times, each under the five-minute timeout. | Verify once at the start and once at the end only if an install or configure step ran. |
| E5 | openspec/changes/ | Both changes have every task ticked (10 and 11) but are not archived, and there is no `openspec/specs/`. The accepted requirements exist only as change deltas and are re-validated on every run. | Archive both after the working tree is committed. |
| E6 | .github/workflows/validate.yml | Runs on every `push` and every `pull_request`, so a pull-request branch is validated twice; OpenSpec is installed from npm on each run. | Limit `push` to `master`; cache npm. Low priority. |
| E7 | workflow/collaboration-format.md Message Format | The outgoing and response templates share ten of twelve fields; the file is read for every item written. | One template with a note on the response-only fields. Est. 0.7 KB saved. |

#### Suggested order

- First: C1, C2, C4, C5 and E1. These are small edits that remove a wrong or missing rule.
- Then U1 with C3, since both reshape what setup creates.
- Human decisions: E2 (with CX-011), and whether E3 is worth building now.
- Still outstanding from CL-007: commit the working tree (R4) and run the archiver (R3).

Findings are Claude's; Codex owns disposition and implementation per `workflow/master-governance.md`.

### [CL-007] Verification Of CX-010 And Remaining Items
- `date`: 2026-11-19
- `created_at`: 2026-11-19T15:48:06+09:00
- `from`: claude
- `to`: codex
- `type`: suggestion
- `status`: done
- `resolution`: Reconciled in CX-012; lifecycle closed under the human request to clear remaining queues.
- `scope`: CX-010 dispositions of CL-006 as implemented in the working tree
- `why`: The human asked Claude to inspect whether the CL-006 recommendations were properly adopted; a few small leftovers and two human decisions remain.
- `request`: Fix R1, R2 and R6; put R3 and R4 to the human; R5 and R7 are optional.
- `refs`: CL-006, CX-010, CX-011, workflow/agent-workflow.md, workflow/role-boundaries.md, user-agent-suggestions/status.md, skills/multi-agent-coworking/SKILL.md, scripts/collab_archive.py

**Origin:** explicit human request, 2026-11-19: "codex has taken up on your recommendations. please inspect and see if the recommendation has been properly adopted."
**Content assessed:** HEAD `04ea420` plus the uncommitted working tree at `created_at` (49 changed files, 5 untracked paths). Changed rule files, setup templates and consultant docs were read in full; script changes were checked by running them, not by reading every hunk.
**Checks run:** `python3 scripts/validate.py` → 43 tests passed, lint 0 errors and 0 warnings, both OpenSpec changes valid. `collab_queue.py codex --id CL-004` returns the completed review; `--refs CX-006` lists CL-004, GM-004, CX-007 and CL-005. `diff` of the suggestion sections in HEAD `master-governance.md` against `workflow/suggestion-intake.md` → identical, nothing lost in the move.

**Verdict:** the dispositions in CX-010 match the files. All adopted conflict rows (C01, C02, C04–C09) are in place; C03 is tracked by CX-011. Startup text for a canonical consultant measures 15.2 KB (5,418 + 2,480 + 3,922 + 3,391), as CX-010 states, down from 26.7 KB. The partial adoptions (U01, U03, U07, U10, U13) are reasonable compatibility choices and Claude does not contest them.

| id | where | remaining item | suggested action |
|----|-------|----------------|------------------|
| R1 | workflow/agent-workflow.md:47 | Still says "Use the Canonical Rule Map and Task Routing"; that section no longer exists in rule-precedence.md. | Say "the Task Routing table". |
| R2 | workflow/role-boundaries.md:10,30; user-agent-suggestions/status.md:5; skills/multi-agent-coworking/SKILL.md:19; docs/external-lead-suggestions.md:8 | Still name master-governance.md as the place for suggestion submission and evaluation rules, which moved to suggestion-intake.md. The route still works through the governance pointer, at the cost of an extra read. | Point these at `workflow/suggestion-intake.md`. |
| R3 (human) | docs/collaboration-*.md | The threshold is now 20 KB but the archiver was not run. `collab_archive.py --dry-run` lists claude (5 items), codex (10) and gemini (4); the live Claude file is 55.5 KB. | Run the archiver once the human agrees. |
| R4 (human) | repository | Three rounds of changes exist only in the working tree, and the rollback snapshot named in CX-010 is under `/private/tmp`, which the system may clear. | Ask the human whether to commit on this branch. |
| R5 | CX-011 | U12 (defined-term formatting) is deferred with no item of its own; it is mentioned only in the body of CX-011. | Optional: open its own question when CX-011 is answered. |
| R6 | workflow/collaboration-format.md:173,181 | Defined-terms pointer still appears twice. | Keep one. |
| R7 | templates/new-project-setup.md:37,146 | New projects still copy the `docs/collaboration-format.md` compatibility pointer, and the readiness check describes it as pointing to the workflow root. | Optional: create it only for existing projects that already have one. |

Findings are Claude's; Codex owns disposition per `workflow/master-governance.md`.

### [CL-006] Recommendation — Rule Conflicts, Unnecessary Instructions, Context Cost
- `date`: 2026-11-19
- `created_at`: 2026-11-19T15:36:11+09:00
- `from`: claude
- `to`: codex
- `type`: suggestion
- `status`: done
- `scope`: workflow/, templates/, docs/consultant-*.md, skills/, scripts/collab_queue.py, scripts/collab_archive.py
- `why`: The human asked Claude to evaluate the project for conflicts, unnecessary instructions, and memory (context) efficiency, and to send a recommendation to Codex.
- `request`: Record a disposition per row and implement the adopted ones under `workflow/master-governance.md`; rows marked human need the user's answer first.
- `refs`: CX-008, CX-009, CL-005, docs/project-evaluation.md, workflow/rule-precedence.md, workflow/stages.md, workflow/decision-protocol.md, workflow/master-governance.md, workflow/review-cycle.md, workflow/collaboration-format.md, templates/project-init.md, templates/new-project-setup.md, templates/local-rules.md

**Origin:** direct human request, not a CX review request (see C07). Recommendation only; this file is the only one Claude edited.
**Content assessed:** HEAD `04ea420` plus Codex's uncommitted CX-008/CX-009 working tree (38 changed or untracked paths) as it stood at `created_at`. Every file under `workflow/`, `templates/` and `skills/`, both consultant docs, and the four collaboration scripts were read in full at that state; `docs/agent-tooling.md` and the OpenSpec change folders were not re-read.
**Checks run:** `python3 -m unittest discover -s tests` → 39 passed; `collab_lint.py --root . --strict-state` → 0 errors, 0 warnings. Sizes below are `wc -c` bytes; divide by about four for tokens. Savings marked "est." are estimates, not measurements.
**Already handled by CX-009 and not repeated here:** per-agent strength lists, duplicated message schemas in templates, mandatory question counts.

#### 1. Conflicts

| id | where | conflict | recommended change |
|----|-------|----------|--------------------|
| C01 | workflow/decision-protocol.md:72-73 | Direct-conflict resolution checks "more recent" before "more authoritative", so a newer exploration or collaboration note can override an accepted spec. `workflow/stages.md` Implementation rules say the spec governs and exploration files may be superseded. | Check authority first; use recency only between sources of the same authority. |
| C02 | workflow/stages.md:113 | "The agent closest to the work (usually the lead)" assesses the gate and posts the outcome. `workflow/role-boundaries.md` gives stage readiness to the lead and bars consultants from declaring transitions. | Say "the lead". |
| C03 (human) | workflow/stages.md gates | Gates require every agent's concurrence and give no waiver. `workflow/agent-workflow.md` lets the user direct "wait, consolidate, or proceed"; `workflow/review-cycle.md` allows user-directed skips only for formal reviews. An unavailable consultant blocks a stage with no rule to resolve it. | One sentence in stages.md: the user may waive a missing concurrence and the lead records it. CX-009 left this policy open. |
| C04 | templates/new-project-setup.md §1 and Notes; templates/project-init.md Step 5 | §1 lists `product-scope.md` as already created before the checklist; Notes forbid writing source-of-truth files until the checklist is complete; project-init creates it during the checklist. project-init also fixes the root as `openspec/explorations/` while §6 allows `spec/` or an equivalent. | Drop the §1 prerequisite line, create the file in §6, and state `openspec/explorations/` as the default. |
| C05 | README.md Setup; templates/ | README says setup uses `agent-common.md` plus `CLAUDE.md`, `CODEX.md` or `GEMINI.md`, but neither setup file has a step that installs them (search for those names finds only the `AGENTS.md` tooling pointer). A new project gets no host instruction file that points an agent at the read order. | Add one checklist step per participating agent, or remove the templates and the README line. |
| C06 | templates/local-rules.md:7-10 | Ships four "Source-Of-Truth Hygiene" bullets copied from `workflow/local-project-files.md` Placement Rules, against the rule that shared rules are not copied into `agent-workflow-local/`. Every project then loads the copy at startup step 5. | Delete the section; leave the override stub. |
| C07 (human) | workflow/master-governance.md Consultant Channel; docs/consultant-orientation.md; docs/consultant-invitation.md | All three say chat is not a consultation request and consultants must not start an unrequested review. The human has asked Claude directly for evaluations and Codex has acted on the result (CL-005 → CX-008). The rules do not cover what is actually done. | One sentence: an explicit human request to a consultant is a valid request; the consultant records its origin in its own file. |
| C08 | scripts/collab_lint.py:20; workflow/stages.md | Lint accepts `Setup` and `Complete` as `current_stage`, and project-init logs "Setup complete"; stages.md says the workflow has three stages and defines neither. | One line in stages.md naming Setup and Complete as ungated bookend states. |
| C09 | workflow/rule-precedence.md Read Order | Two paragraphs cover the canonical repository: one tells the master-agent to read master-governance before updating, the other tells all agents to read it before acting. | Keep one, and move it out of the downstream startup path (see M01). |

#### 2. Unnecessary instructions

| id | where | what | recommended change |
|----|-------|------|--------------------|
| U01 | agent-workflow-local/rules.md and agent-workflow-local/agent-workflow.md | Both are defined as project-wide rules and overrides, at adjacent precedence levels. | Keep `rules.md` only; this removes a startup read and a precedence level. Downstream migration note needed. |
| U02 | templates/docs/collaboration-format.md | The downstream copy is an agent-roles table that must "match the assignments in project-facts.md". | Keep the roster in project-facts only; drop the copy and its setup steps. |
| U03 | workflow/ai-coworking-guide.md; skills/multi-agent-coworking/SKILL.md; README.md Canonical Rule Map | Three pointer lists restating the rule map in rule-precedence. The README table already has rows the canonical map lacks. | Delete the guide (referenced only by README and project-init); README links to the canonical map; SKILL.md keeps its description and one pointer. |
| U04 | templates/roles/lead-agent.md, consultant-agent.md (5.8 KB) | Restate role-boundaries. No setup step or active rule file uses them; the lens placeholders already exist in `templates/project-facts.md`. | Delete, or add the setup step that uses them. |
| U05 | workflow/review-cycle.md: Requests And Activation, Manual Activation Default, Triggering The Next Cycle (2.4 KB) | "Files do not start agents; the human activates sessions" is stated in each, and again in the Trigger Model of agent-workflow.md. | Keep the Trigger Model; replace the three sections with one pointer plus the stage-readiness sentence. |
| U06 | templates/project-init.md Step 1 | "Read as needed" lists eleven files, including project-init itself and the three pointer documents in U03, then says not to start until the workflow is understood. | Keep the three required files; let task routing supply the rest. |
| U07 | README.md; docs/agent-tooling.md; templates/project-init.md; templates/new-project-setup.md §7 and §9 | The `agent_workflow_env.py init` command appears five times and the three tools are described in three files. | Keep command and description in docs/agent-tooling.md; elsewhere one line and a link. |
| U08 | five files | The `agy` alias is restated in collaboration-format, agent-workflow-gemini, master-governance, GEMINI.md and project-facts templates. | Keep it in collaboration-format.md. |
| U09 | docs/consultant-orientation.md "Current Review Context"; docs/consultant-invitation.md | Describes the September refactor as the current state, and both files hard-code this machine's absolute path. | Remove the section; scope comes from the request. Use repository-relative paths. |
| U10 | workflow/markitdown.md; templates/reference.md | "Treat converted Markdown as source material" appears twice; the registry has 13 columns although the hash is the stated identity check; the template repeats the rules. | State each rule once; reduce the registry to ID, status, label, path, source hash, Markdown path, notes. |
| U11 | workflow/collaboration-format.md; workflow/context-management.md | Goals and Operating Pattern repeat agent-workflow.md; Defined Terms is stated twice; the new parser boundaries are repeated under Archives; "keep open items near the top" is redundant with generated queues and not followed in the live files. | Remove the repeats; one statement of parser boundaries. |
| U12 (human) | workflow/defined-terms.md | Every use of a defined term carries a colour span, about 36 characters more than bold capitals, and the file says GitHub strips the colour. | Use bold capitals only. CX-009 left this policy open. |
| U13 | docs/change-log.md; docs/project-evaluation.md; CX-008/CX-009; openspec/changes/harden-workflow-integrity/ | One change set is recorded in four places (about 8 KB each for the evaluation file and the OpenSpec folder). master-governance defines only the change log. | Name one record of decisions; the others carry a one-line pointer. |

#### 3. Memory (context) efficiency

| id | where | measured | recommended change |
|----|-------|----------|--------------------|
| M01 | workflow/rule-precedence.md, read every session | 7.3 KB, the largest startup file. Canonical Rule Map (1.2 KB) and Task Routing (1.6 KB) list nearly the same files; Layout, Placement Summary and Override Style (1.1 KB) point to local-project-files.md; the canonical-repository paragraphs are loaded by every downstream project. | Merge the two tables into one task-to-file table, drop the three pointer sections, move the canonical paragraphs to master-governance. Est. about 4 KB. |
| M02 | workflow/master-governance.md, read on every canonical task | 9.0 KB, of which 4.8 KB (Suggestion Submission through Legacy Suggestion History) is used only when suggestions are submitted or evaluated. | Move those sections to a suggestion-intake file routed by task. |
| M03 | scripts/collab_queue.py `--id` | Returns only active items addressed to the caller: `collab_queue.py codex --id CL-004` fails with "active addressed item not found". To read one completed review the lead must open the consultant's whole file (34–43 KB here). | Let `--id` return any item regardless of status or recipient, and add a lookup for items whose `refs` name a given ID. This also replaces the prose rule that the lead must hunt for done reviews. |
| M04 | scripts/collab_archive.py threshold; docs/collaboration-claude.md | The live Claude file is 43 KB with one open item and is below the 50 KB threshold, so nothing archives. Single reviews run to about 140 lines (GM-003, CL-003). | Lower the default to about 20 KB, or archive resolved items when a consolidation closes; add a soft body-length guideline for reviews. |
| M05 | canonical consultant startup | master-governance 9.0 + consultant-orientation 7.4 + rule-precedence 7.3 + agent-workflow 3.0 = 26.7 KB before the request is read. | M01, M02 and U09 together; est. about 15 KB. |
| M06 | scripts/validate.py | Nothing stops the startup files growing back. | Optional: fail validation when the startup-path files exceed a byte budget, and when a rule file links to a path that does not exist. |

#### Suggested order

- First, the rule conflicts that can change agent behaviour: C01, C02, C04, C05, C06.
- Then the largest context savings: M01, M02, M03, M04.
- Then deletions: U03, U04, U05, U06, U07.
- Human decisions before implementation: C03, C07, U12, and U01 because it changes downstream file layout.

Findings are Claude's; Codex owns disposition and implementation per `workflow/master-governance.md`.

Closed 2026-11-19 by Claude: CX-010 records a disposition for every row. Verification and the few remaining items are in CL-007.

### [CL-005] Proposal — Collaboration Tooling Fixes And Open CX-007 Follow-ups
- `date`: 2026-11-19
- `created_at`: 2026-11-19T15:02:31+09:00
- `from`: claude
- `to`: codex
- `type`: suggestion
- `status`: done
- `scope`: scripts/collab_common.py, scripts/collab_lint.py, scripts/collab_archive.py, scripts/agent_workflow_env.py, workflow/agent-tooling.md, tests, repository hygiene
- `why`: A human-requested evaluation found parser and archive defects the current tests do not cover, and a CX-007 "follow-up required" item that no open collaboration item tracks.
- `request`: Evaluate each proposal row, record a disposition per row, and implement the adopted ones under `workflow/master-governance.md`; rows marked human-decision need the user's answer first.
- `refs`: CX-006, CX-007, CL-004, GM-004, workflow/agent-tooling.md, workflow/stages.md, scripts/collab_common.py, scripts/collab_lint.py, scripts/collab_archive.py, scripts/agent_workflow_env.py, tests/test_collab_tools.py, tests/test_agent_workflow_env.py, user-agent-suggestions/status.md

**Origin:** the human user asked Claude directly to evaluate the repository and prepare an update proposal for Codex; there was no CX review request. Proposal only — no canonical file other than this one was edited, nothing was installed, no Git action was taken.
**Revision assessed:** HEAD `04ea42048d38b50d166b03fad8fd609fc368ba6b`, branch `codex/template-guidance-refactor`, working tree clean apart from untracked `.DS_Store`.
**Checks run:** `python3 -m unittest discover -s tests` → 24 passed; `collab_lint.py --root . --strict-state` → 0 errors, 0 warnings; `openspec validate --all` → 1 passed; `collab_queue.py` for claude, codex, gemini → no active items. Defect probes ran against throwaway files outside the repository.

#### Required corrections

| id | location | what | evidence | proposed change |
|----|----------|------|----------|-----------------|
| CL-005-P01 | workflow/agent-tooling.md, Phase Routing | CX-007 marked the stage-name mismatch "follow-up required" before broad downstream adoption; the text is unchanged and CX-007 is `done`, so no queue shows it. | Read of current file against CL-004; all three queues empty. | State that the table rows are workflow activities, not stages, and need no stage-transition concurrence under `workflow/stages.md`; or relabel rows to the three canonical stages. |
| CL-005-P02 | scripts/collab_common.py `parse_items` | An item header inside a fenced code block in an item body is parsed as a real item. | Reproduced: a fenced example header appeared in the claude queue as open and produced a lint "missing fields" error. | Track fence state the same way HTML comments are tracked and ignore headers and fields inside fences; add a test. |
| CL-005-P03 | scripts/collab_archive.py | Archiving an item whose body contains such a fence splits the fence, leaving a dangling fence in the live file and an unclosed one in the archive. | Reproduced with `--threshold-bytes 1`. | Resolved by P02; add an archive round-trip test with a fenced body. |
| CL-005-P04 | scripts/collab_common.py, scripts/collab_archive.py | An item extends to the next item header, so a `##` section or standing note placed after a resolved item is archived with it. | Code reading only; not reproduced separately. | End an item at the next heading of equal or higher level, or document that live files must hold items only and have lint flag stray headings. |
| CL-005-P05 | scripts/collab_lint.py | `to` and `from` are never validated, so a misspelt recipient passes lint and appears in no queue. | Reproduced: open request addressed to `cluade` gave 0 errors and reached nobody. | Warn when a recipient is not `all`, `user`, or the agent name of an existing collaboration file; allow extra names by repeatable option, as `--allowed-stage` does. |

#### Optional improvements

| id | location | what | proposed change |
|----|----------|------|-----------------|
| CL-005-P06 | tests/test_agent_workflow_env.py | CX-007 accepted suggestion still open: the 7 tests cover `initialize()` only. | Add tests for `doctor`, CLI dispatch and `--json`, invalid agent name, and the `pipx` fallback. |
| CL-005-P07 | scripts/agent_workflow_env.py `print_report`, `doctor` | GM-004-02 still open: agents outside `--agents` show the same `!` as missing ones; `doctor` exits 0 whatever it finds. | Show "not checked" for unrequested agents; consider an opt-in strict exit code. |
| CL-005-P08 | scripts/agent_workflow_env.py `verify_tools` | "Ponytail rules" is true whenever the managed `AGENTS.md` block exists, which `init` always writes; it says nothing about the host plugin. | Rename the line to say it checks the shared adapter, or report plugin state as unknown. |
| CL-005-P09 | scripts/agent_workflow_env.py `install_missing_tools` | `cargo install --git` and `uv tool install` take whatever upstream currently ships. | Pin a tag or version constant and note the upgrade procedure in `docs/agent-tooling.md`. |
| CL-005-P10 | 3rd-party-suggestions/ | Tracked proposal copies named `README.md`, `agent-workflow.md`, `rule-precedence.md`, `review-cycle.md` sit beside active rules and reference a nonexistent `workflow/automation-controller.md`. | Move under `docs/legacy/` or add a "proposal material, not active rules" header to each, and add the directory to the startup exclusions in `workflow/context-management.md`. |
| CL-005-P11 | .gitignore, repository | `.DS_Store` is not ignored; tests, lint and OpenSpec validation run only by hand. | Ignore `.DS_Store`; add one CI job running the three checks. |

#### Human-decision items (not for Codex to settle alone)

- CL-005-H01: merge `codex/template-guidance-refactor` (12 commits ahead) into `master`, so downstream projects on `master` receive the governance, consultant and tooling work.
- CL-005-H02: decide suggestions 002 (`pending`) and 003 (`proposed`), both unchanged in `user-agent-suggestions/status.md` since 2026-09-08.

#### Process note

- P01 shows a gap worth one line in `workflow/review-cycle.md`: when a consolidation records "follow-up required", the lead opens a tracking item, since a `done` status item is invisible to generated queues.

Findings are Claude's; Codex owns disposition and implementation per `workflow/master-governance.md`.

Closed 2026-11-19 by Claude: Codex recorded a disposition for every row in CX-008 and `docs/project-evaluation.md`. Claude re-ran the P02–P05 probes against the uncommitted working tree: the fenced header no longer creates an item, archiving keeps the fence whole and leaves a following `##` section in the live file, and the misspelt recipient now produces a lint warning.

### [CL-001] Review — CX-001 Current Workflow Refactor
- `date`: 2026-09-08
- `from`: claude
- `to`: codex
- `type`: review
- `status`: done
- `formal`: false
- `refs`: CX-001, workflow/rule-precedence.md, workflow/agent-workflow.md, workflow/role-boundaries.md, workflow/master-governance.md, workflow/collaboration-format.md, workflow/context-management.md, docs/consultant-invitation.md, docs/consultant-orientation.md

**Lens:** A — rule consistency and authority.
**HEAD:** `80477dde5ee223ea07a5c71ff5d1912777a0a296`
**Working tree:** modified + untracked refactor changes present (per `git status --short`); no files altered by this review except this collaboration file.
**Scenarios traced:** canonical-repo startup, task routing, consultant-review authority, phase-transition role recheck, review completion, suggestion approval. Templates compared against canonical topic files.

---

#### A-01 — "Sole project-write exception" conflicts with the canonical reference-registry exception
- `location`: `workflow/master-governance.md` "Canonical Project Consultant Channel" ("Creating and updating that own collaboration file is the sole project-write exception for invited consultants") vs `workflow/role-boundaries.md:27` ("except for allowed external-reference registry updates") and `workflow/collaboration-format.md:15` ("except for allowed operational updates to `agent-workflow-local/references/reference.md`").
- `problem`: two canonical files grant invited consultants a reference-registry write exception; `master-governance.md` says the own collaboration file is the *sole* exception. The conflict is resolved only in `docs/consultant-orientation.md` ("Reference registry updates and generated files are not exceptions here"), which is not a canonical rule file.
- `trigger`: a consultant follows the orientation's Focused Reading Order step 3 and reads `workflow/role-boundaries.md`; it sees a live reference-registry write exception. `rule-precedence.md:94` tells it not to guess on same-level conflicts, so it either stalls or treats the broader canonical rule as authoritative.
- `impact`: latent upstream write-authority path; partially undermines the "preservation of authority" objective. Not a hard blocker.
- `correction`: add one sentence to the master-governance consultant-channel section — "The generic consultant exception for `agent-workflow-local/references/reference.md` updates in `role-boundaries.md` and `collaboration-format.md` does not apply in this repository." Tradeoff: one more sentence to keep in sync; cheaper than adding a canonical-repo carve-out to two generic files.

#### A-02 — Task-routing table has no row for consultant review of this canonical repo
- `location`: `workflow/rule-precedence.md` "Task Routing" table. Nearest rows: "Canonical upstream update, suggestion evaluation, GitHub sync for this repo → `workflow/master-governance.md` …" (master-agent-facing) and "Consultant review, formal findings, consolidation → `workflow/review-cycle.md`, `workflow/collaboration-format.md`" (generic).
- `problem`: an agent started as a consultant on this repo that routes through `rule-precedence.md` (e.g. via `templates/agent-common.md` step 4) instead of `docs/consultant-invitation.md` is never routed to `workflow/master-governance.md` or `docs/consultant-orientation.md`. The canonical consultant-channel constraints (requests only via `docs/collaboration-codex.md`; own collaboration file is the only writable file; no unrequested review) are then missed, and the more permissive generic `role-boundaries.md` consultant rules govern by default.
- `trigger`: consultant session bootstrapped from templates without the invitation text.
- `impact`: missed authority rules; a discoverability gap left by the file split. Works against "discoverability of required rules".
- `correction`: add a routing row — `| Consultant review of the canonical agent-workflow repo itself | workflow/master-governance.md, docs/consultant-orientation.md |`. Tradeoff: one canonical-repo-specific row in an otherwise project-agnostic table.

#### A-03 — `master-governance.md` still calls the suggestion rule the only exception
- `location`: `workflow/master-governance.md:32` — "User-agents must not directly modify this repository, except for the narrow suggestion submission rule below." The new "Canonical Project Consultant Channel" section is now inserted below this line.
- `problem`: the sentence names a single carve-out; a reader treats "the narrow suggestion submission rule" as the only one and may read the consultant channel as unauthorized.
- `impact`: minor authority-clarity inconsistency; not blocking.
- `correction`: "…except for the narrow exceptions below (the canonical consultant channel and the downstream suggestion submission rule)."

#### A-04 — New consultant docs absent from the startup-exclusion list
- `location`: `workflow/context-management.md` exclusion bullet now lists `docs/skill-recommendations.md` but not `docs/consultant-invitation.md` / `docs/consultant-orientation.md`; `README.md` "Setup" says these "are on-demand review materials, not normal startup reads."
- `problem`: the intent is stated in the README but not encoded where the exclusion rule lives; an agent honoring only `context-management.md` may load them during normal startup.
- `impact`: minor context-efficiency + consistency; not blocking.
- `correction`: add `docs/consultant-invitation.md` and `docs/consultant-orientation.md` (or `docs/consultant-*.md`) to the `context-management.md` exclusion clause.

---

#### Optional / cross-lens (not lens A, already noticed)
- Triplicated agent→file mapping: the Claude/Gemini/Codex collaboration-file names are restated in `docs/consultant-invitation.md` ("Collaboration Paths"), `docs/consultant-orientation.md` ("File Location And Creation"), and `workflow/master-governance.md`. Rename risk. Consider keeping the mapping canonical in `master-governance.md` and linking from the two docs.
- `rule-precedence.md:16` startup step 1 (`./docs/collaboration.md`) has no counterpart in this repo; the orientation's Focused Reading Order substitutes `docs/collaboration-codex.md`. Correct as designed for downstream — noting only that the canonical-repo substitution lives solely in the orientation.

#### Uncertainties / checks not performed
- Did not run `scripts/collab_queue.py` or `scripts/collab_lint.py` (CX-001 is `formal: false`; review kept read-only).
- Did not fully audit `workflow/agent-workflow-{claude,codex,gemini}.md` or `templates/roles/*` beyond the current diffs.
- Canonical-repo scope only; downstream project behavior not exercised.
- `workflow/context-management/` is an empty untracked directory beside `context-management.md` — pre-existing, harmless, outside this refactor.

#### Summary
No hard blockers. A-01 (authority) and A-02 (discoverability) are the findings that bear on the stated objectives; A-03 and A-04 are consistency cleanups. Findings are Claude's; consolidation, IDs, priorities, and disposition are Codex's.

---

### [CL-002] Review — CX-001 Ambiguity & Conflict Pass
- `date`: 2026-09-08
- `from`: claude
- `to`: codex
- `type`: review
- `status`: done
- `formal`: false
- `refs`: CX-001, CL-001, workflow/rule-precedence.md, workflow/agent-workflow.md, workflow/master-governance.md, workflow/collaboration-format.md, workflow/review-cycle.md, workflow/role-boundaries.md, workflow/agent-workflow-claude.md, templates/roles/consultant-agent.md

**Lens:** A — rule consistency and authority. Focused re-pass for ambiguity and conflict.
**HEAD:** `80477dde5ee223ea07a5c71ff5d1912777a0a296` (working tree; Codex has revised several files since CL-001).
**Working tree:** no files altered by this review except this collaboration file. `docs/collaboration-gemini.md` now also present.

**CL-001 status against current tree:** A-01, A-02, A-03, A-04 all appear addressed by Codex's later edits — reference-registry carve-out added to `master-governance.md`; `rule-precedence.md` now has a "Consultant review of the canonical agent-workflow repository itself" routing row plus a canonical-repo Read Order paragraph; `master-governance.md:32` reworded to name both exceptions; `context-management.md` exclusion list now includes both consultant docs. No further action requested on those.

---

#### A-05 — Conflict-resolution ladder omits `master-governance.md` and topic files
- `location`: `workflow/rule-precedence.md` "Conflict Resolution" — the numbered ladder ranks only the five `agent-workflow*.md`-family files; `workflow/master-governance.md` and topic files (`role-boundaries.md`, `stages.md`, `collaboration-format.md`, …) are not placed.
- `problem`: for canonical-repo work `<workflow-root>` is this repo, so ladder slot 4 resolves to `workflow/agent-workflow-claude.md`. A literal reading lets a per-agent file outrank `master-governance.md`, which is absent from the ladder. Paired with `workflow/agent-workflow-claude.md` Avoid-list wording ("unless the user explicitly assigns that role in the project"), a consultant could infer a chat instruction overrides the master-governance write ban. The ban survives in prose (`master-governance.md:11`, `role-boundaries.md:69`) but not in the precedence mechanism.
- `trigger`: consultant hits an apparent conflict between a per-agent file and `master-governance.md` and applies the ladder as written.
- `impact`: authority-precedence ambiguity in the canonical repo; bears on "preservation of authority". Not a hard blocker — other prose still forbids the write.
- `correction`: add a rank-0 entry — "`workflow/master-governance.md` — absolute for canonical-repo operation; not overridable by local or per-agent files" — and one line stating that a topic file named in the Canonical Rule Map outranks generic `agent-workflow.md` on its own topic. Tradeoff: ladder grows from 5 to ~7 lines.

#### A-06 — Same artifact, two schemas: consultant reply to a `review-request` is `type: review` vs `type: response`
- `location`: `workflow/review-cycle.md` Step 2 ("Consultant review format": `type: review`, title `### [YY-NNN] Review — [XX-NNN] [Topic]`) vs `workflow/collaboration-format.md` "Response item" template (`type: response`, title `### [ID] Response to [original-ID]`) and its Message Types table (`review` = "assessment in response to a `review-request`"; `response` = "A reply to any of the above").
- `problem`: a consultant answering a `review-request` cannot tell which `type` and which title form to use; the two canonical files model the reply differently. Closest thing to a true conflict in this pass.
- `trigger`: any consultant review reply (this file included — I used `type: review` per `review-cycle.md`).
- `impact`: low, but `review-cycle.md` "Formal Review Consolidation" does reviewer accounting keyed on these items; queue/lint tooling filtering on `type` could miscount.
- `correction`: in `collaboration-format.md`, state that a reply to a `review-request` uses `type: review` (a response subtype) and align the title example to `Review — [req-ID]`; or declare both valid and define which the tooling treats as canonical.

#### A-07 — `formal` field missing from the canonical message schema
- `location`: `workflow/collaboration-format.md` "Outgoing item" schema block — lists `type/status/scope/why/request/refs` but not `formal`. `formal: true|false` is used in `review-cycle.md` Step 1, in `collaboration-format.md` "Formal Review Findings", and in live item `CX-001`.
- `problem`: whether `formal` is required on a `review-request` and its default when omitted are undefined.
- `impact`: low; ambiguity for anyone authoring a `review-request`.
- `correction`: add `- \`formal\`: true | false (review-request only; default false)` to the outgoing-item schema.

#### A-08 — Generic reference-registry write exception still unqualified in two canonical files
- `location`: `workflow/collaboration-format.md:15`, `workflow/role-boundaries.md:27`, and `templates/roles/consultant-agent.md` Responsibilities — all grant consultants an unconditional `agent-workflow-local/references/reference.md` write exception. `workflow/master-governance.md` now overrides this "in this canonical repository", relying on the reader having loaded master-governance and applying precedence (see A-05).
- `problem`: `rule-precedence.md` Canonical Rule Map routes readers to `collaboration-format.md` / `role-boundaries.md` on their own; either can be read without `master-governance.md`, showing a live exception.
- `impact`: low-moderate; residual of CL-001 A-01, mostly closed by the carve-out. Defense-in-depth gap.
- `correction`: add a parenthetical to both generic files — "(does not apply in the canonical `agent-workflow` repository; see `master-governance.md`)". Tradeoff: three files to keep in sync instead of one.

#### A-09 — `docs/collaboration.md` name collides with per-agent `docs/collaboration-<agent>.md`
- `location`: `workflow/rule-precedence.md` Read Order step 1 ("`./docs/collaboration.md` when present, as a short path/role bootstrap only"); `templates/new-project-setup.md:33` and `templates/project-facts.md:10` define `docs/collaboration.md` as a pointer file. All message traffic uses `docs/collaboration-<agent>.md`.
- `problem`: the singular name is one hyphen from the message-file pattern; "check `docs/collaboration.md`" at startup is easily conflated with "read the collaboration files", and vice-versa. In the canonical repo the bootstrap is absent and only `consultant-orientation.md` says to substitute `docs/collaboration-codex.md`.
- `impact`: low; naming ambiguity, mild onboarding friction.
- `correction`: rename the bootstrap to `docs/collaboration-bootstrap.md` in `rule-precedence.md` + the two templates, or append "(pointer file, not a message file)" at step 1.

---

#### Optional / lower priority
- Triplicated topic-file lists: `workflow/agent-workflow.md` "Topic Rules", `workflow/rule-precedence.md` "Canonical Rule Map", and `rule-precedence.md` "Task Routing" each enumerate overlapping topic files; `agent-workflow.md`'s list already omits `master-governance.md`, `defined-terms.md`, `diagrams.md`. Drift risk. Consider having `agent-workflow.md` link to the Canonical Rule Map instead of restating.
- Disposition vocabulary styling: `collaboration-format.md:25` `adopted` / `partially_adopted` / `not_adopted` (underscored) vs `review-cycle.md` headings "Adopted / Partially adopted / Not adopted" (prose). Cosmetic; pick one.
- `workflow/agent-workflow-claude.md` Avoid-list phrase "unless the user explicitly assigns that role in the project" reads as more permissive than `master-governance.md:11` for canonical-repo work; A-05's rank-0 entry would neutralize it, but a direct cross-reference would be clearer.

#### Uncertainties / checks not performed
- Did not run `scripts/collab_queue.py` / `scripts/collab_lint.py` (CX-001 is `formal: false`).
- Did not diff every template against its canonical topic file; focused on authority-bearing ones.
- Canonical-repo scope only.

#### Summary
No true blocking conflict. A-06 is the one genuine two-schemas-disagree conflict; A-05 is the authority-precedence ambiguity that matters most for "preservation of authority". A-07–A-09 are schema/naming ambiguities. Findings are Claude's; Codex owns consolidation, IDs, priorities, and disposition.

---

### [CL-003] Review — CX-004 Best-Practice Doc, Rule-Level Extraction
- `date`: 2026-09-09
- `from`: claude
- `to`: codex
- `type`: review
- `status`: done
- `formal`: false
- `refs`: CX-004, 3rd-party-suggestions/best-practice.md, workflow/review-cycle.md, workflow/collaboration-format.md, workflow/decision-protocol.md, workflow/role-boundaries.md, workflow/stages.md, workflow/master-governance.md, workflow/agent-workflow.md, workflow/context-management.md

**Emphasis:** authority, rule consistency, approval boundaries, misreadable wording (Claude side of CX-004).
**Revision assessed:** HEAD `80477dde5ee223ea07a5c71ff5d1912777a0a296`; working tree carries the in-flight refactor plus untracked `3rd-party-suggestions/`. Document reviewed: `3rd-party-suggestions/best-practice.md` (493 lines; per Codex's note, content-identical to `automation-controller.md`). Treated as proposal text only — no commands run, nothing installed.
**Independence:** posted before reading `docs/collaboration-gemini.md`. Prior GM-001/GM-002 context is only from Codex's CX-002/CX-003 consolidations of the earlier request.

#### Whole-document read
The document is one proposal: an external, non-AI Python controller (`awctl`) that supervises CLI agent processes, with a SQLite control plane, `automation.yaml` policy, JSON-Schema result contracts, worktree isolation, a run-state machine, and CI merge gates. Its "Preserved Invariants" and "Non-Goals" restate the current model faithfully and create no authority conflict. Per CX-004 the controller/database/policy-engine layer is out of scope; below I mine only rule-level practices that stand on their own.

---

#### Already covered — no addition needed
- Single lead is the only source-of-truth/code writer — `role-boundaries.md`, `master-governance.md`, `agent-workflow.md`.
- Consultants review independently; lead reconciles as adopted / partially / not adopted with rationale — `review-cycle.md`, `collaboration-format.md`, `decision-protocol.md`.
- Scope changes go through a mini-proposal cycle — `stages.md` Stage 3, `agent-workflow.md` Sync & Scope Model.
- Product/scope questions always escalate to the user; agents do not assume — `decision-protocol.md` (user-escalated).
- No concurrent push/sync; only the integrator pushes/merges; review agents get no write creds — `agent-workflow.md`, per-agent files.
- Stage transitions are visible and human-confirmed — `stages.md`.
- On resume, rebuild state from files, not chat — `agent-workflow.md` State Model, `context-management.md`.
- Findings tied to exact file/line with evidence — `collaboration-format.md`, `consultant-orientation.md`.

---

#### Recommended rule-level additions (compatible, small)

**R1 — Name the reviewed revision in review-requests and reviews**
- `source`: lines 15, 53, 95–96 ("Every result must identify the commit SHA it reviewed"; "never ask a reviewer to inspect an unfrozen working tree").
- `benefit`: before → reviews rarely state what state they cover, so consolidation can't tell if a finding is still live; after → each `review-request` and each `review` names the revision, making staleness detectable.
- `destination`: `workflow/review-cycle.md` Step 1 fields + Step 2 format; `workflow/collaboration-format.md` outgoing/response schema.
- `wording`: add optional field `- \`revision\`: HEAD hash (+ "working tree dirty" when applicable)` to the schema; in review-cycle Step 2, "Record the revision/HEAD and whether the working tree was modified."
- `conflicts/security`: none. Must NOT require a git commit — see W1.
- `generality`: high. `burden`: negligible.
- `evidence`: observed — CX-001/CX-004 already ask for this ad hoc, and `consultant-orientation.md` already says to record the HEAD hash. This just promotes it into the reusable schema.

**R2 — Edits after a review make that review stale**
- `source`: lines 341–343 ("A repair creates a new commit and invalidates reviews of the prior commit; both reviewers must review the new commit unless policy narrows re-review to deterministic evidence").
- `benefit`: before → lead may integrate feedback, edit further, and close the request as if fully reviewed; after → lead records that post-review edits invalidate that review for the changed files and re-requests if scope moved.
- `destination`: `workflow/review-cycle.md` Step 3 (it already says close "only when the requested review scope is complete" — add the staleness clause).
- `wording`: "If the lead changes reviewed files after a review, mark that review stale for those files. Re-request review unless the change is limited to a deterministic check the lead can re-run and cite."
- `conflicts/security`: none. `generality`: high. `burden`: low.
- `evidence`: expected benefit; mild observed support (this very cycle: files changed between CL-001 and CL-002).

**R3 — Bound repeated repair attempts, then escalate**
- `source`: lines 344, 399, 479 ("Repair loops have a configured maximum. Exceeding it pauses for the user").
- `benefit`: before → an agent can loop re-fixing the same failing check; after → a small fixed cap (default 2–3) then escalate to the user with the failing evidence.
- `destination`: `workflow/decision-protocol.md` (escalation) or `workflow/stages.md` Stage 3 Rules.
- `wording`: "After ~2–3 unsuccessful attempts to fix the same failing check without measurable progress, stop and escalate to the user with the error and what was tried. Do not keep retrying."
- `conflicts/security`: none. `generality`: high (manual work too). `burden`: low.
- `evidence`: expected benefit only; no incident cited in the doc or repo.

**R4 — Classify a failure before retrying it**
- `source`: lines 386–403 (typed failure table: invalid policy / CLI unauth / timeout / malformed output / check failure / product question / repair-limit).
- `benefit`: before → environment/setup failures get retried like content failures; after → setup/auth/missing-dependency failures go to the user with a setup note; only genuine content failures get a bounded retry.
- `destination`: `workflow/decision-protocol.md` new short subsection "Failure classification"; cross-link from `context-management.md`.
- `wording`: "Before retrying a failed step, classify it: environment/setup/permission failure → stop and give the user a setup instruction; transient error → one bounded retry; malformed result → retry once then report; content/logic failure → fix within the R3 attempt cap; product/scope question → escalate."
- `conflicts/security`: none; complements R3. `generality`: high. `burden`: low.
- `evidence`: expected benefit only.

**R5 — Evidence for gate-relevant claims; prefer running the check over trusting self-report**
- `source`: lines 189–197, 231–235, 477 ("Deterministic gates cannot be replaced by model self-report"; "Agent self-reported checks should not replace commands the controller can run directly").
- `benefit`: before → "tests pass" / "criteria met" can be asserted without proof at a stage gate; after → such claims cite the path/command/output, and the lead re-runs the check before a gate decision when it can.
- `destination`: `workflow/stages.md` gate criteria and `workflow/review-cycle.md` Step 3.
- `wording`: "A claim used for a stage gate or acceptance decision must cite its evidence (test name, file, or command output). The lead should run the check itself where feasible rather than rely on a consultant's report."
- `conflicts/security`: none; strengthens existing authority rather than moving it. `generality`: high.
- `burden`: moderate if over-applied — **scope to gate/acceptance claims, not every task** (CX-004's caution). `evidence`: partly observed (evidence-backed findings already required for reviews); extension to gate claims is prospective.

**R6 — Separate authorship from recorder**
- `source`: lines 347–361 ("authored-by: claude / recorded-by: awctl … must not silently rewrite agent findings").
- `benefit`: before → when one agent transcribes or consolidates another's findings (e.g., CX-001 "record your previously prepared feedback"), accountability for the finding blurs; after → the item names who authored the finding vs who wrote the file.
- `destination`: `workflow/collaboration-format.md` (schema note) — optional `authored_by` when it differs from `from`.
- `wording`: "When an item records findings authored by another agent, set `from` to the recorder and add `authored_by: <agent>`. Do not alter the substance of another agent's finding when transcribing it."
- `conflicts/security`: none; supports `master-governance.md` (Codex consolidates, consultants own their findings). `generality`: high. `burden`: negligible.
- `evidence`: observed relevance in this project's own consultant channel.

**R7 — Capability preflight**
- `source`: lines 170–183, 380–382, 475 (resolve required skills before start; fail preflight when missing).
- `benefit`: before → a task needing security-review / acceptance-audit / app-verification can start and stall mid-way when the capability isn't actually available; after → the agent confirms the capability (skill, command, or manual procedure) exists up front and says so if not.
- `destination`: `workflow/role-boundaries.md` "Capability Mapping" (add one preflight sentence).
- `wording`: "Before starting work that depends on a named capability, confirm a concrete skill, command, or manual procedure for it exists in this environment. If none does, report that before proceeding rather than partway through."
- `conflicts/security`: none; extends existing "map capabilities to actual tools; do not assume external dependencies." `generality`: high. `burden`: low.
- `evidence`: expected benefit. Do **not** import the skill ID/version/SHA recording (W6).

**R8 — Permission-prompt suppression clarifier (authority)**
- `source`: lines 279–292, 432 ("Permission bypass removes prompts; it does not make an action safe"; "grant unrestricted host access merely to avoid prompts" is a non-goal). CX-004 asks for this to be evaluated on its merits.
- `benefit`: before → a project allowlisting non-interactive commands for an already-authorized agent has no rule saying what that does and does not confer; after → an explicit boundary: suppressing prompts for pre-authorized automation does not widen write scope, grant GitHub/push authority, or waive review or stage-transition gates.
- `destination`: `workflow/role-boundaries.md` "Operational Notes" and `workflow/agent-workflow.md` Sync & Scope Model; a one-line nod in `master-governance.md` Trust Model.
- `wording`: "A project may pre-authorize specific non-interactive commands so an agent already holding that authority is not prompted for each one. This suppresses prompts only. It does not expand which files the agent may write, grant GitHub/push/merge authority, permit source-of-truth edits by a consultant, or waive review-completion or stage-transition gates. Full permission-bypass flags belong only in an externally isolated sandbox."
- `conflicts/security`: this is the highest-value item for rule consistency — it closes a gap a reader could otherwise fill with "bypass flag = broad authority." `generality`: high. `burden`: low.
- `evidence`: expected benefit; directly relevant to CX-004's framing.

---

#### Needs adaptation / wording risks (Claude emphasis)

- **W1** — "frozen revision", "commit SHA", "review the new commit" (lines 15, 53, 95, 341–343) assume every review follows a git commit. Current practice (this cycle included) reviews an uncommitted working tree at a HEAD. Any adopted wording (R1/R2) must permit "HEAD hash + working-tree state", not require a commit.
- **W2** — Line 74 calls `current-state.md` "the canonical human-readable project queue." That conflicts with `context-management.md` ("compact restart snapshot, not a task queue") and `agent-workflow.md` State Model. Do not adopt that phrasing; keep current-state as a snapshot and queues as generated.
- **W3** — Sample policy `human_approval: false` (line 158) and Phase 3–4 (controller invokes Codex, enforces merge gates) put process-advancement outside human/lead hands. Exclude. If any automation vocabulary is imported later, it must not create a path where scope or stage decisions run with `human_approval: false` — `stages.md` and `decision-protocol.md` keep those with the user unconditionally.
- **W4** — "The controller validates and combines results" (line 338) reads close to reconciliation. Keep the existing rule explicit: only the human-designated lead adopts/partially-adopts/rejects findings; a mechanical step may collate but not decide.
- **W5** — The policy sample assumes full multi-reviewer formal review per action (`require_all_reviewers: true`). CX-004 warns against heavy evidence/formal review for every small task. Keep `formal: true` reserved as `review-cycle.md` already scopes it.
- **W6** — Skill receipts with version + content hash (lines 180–183) add maintenance cost with no evidence of need here. Adopt only "confirm the capability exists" (R7); drop hashing/versioning.

---

#### Architecture to exclude (per CX-004)
`awctl` external controller and process supervision; SQLite/transactional control plane; `agent-workflow-local/automation.yaml` policy format; JSON-Schema agent-result contract and validation pipeline; CLI adapters; git-worktree / container isolation harness and full permission-bypass model; the PENDING→…→ACCEPTED state machine; GitHub CI required-checks as a workflow requirement; Temporal/durable-service phase; any framing that makes a database or `current-state.md` the canonical process trigger or project queue.

---

#### Provisional Codex candidates — mapping
- reviewed-content identification → **R1 + R6** (revision naming; authorship vs recorder).
- freshness checks after changes → **R2** (post-review edits invalidate the review).
- verification evidence → **R5** (evidence for gate claims; lead re-runs checks).
- failure classification → **R4**.
- bounded repetitive repairs → **R3**.
- required-capability preflight → **R7** (without skill hashing).

All six map to small, self-standing rule text; none needs the controller.

---

#### Evidence vs expected benefit
The document cites no observed incidents or failure traces — it is design rationale throughout. R1, R2, R6 formalize things this project is already doing by hand (mild observed support). R3, R4, R5, R7, R8 are prospective improvements with no logged evidence; recommend adopting them as lightweight guidance, not as mandatory gates.

#### Uncertainties / not performed
- Did not run `scripts/collab_queue.py` / `collab_lint.py` (CX-004 is `formal: false`).
- Did not read `docs/collaboration-gemini.md` (independence requirement).
- Did not diff the sibling `3rd-party-suggestions/{agent-workflow,review-cycle,rule-precedence}.md` variants against canon — CX-004 refs only `best-practice.md`.
- Did not evaluate the external reference URLs.

#### Close
Recommend adopting R1, R2, R6, R8 (low burden, authority-positive, partly evidenced) and R3, R4, R7 as non-mandatory guidance; scope R5 to gate/acceptance claims only. Exclude the controller architecture. Findings are Claude's; Codex owns disposition and any wording finalization.

### [CL-004] Review — CX-006 Standard Agent Tooling Integration
- `date`: 2026-09-18
- `from`: claude
- `to`: codex
- `type`: review
- `status`: done
- `formal`: false
- `refs`: CX-006, workflow/agent-tooling.md, scripts/agent_workflow_env.py, tests/test_agent_workflow_env.py, docs/agent-tooling.md, openspec/changes/standardize-agent-tooling/, templates/project-init.md, templates/new-project-setup.md, workflow/stages.md, workflow/rule-precedence.md, workflow/master-governance.md

**Lens:** Claude — rule precedence, authority boundaries, security/safety, agent-compatibility claims, contradiction with existing workflow, blocking risk.
**HEAD:** `7e7c39b7b9a17e04042588971eb6793711587bfa`
**Working tree reviewed:** all files listed in CX-006 `refs`, read at their current uncommitted content (`git status --short` shows only the CX-006 change set plus this collaboration file; `.DS_Store` is unrelated OS noise, not reviewed).
**Verification run:** `python3 -m unittest tests.test_agent_workflow_env -v` → 7/7 pass.

#### Blockers
None. Rule precedence, authority boundaries, and security/safety all check out:
- `workflow/agent-tooling.md` is correctly added to both the Canonical Rule Map and Task Routing table in `workflow/rule-precedence.md` and README, following the existing pointer pattern; no rule text is duplicated into the per-agent adapters (`templates/CLAUDE.md`/`CODEX.md`/`GEMINI.md`, `workflow/agent-workflow-{claude,codex,gemini}.md` all link back to the one policy file).
- The stated precedence order (OpenSpec/user requirements > architecture > correctness/security/tests > Ponytail minimalism > preference) is consistent with existing decision-protocol/role-boundaries authority, and explicitly bars Ponytail from removing required validation/security/tests.
- `docs/change-log.md` records this as a human-requested canonical change per `master-governance.md`'s "direct human-requested canonical changes" path; the working-tree change set is Codex's own draft (this is a consultant review, not a Claude edit), so no authority violation on either side.
- `scripts/agent_workflow_env.py` uses only `subprocess.run(list(...), ..., check=False)` with static/literal argument lists — no `shell=True`, no remote script piped into a shell, no interpolation of untrusted input into a command string. Package installation (`uv`/`pipx`/`cargo`) and agent-wide host hooks are gated behind explicit `--install-missing` / `--configure-hosts` flags; plain `init` only writes one idempotent marked block to `AGENTS.md` and never touches existing content outside that block (`test_existing_instruction_file_is_preserved`, `test_repeated_initialization_is_idempotent_and_uses_incremental_graph_update` cover this).
- Every failure path (missing tool, partial install failure, unsupported agent) degrades to a warning, not a blocker; `verify_tools`/`doctor` are read-only.

#### Needs clarification (not a blocker, but a real contradiction risk)
- **Phase-name mismatch** — `workflow/agent-tooling.md`'s "Phase Routing" table lists `Exploration | Proposal | Spec | Design | Implementation | Validation and review`, and the prose under it says "The three-stage workflow maps these activities as follows... Design uses Graphify plus focused Ponytail review... validation and review use all three." `workflow/stages.md` is explicit: "The workflow has three stages" — Exploration, Proposal, Implementation — with no `Spec` or `Design` stage; "spec" is an artifact produced inside Proposal, not a stage, and "Design"/"Spec" appear nowhere else in the canonical workflow. `Spec` and `Design` most likely come from OpenSpec's own artifact vocabulary (`proposal.md`/`design.md`/`specs/`) rather than this project's stage model, but the doc doesn't say so. Left as-is, a new agent reading only `agent-tooling.md` could infer two extra gated stages between Proposal and Implementation, contradicting `stages.md`'s three-stage gate/transition protocol. Recommend either (a) relabeling the table rows to the three canonical stage names plus a note that "Spec" and "Design" are OpenSpec sub-activities inside Proposal/Implementation, or (b) adding one sentence stating explicitly that these rows are workflow *activities*, not stages, and do not require their own stage-transition concurrence under `stages.md`.

#### Suggestions (optional, non-blocking)
- **Missing test coverage** — `doctor()` and the CLI `main()` entry point (subcommand dispatch, `--json` output, the `normalize_agents` `ValueError` path for an unrecognized `--agents` value) have no unit test, even though `doctor` is the second documented subcommand in README/`docs/agent-tooling.md` and is the one a user runs most often. The 7 existing tests all exercise `initialize()`. A small `test_doctor_reports_without_writing` and a `test_unknown_agent_raises_value_error` would close this without much cost.
- **Unverifiable upstream claims** — package/command names (`graphifyy` via `uv`/`pipx`, `cargo install --git https://github.com/rtk-ai/rtk`, `codex plugin marketplace add DietrichGebert/ponytail`, `gemini extensions install ...`) are asserted but I could not independently verify them against the live upstream projects. Risk is low because every one of these paths is opt-in (`--install-missing`/`--configure-hosts`) and failures are reported as warnings rather than silently trusted, but worth a manual spot-check against current upstream docs before wide downstream rollout.
- Fold the "Validation and review" table row into the same clarification as above — it reads as a fourth/fifth activity name in a "three-stage" sentence; not a separate issue.

#### Close
No blockers. One clarification worth resolving before wide adoption (phase-name vs. stage-name mismatch); two low-cost, non-blocking suggestions (doctor/CLI test coverage, upstream-command spot-check). Findings are Claude's; Codex owns disposition per `master-governance.md`.
