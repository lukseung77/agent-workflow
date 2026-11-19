# Project Evaluation And Refactor

Date: 2026-11-19. Baseline: `04ea42048d38b50d166b03fad8fd609fc368ba6b`.
Sources: Claude's CL-005 in `docs/collaboration-claude.md` and Codex's independent
source review. The human requested implementation and a whole-project refactor
after receiving Codex's assessment. Claude's original proposal is preserved.

## Combined Disposition

| Source | Decision | Reason and intended result |
|---|---|---|
| CL-005-P01 | Adopt | Clarify canonical stages versus tooling activities and track unfinished follow-ups explicitly. |
| CL-005-P02/P03 | Adopt together | Ignore fenced example headers and fields; preserve complete item bodies during archival. |
| CL-005-P04 | Adopt boundary rule | End an item at an unprotected heading of level 1–3; headings of level 4–6 remain item content. Preserve standing sections in live files. |
| CL-005-P05 | Adopt with compatibility | Warn on unknown sender/recipient names; support explicit extra names and the documented Gemini alias. |
| CL-005-P06 | Adopt | Exercise doctor, CLI/JSON, invalid names, installation fallback, and partial failures without invoking real tools. |
| CL-005-P07 | Adopt display correction | Distinguish unrequested agents from missing agents. Keep optional tooling non-blocking. |
| CL-005-P08 | Adopt | Report the shared adapter separately from unverifiable native Ponytail plugin state. Preserve the existing JSON tool key for consumers. |
| CL-005-P09 | Defer default pins | No tested release baseline has been selected. Document moving upstream versions and support explicit version/revision selection rather than inventing pins. |
| CL-005-P10 | Adopt labels | Keep proposal paths stable; label draft rule copies and exclude the directory from normal startup. |
| CL-005-P11 | Adopt | Ignore OS metadata and add dependency-light continuous validation. Validate OpenSpec separately when its CLI is available. |
| CL-005 process note | Adopt | A completed consolidation must link separate active items for work still required. |
| CL-005-H01 | Separate release decision | Updating this checkout does not authorize merging or publishing the branch. |
| CL-005-H02 | Retain intake decisions | Suggestions 002 and 003 retain their recorded states; the refactor does not settle deferred product proposals. |

## Independent Findings

| ID | Finding | Intended correction |
|---|---|---|
| CX-008-F01 | HTML-comment fields can overwrite live metadata even though comment headers are ignored. | Use the same Markdown visibility rules for headers and fields. |
| CX-008-F02 | Metadata-looking body bullets overwrite fields from the header. | Parse metadata only in the initial contiguous field block. |
| CX-008-F03 | Queue timestamps sort lexically, so differing UTC offsets can reverse real chronology. | Compare timezone-aware UTC instants; preserve deterministic fallback for invalid legacy input. |
| CX-008-F04 | Archive numbers sort lexically and can collide after 999. | Select the maximum numeric suffix and create archives exclusively. |
| CX-008-F05 | Optional command exceptions can abort the entire bootstrap. | Turn per-command OS and timeout failures into warnings and continue independent integrations. |
| CX-008-F06 | Existing managed adapter markers are trusted without checking closure or updating the pointer. | Replace only a valid managed block, preserve surrounding text, and reject malformed blocks without rewriting them. |
| CX-008-F07 | Formal completion checks see only live files, so archiving reviewer evidence can invalidate a completed review. | Include numbered archives for completion evidence while keeping active queues limited to live files. |
| CX-008-F08 | A local `RTK.md` can suppress explicitly requested global host configuration. | Only use the local adapter to skip Antigravity's project-scoped setup; let the upstream CLI handle requested global setup. |

## Assumption Review

An installed `grill-me` skill was not found in the available skill catalog or
local skill directories. Use its question-driven approach as an equivalent
review method, without claiming to have invoked that skill.

- What outcome matters? Ask the human whether to preserve and harden the current
  workflow, simplify with breaking changes, or introduce orchestration.
- What must remain stable? Existing file paths, command entry points, governance,
  manual activation, agent ownership, and downstream adapters are compatibility
  contracts unless the human requests a change.
- Can an example silently become work? Markdown examples, comments, and body
  metadata must never create tasks or change their lifecycle state.
- Can cleanup change meaning? Archival must preserve complete items and leave
  standing sections intact. Archived review evidence must remain discoverable.
- Does a green indicator prove the claimed capability? Distinguish an installed
  CLI, a shared instruction adapter, an unrequested agent, and unknown plugin state.
- Is a rewrite necessary? Keep the standard-library tools and focused rule map;
  refactor shared behavior and contradictions instead of adding a framework.
- What counts as completion? Regression coverage for the actual failures,
  repository lint, repeatable validation, documented compatibility and rollback.

This is a Codex assumption review, not a second consultant review. A scope
question was presented with three alternatives: preserve and harden the current
workflow, accept breaking simplification, or introduce orchestration. No answer
was received during implementation. Preserving the workflow is the lead's
conservative working assumption, not an additional human-confirmed decision.
The human's direct instruction authorizes the combined fixes and refactor.

## Compatibility And Remaining Decisions

- Existing commands, paths, and JSON keys remain available. The diagnostic label
  `Shared adapter` replaces `Ponytail rules`; `tools.ponytail` still means shared
  adapter presence for JSON consumers. Native plugin state remains unknown.
- Keep item metadata contiguous in its header. Move level 3 body subheadings to
  level 4 or deeper before downstream adoption. Fenced examples are preserved.
- Real optional-tool installation and host configuration were not exercised;
  lifecycle tests use fakes. CI configuration is added but has not run on GitHub.
- Default upstream install versions remain unpinned. Explicit selectors support
  a project's tested versions without claiming a universal supported release.
- Broadcast review rosters, authorized reviewer skips, and exact finding mapping
  remain lead checks; the linter does not certify the entire formal review gate.
- The two older downstream suggestion statuses remain unchanged. The branch is
  not merged or published by this maintenance task.

## Final Verification

`python3 -B scripts/validate.py --require-openspec` passed against the final
implementation: 39 unit tests passed, collaboration lint reported zero errors
and zero warnings, and both OpenSpec changes validated with OpenSpec 1.3.1.
`git diff --check` passed. The CI workflow uses that same explicit OpenSpec
version. Actual upstream installations, host hooks, and GitHub CI execution are
outside the verified results. Existing Python entry points and project paths
were retained; OS metadata was ignored without deleting the user's file.

## Follow-up: Prompt Simplification

The human approved applying the subsequent unnecessary-prompt findings. Agent
templates and shared prompts now use explicit project assignments rather than
model-strength prescriptions. The three instruction templates decreased from
152 to 55 lines combined. Canonical routing and message examples replace copies;
current stage and constraints stay in local state/rules files. Interview counts
are optional, joining-project reads follow affected files and dependencies, and
environment constraints are reported when they affect work. Consultants report
cleanup findings within their authority. Defined-term formatting and stage
concurrence remain policy choices for a separate decision.

This documentation pass passed collaboration lint with zero errors/warnings and
`git diff --check`. Runtime tests were not rerun for these prompt-only changes.

## Follow-up: Critical Review And CL-006

The approved critical-review integration and every CL-006 disposition, including
compatibility decisions, deferred policies, measured context reduction, and final
verification, are recorded once in `docs/collaboration-codex.md` item CX-010.
