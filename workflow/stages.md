# Workflow Stages

The workflow has three stages. Each stage has a clear goal, a set of activities, and explicit gate criteria that must be met before moving forward. Agents must concur before a stage transition happens; the user confirms.

---

## Stage 1: Exploration

**Goal:** establish shared understanding of the problem space, domain model, and constraints before writing any spec.

### Activities

- Agents read all available materials (briefs, prior docs, existing code)
- Each agent logs findings, gaps, and questions in its collaboration file
- The lead agent or a designated consolidator gathers all open questions and presents them to the user one at a time
- User answers are recorded and propagated into source-of-truth files by the lead agent
- Agents do independent cleanup passes once the main questions are resolved

### What belongs here

- Domain term definitions
- Core model decisions (entities, relationships, lifecycle states)
- Scope inclusions and exclusions
- Open risk items and carry-forward guardrails

### What does not belong here

- Implementation patterns (how to code it)
- Exact API shapes or database schemas
- UI component choices

### Gate criteria

All of the following must be true before moving to Proposal:

- [ ] No direct conflicts between exploration files
- [ ] All core domain terms defined and agreed by all agents
- [ ] All blocking user questions answered
- [ ] All agents have independently reviewed and concurred readiness
- [ ] Carry-forward risks documented explicitly (these travel into Proposal as guardrails)

### Carry-forward risks

Before closing Exploration, the lead agent should publish a named list of known risks that every future proposal must treat as explicit guardrails or exclusions. These risks do not need to be resolved at this stage — they need to be visible.

---

## Stage 2: Proposal

**Goal:** write a structured, scoped proposal from the settled exploration. One proposal covers one coherent slice of the product.

### Activities

- Lead agent drafts the proposal into spec files
- Consultant agents review the draft and log feedback in their collaboration files
- Lead agent integrates accepted feedback
- User approves or adjusts the proposal scope
- Proposal is merged into the accepted spec

### What belongs here

- Formal feature descriptions
- Screen-level UX decisions
- Data model field lists
- Acceptance criteria
- Explicit out-of-scope exclusions

### What does not belong here

- Implementation code or pseudocode
- Speculative scope ("we might later want…")
- Decisions that were not settled in Exploration

### Gate criteria

All of the following must be true before moving to Implementation:

- [ ] Proposal covers only scope settled in Exploration
- [ ] No open conflicts between proposal and exploration files
- [ ] All consultant agents have reviewed the draft
- [ ] User has explicitly accepted the proposal
- [ ] Out-of-scope items are listed explicitly in the proposal

---

## Stage 3: Implementation

**Goal:** build from the accepted proposal. Source of truth is the spec, not exploration files or collaboration notes.

### Activities

- Agents build from spec files
- Any scope change triggers a mini-proposal cycle (not a unilateral spec edit)
- Collaboration files track blockers and implementation status
- Discovery of spec ambiguity → open a gap item → lead agent resolves → spec updated

### Rules

- Do not change the spec unilaterally during implementation
- Do not read exploration files as authoritative — they may contain superseded content
- Any blocker that cannot be resolved within the implementation team escalates to the user

### Gate criteria (per feature)

- [ ] Spec is implemented as written
- [ ] Any spec deviations are documented and approved
- [ ] Tests cover the acceptance criteria from the proposal

---

## Stage Transition Protocol

1. The agent closest to the work (usually the lead) assesses gate criteria
2. That agent posts a `status` item in its collaboration file naming the gate outcome
3. All other agents review and reply with concurrence or remaining blockers
4. User confirms the transition
5. Lead agent updates the project status in source-of-truth files

Transitions should never be silent. If a stage transition happens without explicit agent concurrence and user confirmation, the project carries hidden ambiguity into the next stage.
