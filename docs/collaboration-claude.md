# Claude Collaboration

## Resolved History

Resolved items are preserved in [numbered archives](collaboration-archives/).
Retrieve any item with `python3 scripts/collab_queue.py claude --id ITEM-ID`.

### [CL-010] Foundation evaluation — inefficiency, inconsistency, redundancy, refactor
- `date`: 2026-11-23
- `created_at`: 2026-11-23T13:16:18+09:00
- `from`: claude
- `to`: codex
- `type`: suggestion
- `status`: open
- `scope`: `agent-workflow-foundation/` (product source)
- `why`: Third-party tooling guidance is now 52% of the product and repeats one procedure in seven places; several rules disagree with each other.
- `request`: Disposition each finding; the three items marked "human" need the user's decision first.
- `refs`: `agent-workflow-foundation/`

Origin: explicit human assessment request to Claude on 2026-11-23, quoted exactly: "please evaluate agent-workflow-foundation for inefficiency, inconsistancy, redundant then refactor suggestions."

#### Reviewed content and checks

- Branch `codex/template-guidance-refactor`, HEAD `341f5cf` plus the uncommitted working tree (9 modified foundation files; untracked `docs/integrations/`, `docs/tool-selection.md`, `scripts/tooling_review.py`, `workflow/grill-me.md`, `workflow/tool-integrations.md`, `workflow/tooling-review.md`, `templates/agent-workflow-local/tooling-reviews.json`).
- Read in full: all 23 `workflow/*.md`, all templates, `README.md`, `foundation.json`, `SKILL.md`, `docs/agent-tooling.md`, `docs/tool-selection.md`, and 3 of the 8 `docs/integrations/` adapters (engineering, efficiency, references). The other 5 adapters were only searched, not read.
- `third-party/origins.json` was analysed structurally (fields and value counts), not entry by entry. Origin URLs were not checked against the network.
- Scripts were not code-reviewed; I read `foundation.py:83-124` and the function lists only.
- Ran `collab_queue.py user` and `tooling_review.py --root .` (both exit 0). The test suite was not run. Paths below are relative to `agent-workflow-foundation/`.

#### Inconsistencies

| ID | Location | What | Correction |
|---|---|---|---|
| I1 | `workflow/stages.md:42,83,108-110` vs `:118` | The transition protocol requires explicit concurrence from every agent for every transition. The Exploration gate lists it, the Proposal gate only says consultants "have reviewed the draft", and the Implementation gate lists nothing. | Remove the per-stage reviewer bullets and keep concurrence only in the protocol, or make the three gates say the same thing. |
| I2 | `templates/new-project-setup.md:37` vs `workflow/tooling-review.md:13-17` | Setup says run the tooling review "before final tool selection"; the review says run it "after establishing ... selected capabilities" and its command needs `--tools SELECTED_REGISTRY_IDS`. | State one order: candidate selection, review, then install. |
| I3 | `workflow/tooling-review.md:35` vs `:107` | `current` means "this event has a recorded review" for the checker and "tool is up to date" for a per-tool status. The file needs a disclaimer to explain it. | Rename the checker result (for example `recorded`). |
| I4 | `third-party/origins.json`; `docs/tool-selection.md:124-126`; `workflow/tool-integrations.md:55-58` | `auto_install` is `false` on all 35 entries, including Graphify and RTK, which `agent_workflow_env.py --install-missing` can install. The text says "new catalog entries have `auto_install: false`", implying a distinction the data does not have. | Mark the entries the bootstrap can install, or drop the field. |
| I5 | `workflow/review-cycle.md:161-168` vs `:134` | The consolidation template has Adopted, Partially adopted and Not adopted but no Deferred, although deferral is an allowed disposition. | Add a `Deferred:` block with owner or trigger. |
| I6 | `workflow/rule-precedence.md:8-10` | `docs/collaboration-*.md` resolves from the project root while `docs/agent-tooling.md`, `docs/tool-selection.md` and `docs/integrations/` resolve from the foundation root. This repository also has its own root `docs/agent-tooling.md`. The same prefix means two roots. | See R5. |
| I7 | `templates/project-init.md:38` vs `templates/new-project-setup.md:23-29` | Tool setup points to `docs/agent-tooling.md` in one file and to `docs/tool-selection.md` plus `workflow/tool-integrations.md` in the other. | See R6. |
| I8 | `README.md:5-6` vs `docs/tool-selection.md:18,45,48,61,64,71`; `workflow/tool-integrations.md:64,66`; `request_items` in `origins.json` | The README says the product contains no consuming project's state. The catalog still records one request's history: "Evaluation Of The Requested Options", request numbering, "Corrected `haydenschitty`", "presumably the intended tree.js", "this request", "by human direction", "This foundation repository already has ...". | See R2. |
| I9 | `workflow/agent-workflow.md:29-30` | Two lead-only startup duties sit in the shared file every agent reads at startup. | Move them to a lead section in `role-boundaries.md` or to the startup command in R4. |

#### Redundancy

| ID | What | Where |
|---|---|---|
| D1 | The select → install from official origin → verify → record in `tooling.json` procedure is written seven times. | `workflow/tool-integrations.md:28-52`, `docs/tool-selection.md:88-122`, `workflow/grill-me.md:9-39`, `workflow/foundation-lifecycle.md:67-74`, `workflow/agent-tooling.md:3-7`, `docs/agent-tooling.md:3-5`, `templates/new-project-setup.md:23-40` |
| D2 | The assessment table restates fields the registry already has (`disposition`, `activate_when`, `considerations`). | `docs/tool-selection.md:57-86` vs `third-party/origins.json` |
| D3 | The excluded-tool list appears six times. | `workflow/tool-integrations.md:61-68`, `docs/tool-selection.md:14-19`, `README.md:36`, `templates/new-project-setup.md:30-32`, `workflow/tooling-review.md:50-51`, `integration_exclusion` in the registry |
| D4 | The tooling-review trigger is stated six times. | `workflow/stages.md:121`, `workflow/agent-workflow.md:30`, `workflow/tool-integrations.md:30-32`, `templates/new-project-setup.md:37-40`, `README.md:38-40`, `workflow/tooling-review.md:3-9` |
| D5 | Grilling interview rules are written twice. | `workflow/question-model.md:43-53`, `workflow/grill-me.md:46-60` |
| D6 | "Accepted decisions must flow into source-of-truth files" appears six times. | `workflow/agent-workflow.md:12`, `workflow/role-boundaries.md:75`, `workflow/decision-protocol.md:107-109`, `workflow/collaboration-format.md:9`, `workflow/context-management.md:21`, `SKILL.md:34` |
| D7 | "Local authority does not reach the upstream foundation" appears six times. | `workflow/role-boundaries.md:22,74,76`, `workflow/rule-precedence.md:5-6,49-50`, `workflow/upstream-feedback.md` |
| D8 | The reference-registry write exception appears three times. | `workflow/role-boundaries.md:18`, `workflow/collaboration-format.md:7`, `workflow/markitdown.md:38-40` |
| D9 | File-placement rules appear twice. | `workflow/context-management.md:33-40`, `workflow/local-project-files.md:17-21` |
| D10 | Seven files are referenced by no rule, template or script, and `foundation.py` installs none of them (it uses only `templates/agent-workflow-local/` and the three host files). | `templates/agent-common.md`, `templates/roles/lead-agent.md`, `templates/roles/consultant-agent.md`, `templates/docs/collaboration-agent.md`, `templates/docs/collaboration-format.md`, `templates/docs/collaboration-index-agent.md`, `workflow/ai-coworking-guide.md` |
| D11 | The `foundation.py init` command is shown three times with two different rosters. | `README.md:16`, `workflow/foundation-lifecycle.md:18`, `templates/new-project-setup.md:11` |
| D12 | Registry boilerplate: 29 identical `installation` strings and two constant fields (`optional: true`, `auto_install: false` on all 35). | `third-party/origins.json` |

#### Inefficiency

| ID | What | Evidence |
|---|---|---|
| E1 | Optional third-party tooling outweighs the workflow itself. | Tooling files total 122.8 KB of 234 KB (52%); the ten core rule files total 50.9 KB. |
| E2 | Lead startup takes four commands (own queue, `user` queue, `--refs` for open requests, tooling review). The tooling check prints 60 lines (2.5 KB) of JSON when the answer is simply `current`. | `workflow/agent-workflow.md:29-30,36`; measured output of `tooling_review.py --root .` |
| E3 | (human) A fresh online review of every selected tool is required at every stage transition and every new OpenSpec change, "even if little time has elapsed". Cost grows with the number of tools and changes. | `workflow/tooling-review.md:3-9,38-39` |
| E4 | Each per-agent adapter is read at every startup but holds mostly maintainer advice ("Keep `CLAUDE.md` as a short bootstrap") and three identical header lines. | `workflow/agent-workflow-{claude,codex,gemini}.md` |
| E5 | Legacy handling is spread through the startup path: two of six read-order steps, one of five precedence levels, and persistent-index notes in four files. | `workflow/rule-precedence.md:16,20,54`; `workflow/agent-workflow.md:26`; `workflow/collaboration-format.md:164`; `workflow/context-management.md:59` |

#### Refactor suggestions, in priority order

- **R1 — One tooling policy, one catalog.** Merge `workflow/agent-tooling.md`, `workflow/tool-integrations.md` and the procedure half of `docs/tool-selection.md` into a single `workflow/tooling.md` that holds the policy, the lifecycle (once) and the exclusion rule (once). Keep `origins.json` as the only catalog and delete the assessment table. Adapters keep only their per-tool tables. `grill-me.md` and `tooling-review.md` keep what is specific to them and link to the lifecycle. Resolves D1–D4, I4, I7, most of E1.
- **R2 — Remove request history from the product.** Rewrite the catalog wording as general guidance and drop `request_items`; keep the history in this repository's change log. Resolves I8.
- **R3 — (human) Retire or isolate legacy support.** Delete the seven dead files (D10). Move the remaining legacy rules into one `workflow/compatibility.md` that is outside the startup path. This is safe only if no existing project still uses the old layout, which I cannot determine from this repository. Resolves D10, E5.
- **R4 — One lead-startup command.** For example `collab_queue.py <agent> --startup`: own queue, open `to: user` items, responses to the lead's open review requests, and a one-line tooling-review status. Print the full review plan only when the status is `review-required`. Resolves E2, I9.
- **R5 — (human) Rename the foundation's `docs/` directory** (for example `guides/`) so `docs/` always means the project root, and stop using the basename `agent-tooling.md` in two directories. This changes paths for existing consumers, so it needs the user's decision. Resolves I6.
- **R6 — One setup document.** Merge `templates/project-init.md` and `templates/new-project-setup.md`; show the init command there only and link to it from the README and lifecycle file. Resolves I2, I7, D11.
- **R7 — State each cross-cutting rule once.** Pick one owner for D5–D9 (suggested: `grill-me.md`, `decision-protocol.md`, `upstream-feedback.md`, `markitdown.md`, `local-project-files.md`) and replace the other copies with nothing or a short link.
- **R8 — Small fixes.** I1, I3, I5; fold each per-agent adapter's one or two host-specific lines into the host entry template or make the adapter an on-demand read (E4); drop the constant registry fields and default the `installation` string (D12); remove the empty stray directory `workflow/context-management/` (local only, not tracked by Git).
- **E3 — (human) Tooling-review frequency.** Option: reuse a completed review for a set period (for example 30 days) unless a tool was added or the stage needs a new capability. The current always-fresh rule was the user's choice, so this is theirs to change.

### [CL-011] Update to CL-010 — human decisions on legacy support and tooling-review frequency; migration plan
- `date`: 2026-11-23
- `created_at`: 2026-11-23T13:40:00+09:00
- `from`: claude
- `to`: codex
- `type`: suggestion
- `status`: open
- `scope`: `agent-workflow-foundation/` legacy handling, tooling-review triggers, migration from the pre-foundation layout
- `why`: The human answered two of the three open decisions in CL-010 and asked for a migration plan.
- `request`: Use this item in place of CL-010 R3 and E3; disposition M1–M4 and T1–T5 with the rest of CL-010. CL-010 R5 (rename foundation `docs/`) still awaits the human.
- `refs`: CL-010, `agent-workflow-foundation/`

Origin: human reply to Claude on 2026-11-23, quoted exactly: "legacy support is only limited to existing project.  also devise a migration plan to move from older agent-workflow.  tooling review frequency is when openspec stage changes and manual request.  please update your suggestions"

Reviewed content: same working tree as CL-010 (HEAD `341f5cf` plus uncommitted changes). Additional checks: read `scripts/foundation.py:144-232` (init and update), the old setup checklist at `130975c:templates/new-project-setup.md`, and the argument list of `scripts/tooling_review.py`. Nothing was executed against a real older project, so the migration steps are a design, not a tested procedure.

#### Decision 1 — legacy support only for existing projects (replaces CL-010 R3)

- **L1.** New projects get no legacy path. Remove legacy wording from everything a new project reads at startup: `workflow/rule-precedence.md:16` (the `docs/collaboration.md` clause), `:20` (step 5), `:54` (precedence level 3); the persistent-index notes in `workflow/agent-workflow.md:26`, `workflow/collaboration-format.md:164`, `workflow/context-management.md:59`; the legacy line in `workflow/local-project-files.md:10`.
- **L2.** Put all remaining legacy rules in one on-demand file, `workflow/migration.md` (see M1), with one routing-table row: "Existing project on the pre-foundation layout".
- **L3.** Detection rule, stated once in `rule-precedence.md`: a project with no `agent-workflow-local/foundation-state.json` is a legacy project; read `workflow/migration.md` before other work.
- **L4.** Delete the seven unused pointer files listed in CL-010 D10. They do not help an unmigrated project: the old layout pointed at `<workflow-root>/workflow/` and `<workflow-root>/templates/` at the repository root, and those directories no longer exist there (the root now holds only `agent-workflow-foundation/`, project files and a `scripts/` directory containing `validate.py`). An older project that pulls the current repository as its sibling workflow root therefore already has broken pointers. That makes migration the only working legacy path, and it should be stated in the repository README.

#### Decision 2 — migration plan from the older agent-workflow layout

What the old layout looks like (from `130975c`): workflow root as a sibling `../agent-workflow/` or vendored `./agent-workflow/`; `docs/collaboration.md` bootstrap; `docs/collaboration-format.md` pointer; `agent-common.md`; `CODEX.md` plus a pointer line in `AGENTS.md`; roles in `agent-workflow-local/agent-workflow-{agent}.md`; optional `agent-workflow-local/agent-workflow.md`; optional `docs/collaboration-index-*.md`; a tooling block in `AGENTS.md` pointing at `<workflow-root>/workflow/agent-tooling.md`.

- **M1 — Write `workflow/migration.md`** with the procedure below. It is run by the project's lead, on the human's request, in one commit.
- **M2 — Add `foundation.py migrate --project .`** (read-only by default, `--apply` to write), so the inventory and mechanical steps are not done by hand. Until it exists, the lead follows M1 manually.
- **M3 — Fix one installer gap.** `initialize` skips existing local files (`foundation.py:160-163`) yet records the new template as their merge base (`:176`). For a migrated project the first `update` then treats every pre-existing local file as locally edited. Either record the actual file content as the base for pre-existing files, or document that the first update after migration needs manual review.
- **M4 — Test it.** Add a fixture of the old layout under `tests/` and a test that runs init plus migrate and then lint.

Procedure for M1:

| Step | Action | Writes |
|---|---|---|
| 0. Prepare | Commit or stash the project so the migration is one revertible commit. Note the old workflow-root path and its commit. | none |
| 1. Inventory | List which legacy items exist: the files named above, old path strings (`agent-workflow/workflow`, `agent-common.md`, `CODEX.md`) in host files, and where roles are recorded. | none |
| 2. Install | `foundation.py init --project . --source SOURCE --project-name NAME --agents ROSTER --lead LEAD`. This copies the foundation, adds the managed startup block to each host file, and leaves existing local configuration and collaboration files untouched. | `agent-workflow-foundation/`, host files, `foundation-state.json` |
| 3. Facts | In `project-facts.md`: add the foundation root; move lead, consultants and review lenses out of the per-agent local files. Keep a per-agent file only if it still holds a restriction; otherwise delete it. | `agent-workflow-local/` |
| 4. Overrides | Move each rule in `agent-workflow-local/agent-workflow.md` into `rules.md` using the override style (rule, reason, replacement), then delete the file. | `agent-workflow-local/` |
| 5. Host files | Remove old pointer lines to `agent-common.md`, `CODEX.md` and `docs/collaboration.md`. Re-point the tooling block with `agent_workflow_env.py init --foundation-root agent-workflow-foundation`. Keep all other project instructions. | host files |
| 6. Remove | Delete `docs/collaboration.md`, `docs/collaboration-format.md`, `agent-common.md`, `CODEX.md`, index files (after step 7 confirms queues work), and any vendored `./agent-workflow/` copy. | project root, `docs/` |
| 7. Verify | Lint with `--strict-state`; queue for each agent and for `user`; `--id` on one archived item; search for leftover old path strings. | none |
| 8. Record | One `status` item in the lead's file: old root and commit, new foundation fingerprint, files removed, rollback (revert the migration commit). | lead's collaboration file |

Not changed by migration: current stage, accepted decisions, collaboration history and item IDs, archives, the reference registry, installed tools. No scope interview is repeated. Tooling review is not triggered by migration (see T2).

#### Decision 3 — tooling review only on OpenSpec stage change and manual request (replaces CL-010 E3)

- **T1.** State the two triggers once, in `workflow/tooling-review.md`: a confirmed stage change, and an explicit human request.
- **T2.** Remove the automatic setup trigger: `workflow/tooling-review.md:3,13-17`, `templates/new-project-setup.md:37-40`, `workflow/tool-integrations.md:30-32`, `README.md:38-40`, and the "new-project setup" wording in the routing row of `workflow/rule-precedence.md`. Setup still selects tools; it no longer runs a freshness review unless the human asks.
- **T3.** Remove the every-startup check: `workflow/agent-workflow.md:30` and `workflow/tooling-review.md:30-39`. If a missed stage-change review must still be caught, show it as one line in the startup command of CL-010 R4 instead of a separate command. This also removes most of CL-010 E2.
- **T4.** In `scripts/tooling_review.py`, replace the `setup` event with `manual` (events today are `setup`, `stage-change`, `resume`) and adjust `tests/test_tooling_review.py`.
- **T5.** Two points of interpretation for the human to confirm, because the reply did not settle them:
  - I read "openspec stage changes" as the stage transitions in `workflow/stages.md` (Exploration → Proposal → Implementation). The current rule also fires when a new OpenSpec change enters a stage with the same name (`workflow/stages.md:121`, `workflow/tooling-review.md:8-9`). I have left that in; say so if it should go.
  - T3 removes the resume check on the reading that only the two named triggers should cost anything.

#### Effect on CL-010

- R3 is replaced by L1–L4 and M1–M4.
- E3 is replaced by T1–T5.
- D4 (trigger stated six times) is resolved by T1–T3.
- E5 (legacy in the startup path) is resolved by L1–L3.
- All other CL-010 findings stand unchanged.
