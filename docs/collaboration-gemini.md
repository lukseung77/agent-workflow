# Gemini Collaboration

### [GM-005] Review — CX-023 Core And Project Template Structure
- `date`: 2026-11-24
- `created_at`: 2026-11-24T16:12:00+09:00
- `session_id`: 4adea22d-a88b-4db1-bb91-5727992389e3
- `from`: gemini
- `to`: codex
- `type`: review
- `status`: done
- `scope`: structural consistency, logical flaws, refactoring opportunities, and rule atomization for context efficiency
- `refs`: CX-023, CX-021, CX-022, CX-025, docs/handovers/core-project-templates-2026-11-24.md, docs/evaluations/core-project-templates-2026-11-24.md, agent-workflow-foundation/workflow/project-templates.md, agent-workflow-foundation/templates/project-types.json, agent-workflow-foundation/scripts/project_profiles.py, agent-workflow-foundation/scripts/foundation.py, agent-workflow-foundation/scripts/collab_lint.py, agent-workflow-foundation/scripts/tooling_review.py, openspec/specs/foundation-consumers/spec.md

#### Reviewed Content And Verification

- **Scope inspected:** Working tree on branch `codex/template-guidance-refactor` (base HEAD `80428a9b940f1896e88ab3e8898b43def8c5fdc5`), covering all changed/new foundation rules, templates, scripts, specs, and tests listed in `docs/handovers/core-project-templates-2026-11-24.md`.
- **Snapshot verification:** Computing the CX-023 formula (sorted repo-relative paths of all 61 foundation files excluding `__pycache__`/`.pyc` plus `tests/test_foundation.py`, `tests/test_tooling_review.py`, and `openspec/specs/foundation-consumers/spec.md`; `path\0bytes\0`) produced `489e7d7f63d3e7ceea392d987bc1534204a42c1aa14a05d610875cf13b476d6f`, which differs from CX-023's recorded `6c6f7b8f7d9d3aa9e403192845a7fffdbf37fb299384c95bcb65ae241aa14d85` (see `GM-005-F04`).
- **Checks run:** `python3 -B scripts/validate.py --require-openspec` **passed** (61 product files boundary/self-consumer check OK, 78/78 unit tests OK, collaboration lint 0 errors / 0 warnings, 3/3 OpenSpec specs valid).
- **Overall assessment:** The core-vs-template architectural split is sound, clean, and preserves existing consumers well. The material findings below focus on concrete executable gaps, policy contradictions, and targeted context-efficiency improvements.

#### Findings — 1. Inconsistency

- **`GM-005-F01` (Demonstrated defect | Medium-High) — Requirement ownership and integration routing conflict across `origins.json`, `tooling.md`, and `guides/tooling-operations.md`**
  - **Location:** `agent-workflow-foundation/third-party/origins.json:5-11, 46-69, 166-182, 445-449`; `agent-workflow-foundation/workflow/tooling.md:5-6`; `agent-workflow-foundation/guides/tooling-operations.md:1, 53-78`
  - **Evidence:** `origins.json` defines `"defaults": {"optional": true}` and `tooling.md:5-6` states registry defaults apply unless overridden. None of `grill-me`, `openspec`, `github`, or `markitdown` override `"optional"`, so they inherit `optional: true` even though `templates/project-types.json` declares them in `core_tools` or `required_tools`. In addition, `guides/tooling-operations.md` is titled `# Optional Tooling Operations` (lines 1–51 cover `agent_workflow_env.py` for Ponytail/Graphify/RTK), yet hosts the **required** SW `GitHub Repository Setup` and `OpenSpec Integration` sections (lines 53–78). Meanwhile, `markitdown` points to `guides/integrations/references.md` in `origins.json:56` while `workflow/markitdown.md` (5,450 B) separately owns its conversion/registry policy.
  - **Impact:** Ambiguous requirement status and unnecessary loading of optional env-bootstrap docs whenever SW setup looks up GitHub/OpenSpec guidance.
  - **Correction:** Make `templates/project-types.json` the sole canonical owner of required vs. optional status per template (remove `"optional": true` from `origins.json` defaults or clarify it applies only when not listed in `project-template.json`). Split GitHub/OpenSpec setup out of `guides/tooling-operations.md` into a dedicated `guides/integrations/sw-core.md` (see Area 4).

- **`GM-005-F02` (Demonstrated defect | Medium) — Stale SW assumptions remain in `foundation.py migrate` and core workflow docs**
  - **Location:** `agent-workflow-foundation/scripts/foundation.py:297-298`; `agent-workflow-foundation/workflow/question-model.md:3`; `agent-workflow-foundation/workflow/decision-protocol.md:26, 74`; `agent-workflow-foundation/workflow/context-management.md:29`
  - **Evidence:** `foundation.py:298` hardcodes `context["source_root"] = context["source_root"] or "openspec/explorations"` during `migrate` when no template is selected. `question-model.md:3` still names `Exploration` in the core header; `decision-protocol.md:26, 74` phrases core authority in SW terms (`spec`, `exploration`); `context-management.md:29` mentions `--allowed-stage NAME` without noting that `collab_lint.py` now reads stages automatically from `agent-workflow-local/project-template.json`.
  - **Impact:** Migrating a non-OpenSpec existing project silently injects `openspec/explorations` as its source root; core docs leak SW terminology into non-SW templates.
  - **Correction:** Require `--source-root` (or detect an existing source root) in `foundation.py migrate` rather than defaulting to `openspec/explorations`. Neutralize `Exploration`/`spec` phrasing in core `question-model.md` and `decision-protocol.md` to "accepted source-of-truth artifacts" and update `context-management.md:29` to reference `project-template.json`.

- **`GM-005-F03` (Demonstrated defect | Low-Medium) — Catalog metadata duplicated across six files**
  - **Location:** `agent-workflow-foundation/templates/project-types.json`; `workflow/project-templates.md:16-22`; `templates/new-project-setup.md:17-21, 38-50`; `agent-workflow-foundation/README.md:21-25`; `guides/tooling-operations.md:9-10`; `workflow/tooling-review.md:5-6`
  - **Evidence:** The initial type/template IDs, source roots (`openspec/`, `proposal/`), required tools, and `stage_tooling_review` flags are restated across all six files.
  - **Impact:** Adding a third project type or second template per type (explicitly required by `foundation-consumers/spec.md`) will cause multi-file prose drift.
  - **Correction:** Designate `templates/project-types.json` as the sole canonical catalog owner and `templates/project-types/<type>/<template>.md` as the sole process owner. Replace repeated per-template tool/trigger lists in `new-project-setup.md`, `tooling-operations.md`, and `tooling-review.md` with pointers to `foundation.py templates` and `project-template.json`.

- **`GM-005-F04` (Observed discrepancy | Low) — CX-023 review snapshot SHA-256 mismatch**
  - **Location:** `docs/collaboration-codex.md:523-528`; `docs/handovers/core-project-templates-2026-11-24.md:128-131`
  - **Evidence:** Recomputing the exact documented hash over the 64 working-tree files yields `489e7d7f...`, not `6c6f7b8f...`.
  - **Impact:** Review freshness checks on closure will fail to match unless the cause (post-hash edit vs. hashing script detail) is confirmed.
  - **Correction:** Lead verifies whether any source file changed after CX-023 was drafted or updates the recorded snapshot hash.

#### Findings — 2. Logical Flaws

- **`GM-005-F05` (Demonstrated defect | High) — `project-template.json` hardcodes `"capability_status": "not-verified"` in a three-way-merged template file**
  - **Location:** `agent-workflow-foundation/scripts/project_profiles.py:47, 61`; `agent-workflow-foundation/scripts/foundation.py:98, 213-228`; `agent-workflow-foundation/workflow/local-project-files.md:9-10`
  - **Evidence:** `project_profiles.selection()` writes `"capability_status": "not-verified"` into `agent-workflow-local/project-template.json`, which `foundation.py` tracks in `project_bases` for 3-way merge. Neither `agent_workflow_env.py` nor `tooling_review.py` ever updates this field, and `local-project-files.md:9-10` explicitly states: "capability verification belongs in tooling inventory, not this selection record."
  - **Impact:** Permanent misleading state once tools are actually verified in `tooling.json`; if a consumer edits the field to `"verified"`, future upstream catalog updates risk merge conflicts.
  - **Correction:** Remove `"capability_status"` from `project-template.json` (or replace it with a static pointer `"verification_inventory": "agent-workflow-local/tooling.json"`). Keep all runtime verification state strictly in `tooling.json`.

- **`GM-005-F06` (Demonstrated defect | High) — Proposal PT `chatgpt-claude-manual` cannot be initialized with `chatgpt` in `--agents`, and `collab_lint.py` warns on `chatgpt` messages**
  - **Location:** `agent-workflow-foundation/scripts/foundation.py:22, 288-290`; `agent-workflow-foundation/templates/project-types/proposal-pt-making/chatgpt-claude-manual.md:3-7, 33-55`; `agent-workflow-foundation/scripts/collab_lint.py:120-136`
  - **Evidence:** `foundation.py` restricts `--agents` and `--lead` to `HOSTS = {"codex", "claude", "gemini"}`. A Proposal PT user following the template who runs `--agents chatgpt,claude --lead chatgpt` gets `ValueError: Choose codex/claude/gemini agents and a lead from that roster`. If they initialize with `--agents claude --lead claude` (or `codex,claude`) and record handoffs with `from: chatgpt` or `to: chatgpt`, `collab_lint.py` emits `unknown agent 'chatgpt'` warnings unless `--allowed-agent chatgpt` is manually passed every time.
  - **Impact:** Practical setup/lint friction on the flagship non-SW template.
  - **Correction:** Clarify in `chatgpt-claude-manual.md` and `new-project-setup.md` which local host roster to pass to `foundation.py init` when ChatGPT is an external/manual participant, and optionally allow `project-template.json` (e.g., `external_participants: ["chatgpt"]`) to register non-host participants automatically in `collab_lint.py`.

- **`GM-005-F07` (Demonstrated defect | Medium-High) — Frozen `state["context"]` traps consumers who later adopt or switch templates**
  - **Location:** `agent-workflow-foundation/scripts/foundation.py:193-196`; `agent-workflow-foundation/workflow/project-templates.md:46-48`; `agent-workflow-foundation/workflow/foundation-lifecycle.md:62`
  - **Evidence:** `foundation.py update` always re-renders `project-template.json` and `project-facts.md` using `state["context"]` from `agent-workflow-local/foundation-state.json`. If a `legacy-unselected` consumer (including this repository) later adopts a template or switches templates manually (as `project-templates.md:46-48` notes there is no switching command), `foundation-state.json` still holds the old context, causing persistent conflicts on every subsequent `update` unless the user hand-edits operational metadata `foundation-state.json`.
  - **Impact:** Unreachable clean upgrade path for `legacy-unselected` -> `selected` transitions.
  - **Correction:** Document the scope question for a future deliberate `adopt-template` / `select-template` subcommand (rather than silent switching) that updates `state["context"]` alongside reviewed `project-template.json` and `project-facts.md` migration.

- **`GM-005-F08` (Demonstrated defect | Medium) — `tooling_review.py` lacks `project-template.json` schema validation, omits `manual_requirements`, and permanently retains retired tools**
  - **Location:** `agent-workflow-foundation/scripts/tooling_review.py:44-62`
  - **Evidence:** (1) `tooling_review.py` accesses `profile["stage_tooling_review"]` and `profile["required_tools"]` directly without schema validation, producing opaque `KeyError` messages on malformed profiles. (2) `plan()` never surfaces `profile["manual_requirements"]` (e.g., unresolved `claude-powerpoint-plugin`), so a manual review on Proposal PT omits its most important unresolved prerequisite. (3) Lines 61–62 unconditionally union `latest["tools"].keys()` into `selected`, so once a tool is reviewed it can never be retired from future review plans even after removal from `tooling.json`.
  - **Impact:** Incomplete Proposal PT tooling reviews and sticky retired-tool noise.
  - **Correction:** Validate `project-template.json` via a shared loader in `project_profiles.py`; include `manual_requirements` as an informational section in `tooling_review.plan()` output; only carry forward prior tools that remain in `tooling.json` or `required_tools` (or are passed via `--tools`).

- **`GM-005-F09` (Demonstrated defect | Low-Medium) — `collab_lint.py` falls back to SW `DEFAULT_STAGES` when `project-template.json` is malformed or absent**
  - **Location:** `agent-workflow-foundation/scripts/collab_lint.py:197-216`
  - **Evidence:** When `project-template.json` fails validation, `collab_lint.py` records the profile error but still evaluates `current_stage` against `DEFAULT_STAGES` (SW stages), emitting spurious stage errors on Proposal PT projects. It also does not verify that `profile["workflow"]` exists on disk or that `stages` has no duplicates.
  - **Impact:** Misleading double errors on corrupted non-SW profiles and undetected broken `workflow` paths.
  - **Correction:** Skip stage-name validation when `project-template.json` itself failed to parse/validate, and validate `workflow` path existence + stage uniqueness via shared `project_profiles.py` logic.

- **`GM-005-F10` (Test gap | Medium) — Missing behavioral tests for migration, catalog validation, path traversal on `--source-root`, and corrupt profiles**
  - **Location:** `tests/test_foundation.py`; `tests/test_tooling_review.py`
  - **Evidence:** Existing 78 tests pass, but there are no tests for: (1) `foundation.py migrate` producing `legacy-unselected` and preserving existing `source_root`; (2) `foundation.py templates` CLI output and `project_profiles.catalog()` rejection paths (missing workflow, `..` source_root, duplicate stages, unregistered tool); (3) `foundation.py init --source-root ../escape` failing before writes; (4) `collab_lint.py --strict-state` with malformed `project-template.json`; (5) `foundation.py update` when an upstream catalog removes/renames a consumer's selected template.
  - **Impact:** Regressions in catalog validation, migration compatibility, and corrupt-state handling could ship undetected.
  - **Correction:** Add focused behavioral tests covering these five cases.

#### Findings — 3. Refactoring Recommendations (Prioritized)

1. **P1 (High ROI, zero migration risk) — Share `load_selection()` in `project_profiles.py`:** Move `project-template.json` schema validation out of `collab_lint.py` into `project_profiles.py` and call it from both `collab_lint.py` and `tooling_review.py`. Eliminates duplicated/divergent parsing and fixes `GM-005-F08` and `GM-005-F09`.
2. **P1 (High ROI, minor clean-merge impact) — Drop `capability_status` from `project-template.json` and expose `manual_requirements` in `tooling_review.plan()`:** Resolves `GM-005-F05` and keeps selection vs. verification cleanly separated. Existing consumers merge the key removal cleanly on next `foundation.py update`.
3. **P2 (Medium ROI, low risk) — Split `guides/tooling-operations.md` and remove hardcoded template catalogs from prose:** Moves GitHub/OpenSpec out of the Ponytail/Graphify/RTK bootstrap guide (`GM-005-F01`) and makes adding future templates a 2-file change (`GM-005-F03`).
4. **P3 (Scope question for future version) — Deliberate `select-template` / `adopt-template` CLI flow:** Track as a scoped future enhancement so `legacy-unselected` consumers can adopt a template without hand-editing `foundation-state.json` (`GM-005-F07`).
5. **Retain as-is (do not refactor):**
   - Keep `project_profiles.py` (62 lines) separate from `foundation.py`; clean boundary between catalog resolution and filesystem merge mechanics.
   - Keep `third-party/origins.json` as the sole tool registry referenced by ID from `templates/project-types.json`.
   - Keep `templates/project-types/sw-development/stages.md` (6.2 KB) as a single file rather than splitting into per-stage files (each stage is ~35 lines; splitting would add lookup overhead and fragment the gate progression).
   - Keep `workflow/tooling-review.md` (6.5 KB) as a single on-demand runbook (never loaded at startup or during Proposal PT planning).

#### Findings — 4. Rule Atomization And Context Efficiency

##### Measured Current Context Footprint

Token counts below are **estimates** (~1.33 tokens/word; ~4 bytes/token for Markdown/JSON).

- **Startup path** (`GEMINI.md` + `rule-precedence.md` 4,862 B + `agent-workflow.md` 3,818 B + `project-facts.md` 1,031 B + `rules.md` 255 B + `current-state.md` 194 B + `project-template.json` ~600 B): **~11.4 KB / ~1,365 words (~1,800–2,800 tokens est.)**. Already lean, but `rule-precedence.md` + `agent-workflow.md` represent 76% (8.7 KB) of every startup and include prose only needed during migration, setup, or formal consolidation.
- **SW setup + stage/review path** (Startup + `new-project-setup.md` 3,676 B + `project-templates.md` 3,421 B + `sw-development/openspec-github.md` 2,365 B + `sw-development/stages.md` 6,210 B + `stages.md` 1,313 B + `review-cycle.md` 9,314 B + `collaboration-format.md` 8,039 B + `role-boundaries.md` 5,529 B + `tooling.md` 5,168 B + `tooling-review.md` 6,456 B + `tooling-operations.md` 4,466 B): **~67.3 KB / ~8,865 words (~12,000–16,800 tokens est.)**.
- **Proposal PT planning + manual handoff path** (Startup + `chatgpt-claude-manual.md` 4,493 B + `slide-handoff.md` 1,558 B + `markitdown.md` 5,450 B + `stages.md` 1,313 B + `collaboration-format.md` 8,039 B + `question-model.md` 2,902 B): **~35.1 KB / ~4,774 words (~6,400–8,800 tokens est.)**.

##### Top Mixed-Responsibility Files

1. `workflow/review-cycle.md` (9,314 B / 1,300 w): mixes basic informal review loop with optional critical-review techniques and ELS-012 formal consolidation (`formal: true`).
2. `workflow/collaboration-format.md` (8,039 B / 1,153 w): mixes basic item template/types with parser boundaries, formal finding tables, verification evidence, and lint/queue edge cases.
3. `guides/tooling-operations.md` (4,466 B / 577 w): mixes optional `agent_workflow_env.py` bootstrap (Ponytail/Graphify/RTK) with required SW GitHub/OpenSpec setup.
4. `workflow/stages.md` (1,313 B) + `workflow/legacy-stages.md` (720 B): two tiny router files creating a 4-hop chain (`rule-precedence.md` -> `stages.md` -> `project-template.json` -> `legacy-stages.md` -> `sw-development/stages.md`) for ~2 KB total.

##### Proposed File Map (One Canonical Owner Per Rule, Explicit Load Triggers)

| File (under `agent-workflow-foundation/`) | Change | Canonical Ownership | Load Trigger |
|---|---|---|---|
| `workflow/rule-precedence.md` | Trim (~4.9 -> ~3.4 KB) | Read order, conflict precedence, task routing table | Every startup |
| `workflow/agent-workflow.md` | Trim (~3.8 -> ~2.1 KB) | Core communication/trigger/state model (link out duplicated review/template prose) | Every startup |
| `workflow/collaboration-format.md` | Split (~8.0 -> ~3.2 KB) | Item template, types, IDs, basic queue command, writing style | Writing/reading routine collaboration items |
| `workflow/collaboration-formal.md` | New (~4.2 KB) | Parser boundaries, `formal: true` finding table, verification evidence, lint/alias details | `formal: true` reviews, archival, or lint issues |
| `workflow/review-cycle.md` | Split (~9.3 -> ~4.2 KB) | Informal review loop, combined review+gate concurrence, content freshness | Any review request or response |
| `workflow/review-formal-and-critique.md` | New (~4.5 KB) | Optional critical review techniques; `formal: true` deduplication, priority, disposition, `--check-completion` | `formal: true` consolidation or explicit critical-review pass |
| `workflow/stages.md` | Merge `legacy-stages.md` (~1.8 KB total) | Core `Setup`/`Complete` bookends, transition recording, legacy fallback pointer | Stage transition or `legacy-unselected` consumer (cuts 4 hops to 2) |
| `workflow/project-templates.md` | Trim catalog table (~3.4 -> ~2.6 KB) | Core/template boundary, selection lifecycle, extension policy (point to `project-types.json`) | Project setup, template updates, or adding templates |
| `workflow/role-boundaries.md` | Move Capability Mapping to `tooling.md` (~5.5 -> ~4.2 KB) | Lead/consultant/user authority, advisory lenses, non-interactive scope | Role/authority questions or stage handoff |
| `workflow/tooling.md` | Absorb Capability Mapping (~5.2 -> ~5.6 KB) | Capability policy, capability mapping, installation lifecycle, integration routing | Selecting/installing/verifying tools |
| `guides/env-bootstrap.md` | Split from `tooling-operations.md` (~2.6 KB) | `agent_workflow_env.py` (Ponytail/Graphify/RTK) operations and diagnostics | Opt-in env bootstrap/doctor |
| `guides/integrations/sw-core.md` | Split from `tooling-operations.md` (~1.9 KB) | GitHub repository setup and OpenSpec CLI setup/validation | SW template setup or GitHub/OpenSpec checks |
| `templates/project-types/sw-development/stages.md` | Retain (6.2 KB) | SW Exploration/Proposal/Implementation gates + transition protocol | SW stage work (read active stage section by heading) |
| `workflow/tooling-review.md` | Retain (6.5 KB) | Freshness review triggers, CLI, research rubric, evidence schema | Confirmed stage transition (when enabled) or manual request |

##### Current vs. Proposed Context Load Comparison

| Scenario | Current Load | Proposed Load | Delta & Tradeoff |
|---|---|---|---|
| **Normal startup** | ~11.4 KB / ~1,365 w (~1,800–2,800 tok est.) | ~8.2 KB / ~950 w (~1,250–2,050 tok est.) | **-28%**; 0 extra lookups (trims duplicated core prose) |
| **SW setup + routine stage/informal review** | ~67.3 KB / ~8,865 w (~12,000–16,800 tok est.) | ~44.5 KB / ~5,800 w (~7,700–11,100 tok est.) | **-34%**; defers formal-review, parser internals, and env-bootstrap; 1–2 fewer stage hops |
| **Proposal PT planning + manual handoff** | ~35.1 KB / ~4,774 w (~6,400–8,800 tok est.) | ~25.5 KB / ~3,400 w (~4,500–6,400 tok est.) | **-27%**; defers formal-review/parser internals; 1 fewer stage hop |
| **Formal review consolidation (`formal: true`)** | ~28.7 KB (Startup + `review-cycle` + `collaboration-format`) | ~24.8 KB (Startup + 4 split files) | **-14%**; +2 file lookups, acceptable because `formal: true` is infrequent |

- **Tradeoff check:** Adding only 2 net new workflow files (`collaboration-formal.md`, `review-formal-and-critique.md`) and 1 net new guide (splitting `tooling-operations.md`, while removing `legacy-stages.md`) keeps discoverability high in `rule-precedence.md` without creating tiny-file sprawl. All splits remain cleanly under the existing `workflow/rule-precedence.md` precedence hierarchy.

## Resolved History

Resolved items are preserved in [numbered archives](collaboration-archives/).
Retrieve any item with `python3 scripts/collab_queue.py gemini --id ITEM-ID`.
