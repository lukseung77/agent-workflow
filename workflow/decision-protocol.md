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

**Rule:** agents fix these directly. They log what they did in their collaboration file as a `status` item. They do not ask the user.

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

When multiple open user questions accumulate (e.g., end of Exploration stage), use this protocol:

1. One agent (usually the consolidator for that session) gathers all open questions from all collaboration files
2. Deduplicate — many questions from different agents are the same question in different words
3. Classify each remaining question: agent-resolvable, lead-resolvable, or user-escalated
4. Resolve agent-resolvable and lead-resolvable items first, without involving the user
5. For user-escalated items: order them by impact (highest-blocking first)
6. Ask the user **one question at a time**, waiting for a response before asking the next
7. Record each answer in the collaboration file immediately, with the exact wording of the decision
8. After all questions are answered, the lead agent updates source-of-truth files

### Question format (for user questions)

Keep it short. State:
- What the question is about (one sentence)
- The options (A, B, or a short list)
- Which option the agent recommends and why (optional, one sentence)

Do not dump context. Do not include all the background reasoning. If the user wants more context, they will ask.

---

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

After recording, the lead agent writes the decision into the source-of-truth files. The collaboration entry then becomes `done` and is commented out.

**Do not let decisions float.** A decision that is not written into a source-of-truth file within the same session is likely to be lost or relitigated.

---

## Preventing Decision Fatigue

- Never ask the user more than one question per message
- Never ask about something agents can resolve themselves
- Never re-ask a question that has already been answered (check collaboration files first)
- Never ask for implementation preferences during Exploration (defer to Proposal/Implementation stage)
- Batch related cleanup into one agent action, not one question per line
