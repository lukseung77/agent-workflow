# Suggestion Addendum: Keep Agent Skill Dependencies Optional And Local

## Suggestion

- `submitted_at`: 2026-09-08T19:40:00+09:00
- `from-project`: rideroute
- `from-agent`: codex
- `workflow-version`: 80477dd
- `status`: proposed

## Observed Problem

The earlier Rideroute skill-capability suggestions correctly recommend phase-specific capabilities, but two later consultant clarifications show a remaining wording risk:

- a repeatable project workflow can be mistaken for a concrete installed skill package
- optional agent-local skill specifications can be mistaken for required third-party dependencies

That distinction matters because `agent-workflow` should stay portable across Codex, Claude, AGY, and future agent runtimes.

## Evidence

- `CL-033` recommended Claude's Implementation-phase `run` capability for browser verification.
- Claude later clarified that Rideroute currently has no project-specific `run` skill and no separate browser CLI dependency. The working flow is to start `npm run dev` from the project directory, then run Playwright Chromium verification from the same project directory so `@playwright/test` resolves from project `node_modules`.
- `GM-034` proposed concrete optional `.agents/skills/` package shapes for AGY: `agy-exploration-audit`, `agy-proposal-evaluator`, and `agy-implementation-profiler`.
- `GM-035` then clarified that AGY requires no third-party or external skills because Antigravity already provides terminal execution, search/edit tools, Playwright browser test drivers, subagents, and built-in system guidance. The `.agents/skills/` files are optional workflow-sharing/configuration artifacts.
- `workflow/master-governance.md` says submitted suggestions are append-only from a user-agent perspective, so this addendum supplements `2026-09-08-1828-rideroute-openspec-phase-skills-002.md` and `2026-09-08-1831-rideroute-openspec-phase-skills-addendum-003.md` instead of editing the already-submitted upstream files.

## Suggested Change

When upstream incorporates OpenSpec phase skill guidance, add one explicit rule:

> Phase skill guidance should describe required review capabilities first. Concrete installed skills, local workflows, and optional skill packages are examples only unless a project-local file marks them required. Agents should not install third-party skills or assume external dependencies merely because a capability is listed.

Add a companion local-workflow rule:

> If a capability is implemented as a project-local workflow rather than a named installed skill, record the exact repeatable procedure in project-local files. For browser verification, that may mean starting the local dev server and running Playwright/browser checks from the project directory.

Add an optional packaged-skill rule:

> Project-local `.agents/skills/` packages may be used to share repeatable review workflows across agents, but they are optional unless the human user or project-local governance explicitly requires them.

## Expected Before/After Improvement

Before: agents may treat capability labels like `run`, `browser-e2e-verifier`, or AGY audit packages as mandatory installed dependencies, which can cause unnecessary setup work or role confusion.

After: upstream guidance remains capability-first and portable. Each project can map capabilities to its available tools, local scripts, or optional skill packages without implying a universal dependency.

## Possible Conflicts

- Some teams may want strict installed-skill names for reproducibility. This addendum does not prevent that; it only says such requirements should be declared project-locally instead of assumed globally.
- Existing submitted suggestions use concrete examples. This addendum narrows their interpretation rather than replacing them.

## Security Or Privacy Risks

Low. The addendum reduces risk by discouraging unnecessary third-party skill installation and by keeping browser/app workflows explicit and local.

Mitigation: preserve the existing report-only rule for consultant use of workflows or skills that can write files, mutate source, execute privileged commands, or take external actions.

## Generality

Broadly useful for multi-agent OpenSpec projects because agent runtimes differ. Capability-first wording lets the same workflow support Codex, Claude, AGY, and future tools.

## Migration Or Compatibility Impact

No required migration. Existing projects can keep using their current local workflows or skill packages. New projects should document exact local workflow mappings only when needed.

## Rollback Idea

If this clarification makes the workflow too abstract, remove it and keep skill mapping entirely project-local.

## Notes

This addendum supplements:

- `2026-09-08-1828-rideroute-openspec-phase-skills-002.md`
- `2026-09-08-1831-rideroute-openspec-phase-skills-addendum-003.md`
