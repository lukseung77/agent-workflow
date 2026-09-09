# Decision Protocol

Decisions are the hardest part of multi-agent collaboration to get right. Agents will disagree, surface conflicting rules, and generate many more questions than the user has time to answer. This protocol keeps the process fast and the user sane.

---

## Types of Decisions

### Agent-resolvable

Agents can resolve these without user input:

- Wording inconsistencies where the intent is clear from context
- Duplicate content where one source is obviously authoritative
- Stale language that no longer matches the domain model
- Minor structural cleanup (empty sections, misplaced content)

**Rule:** these do not require user input. The agent authorized to write the affected file fixes them directly and logs the change. A consultant without write authority records the issue for the lead instead of editing source-of-truth files.

### Lead-agent-resolvable

The lead agent can resolve these after reading all consultant input:

- Disagreements between consultant agents where one position is clearly better supported
- Gaps where the answer is implied by already-settled decisions
- Implementation patterns where the spec is clear enough to decide

**Rule:** the lead agent decides and logs the rationale. Consultant agents may challenge the decision with a `gap` item if they disagree.

### User-escalated

Only the user can resolve these:

- Scope inclusions and exclusions
- Product decisions with no clearly correct answer
- Conflicts between settled decisions (true contradictions)
- Risk acceptance (knowingly proceeding with a known ambiguity)

**Rule:** agents escalate these to the user. Do not assume. Do not resolve by picking the most convenient option.

---

## Decision Queue Protocol

Use `workflow/question-model.md` for queue consolidation, one-question-at-a-time flow, remaining-question estimates, and user-facing question format. Use this file for decision classification, conflicts, and failure handling.

---

## Failures And Retries

Before retrying, distinguish task defects, environment/authentication/permission
failures, transient errors, malformed results, and product/scope decisions.
Resolve setup issues within existing authority when possible; do not modify
product behavior to disguise an environment failure or bypass denied access.
Escalate to the lead or human only when authority, access, or a decision is
missing. Continue independent work that is not blocked.

Bound repeated attempts at the same failure by task-appropriate time/attempt
limits and progress. Do not repeat an unchanged failing approach indefinitely.
When progress stops, summarize evidence and attempts, change the approach, or
report the blocker to the appropriate decision owner. There is no universal
two-cycle ceiling and no requirement to ask the user while useful authorized
progress continues. Missing or malformed results are not successful completion.

## Conflict Resolution

### Direct conflict

Two rules that cannot both be true. Example: "field X is required" and "entity Y may exist without field X."

Resolution order:
1. Check if one source is more recent — the newer decision usually supersedes
2. Check if one source is more authoritative (spec > exploration > collaboration note)
3. If still unclear, escalate to the user as a user-escalated decision

### Indirect conflict

Two rules that produce divergent implementation without technically contradicting each other. Example: "screen A shows the active plan" and "imminent maintenance takes precedence on the dashboard" — if not qualified, an implementation could read these as conflicting.

Resolution order:
1. Add a qualifying phrase to the less authoritative statement
2. Add a cross-reference so both rules point to the same source of truth
3. If the ambiguity could produce meaningfully different implementations, escalate to the user

### Wording drift

The same rule stated differently in two places. One will be taken as authoritative; the other as a correction.

Resolution:
1. Pick one canonical location (usually the more detailed file)
2. Replace the duplicate with a one-line reference to the canonical location
3. Log the change as a `status` item

---

## Recording Decisions

Every user decision must be recorded:

- In the collaboration file of the agent who asked, under the item that triggered it
- With the exact decision (not a paraphrase)
- With the date
- With any clarifications the user added

After recording, the lead agent writes the decision into the source-of-truth files. The collaboration entry then becomes `done` and remains parseable until `scripts/collab_archive.py` archives it; do not comment it out.

**Do not let decisions float.** A decision that is not written into a source-of-truth file within the same session is likely to be lost or relitigated.

---

## Preventing Decision Fatigue

Use `workflow/question-model.md` for user-question guardrails. The decision-specific rule is: resolve agent-resolvable and lead-agent-resolvable items before escalating anything to the user.
