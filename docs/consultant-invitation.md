# Consultant Invitation

Use the following invitation to start each consultant session. Assignments and
review lenses come only from Codex's collaboration requests; this invitation
provides orientation, not a consultation request.

## Invitation

You are invited to review the current `agent-workflow` refactor as a consultant.

- Repository: `/Volumes/Data/troy/Documents/_lukseung/__Projects/agent-workflow`
- Role: consultant, not master-agent or co-lead
- Assignment: review current rules and file structure for context efficiency,
  discoverability of required rules, consistency, and preservation of authority
- Lens: use the lens assigned in the addressed collaboration request
- Start with: `docs/consultant-orientation.md`
- Review target: the current working tree, including modified and untracked files
- Request channel: `docs/collaboration-codex.md`
- Deliverable: create or update only your own
  `docs/collaboration-[agent].md`, referencing the request ID

Codex is this project's master-agent and sole project-file maintainer. Other
agents may create and update only their own collaboration file to communicate
with Codex. They must not create or edit other files, commit, push, install
dependencies, or apply fixes. Receive consultation requests and deliver findings
through collaboration files only, not chat or invitation text. If no addressed
open request exists, wait after preparing your own collaboration file.
This invitation does not authorize an upstream suggestion submission.

## Collaboration Paths

All paths are relative to the repository above; its `docs/` directory already exists.

| Agent | Own writable file |
|-------|-------------------|
| Claude | `docs/collaboration-claude.md` |
| Gemini (including `agy`) | `docs/collaboration-gemini.md` |
| Codex (master-agent) | `docs/collaboration-codex.md` |

Other invited agents use `docs/collaboration-<agent>.md` with their own stable
lowercase kebab-case agent name. Never use another agent's identity. Follow the
creation and message instructions in `docs/consultant-orientation.md`.

### Lens A: Rule Consistency And Authority

Trace startup, task routing, role authority, phase changes, review completion,
and suggestion approval. Find conflicting rules, missing routes, ambiguous
ownership, and ways a consultant or downstream agent might mistakenly acquire
upstream write authority. Check templates against canonical rules.

### Lens B: Context Efficiency And Structure

Trace the minimum reading path for startup, project setup, consultant review,
phase transition, and upstream maintenance. Find unnecessary repetition,
avoidable context load, excessive procedural burden, broken references, and
rules that become difficult to discover after splitting files. Recommend the
smallest useful correction and describe its tradeoff.

Review independently before considering other consultants' conclusions.
Report concrete problems first; keep optional improvements separate. Do not
invent findings to meet a quota.
