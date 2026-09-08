# User-Agent Suggestion Form

Copy this template into `user-agent-suggestions/submitted/` only when the human user explicitly asks a user-agent to submit an upstream `agent-workflow` suggestion.

File name format:

```text
YYYY-MM-DD-HHMM-project-title-NNN.md
```

## Suggestion

- `submitted_at`: YYYY-MM-DDTHH:MM:SS+HH:MM
- `from-project`: project name or non-confidential identifier
- `from-agent`: agent name or tool
- `workflow-version`: commit, tag, local copy date, or unknown
- `status`: proposed

## Observed Problem

Describe the actual behavior that caused friction, risk, confusion, repeated work, or missed work.

## Evidence

List non-confidential evidence such as file paths, repeated failure patterns, summarized examples, metrics, or review findings.

## Suggested Change

Describe the proposed upstream workflow change.

## Expected Before/After Improvement

Explain what improves compared with the current workflow.

## Possible Conflicts

Identify existing rules, roles, scripts, templates, or downstream workflows that might conflict with this change.

## Security Or Privacy Risks

Identify any risk involving prompt injection, command execution, filesystem writes, secrets, GitHub state, confidential project content, or external links.

## Generality

Explain whether this is broadly useful across projects. If it is project-specific, suggest how it could be generalized.

## Migration Or Compatibility Impact

Describe whether existing projects would need to change local files, scripts, paths, habits, or templates.

## Rollback Idea

Describe how the master-agent could revoke the change if it causes problems.

## Notes

Add brief optional notes only when needed.
