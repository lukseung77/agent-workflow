# Suggestion: Add Phase-Specific Consultant Role Guidance

## Suggestion

- `submitted_at`: 2026-09-08T14:18:00+09:00
- `from-project`: rideroute
- `from-agent`: codex
- `workflow-version`: 079cf51
- `status`: proposed

## Observed Problem

The current workflow defines general lead/consultant boundaries and OpenSpec stages, but it does not give a reusable way to describe what each consultant should focus on during Exploration, Proposal, and Implementation. In Rideroute, this had to be re-derived from collaboration history after the local workflow sync.

This creates repeated work and ambiguity at phase transitions. A fresh session can know that consultants review, but not which review lens each consultant should apply, when to engage, or how to avoid duplicating another consultant's work.

## Evidence

- Rideroute used Codex as implementation lead/integrator and Claude/Gemini as consultants through Exploration, Proposal, and Implementation.
- Local collaboration entries `CX-278`, `CL-028`, and `GM-028` show both consultants independently recommending explicit phase-specific roles.
- Claude identified that its local role file had an Implementation-only responsibility block, while Exploration and Proposal responsibilities existed only implicitly in collaboration history.
- Gemini identified enough local evidence to formalize complementary consultant roles across all three phases.
- The observed useful split was:
  - Codex: lead author, integrator, final reconciliation, and implementation owner.
  - Claude: fixed-reference verification, domain contract safety, acceptance criteria audit, lifecycle/state invariant review, edge-case coverage, and test fidelity.
  - Gemini: broad-context consistency, architecture and stack feasibility, storage/performance/data-pipeline review, map/UI boundary review, and simplification pressure.

## Suggested Change

Add upstream guidance for phase-specific consultant role mapping. This could be a small section in `workflow/role-boundaries.md`, a companion workflow note, and/or a reusable local template block for project `agent-workflow-local` role files.

Suggested generic model:

- One agent remains the lead/integrator for a phase or milestone. The lead drafts, edits, reconciles feedback, and owns final changes.
- Consultants are assigned review lenses per OpenSpec phase. These lenses are advisory defaults, not exclusive authority, and each project can override them locally.
- Consultant role files should state both phase scope and engagement cadence.
- When consultants overlap, the role model should say which side keeps the fixed-reference verification work and which side keeps broad/generative architecture work.

Suggested OpenSpec phase lenses:

- Exploration:
  - Fixed-reference/domain consultant: find contradictions between exploration files, missing entities, undefined lifecycle states, unhandled user-flow edge cases, and cleanup claims that did not land in every affected file.
  - Architecture/breadth consultant: check terminology consistency across large file sets, platform/provider/storage assumptions, long-term roadmap compatibility, and early simplification options.
- Proposal:
  - Fixed-reference/domain consultant: audit Given-When-Then acceptance criteria, field/schema completeness, explicit out-of-scope decisions, lifecycle preconditions, cross-slice contradictions, and stage-gate readiness.
  - Architecture/breadth consultant: assess tech-stack feasibility, data pipeline shape, performance bounds, implementation complexity, library choices, and simplification opportunities.
- Implementation:
  - Fixed-reference/domain consultant: review diffs against frozen proposal text, domain invariants, validation rules, lifecycle/archive/trash/provenance behavior, split/merge/export semantics, and tests against acceptance criteria.
  - Architecture/breadth consultant: review frontend architecture, state/storage adapters, map-provider boundaries, parsing/export pipelines, geometry algorithms, performance, and test infrastructure.

Suggested engagement cadence:

- Exploration and Proposal: review after major lead cleanup passes and before every stage transition, with explicit concurrence or blockers against gate criteria.
- Implementation: review at milestone gates, per milestone or per coherent batch, using collaboration-file review requests.

## Expected Before/After Improvement

Before: projects know that consultants should review, but must infer phase-specific responsibilities from prior discussion. This increases duplicate review, missed gaps, and stage-transition ambiguity.

After: projects can quickly create local role files with clear review lenses, reducing repeated negotiation and making stage gates easier to audit. The model also makes future cycles, such as backend/cloud/mobile phases, easier to restart without losing the previous collaboration pattern.

## Possible Conflicts

- `workflow/role-boundaries.md` may already define generic role boundaries. The suggested change should extend those boundaries without turning consultants into co-leads.
- `workflow/stages.md` already defines stage gates. The suggested change should reference those gates rather than duplicate or override them.
- Project-local role files may intentionally assign different agents or different review lenses. Upstream guidance should be template-like and overrideable.

## Security Or Privacy Risks

Low. The change is process guidance only. It should not require command execution, external links, repository writes beyond normal workflow files, or access to secrets.

To avoid privacy leakage, examples should stay generic and should not include private project implementation details beyond non-confidential summarized collaboration patterns.

## Generality

Broadly useful across multi-agent projects that use OpenSpec phases and collaboration files. The specific agent names in Rideroute can be generalized into review lenses: lead/integrator, fixed-reference/domain verifier, and architecture/breadth/simplification reviewer.

## Migration Or Compatibility Impact

Existing projects do not need to change immediately. New or updated projects could optionally add a `Role By OpenSpec Phase` section to local agent role files or create a small local phase-role note referenced from `project-facts.md`.

## Rollback Idea

If the guidance causes confusion or over-prescriptive role assignments, revert the added upstream section/template and leave projects to define phase roles only in local role files.

## Notes

Rideroute's local recommendation is to keep Codex as lead/integrator, Claude as fixed-reference/domain verification consultant, and Gemini as architecture/breadth/simplification consultant across all future OpenSpec cycles.
