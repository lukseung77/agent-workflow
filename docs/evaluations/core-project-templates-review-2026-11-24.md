# Core and Project Templates Review Consolidation

Claude CL-012 and Gemini GM-005 both completed CX-023. Both support the core/template
architecture. Lifecycle and authority gaps need correction before publication.
This report evaluates their findings; implementation follow-up is CX-027.

## Evidence and Content Identity

Both consultants validated the working tree based on
`80428a9b940f1896e88ab3e8898b43def8c5fdc5`: 78 tests, three specifications, clean
collaboration lint, and the 61-file distribution/self-consumer check passed.
Passing checks do not cover the demonstrated lifecycle gaps.

The lead independently reproduced these behaviors in disposable consumers:

| Check | Result |
|---|---|
| Rename `TOC Planning` in the upstream catalog and apply update | Update succeeds; strict lint then rejects the retained current stage |
| Request another template through init on an initialized consumer | Exit 0, `already initialized`; changed selection flags are ignored |
| Set the local workflow path to a missing file | Strict lint reports zero errors |
| Migrate the `specs/accepted.md` fixture without a source-root argument | The file survives but installation context records `openspec/explorations` |

The snapshot discrepancy is resolved. The original script sorted Python `Path`
objects component-wise; the reviewers sorted strings lexically. The same 64 files
produce both recorded digests using the same `path + NUL + bytes + NUL` formula:

- `sorted(paths)`: `6c6f7b8f7d9d3aa9e403192845a7fffdbf37fb299384c95bcb65ae241aa14d85`.
- `sorted(paths, key=str)`: `489e7d7f63d3e7ceea392d987bc1534204a42c1aa14a05d610875cf13b476d6f`.

The ambiguity was in the documented sorting method; source drift was not
demonstrated. Future snapshot tooling should expose an explicit sorting algorithm.
No product source was changed while consolidating the reviews.

## Findings and Dispositions

Accepted means accepted into follow-up work, not already implemented. Priorities
are the lead's assessment. All 24 numbered consultant findings are accounted for;
compound findings are split where their implications differ.

| ID | Source findings | Priority and disposition |
|---|---|---|
| R01 | CL-012-F01 | **High; accept.** Detect process-field and selected workflow changes, show them distinctly in update review, and require deliberate acceptance before applying changes that can invalidate current work. A textual merge is not a compatibility check. |
| R02 | CL-012-F02, GM-005-F07 | **High; partially accept.** Changed selection flags must not disappear into a successful init no-op. There is no supported adoption path; a review-first adoption command is a proposed feature requiring a scope decision. Manual edits can remain locally preserved while leaving stored context inconsistent; they do not necessarily conflict immediately on every update. |
| R03 | CL-012-F03 | **Medium; defer policy choice.** Legacy updates add Grill-Me to review selection despite the no-new-integration compatibility promise. Clarify whether existing consumers preserve requirements or receive an offered core capability. Lead must settle this before changing behavior. |
| R04 | CL-012-F04 | **Medium; accept ambiguity, defer policy choice.** Distinguish core inclusion, required native availability, requested invocation, and disclosed fallback. Do not infer mandatory interviews or installation from core inclusion. |
| R05 | CL-012-F05, GM-005-F06 | **High for proposal usability; accept.** Separate local file-capable hosts from external/manual participants, assign record ownership, and define Claude's production delegation. Manual transfer is settled; ChatGPT filesystem authority is not. Prefer explicit role/record guidance before adding new host support. |
| R06 | CL-012-F06 | **Medium; accept with qualification.** Explicitly place local selection, catalog defaults, template process, and generic rules in precedence. Template process must not expand write/publication authority; JSON fields are not unrestricted authority overrides. |
| R07 | CL-012-F07 | **Medium; accept intent.** Check stage-name and workflow-criteria consistency. SW intentionally uses a separate stage document, so validate that reference as well instead of requiring every heading in the primary template file. |
| R08 | CL-012-F08, GM-005-F03 | **Medium; accept.** Remove duplicated operational lists from shared procedures. Catalog owns selectable metadata; template files own process; local record governs the installed selection. READMEs may retain descriptive overviews. |
| R09 | CL-012-F09, GM-005-F05 | **Medium; partially accept.** Remove permanent `capability_status`; point to actual tooling inventory. Guided installation is legitimate static policy and should remain. Define handoff vocabulary and manual prerequisites; agent-readable metadata need not have an executable reader to be useful. |
| R10 | CL-012-F10, GM-005-F08, GM-005-F09 | **Medium; accept.** Share record validation, check safe/existing workflow paths and unique stages, and avoid secondary SW-stage errors after profile failure. Surface manual prerequisites informationally. Make tool retirement explicit while preserving intentional selections awaiting inventory; blindly removing prior explicit selections would regress resume behavior. An absent record still needs the deliberate legacy fallback. |
| R11 | CL-012-F11 | **Medium; accept.** Add plugin verification to the production entry gate. Define RFP amendments, brief revisions/re-approval, changed slide IDs, and correction loops within final review. Preserve manual handoffs. |
| R12 | CL-012-F12, terminology part of GM-005-F02 | **Low; accept.** Neutralize generic SW wording, document automatic template-stage loading, and label SW examples. Keep useful domain examples where their scope is explicit. |
| R13 | CL-012-F13, GM-005-F10 | **Medium; accept.** Add generated-record integration cases, migration root/review-scope cases, corrupt-profile handling, catalog rejection cases, source-root traversal, and removed selected templates. Test guarantees rather than implementation details. |
| R14 | CL-012-F14, GM-005-F04 | **Low; resolved.** Both digests reproduce; clarify sorting in the snapshot record. No stale source was established. |
| R15 | GM-005-F01 | **Medium; accept.** Registry `optional: true` conflicts with template requirements. Selection owns requirement status. Separate SW setup instructions from optional environment bootstrap; retain MarkItDown's valid distinction between conversion policy and installation adapter. |
| R16 | migration part of GM-005-F02 | **High for affected consumers; accept.** Recover an authoritative existing source root or require a missing choice before writes. Do not inject an OpenSpec root into migration of another project layout. |

## Refactoring and Context Efficiency

Correct lifecycle behavior and authority first. Keep catalog resolution separate
from installer merge mechanics, and retain the local selection as a project pin
rather than resolving all fields live from a changing catalog.

Recommended ownership and read triggers:

| Owner | Responsibility and load trigger |
|---|---|
| `workflow/rule-precedence.md` | Startup order, precedence, task routing; every startup |
| `workflow/agent-workflow.md` | Compact communication, trigger, state model; every startup |
| `workflow/project-templates.md` | Selection lifecycle and extension; setup/adoption/template work |
| Catalog and local record | New selection defaults versus installed metadata; scripts/relevant setup and stage work |
| Selected template workflow | Process, roles, gates, amendments, handoff ownership; relevant project work |
| `workflow/stages.md` | Transition recording and concise legacy fallback; stage work |
| `workflow/grill-me.md` | Availability, invocation, fallback, dependency adapter; setup/requested interview |
| `workflow/foundation-lifecycle.md` | Update acceptance and adoption guarantees; lifecycle operations |
| `workflow/tooling.md` | Capability mapping, lifecycle, integration routing; capability selection/setup |
| Separate SW integration guide | GitHub/OpenSpec operations; use of those integrations |
| Environment bootstrap guide | Optional adapter operations; explicit bootstrap/doctor |
| Routine collaboration/review files | Routine message/review contracts; writing or evaluating messages |
| Optional formal-review material | Detailed formal findings/accounting; formal reviews/completion audits |

Accept removing the extra legacy routing hop, moving capability mapping to its
tooling owner, and separating SW integration from environment bootstrap. Preserve
redirects or deliberate consumer update handling when paths change. Keep SW stage
definitions together, the proposal process together, and its copyable handoff form
separate. Splitting each stage or paragraph would add retrieval overhead.

Partially accept separating formal-review details from routine review guidance.
Optional critique and formal accounting have different load triggers and should
not be combined solely because both are infrequent. Keep parser invariants needed
by every message author visible in routine collaboration guidance; detailed
implementation mechanics can be loaded on demand.

Gemini's projected 27–34% context reductions are estimates, not achieved savings.
The reviewers used different scenario boundaries and local/scaffold combinations.
Measure identical representative consumers and tasks before and after refactoring;
record words/bytes and lookup counts, labeling token conversions as estimates.

## Follow Up

CX-027 keeps required correction work visible for Codex. Both responses and all
findings have been reconciled, so CX-023 may close independently of implementation.
Closure does not establish that fixes, stage gates, or publication are complete.
Settle adoption scope and Grill-Me compatibility/fallback before dependent changes.
Preserve the consultant-authored review files unchanged.
