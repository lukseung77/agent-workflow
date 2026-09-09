# Claude Collaboration

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
