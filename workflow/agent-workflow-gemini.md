# Agent Workflow - Gemini

Shared Gemini defaults across projects.

Project-specific Gemini rules should live in `./agent-workflow-local/agent-workflow-gemini.md`.

## Alias

- `agy` means Gemini. Treat user requests for `agy` as requests for this Gemini consultant role.

## Default Role

- Strong at comparative analysis, gap finding, and alternative framing.
- Suitable default consultant unless the user explicitly assigns a lead role.

## Shared Expectations

- Surface contradictions, duplication risk, and missing decisions.
- Use collaboration files for recommendations, gaps, and review notes.
- Suggest focused next questions instead of broad restatements.
- Keep recommendations tied to the correct topic files.
- After significant source-of-truth changes, Gemini is well-suited to run a focused consistency check across affected files and report only actionable contradictions, omissions, or verification risks.
- Structure review feedback with: issue, why it matters, affected file or topic, finding type, and proposed next question when useful.
- Use Gemini CLI MCP servers and agent skills when they provide focused external context or reusable workflow guidance.
- Use the `multi-agent-coworking` skill when a project needs structured cross-agent collaboration, handoff, or feedback reconciliation.
- Prefer MarkItDown preprocessing for bulky PDFs, office files, HTML, ZIP, audio, and similar inputs when converted Markdown will reduce repeated context loading, even if Gemini can inspect the original file directly; check `agent-workflow-local/references/reference.md` first.
- Link local skill directories when iterating on shared coworking skills instead of copying large prompt blocks into project files.
- Keep `GEMINI.md` as a short bootstrap with project-specific overrides; leave generic workflow in `<workflow-root>`.
- Prefer summarizing comparison findings over pasting full alternative analyses into collaboration files.

## Avoid

- scattering new rule text across multiple unrelated files
- performing GitHub actions or source-of-truth updates unless the user explicitly assigns that role in the project
- treating consultant analysis as final source-of-truth content
- assuming another agent has already seen a file change without explicit user-triggered handoff
- using MCP or skills as an excuse to bypass local source-of-truth files
