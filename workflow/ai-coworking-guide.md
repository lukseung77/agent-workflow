# AI Coworking Guide

This guide is a reusable working agreement for projects where multiple AI agents help the same user define, review, and implement a product.

It is intentionally generic. Project-specific details should live in the project's collaboration file, not here.

## Core Principle

One agent should lead each phase.

Other agents may review, critique, suggest alternatives, and identify missed questions, but they should not independently redirect the project unless the user explicitly changes ownership.

## Roles

### Exploration Lead

The exploration lead owns:

- synthesizing user decisions
- choosing the next focused question
- keeping the requirement record coherent
- reconciling conflicting consultant feedback
- deciding where confirmed requirements belong in the project documents

### Consultant Agents

Consultant agents should:

- review for inconsistencies
- identify missed edge cases
- suggest better wording or file structure
- propose focused follow-up questions
- explain why each suggestion matters

Consultant agents should not:

- rewrite confirmed decisions directly without coordination
- reopen settled terminology unless there is a direct contradiction
- scatter new requirement notes in unrelated files
- perform repository sync or GitHub actions unless explicitly assigned

### Implementation Lead

The implementation lead owns:

- final code integration
- test execution and verification
- merging consultant or worker outputs
- avoiding conflicting edits

This may be the same agent as the exploration lead, or a different agent if the user explicitly assigns the role.

## Question-At-A-Time Policy

When requirements are still emerging, ask one focused question at a time.

Each question should:

- target one decision
- avoid mixing multiple unrelated choices
- include only enough context for the user to answer confidently
- avoid reopening already-settled decisions
- be recorded back into the project documents after the user answers

If there are many possible questions, keep a pending-question list and ask the highest-value one next.

For long-running exploration, it is useful to include a rough remaining-question estimate in parentheses, for example:

- `Should this appear on Dashboard or only in detail view? (roughly 3 questions left)`

## Source Of Truth

Use durable project files as the source of truth, not chat history.

Recommended structure:

- `openspec/explorations/`
  Active discovery and requirement exploration
- `openspec/changes/`
  Formal proposals after exploration has converged
- `docs/collaboration.md`
  Project-specific agent coordination and handoff rules
- GitHub issues
  Track work items, investigation threads, and proposal tasks when the project is ready
- Pull requests
  Review and preserve meaningful documentation or implementation changes

## Exploration Workflow

1. Read the project collaboration file.
2. Read the top-level exploration synthesis.
3. Read only the focused exploration files relevant to the next question.
4. Summarize the minimum current context.
5. Ask one focused question.
6. Record the user's answer into the relevant exploration file.
7. If consultant feedback exists, reconcile it explicitly:
   - adopted
   - partially adopted
   - not adopted
   - reason
8. Keep a pending-question list for later questions.

## Consultant Feedback Workflow

Consultant agents should leave feedback in a predictable place.

Good consultant feedback should include:

- the specific issue
- why it matters
- which file or topic it belongs to
- whether it is a contradiction, missing detail, wording issue, or future-facing suggestion
- a proposed next question, if useful

The lead agent should then add a short reconciliation note:

- `Adopted: ...`
- `Partially adopted: ...`
- `Not adopted: ...`

The note should explain why. This helps future consultant agents avoid repeating already-reviewed feedback.

## GitHub And Sync Policy

Use GitHub as the shared persistence layer when the project is ready for it.

Recommended policy:

- keep exploration decisions in repository files
- use GitHub issues for tracked open work
- use pull requests for significant changes
- avoid multiple agents pushing or syncing at the same time unless explicitly coordinated
- designate one agent as final integrator for GitHub sync during exploration

## Restart / Handoff Policy

After a context reset or when a new agent joins:

1. Read the project collaboration file.
2. Read the top-level exploration synthesis.
3. Read the focused files related to the next pending question.
4. Do not ask the user to restate the whole project.
5. Summarize only the minimum useful context.
6. Continue from the latest unresolved question.

If the next question is unclear, infer it from the pending-question list and the latest confirmed exploration files.

## Trigger Model

Shared files support handoff and reduce repeated context-setting, but they do not automatically trigger other agents across different tools, platforms, or terminals.

The practical trigger is still the user explicitly starting the next agent session or sending that agent a short instruction to re-read the updated files.

A good minimal trigger message is:

- `Files updated. Re-read docs/collaboration.md and continue from the next unresolved question.`

Agents should not assume another agent has seen a file update unless the user has explicitly triggered that follow-up session.

## Generic File Placement Guidance

Use focused files to reduce drift.

Examples:

- domain model and terminology in a domain-focused file
- screen behavior in a navigation or screen-focused file
- import or export behavior in a sharing or portability file
- notification behavior in a dashboard or notification file
- mapping behavior in a mapping file
- maintenance or history behavior in a maintenance/history file

Avoid putting every decision into one monolithic product-scope document. The top-level scope file should be an index and synthesis, not the only source of detail.
