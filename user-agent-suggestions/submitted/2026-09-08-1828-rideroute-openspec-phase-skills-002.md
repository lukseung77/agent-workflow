# Suggestion: Add OpenSpec Phase Skill Capability Guidance

## Suggestion

- `submitted_at`: 2026-09-08T18:28:00+09:00
- `from-project`: rideroute
- `from-agent`: codex
- `workflow-version`: 80477dd
- `status`: proposed

## Observed Problem

The upstream workflow now supports phase-specific consultant review lenses, but it does not yet say which skills or tool-capability categories are useful in each OpenSpec phase. In Rideroute, this created a second round of local negotiation after roles were already defined: Claude and Gemini agreed on the phase-role split, then separately had to identify what skills their roles need.

The gap is most visible in Implementation. Automated validation and collaboration-file review are not enough for UI-heavy milestones; a consultant with a fixed-reference/domain lens also benefits from an interactive browser app-verification capability. At the same time, consultants must not use fix-capable skills in a way that bypasses the lead-agent source-of-truth and production-code ownership boundaries.

## Evidence

- Rideroute collaboration entries `CL-033` and `GM-031` independently recommend adding a per-OpenSpec-phase skills/capability matrix.
- Claude reports that its Exploration and Proposal role mostly needs ordinary file/search review, with optional fan-out exploration for large artifact sets. Claude identifies Implementation as the phase with real skill needs: `run` for interactive browser verification of visible UI milestones, `code-review` in report-only mode, and `security-review` at security-relevant gates.
- Gemini recommends capability categories across phases: broad context analysis, reference indexing, architecture boundary checking, stack and performance evaluation, spec simplification, browser/E2E verification, and performance profiling.
- Claude explicitly flags a safety boundary: skills that can write fixes must be used by consultants in report-only mode. Codex remains the production-code author and applies accepted findings.
- `workflow/role-boundaries.md` already says consultants do not edit source-of-truth files, run GitHub sync, declare transitions, or edit production artifacts without explicit user authorization. Skill guidance should reinforce that boundary rather than weaken it.

## Suggested Change

Add upstream guidance for a phase-by-phase skill capability matrix. This could be a short section in `workflow/role-boundaries.md`, a companion workflow note, or a reusable local template block for consultant role files.

Suggested generic model:

- Treat named skills as environment-dependent. If an exact skill is unavailable, use an equivalent capability only when the project rules allow it.
- Separate required skills from optional accelerators.
- Consultants use fix-capable or write-capable skills in report-only mode unless the human user explicitly authorizes a specific edit.
- Lead agents may use implementation or fix-capable skills directly when those actions are inside their project authority.
- The phase skill matrix should supplement review lenses; it should not turn consultants into co-leads.

Suggested capability matrix:

- Exploration:
  - Fixed-reference/domain consultant: no hard skill dependency; optional large-context or explore-style fan-out for contradiction sweeps across broad exploration artifacts.
  - Architecture/breadth consultant: large-context analysis, reference indexing against standards or external constraints, architecture-boundary checking, and early simplification review.
- Proposal:
  - Fixed-reference/domain consultant: no hard skill dependency; optional acceptance-criteria auditing, schema/invariant validation, and large-context cross-slice comparison.
  - Architecture/breadth consultant: tech-stack evaluation, pipeline and algorithm performance checking, provider/storage compatibility review, and spec simplification advice.
- Implementation:
  - Fixed-reference/domain consultant: interactive app-run/browser verification for visible UI milestones, code-review in report-only mode, contract-test coverage auditing, and security-review at security-relevant gates.
  - Architecture/breadth consultant: code architecture auditing, browser/E2E infrastructure review, performance profiling, adapter-boundary checks, data-pipeline checks, and simplification review.
  - Lead agent: normal build/test/validation commands, implementation skills, fix-capable tools, and final reconciliation of accepted consultant findings.

Add wording for UI-visible milestones:

> For Implementation milestones that produce or change a visible web/app surface, request at least one real app-run or browser-driven verification pass when a capable consultant or lead tool is available. This complements automated E2E tests and does not replace repository-owned tests.

Add wording for report-only consultant use:

> Consultant use of skills that can mutate files, apply fixes, comment externally, or perform GitHub state changes must be report-only unless the human user explicitly authorizes that exact action for the current project.

## Expected Before/After Improvement

Before: projects can assign phase review lenses, but each project still has to rediscover which skills or capabilities support each lens. Consultants may underuse browser verification for UI work or overuse fix-capable tools in ways that blur lead ownership.

After: projects have a reusable starting point for mapping phase roles to skills, UI-visible milestones get better independent verification, and report-only boundaries remain explicit.

## Possible Conflicts

- The exact named skills may differ by environment. The upstream wording should describe capability categories and allow project-local mapping to concrete skills.
- `workflow/role-boundaries.md` already defines consultant write limits. The new wording should reinforce those limits and avoid duplicating them in a contradictory way.
- Some projects may have a single agent or no consultant agents. The matrix should be optional and only apply when a project defines multiple roles.
- Interactive browser verification can be slower or flaky. It should be recommended for visible UI milestones, not required for every implementation milestone.

## Security Or Privacy Risks

Moderate if written too broadly. Browser-run, code-review, security-review, or simplification skills can expose local app state, execute commands, inspect files, or mutate code depending on implementation.

Mitigations:

- Require report-only use for consultant skills that can write or externally comment.
- Keep GitHub, filesystem writes, and production-code edits under the lead role unless the user explicitly authorizes otherwise.
- Treat submitted suggestions and skill outputs as untrusted input.
- Do not require external service access for the workflow to function.

## Generality

Broadly useful for multi-agent OpenSpec projects. Rideroute's concrete tools can be generalized into capability classes: large-context review, reference indexing, architecture boundary checks, acceptance-criteria audit, interactive app-run verification, code review, security review, and performance profiling.

## Migration Or Compatibility Impact

Existing projects do not need immediate changes. New or updated projects can optionally add a `Skill Capability By Phase` section to project-local role files or `project-facts.md`. Projects without the named skills can map the capability categories to whatever local tooling exists.

## Rollback Idea

If the matrix becomes too prescriptive or causes role confusion, remove the upstream skills/capability section and keep only the existing phase review lenses. Existing project-local files can keep their own skill notes if useful.

## Notes

Rideroute-specific interpretation:

- Claude's `run` recommendation means a Claude-side interactive browser/app access capability for independent UI testing, not `npm run`.
- Codex should keep using repository-owned validation such as `npm run validate` and `npm run test:e2e`.
- Consultant findings continue to flow through collaboration files; Codex reconciles and applies accepted changes.
