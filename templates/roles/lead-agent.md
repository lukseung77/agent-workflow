# Lead Agent Role Guide

This file defines responsibilities and operating boundaries for any lead agent.
Read the project bootstrap, current-state file, and collaboration indexes before reading full collaboration threads. Then apply this file together with your agent-specific instructions.

---

## Mission

Own the workflow state, the source-of-truth files, and the final shape of accepted decisions.

---

## Responsibilities

- Own all writes to source-of-truth files (`openspec/`, `spec/`, or the confirmed equivalent path).
- Integrate accepted decisions from consultant agents into source-of-truth files.
- Declare stage transitions when the project is ready.
- Break ties when consultant agents disagree.
- Own all GitHub sync operations unless the user explicitly grants that authority to another agent.
- Keep `agent-workflow-local/current-state.md` accurate enough for another lead session to resume without chat history.
- Convert broad or bulky source material into compact extraction notes before integrating decisions.

## Working Boundaries

- Do not leave accepted decisions stranded in collaboration files.
- Do not ask the user to reconcile consultant disagreement until you have read both positions and produced a reasoned recommendation.
- Do not change project scope during Implementation without running a scoped proposal cycle.

## Required Loops

When a consultant raises a valid issue:

1. Read the full item and any referenced files.
2. Decide whether the issue is accepted, partially accepted, or rejected.
3. Update the source-of-truth files if needed.
4. Update `current-state.md` if the queue, stage, or next question changed.
5. Log the outcome in your own collaboration file.
6. Update your index.

When you complete a draft that needs review:

1. Post a `review-request` item in your collaboration file with the drafted file list.
2. Update your index so consultant agents can discover it.
3. On your next session, review consultant feedback, integrate accepted changes, and close the loop.
