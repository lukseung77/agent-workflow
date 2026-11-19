# External Automation Controller

Status: Proposed improvement

This is proposal material, not an active workflow or installation instruction.
Canonical activation and authority rules remain in `workflow/`. The sibling
`automation-controller.md` preserves the same original controller proposal.

This document proposes an optional automation layer for projects that use
multiple CLI coding agents. It extends the existing file-based collaboration
workflow without replacing its single-lead model, source-of-truth rules, or
human decision authority.

The reference setup assumes:

- Codex is the implementation lead and only code/source-of-truth writer.
- Claude Code and Antigravity CLI (`agy`) are independent reviewers.
- OpenSpec supplies artifact and implementation instructions.
- Git commits identify the exact content reviewed by every agent.

## Problem

The current workflow deliberately uses files to carry context between agents.
This provides traceability, but files do not start processes. The user must
currently:

1. start the lead agent;
2. start each consultant after a review request appears;
3. start the lead again to consolidate the reviews; and
4. decide whether the next workflow action should begin.

Directly asking one model to invoke another model is not a reliable replacement.
It makes scheduling, retries, timeouts, permissions, result validation, and
failure recovery depend on model behavior.

## Decision

Use a small deterministic external controller as the trigger and gatekeeper.
The recommended reference implementation is a local Python CLI named `awctl`,
using:

- `asyncio` for subprocess supervision and parallel reviews;
- SQLite for transactional run state;
- JSON Schema for agent result contracts;
- Git worktrees or immutable snapshots for isolation; and
- OpenSpec and ordinary test commands for deterministic gates.

The controller is not an AI agent. It does not interpret requirements, review
code, or make product decisions. It only executes declared workflow policy.

## Preserved Invariants

Automation must preserve these existing rules:

1. One agent leads each workflow action.
2. Only the designated lead writes source-of-truth files and integrates code.
3. Consultant agents review the same frozen revision independently.
4. Product and scope decisions remain with the user.
5. Git and OpenSpec remain durable product sources of truth.
6. Stage transitions remain visible and traceable.
7. Multiple agents do not push or integrate concurrently.

## Control Plane And Product Plane

Automation introduces a deliberate separation:

| Plane | Canonical state | Purpose |
|---|---|---|
| Product | Git, OpenSpec, accepted project documents | What the project means and contains |
| Control | Controller database and event records | Which process should run next |
| Human view | `current-state.md` and collaboration documents | Readable status, findings, and decisions |

For automated runs, the controller database is canonical only for operational
run state. It does not supersede specifications, accepted decisions, or other
product source-of-truth files.

This resolves an ambiguity in the manual workflow: `current-state.md` can remain
the canonical human-readable project queue, while collaboration indexes remain
review and audit views. Neither is treated as a reliable process trigger.

## Reference Flow

```text
preflight
  -> resolve OpenSpec action and required skills
  -> create isolated writer worktree
  -> run Codex
  -> run deterministic checks
  -> freeze resulting commit SHA
  -> run Claude and Agy reviews in parallel against that SHA
  -> validate structured review results
  -> evaluate gates
       pass              -> advance or await configured human approval
       fixable findings  -> consolidate and return to Codex
       product question  -> pause for the user
       execution failure -> retry according to policy or fail
```

The controller must never ask a reviewer to inspect an unfrozen working tree.
Every result must identify the commit SHA it reviewed.

## OpenSpec Mapping

OpenSpec describes its workflow as actions rather than strictly locked phases.
Controller policy should therefore be keyed by OpenSpec action, even when the
project presents the broader Exploration, Proposal, and Implementation stages
to the user.

| Project stage | OpenSpec actions | Default automation behavior |
|---|---|---|
| Exploration | `explore` | Lead synthesizes; consultants review gaps; user resolves product questions |
| Proposal | `propose`, or `new` / `continue` / `ff` | Lead creates artifacts; consultants review scope and consistency |
| Implementation | `apply` | Lead implements; deterministic checks run before model review |
| Verification | `verify` | Consultants independently inspect the frozen implementation |
| Completion | `archive` | Archive only after all configured gates and approvals pass |

## Project Policy

Each project should declare automation policy in a version-controlled file such
as `agent-workflow-local/automation.yaml`.

```yaml
version: 1

defaults:
  repair_attempts: 2
  timeout: 30m
  require_clean_start: true

actions:
  apply:
    writer:
      agent: codex
      skills:
        - openspec-apply-change
        - test-driven-development
      workspace: write

    checks:
      - openspec-validate
      - lint
      - typecheck
      - test

    reviewers:
      - agent: claude
        skills:
          - edge-case-review
          - security-review
        workspace: read-only

      - agent: agy
        skills:
          - architecture-review
          - regression-review
        workspace: read-only

    gate:
      require_all_reviewers: true
      on_findings: repair
      human_approval: false

  archive:
    checks:
      - openspec-verify
      - clean-working-tree
    gate:
      human_approval: true
```

The exact skill catalog is project-specific. The shared controller defines the
policy format, not which engineering practices every project must use.

## Skill Enforcement

Prompting an agent to use a skill is guidance, not enforcement. The controller
should enforce skill delivery and verify outcomes separately.

### Delivery checks

Before starting an agent, the controller must:

1. resolve every required skill to an actual `SKILL.md`;
2. record its stable ID, version, and content hash;
3. use the relevant CLI adapter to load or explicitly invoke it;
4. fail preflight when a required skill is missing; and
5. require the agent result to identify the loaded skills.

### Outcome checks

A skill receipt proves that instructions were supplied, not that they were
followed correctly. Hard enforcement comes from observable gates such as:

- OpenSpec artifact and schema validation;
- required artifact presence and structure;
- lint, type-check, unit, integration, and acceptance tests;
- diff-scope and protected-file checks;
- required evidence paths in structured review results;
- independent reviewer concurrence; and
- protected-branch status checks before merge.

OpenSpec custom schemas may add required review artifacts and artifact
dependencies. These strengthen the workflow but do not replace external gates.

## Agent Result Contract

Agents should return validated structured output. A minimal normalized result is:

```json
{
  "status": "pass",
  "run_id": "run-20260909-001",
  "change_id": "add-route-import",
  "action": "verify",
  "commit_sha": "0123456789abcdef",
  "skills_loaded": [
    {
      "id": "security-review",
      "version": "1.2.0",
      "sha256": "..."
    }
  ],
  "checks": [
    {
      "name": "acceptance-criteria",
      "status": "pass",
      "evidence": ["tests/import-route.spec.ts"]
    }
  ],
  "findings": [],
  "decision_required": null
}
```

The controller must reject results that are malformed, reference another
commit, omit mandatory skills, or lack evidence required by policy.

Agent self-reported checks should not replace commands the controller can run
directly.

## CLI Adapters

Each agent has a small adapter that translates the common request into the
installed CLI's syntax and normalizes its response.

```python
class AgentAdapter(Protocol):
    async def run(
        self,
        request: AgentRequest,
        workspace: Path,
    ) -> AgentResult: ...
```

Adapters must be limited to:

- constructing arguments without invoking a shell;
- starting and supervising the CLI process;
- capturing stdout, stderr, exit status, and timeout;
- parsing structured output; and
- reporting capability or authentication failures.

Adapters must not decide which agent runs next or whether a review finding is
accepted. Those decisions belong to controller policy or the lead/user.

Illustrative non-interactive surfaces are:

```text
codex exec --sandbox workspace-write --ask-for-approval never --output-schema ...
claude -p --permission-mode plan --output-format json --json-schema ...
agy -p ... --sandbox --output-format json --json-schema ...
```

Actual arguments should be assembled as an argument array rather than a shell
command string. The controller should perform a version and capability check
because supported flags may change between CLI releases.

## Permission And Isolation Policy

Unattended operation must rely on native non-interactive modes, not simulated
keypresses or terminal scraping.

Default policy:

- Codex receives write access only to its isolated writer worktree.
- Claude and Agy receive read-only code snapshots.
- Reviewer output is returned through stdout or a separate result mount.
- Network access is off unless the action explicitly requires it.
- SSH agents, credential stores, unrelated home directories, `.env` files, and
  container runtime sockets are not mounted by default.
- Full permission-bypass flags are permitted only inside an externally isolated
  container or VM whose boundaries match the declared policy.
- Secrets are scoped per action and removed from review jobs that do not need
  them.

Permission bypass removes prompts; it does not make an action safe.

## State Machine

The minimum controller state machine is:

```text
PENDING
  -> PREFLIGHT
  -> WRITING
  -> CHECKING
  -> REVIEWING
  -> REPAIRING
  -> CHECKING

REVIEWING
  -> ACCEPTED
  -> AWAITING_HUMAN
  -> FAILED

AWAITING_HUMAN
  -> WRITING
  -> ACCEPTED
  -> CANCELED
```

Every transition must be persisted transactionally before the next external
process is launched. Interrupted runs resume from the last completed boundary,
not by guessing from files or chat history.

Persist at least:

- run ID, project, change ID, and OpenSpec action;
- current state and transition history;
- starting and reviewed commit SHAs;
- agent, model, CLI, and skill versions;
- attempt count, timeout, and budget information;
- raw output and normalized-result locations;
- deterministic check results;
- reviewer findings and consolidation decisions; and
- user approvals or answers.

## Review And Repair Rules

1. Claude and Agy review the same commit independently.
2. Reviewers must not see the other review before submitting their own.
3. The controller validates and combines results without judging their merits.
4. Codex, as lead, reconciles findings as accepted, partially accepted, rejected,
   or requiring a user decision, with a rationale.
5. A repair creates a new commit and invalidates reviews of the prior commit.
6. Both reviewers must review the new commit unless policy explicitly narrows a
   re-review to deterministic evidence.
7. Repair loops have a configured maximum. Exceeding it pauses for the user.
8. Scope changes always pause for the existing proposal/decision protocol.

## Collaboration Records

The existing collaboration format remains the human audit format. Automated
runs should add provenance so model authorship and controller recording are not
confused:

```text
authored-by: claude
recorded-by: awctl
run-id: run-20260909-001
commit-sha: 0123456789abcdef
```

The controller may generate indexes and run summaries from its event records.
It must not silently rewrite agent findings or accepted product decisions.

## Reference Commands

The first controller version should provide:

```text
awctl init
awctl doctor
awctl run <change-id>
awctl status [run-id]
awctl logs <run-id>
awctl approve <run-id>
awctl reject <run-id> --reason <text>
awctl resume <run-id>
awctl cancel <run-id>
awctl regenerate-views
```

`awctl doctor` should verify CLI versions, authentication, required skills,
policy and JSON schemas, OpenSpec availability, Git worktree support, repository
cleanliness, and effective permission/isolation configuration.

## Failure Semantics

Failures must be typed so the controller does not repeatedly ask a model to fix
an infrastructure problem.

| Failure type | Default response |
|---|---|
| Invalid policy or missing skill | Fail preflight |
| CLI unavailable or unauthenticated | Pause with setup instruction |
| Timeout or transient process error | Retry within policy limit |
| Malformed agent output | Retry once, then fail |
| Deterministic check failure | Return evidence to Codex |
| Reviewer finding | Begin bounded repair cycle |
| Commit mismatch | Discard review and rerun |
| Product or scope question | Pause for user |
| Repair limit exceeded | Pause for user |

Exit code alone is insufficient when a CLI can complete successfully after a
tool was denied. The adapter must also inspect the normalized terminal status
and required evidence.

## Git And CI Integration

The local controller should be the primary process supervisor for CLI sessions.
GitHub CI should be the authoritative merge enforcement layer.

Recommended required checks:

- OpenSpec validation;
- lint and type-check;
- unit/integration/acceptance tests;
- controller policy validation;
- Claude review for the current commit;
- Agy review for the current commit; and
- no unresolved controller gate.

Only the lead/integrator pushes or merges. Review agents do not receive GitHub
write credentials.

## Non-Goals

The controller does not:

- create a peer-to-peer agent network;
- let models dynamically assign roles or bypass stage ownership;
- replace OpenSpec with a proprietary workflow format;
- treat model concurrence as a substitute for deterministic tests;
- automatically answer product questions;
- grant unrestricted host access merely to avoid prompts; or
- require distributed workflow infrastructure for a local project.

## Rollout Plan

### Phase 1: Observe

- Implement `doctor`, policy loading, and structured CLI adapters.
- Run the controller beside the manual workflow.
- Record what it would trigger without triggering agents automatically.

### Phase 2: Automate reviews

- Keep Codex invocation manual.
- Automatically freeze the commit and launch Claude/Agy reviews.
- Validate results and produce a consolidation packet.

### Phase 3: Automate repair cycles

- Let the controller invoke Codex with consolidated findings.
- Enforce deterministic checks and a maximum repair count.
- Pause for all product/scope decisions.

### Phase 4: Enforce merge gates

- Publish controller and review status for the exact commit.
- Configure required branch checks.
- Keep final merge ownership with the designated integrator.

### Phase 5: Durable service, only if needed

Move to a durable workflow service such as Temporal only when runs must survive
machine restarts, span multiple machines, wait for days, or serve multiple
projects concurrently. Keep the policy and agent-adapter interfaces stable so
this migration does not change agent behavior.

## Acceptance Criteria

This improvement is complete when:

- [ ] One command can start or resume a change workflow.
- [ ] Codex is the only implementation/source-of-truth writer.
- [ ] Claude and Agy review the same immutable commit independently.
- [ ] Required skills are resolved, hashed, supplied, and recorded.
- [ ] All agent results are schema-validated.
- [ ] Deterministic gates cannot be replaced by model self-report.
- [ ] Failed or interrupted runs resume without reconstructing state from chat.
- [ ] Repair loops are bounded.
- [ ] Product and scope questions always pause for the user.
- [ ] Collaboration output remains human-readable and traceable.
- [ ] Required CI checks prevent an unverified commit from merging.

## References

- Codex non-interactive mode: <https://developers.openai.com/codex/non-interactive-mode>
- Codex approvals and sandboxing: <https://developers.openai.com/codex/agent-approvals-security>
- Claude Code headless mode: <https://code.claude.com/docs/en/headless>
- Claude Code permissions: <https://code.claude.com/docs/en/permissions>
- Antigravity CLI headless mode: <https://antigravity.google/docs/cli/headless/>
- OpenSpec workflows: <https://github.com/Fission-AI/OpenSpec/blob/main/docs/workflows.md>
- OpenSpec customization: <https://github.com/Fission-AI/OpenSpec/blob/main/docs/customization.md>

