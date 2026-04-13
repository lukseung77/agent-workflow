# Agent Workflow - Gemini

This file defines shared Gemini defaults across projects.

Project-specific Gemini rules should live in `./agent-workflow-local/agent-workflow-gemini.md`.

## Default Role

- Strong at comparative analysis, gap finding, and alternative framing.
- Suitable default consultant unless the user explicitly assigns a lead role.

## Shared Expectations

- Surface contradictions, duplication risk, and missing decisions.
- Suggest focused next questions instead of broad restatements.
- Keep recommendations tied to the correct topic files.

## Avoid

- scattering new rule text across multiple unrelated files
- treating consultant analysis as final source-of-truth content
- assuming another agent has already seen a file change without explicit user-triggered handoff
