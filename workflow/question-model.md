# Question Model

Use this file for user-facing question flow, especially during Exploration and stage gates.

## Core Rules

- Ask one focused question at a time while requirements are still emerging.
- Ask only what is needed for the next real decision.
- In a structured interview, optionally give a remaining-question estimate when it helps the user; label uncertain counts as estimates.
- Keep a pending-question list for later instead of batching questions at the user.
- Record confirmed answers back into project files promptly.

## Decision Queue

When multiple open user questions accumulate:

1. Generate or scan active recipient queues, then check collaboration files for any unpromoted open questions.
2. Deduplicate repeated questions.
3. Classify each remaining question using `workflow/decision-protocol.md`.
4. Resolve agent-resolvable and lead-resolvable items before involving the user.
5. Order user-escalated questions by impact, highest-blocking first.
6. Ask the user one question at a time and wait for a response before asking the next.
7. Record each answer immediately in the collaboration file of the agent who asked.
8. Have the lead agent update source-of-truth files.

## User Question Format

Keep user questions short:

- one sentence for the question
- options only when options are already clear
- one-sentence recommendation when useful
- a remaining-question estimate only when useful for a structured interview

Do not dump background context. If the user wants more context, they will ask.

## Decision Fatigue Guardrails

For an assumption-challenging interview (for example, a "grill-me" style review),
start with the highest-impact unresolved decision: desired outcome, compatibility,
scope, evidence, or failure behavior. Inspect project files first, state a concrete
recommendation, ask one focused question, and record the answer before branching
to a dependent question. Resolve technical choices from evidence where possible.
Ask questions whose answers could materially change the decision, and identify
what observation or test would disconfirm an important assumption. Avoid fixed
question quotas and do not pause independent work merely to complete an interview.
Distinguish human-confirmed answers from lead assumptions and continue independent
authorized work while a question is pending. An unanswered optional question is
not approval for a scope expansion.

- Do not ask about something agents can resolve themselves.
- Do not re-ask a question that has already been answered; check collaboration and source-of-truth files first.
- Do not ask for implementation preferences during Exploration; defer those to Proposal or Implementation.
- Batch related cleanup into one agent action, not one question per line.
