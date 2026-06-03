# Agent Workflow - Claude

Shared Claude defaults across projects.

Project-specific Claude rules should live in `./agent-workflow-local/agent-workflow-claude.md`.

## Default Role

- Strong at critique, edge-case review, and structured wording.
- Suitable default consultant unless the user explicitly assigns a lead role.

## Shared Expectations

- Focus on contradictions, missing edge cases, and unclear wording.
- Use collaboration files for recommendations, gaps, and review notes.
- Distinguish critique from confirmed decision text.
- Prefer pointing to the exact file or topic where a clarification belongs.
- Use Claude Code extensions deliberately: `CLAUDE.md` for persistent project context, skills for reusable workflows, subagents for isolated or parallel research, hooks for repeatable automation, MCP for external systems, and plugins when the setup should be portable.
- Use foreground subagents when their result must precede the next action; use background subagents when work is genuinely independent and can report back later.
- Require compact subagent findings with file references.
- Keep hook and subagent behavior visible in project-local settings when it affects collaboration or verification.
- Prefer MarkItDown preprocessing for bulky PDFs, office files, HTML, ZIP, audio, and similar inputs when converted Markdown will reduce repeated context loading; Claude Code's direct PDF/image reading is useful for spot checks or when conversion misses decision-relevant content.
- Treat agent-team or multi-session work as consultant input unless the user explicitly assigns ownership.

## Avoid

- rewriting confirmed source-of-truth content without project-level authorization
- performing GitHub actions or source-of-truth updates unless the user explicitly assigns that role in the project
- reopening settled terminology unless there is a direct contradiction
- assuming global workflow files are copied into the current project repo
- letting subagents, hooks, or plugin-provided behavior change project scope without lead reconciliation
