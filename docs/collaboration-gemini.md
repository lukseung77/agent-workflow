# Gemini Collaboration

### [GM-001] Review — CX-001 Current Workflow Refactor
- `date`: 2026-09-08
- `from`: gemini
- `to`: codex
- `type`: review
- `status`: done
- `scope`: workflow/ rules, templates, and startup paths
- `why`: Independent consultant review for context memory efficiency and structure under Lens B.
- `request`: Codex to verify and reconcile findings into canonical workflow refactor.
- `refs`: CX-001, docs/consultant-orientation.md, workflow/rule-precedence.md, workflow/agent-workflow.md, workflow/ai-coworking-guide.md, workflow/context-management.md

**Review Header**
- Lens: Lens B (Context Efficiency And Structure)
- Git HEAD: `80477dde5ee223ea07a5c71ff5d1912777a0a296`
- Review target: Current working tree including modified rules and untracked docs/workflows

#### Findings

- **Finding ID**: `B-01`
  - **Location**: `workflow/rule-precedence.md:16`
  - **Problem**: Startup step 1 specifies reading `./docs/collaboration.md`. In modern multi-agent setups, collaboration is strictly partitioned into per-agent files (`docs/collaboration-[agent].md`) and active work is discovered via `scripts/collab_queue.py`. Reading a non-existent or monolithic legacy collaboration file causes errors or loads stale historical context before queue filtering.
  - **Impact**: High. Directly inflates base token cost on every startup; blocks the refactor objective of minimal startup context.
  - **Correction**: Replace step 1 with targeted active queue generation (`python3 <workflow-root>/scripts/collab_queue.py <agent>`) and reading the selected item only.
  - **Tradeoff**: Non-script environments retain persistent indexes as fallback, which is already documented.

- **Finding ID**: `B-02`
  - **Location**: `workflow/ai-coworking-guide.md:1-166`
  - **Problem**: This 166-line document is completely omitted from both the Canonical Rule Map (`workflow/rule-precedence.md:42-58`) and the Task Routing table (`workflow/rule-precedence.md:63-79`). It acts as an unmapped, floating guide that duplicates principles canonicalized in `workflow/agent-workflow.md`, `workflow/role-boundaries.md`, `workflow/stages.md`, and `workflow/local-project-files.md`.
  - **Impact**: High. Agents discovering it via directory scanning or search ingest ~1,500 redundant tokens with potential rule drift.
  - **Correction**: Move `workflow/ai-coworking-guide.md` to `docs/legacy/` or archive it, migrating any still-unique narrative advice into `workflow/agent-workflow.md`.
  - **Tradeoff**: None; active workflow rules already supersede it.

- **Finding ID**: `B-03`
  - **Location**: `workflow/question-model.md:1-44` and `workflow/decision-protocol.md:1-98`
  - **Problem**: Circular cross-references and split responsibility between decision triage (agent/lead/user classification) and user question presentation (one-at-a-time interview format, remaining count estimation, decision fatigue guardrails). Agents handling user questions must read both files in tandem.
  - **Impact**: Moderate. Causes multiple round-trip file reads and fragmented context for a single operational task.
  - **Correction**: Consolidate `workflow/question-model.md` into `workflow/decision-protocol.md` under a unified decision-and-escalation protocol.
  - **Tradeoff**: Combined file is ~130 lines, but eliminates a frequent two-file hop.

- **Finding ID**: `B-04`
  - **Location**: `workflow/diagrams.md:1-12` and `workflow/defined-terms.md:1-29`
  - **Problem**: Micro-file fragmentation. Standalone files consisting of 12 and 29 lines each introduce file-system clutter and lookup overhead for single formatting or syntax conventions.
  - **Impact**: Moderate. Extra file reads and search noise across the repository.
  - **Correction**: Fold `workflow/defined-terms.md` into `workflow/collaboration-format.md` (where it is already referenced), and fold `workflow/diagrams.md` into `workflow/local-project-files.md` or `workflow/stages.md`.
  - **Tradeoff**: Slightly lengthens host files by ~10-25 lines, but reduces overall file count and tool calls.

- **Finding ID**: `B-05`
  - **Location**: `workflow/collaboration-format.md:82-103` and `workflow/review-cycle.md:104-117`
  - **Problem**: Both files duplicate formal review consolidation mechanics (reviewer accounting, table format deduplication, canonical ID assignment, and P0-P2 priority tiers).
  - **Impact**: Low-to-Moderate. Unnecessary prose repetition across two related review documents.
  - **Correction**: Keep the Markdown table schema definition exclusively in `workflow/collaboration-format.md` and consolidation logic exclusively in `workflow/review-cycle.md`.
  - **Tradeoff**: Clean separation between schema and lifecycle.

#### Optional Improvements & Structural Suggestions
1. **Tiered Startup Order**: Condense the 9-step flat reading order in `workflow/rule-precedence.md` into 4 logical tiers (Tier 1: Snapshot state/facts -> Tier 2: Queue task selection -> Tier 3: Local project rules -> Tier 4: JIT task topic rule).
2. **Token Caps on Collaboration Items**: Add a soft guideline in `workflow/collaboration-format.md` recommending that review and status bodies stay under 50 lines to prevent collaboration files from triggering premature 50 KB archive splits.

#### Uncertainties & Checks Not Performed
- Did not independently review Lens A in GM-001; performed full Lens A audit in GM-002 below.

### [GM-002] Review — CX-001 Ambiguity, Conflict, and Authority Audit
- `date`: 2026-09-08
- `from`: gemini
- `to`: codex
- `type`: review
- `status`: done
- `scope`: canonical rules, role templates, scripts, and suggestions ledger
- `why`: Lens A audit for conflicting rules, ambiguities, authority leaks, and template drift.
- `request`: Codex to verify and reconcile findings into canonical workflow refactor.
- `refs`: CX-001, workflow/role-boundaries.md, workflow/stages.md, templates/roles/lead-agent.md, workflow/decision-protocol.md, workflow/collaboration-format.md, scripts/collab_archive.py, user-agent-suggestions/status.md

**Review Header**
- Lens: Lens A (Rule Consistency And Authority)
- Git HEAD: `80477dde5ee223ea07a5c71ff5d1912777a0a296`
- Review target: Canonical rules, role templates, tooling scripts, and suggestion ledgers

#### Findings

- **Finding ID**: `A-01`
  - **Location**: `templates/roles/lead-agent.md:18` & `templates/project-init.md:14` vs. `workflow/stages.md:3, 111-121` & `workflow/role-boundaries.md:21, 64`
  - **Problem**: Direct authority contradiction on stage transitions. `templates/roles/lead-agent.md:18` asserts that the lead agent "Declares stage transitions when the project is ready", and `templates/project-init.md:14` states "only you declare when the project moves...". However, `workflow/stages.md` and `workflow/role-boundaries.md` explicitly mandate that stage transitions require (1) lead declaring readiness, (2) all consultant agents independently concurring, and (3) user confirmation.
  - **Impact**: High. A downstream lead agent reading its role template could assume unilateral authority and execute unconfirmed stage transitions.
  - **Correction**: Update `templates/roles/lead-agent.md` and `templates/project-init.md` to match canonical governance: "Declare stage readiness and record stage transitions after consultant concurrence and user confirmation."
  - **Tradeoff**: None; preserves canonical human and peer-agent checks.

- **Finding ID**: `A-02`
  - **Location**: `workflow/decision-protocol.md:89` & `workflow/collaboration-format.md:144` vs. `scripts/collab_archive.py:33` & `scripts/collab_common.py:63-66`
  - **Problem**: Tooling and protocol conflict on item retirement. Rules state: "mark the collaboration item done and comment it out" (`<!-- ... -->`). However, `scripts/collab_common.py:66` explicitly skips commented-out lines during item parsing (`match = None if in_comment else ITEM_RE.match(line)`). When an item is commented out, `collab_archive.py` cannot parse it as an `Item`, never counts it toward the 50 KB threshold, and never removes it from the live collaboration file. Commented items remain permanently trapped in live files.
  - **Impact**: High. Breaks automated size-based archiving and causes silent context bloat.
  - **Correction**: Remove the instruction to comment out items from `decision-protocol.md` and `collaboration-format.md`. Mark them `status: done` only; let `collab_archive.py` handle extraction to `docs/collaboration-archives/`.
  - **Tradeoff**: None; aligns rule instructions directly with script behavior.

- **Finding ID**: `A-03`
  - **Location**: `workflow/collaboration-format.md:61, 76`, `scripts/collab_queue.py:14, 58-60`, `scripts/collab_common.py:102-106` vs. `workflow/review-cycle.md:75-78`
  - **Problem**: Asymmetric queue discovery for completed review items. Consultant reviews use `type: review`, `to: [lead]`, and `status: done`. Because `collab_queue.py` strictly filters `status in {"open", "active"}`, completed reviews never appear in `collab_queue.py <lead>` ("No active addressed items"). A lead starting a session following standard startup rules (`templates/agent-common.md:8`) sees an empty queue and has no script-driven indicator that consultant feedback is ready for consolidation.
  - **Impact**: Medium. Creates friction and ambiguity during review handoffs.
  - **Correction**: Explicitly clarify in `workflow/review-cycle.md` and `workflow/agent-workflow.md` that leads with an open `review-request` must check consultant files for responses referencing that request ID rather than relying solely on `collab_queue.py` output. (Optional future tooling enhancement: add `--review-responses` flag to `collab_queue.py`).
  - **Tradeoff**: Requires explicit lead procedure during the consolidation step.

- **Finding ID**: `A-04`
  - **Location**: `user-agent-suggestions/submitted/2026-09-08-1831-rideroute-openspec-phase-skills-addendum-003.md` vs. `user-agent-suggestions/status.md:21-26`
  - **Problem**: Missing ledger entry for submitted suggestion. The working tree contains submitted proposal file `2026-09-08-1831-rideroute-openspec-phase-skills-addendum-003.md`, but `user-agent-suggestions/status.md` records only suggestions 001, 002, and 004.
  - **Impact**: Medium. Governance violation of `workflow/master-governance.md:84-86` (untracked submission ledger).
  - **Correction**: Master-agent to add a row for `003` in `user-agent-suggestions/status.md` (e.g., recorded as `superseded` or `implemented` via `004`).
  - **Tradeoff**: None; restores complete audit ledger.

- **Finding ID**: `A-05`
  - **Location**: `templates/docs/collaboration-format.md:10-12` vs. `templates/new-project-setup.md:72` & `workflow/local-project-files.md:20`
  - **Problem**: Path inconsistency. `templates/docs/collaboration-format.md` lists `collaboration-[lead].md` and `collaboration-[agent-a].md` without the `docs/` folder prefix, whereas canonical files and templates specify `docs/collaboration-*.md`.
  - **Impact**: Low. Ambiguity when scaffolding new downstream projects.
  - **Correction**: Add the `docs/` prefix: `docs/collaboration-[lead].md`, `docs/collaboration-[agent-a].md`.
  - **Tradeoff**: None.

- **Finding ID**: `A-06`
  - **Location**: `templates/project-init.md:103-121` vs. `workflow/agent-workflow.md:38-40` & `workflow/role-boundaries.md`
  - **Problem**: Mandatory external GitHub execution during project setup. `templates/project-init.md` Step 4 prescribes running `gh repo create` as a mandatory step, conflicting with canonical guidelines to withhold GitHub sync unless requested and prefer local inspection/edits.
  - **Impact**: Low. Causes setup failure in local-only, unauthenticated, or offline environments.
  - **Correction**: Frame Step 4 as optional/conditional: "If the project uses a GitHub remote... otherwise initialize local git repo."
  - **Tradeoff**: None.

#### Optional Improvements & Uncertainties
- Verified `scripts/collab_lint.py` passes cleanly across all existing files.
- Confirmed `docs/collaboration-gemini.md` is strictly the sole modified/created file within consultant permissions.

### [GM-003] Review — CX-004 Assessment of Automation Best Practices
- `date`: 2026-09-09
- `from`: gemini
- `to`: codex
- `type`: review
- `status`: done
- `scope`: 3rd-party-suggestions/best-practice.md
- `why`: Independent assessment of 3rd-party automation best practices for rule-level additions, context efficiency, and minimal integration without architectural changes.
- `request`: Codex to reconcile findings and incorporate compatible rule-level practices into canonical workflow files.
- `refs`: CX-004, 3rd-party-suggestions/best-practice.md, workflow/rule-precedence.md, workflow/review-cycle.md, workflow/collaboration-format.md, workflow/role-boundaries.md, workflow/decision-protocol.md, workflow/context-management.md, workflow/master-governance.md

**Review Header**
- Focus: Practical benefit, context cost, maintenance burden, evidence calibration, and minimal integration.
- Evaluated document: `3rd-party-suggestions/best-practice.md` (494 lines).
- Git HEAD: `80477dde5ee223ea07a5c71ff5d1912777a0a296` + current working tree.
- Method: Full document evaluation conducted independently prior to reviewing peer consultant inputs.

#### 1. Architecture Changes to Exclude

The proposal outlines an external automation daemon/supervisor (`awctl`) built with `asyncio`, SQLite, JSON Schema contracts, CLI adapters, and ephemeral Git worktrees. These architectural changes should be **firmly excluded** from the core workflow:

1. **SQLite Control Plane & Daemon (`awctl`)**:
   - *Burden*: Introduces external dependencies, background daemon supervision, process state tracking, and schema migrations.
   - *Assessment*: Violates the lightweight file-based pair programming model. The existing state machine (`agent-workflow-local/current-state.md` + `scripts/collab_queue.py`) is transparent, human-readable, and zero-dependency.
2. **Mandatory JSON Schema Result Wrappers**:
   - *Burden*: Forcing CLI models to output strict JSON schemas for every review item increases token generation failures, parse errors, and breaks natural review readability in `docs/collaboration-[agent].md`.
3. **Automated Git Worktree Multiplexing**:
   - *Burden*: Maintaining dynamic worktree lifecycles on single-user local systems adds git lock contention and path complexity with negligible gain over standard frozen commit inspection.
4. **OpenSpec Action State Overhaul**:
   - *Burden*: Re-keying the workflow exclusively to OpenSpec action verbs (`explore`, `propose`, `apply`, `verify`, `archive`) creates an unnecessary layer of terminology churn over the established Exploration -> Proposal -> Implementation stages.

#### 2. Practices Already Covered by the Existing Workflow

- **Single-Lead Model & Non-Concurrent Pushes**: Canonicalized in `workflow/agent-workflow.md:8-14` and `workflow/role-boundaries.md:15-31`.
- **Independent Consultant Review Separation**: Canonicalized in `workflow/review-cycle.md:43-71` (no shared writing; separate consultant files).
- **Human Authority for Product & Scope Decisions**: Canonicalized in `workflow/decision-protocol.md:32-40` and `workflow/stages.md:3`.
- **Durable Product vs. Operational Record Separation**: Canonicalized in `workflow/local-project-files.md:16-22`.
- **Lead Consolidation & Disposition Logic**: Canonicalized in `workflow/review-cycle.md:73-117`.

#### 3. Recommended Rule-Level Additions

The proposal contains valuable discipline that can be extracted into pure rule-level guidelines without adopting any new software. Below are the specific recommended additions evaluated against the provisional Codex candidates and operational policies:

##### Rule 1: Reviewed-Content Identification (Frozen Ref / Commit SHA)
- **Source Section**: Lines 85–86, 95–97, 211 (`Reference Flow`, `Agent Result Contract`).
- **Before / After**:
  - *Before*: Review requests often point vaguely to dirty working trees or branch names (`refs: path:line`). If the lead modifies files while a consultant reviews, the review assesses shifting content.
  - *After*: Review requests for formal reviews or implementation batches must cite a frozen Git commit SHA (or immutable snapshot ref).
- **Evidence vs Benefit**:
  - *Observed Evidence*: Multi-agent reviews on unfrozen trees frequently report phantom findings or mismatch line numbers when edits occur concurrently.
  - *Expected Benefit*: Absolute repeatability of review findings and clean deduplication.
- **Destination**: `workflow/review-cycle.md` (Step 1) and `workflow/collaboration-format.md` (Message Format).
- **Minimal Proposed Wording**:
  > For code implementation reviews and formal reviews, the review-request must reference a frozen commit SHA or immutable snapshot ref in `refs:`. Reviewers must record the exact commit SHA reviewed in their report header.
- **Generality & Burden**: Very general; negligible burden (~1 line of metadata). In informal exploration, allow file paths as fallback.

##### Rule 2: Freshness Checks & Review Invalidation After Changes
- **Source Section**: Lines 341–343 (`Review And Repair Rules`).
- **Before / After**:
  - *Before*: After consultant reviews find issues, the lead repairs them, but the resulting commit is often merged without re-verifying whether the fix introduced regressions or actually addressed the finding.
  - *After*: Substantive code changes following a review explicitly invalidate prior reviews. The lead must obtain fresh concurrence or run deterministic checks before advancing.
- **Evidence vs Benefit**:
  - *Observed Evidence*: In repair cycles, fix commits often introduce subtle syntax or logic defects that bypass scrutiny because the feature was already marked "reviewed".
  - *Expected Benefit*: Prevents stale sign-offs on modified artifacts.
- **Destination**: `workflow/review-cycle.md` (Step 3) and `workflow/stages.md`.
- **Minimal Proposed Wording**:
  > Code modifications made to resolve review findings invalidate prior consultant approvals for the affected scope. The lead must run deterministic checks and request focused re-review if the fix alters architecture, contracts, or public behavior.
- **Generality & Burden**: Moderate. Calibrate to avoid endless loops: trivial/formatting fixes require only deterministic checks; behavioral fixes require targeted re-review.

##### Rule 3: Verification Evidence Over Model Self-Certification
- **Source Section**: Lines 187–197, 234–235, 429–430 (`Skill Enforcement`, `Non-Goals`).
- **Before / After**:
  - *Before*: Agents frequently declare "tests pass" or "code verified" based solely on model self-assessment without executing commands or linking proof.
  - *After*: Verification claims in Implementation must cite concrete, observable evidence: command invocation, exit code, test summary, or lint output.
- **Evidence vs Benefit**:
  - *Observed Evidence*: LLMs under context pressure frequently claim verification without running test commands or overlook failing suites.
  - *Expected Benefit*: Elimination of phantom verification.
- **Destination**: `workflow/review-cycle.md` (Formal Reviews) and `templates/roles/lead-agent.md`.
- **Minimal Proposed Wording**:
  > In Implementation, review completion and stage gates cannot rely on agent self-certification. Claims that tests pass or requirements are met must cite observable execution evidence (test runner output, exit code, or command receipt).
- **Generality & Burden**: High benefit; minimal token burden. Limit strict command receipts to code implementation; do not mandate execution proof for simple markdown or exploration edits.

##### Rule 4: Failure Classification (Environment/Tool vs. Code/Spec)
- **Source Section**: Lines 384–404 (`Failure Semantics`).
- **Before / After**:
  - *Before*: When an agent encounters missing CLI tools, network blocks, or permission denials, it often enters a hallucinated debugging spiral trying to "fix" local code to bypass an environment block.
  - *After*: Clear classification separating environment/tooling failures (pause/escalate to user) from task/logic defects (repair internally).
- **Evidence vs Benefit**:
  - *Observed Evidence*: Agents frequently burn hundreds of tokens refactoring test harnesses when the real issue was an unauthenticated API, missing binary, or permission prompt.
  - *Expected Benefit*: Immediate stopping and escalation of infrastructure failures.
- **Destination**: `workflow/decision-protocol.md` (Types of Decisions).
- **Minimal Proposed Wording**:
  > **Environmental / Tooling Failures**: Failures caused by missing system binaries, denied permissions, unauthenticated CLIs, or network barriers are environmental, not code bugs. Agents must immediately pause and escalate them to the user or setup guide rather than attempting code workarounds.
- **Generality & Burden**: Extremely high practical benefit; zero token overhead.

##### Rule 5: Bounded Repetitive Repairs (Loop Ceiling)
- **Source Section**: Lines 121, 344, 399, 479 (`Defaults`, `Review And Repair Rules`, `Acceptance Criteria`).
- **Before / After**:
  - *Before*: No defined limit on review-repair cycles. Lead and consultants can enter multi-round debate loops on styling or minor preferences.
  - *After*: Maximum of 2 repair cycles per review-request. If unresolved after 2 iterations, the issue must be escalated to the user as a trade-off or decision.
- **Evidence vs Benefit**:
  - *Observed Evidence*: Without bounds, agents consume excessive context arguing over design nuances where neither position is wrong.
  - *Expected Benefit*: Hard cap on token waste and fast escalation of contentious items.
- **Destination**: `workflow/review-cycle.md` (Step 3) and `workflow/decision-protocol.md`.
- **Minimal Proposed Wording**:
  > Review-repair loops are bounded to a maximum of two revision cycles. If consultant feedback cannot be resolved within two iterations, the lead must escalate the disagreement to the user with a concise trade-off summary.
- **Generality & Burden**: High benefit; saves thousands of tokens during contentious tasks.

##### Rule 6: Required-Capability Preflight Check
- **Source Section**: Lines 171–185, 380–383 (`Skill Enforcement`, `Reference Commands`).
- **Before / After**:
  - *Before*: Tasks begin without confirming whether required tools (e.g. `python3`, `markitdown`, test runners) exist, failing mid-execution.
  - *After*: A lightweight preflight check during setup or before large phase transitions to verify that capabilities listed in `project-facts.md` are operational.
- **Evidence vs Benefit**:
  - *Expected Benefit*: Prevents aborted work mid-stream.
- **Destination**: `workflow/role-boundaries.md` (Capability Mapping) and `templates/agent-common.md`.
- **Minimal Proposed Wording**:
  > Before undertaking phase tasks, agents should verify that required tools, scripts, and linters mapped in `project-facts.md` are accessible. Missing capabilities must be reported as startup blockers before editing project files.
- **Generality & Burden**: Low burden; complements existing capability mapping.

##### Rule 7: Permission-Prompt Suppression & Non-Interactive Clarity
- **Source Section**: Lines 262–273, 274–293 (`CLI Adapters`, `Permission And Isolation Policy`).
- **Before / After**:
  - *Before*: Ambiguity around whether running agents with non-interactive flags (e.g. `--ask-for-approval never`, `-p`) violates approval policies.
  - *After*: Clarify that non-interactive flags are legitimate operational mechanisms for pre-authorized tasks, but do not expand the agent's authority boundary or make destructive commands safe.
- **Evidence vs Benefit**:
  - *Expected Benefit*: Enables reliable unattended agent automation while maintaining strict authority boundaries.
  - *Destination**: `workflow/role-boundaries.md` (Operational Notes).
- **Minimal Proposed Wording**:
  > Operating in non-interactive or prompt-suppressed modes (such as headless CLI flags) is permitted for authorized automation, but does not grant expanded repository or file authority. The agent remains bound to its assigned role permissions regardless of CLI execution flags.
- **Generality & Burden**: Very clean, clarifies security without operational burden.

#### 4. Summary of Context Cost and Maintenance Impact

Adopting these 7 rules into existing files adds approximately **40–60 lines total** across `workflow/review-cycle.md`, `workflow/decision-protocol.md`, `workflow/role-boundaries.md`, and `workflow/collaboration-format.md`.

- **No new files created**.
- **No external software or dependencies required**.
- **Significant token savings**: Eliminates hallucinated verification, bounds infinite review debates, and halts environmental failure loops immediately.

### [GM-004] Review — CX-006 Standard Agent Tooling Integration
- `date`: 2026-09-18
- `created_at`: 2026-09-18T20:13:00+09:00
- `from`: gemini
- `to`: codex
- `type`: review
- `status`: done
- `scope`: newly added Ponytail, Graphify, and RTK rules, bootstrap, agent adapters, OpenSpec artifacts, tests, and documentation
- `why`: Independent consultant assessment under Gemini lens (architecture fit, duplication, context cost, phase routing, idempotency, test coverage, upstream coupling, and minimal refactoring).
- `refs`: CX-006, workflow/agent-tooling.md, scripts/agent_workflow_env.py, openspec/changes/standardize-agent-tooling/, templates/project-init.md, templates/new-project-setup.md, docs/agent-tooling.md

**Review Header**
- Lens: Gemini Lens (Architecture Fit, Duplication, Context Cost, Phase Routing, Idempotency, Test Coverage, Upstream Coupling, Minimal Refactoring)
- Git HEAD: `7e7c39b` + uncommitted working tree
- Scope verified: `workflow/agent-tooling.md`, `docs/agent-tooling.md`, `scripts/agent_workflow_env.py`, `tests/test_agent_workflow_env.py`, `openspec/changes/standardize-agent-tooling/`, `templates/project-init.md`, `templates/new-project-setup.md`, `templates/CLAUDE.md`, `templates/CODEX.md`, `templates/GEMINI.md`, `workflow/agent-workflow-*.md`, `workflow/rule-precedence.md`
- Verification commands run:
  - `python3 -m unittest discover -s tests -v`: 24 passed (0.78s)
  - `python3 scripts/collab_lint.py --root .`: 0 errors, 0 warnings

---

#### 1. Executive Summary & Blocker Check

- **Blockers / Fatal Contradictions**: **None**.
  - *Rationale*: The architecture adheres strictly to graceful degradation. When tools (Ponytail, Graphify, RTK) or agents are absent, initialization issues warnings and leaves standard file-based workflow fully functional. No mandatory external dependencies or remote execution scripts were introduced; package installation and host hooks remain strictly opt-in behind explicit flags (`--install-missing`, `--configure-hosts`). Normal development is never blocked.
- **Overall Assessment**: Well-structured design with clear separation of concerns (policy in `workflow/agent-tooling.md`, operational CLI/matrix in `docs/agent-tooling.md`, execution in `scripts/agent_workflow_env.py`). Several non-blocking unsupported assumptions and test coverage gaps exist and should be addressed.

---

#### 2. Gemini Lens Evaluation

##### A. Architecture Fit & Duplication
- **Policy Placement**: `workflow/agent-tooling.md` cleanly centralizes shared rules (precedence, capability roles, phase routing, repository lifecycle).
- **Rule Precedence Alignment**: Correctly integrated into `workflow/rule-precedence.md` in both the Canonical Rule Map (`Optional agent tooling and phase routing`) and Task Routing table (`Repository discovery, implementation, validation, or verbose CLI execution`).
- **Thin Host Adapters**: `templates/CLAUDE.md`, `templates/CODEX.md`, `templates/GEMINI.md`, and `workflow/agent-workflow-*.md` link directly to `workflow/agent-tooling.md` rather than duplicating rule semantics.
- **Duplication Risk**: Minimal. Operations, installation commands, and troubleshooting belong in `docs/agent-tooling.md`; semantic policy belongs in `workflow/agent-tooling.md`.

##### B. Context Cost & Phase Routing
- **Context Footprint**: `workflow/agent-tooling.md` is compact (61 lines, ~800 tokens).
- **On-Demand Loading**: The topic file is not included in mandatory agent startup reading (`templates/agent-common.md:29` only references it; `rule-precedence.md` routes it JIT). Agents do not ingest tooling rules until performing repository exploration, code modifications, or verbose CLI commands.
- **Phase Routing**: Clean matrix mapping of activities (Exploration, Proposal, Spec, Design, Implementation, Validation/Review) across the three tools, cleanly nested inside the canonical 3-stage model (`workflow/stages.md`).

##### C. Idempotency & Lifecycle
- **Adapter Insertion**: `ensure_repository_adapter` uses boundary comments (`<!-- agent-workflow:tooling:start -->` ... `<!-- agent-workflow:tooling:end -->`) and checks for presence before appending, ensuring zero duplication across multiple runs.
- **Graphify Index**: Detects existing `graphify-out/graph.json` or `graph.json` and runs `graphify update .` instead of full rebuild.
- **Doctor Command**: `doctor` runs read-only tool checks and inspection without modifying repository state.

##### D. Upstream-Command Coupling & Safety
- **Safe Subprocess Execution**: Arguments are structured lists passed to `subprocess.run(check=False)`. No shell expansion or remote script piping.
- **Packaging Accuracy**: Uses official upstream targets (`graphifyy` on PyPI via `uv`/`pipx`, `rtk-ai/rtk` via `cargo`, `DietrichGebert/ponytail` plugins).
- **Safe Opt-In Boundaries**: Package installs require `--install-missing`; host hooks require `--configure-hosts`.

---

#### 3. Issues & Unsupported Assumptions

- **Finding GM-004-01**: `_agent_detected("antigravity", ...)` assumes an `antigravity` CLI binary on `PATH`.
  - *Location*: `scripts/agent_workflow_env.py:112-113`
  - *Problem*: Antigravity is an IDE / environment whose CLI is `agy` and whose project configuration lives in `.agents/`. There is no `antigravity` executable on standard systems. Checking `_command_available("antigravity", which)` returns `False` even when Antigravity is actively used and configured.
  - *Impact*: Low/Moderate. Running `doctor --agents antigravity` or `doctor --agents codex,claude,agy,antigravity` marks Antigravity with `!` (not detected) even after adapters exist.
  - *Correction*: In `_agent_detected`, check for `_command_available("agy", which)`, `_command_available("antigravity", which)`, `(root / ".agents").exists()`, or adapter existence (`_graphify_adapter_exists(root, "antigravity")` or `_rtk_adapter_exists(root, "antigravity")`).

- **Finding GM-004-02**: `print_report` displays unrequested agents as missing/failed `!`.
  - *Location*: `scripts/agent_workflow_env.py:432-433`
  - *Problem*: `print_report` iterates over all `KNOWN_AGENTS` and checks `report.agents.get(agent, False)`. When a user runs `doctor --agents codex`, `report.agents` contains only `codex: True`. Claude, agy, and Antigravity default to `False` and are rendered with an exclamation mark (`!`), misleading the user into thinking those agents failed checks.
  - *Impact*: Low (cosmetic/reporting). Misleading CLI output when inspecting a subset of agents.
  - *Correction*: In `print_report`, iterate over `report.agents.keys()` if specific agents were filtered, or mark uninspected agents as `"-"` (not checked) rather than `!`.

- **Finding GM-004-03**: Multi-pass `verify_tools` causes duplicate entries in `report.actions`.
  - *Location*: `scripts/agent_workflow_env.py:215, 221, 397, 409`
  - *Problem*: `verify_tools` invokes `_run(..., "Graphify version check")` and `_run(..., "RTK verification")`, which append directly to `report.actions`. In `initialize()`, `verify_tools` is called at line 397 and again at line 409. If both tools are present, `Graphify version check: ok` and `RTK verification: ok` appear twice in `report.actions`.
  - *Impact*: Low. Redundant output lines in initialization summaries.
  - *Correction*: Separate verification probing from action recording, or deduplicate/guard probe logging in `verify_tools`.

- **Finding GM-004-04**: Test suite coverage gaps for `doctor()`, argument parsing, and CLI entry points.
  - *Location*: `tests/test_agent_workflow_env.py`
  - *Problem*: The test suite only invokes `initialize()`. The following functions/branches have zero unit test coverage:
    1. `doctor()` function is never invoked or asserted.
    2. `main()` and `build_parser()` (argument parsing, flags like `--json`, `--root`, `--agents`) are never tested.
    3. `print_report()` output formatting and JSON output formatting are never tested.
    4. `normalize_agents()` error handling (e.g. invalid agent names raising `ValueError`) is untested.
    5. `install_missing_tools()` fallback path for `pipx` when `uv` is unavailable is untested.
    6. `configure_ponytail(..., configure_hosts=True)` commands for Codex, Gemini, and Claude are unasserted.
  - *Impact*: Moderate. Regressions in doctor output, JSON reporting, or CLI flags would not be caught by CI.
  - *Correction*: Add a test class (or test methods in `test_agent_workflow_env.py`) covering `doctor()`, `main(["doctor", "--json"])`, `normalize_agents` validation, and `pipx` install fallback.

---

#### 4. Optional Refactoring Suggestions

1. **Differentiate Notices from Warnings in CLI Output**:
   - In `configure_ponytail` and `configure_rtk`, when `--configure-hosts` is omitted, notes like `"Ponytail Codex plugin not changed; rerun with --configure-hosts..."` are pushed to `report.warnings` and printed to `sys.stderr`.
   - *Suggestion*: Introduce an `informational` or `notices` bucket in `EnvironmentReport` so that normal, expected opt-out notices don't write to `stderr` and look like execution warnings.

2. **Graphify Index Verification Resilience**:
   - In `initialize_graph`, line 287 verifies `report.graph_index = _graph_index_exists(root)`. Some projects generate the graph in custom output locations or take time to write out. Adding a short note or checking standard alternate output directories prevents false warnings.

3. **Expose Doctor via Makefile or Task Helper**:
   - Consider documenting `python3 <workflow-root>/scripts/agent_workflow_env.py doctor` in `templates/project-init.md` alongside `collab_lint.py` so downstream projects have a single standard preflight recipe.
