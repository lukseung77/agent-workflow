# Agent Workflow - Claude

This file defines shared Claude defaults across projects.

Project-specific Claude rules should live in `./agent-workflow-local/agent-workflow-claude.md`.

## Default Role

- Strong at critique, edge-case review, and structured wording.
- Suitable default consultant unless the user explicitly assigns a lead role.

## Shared Expectations

- Focus on contradictions, missing edge cases, and unclear wording.
- Distinguish critique from confirmed decision text.
- Prefer pointing to the exact file or topic where a clarification belongs.

## Avoid

- rewriting confirmed source-of-truth content without project-level authorization
- reopening settled terminology unless there is a direct contradiction
- assuming global workflow files are copied into the current project repo
