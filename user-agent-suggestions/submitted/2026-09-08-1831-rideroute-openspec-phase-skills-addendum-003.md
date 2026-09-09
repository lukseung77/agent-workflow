# Suggestion Addendum: Distinguish Concrete Skills From Capability Labels

## Suggestion

- `submitted_at`: 2026-09-08T18:31:00+09:00
- `from-project`: rideroute
- `from-agent`: codex
- `workflow-version`: 80477dd
- `status`: proposed

## Observed Problem

The previously submitted Rideroute suggestion on OpenSpec phase skill capabilities can be misread if concrete agent skills, project-local test workflows, and generic capability labels are mixed together. Gemini added a clarification after submission that should be considered when the upstream master-agent evaluates the suggestion.

The problem is not that every capability label must become a concrete skill. The problem is that workflow guidance should tell projects how to separate:

- concrete built-in skills available to a specific agent environment
- project-local or environment-specific test workflows
- generic capability descriptions that can be mapped to different tools per project

## Evidence

- `GM-032` explicitly distinguishes three tiers:
  - concrete built-in system skills currently active for Gemini/AGY, such as `antigravity-guide` and `agy-customizations`
  - concrete environment testing skill/workflow, especially Claude's `run` for local browser app verification
  - functional capability descriptions for OpenSpec phases, such as `context-analysis`, `reference-indexer`, `tech-stack-evaluator`, `acceptance-criteria-auditor`, `code-architecture-auditor`, `performance-profiler`, and `browser-e2e-verifier`
- `CL-033` similarly warns against padding Exploration and Proposal with fake hard dependencies for Claude's fixed-reference role.
- Rideroute's submitted suggestion `2026-09-08-1828-rideroute-openspec-phase-skills-002.md` already recommends treating named skills as environment-dependent, but it does not explicitly name the three-tier classification from `GM-032`.

## Suggested Change

When incorporating the OpenSpec phase skill capability suggestion, include a small classification rule:

1. **Concrete system skills** are named skills available in a specific agent/runtime environment. Workflow templates may show them as examples, but upstream rules should not assume all projects have them.
2. **Project-local workflows** are repeatable project procedures or custom skills, such as a local app-run/browser verification workflow. They should be recorded in project-local files and used when available.
3. **Functional capability labels** describe the kind of review or testing needed, independent of implementation. Upstream workflow guidance should prefer these generic labels, then let local projects map them to concrete skills.

Suggested wording:

> Phase skill guidance should distinguish concrete installed skills from generic capability labels. Upstream templates may recommend capabilities such as large-context analysis, acceptance-criteria auditing, interactive app-run verification, security review, performance profiling, or architecture-boundary checks. Project-local role files should map those capabilities to the actual skills, commands, or manual workflows available in that environment.

For UI-visible Implementation milestones, keep the previously submitted recommendation:

> Use a real app-run or browser-driven verification pass when available, especially for consultant review of visual and interaction behavior. This complements, but does not replace, repository-owned automated tests.

## Expected Before/After Improvement

Before: skill guidance risks becoming brittle by naming tools that only exist in one agent environment, or vague by listing capability labels as if they were real executable skills.

After: upstream guidance stays portable while still letting local projects capture concrete skills like Claude's `run` or Gemini/AGY-specific documentation/customization skills.

## Possible Conflicts

- If upstream wants only concrete installed skills in skill guidance, this addendum argues for a more portable capability-first model.
- If upstream wants no skill guidance at all, this addendum is unnecessary and can be denied together with the prior suggestion.
- Project-local files may still choose exact skills. The upstream guidance should not prevent that.

## Security Or Privacy Risks

Low to moderate. The classification itself is process guidance, but it helps avoid unsafe assumptions around skills that can run apps, inspect browser state, execute commands, or write files.

Mitigation: preserve the existing consultant report-only rule for any skill or workflow that can mutate files, apply fixes, comment externally, perform GitHub actions, or execute privileged commands.

## Generality

Broadly useful anywhere `agent-workflow` is used across different agent runtimes. The exact skill names will change, but the concrete-skill / project-workflow / functional-capability distinction remains applicable.

## Migration Or Compatibility Impact

No required migration. Existing projects can keep local skill notes as-is. New projects can use the classification when filling role templates.

## Rollback Idea

Remove the classification wording if it causes confusion and return to simple project-local skill naming.

## Notes

This addendum supplements `2026-09-08-1828-rideroute-openspec-phase-skills-002.md`; it does not replace it.
