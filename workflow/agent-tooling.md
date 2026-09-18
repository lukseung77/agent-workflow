# Agent Tooling

This is the shared policy for optional repository-intelligence, implementation-discipline, and execution-efficiency tools. Agent adapters may point to this file, but must not copy its semantic rules into separate, independently maintained policies.

## Capability Roles

- **Ponytail** is implementation discipline. Apply its YAGNI ladder while implementing or modifying code: first question whether the change is needed, then reuse existing project code, the standard library, native platform functionality, or an already-installed dependency before adding a new abstraction or dependency.
- **Graphify** is repository intelligence. Use it to navigate dependency relationships, callers/callees, symbols, modules, architecture, and likely blast radius before repeatedly scanning a large repository. Its graph is an index, not the source of truth.
- **RTK (Rust Token Killer)** is execution efficiency. Prefer its supported command rewriting or compact-output mode for verbose shell commands, while retaining a path to the underlying output whenever a failure or diagnosis needs more detail.

## Precedence

The order of authority is:

1. OpenSpec requirements and explicit user/project requirements
2. Explicit project architecture and constraints
3. Correctness, security, accessibility, and test requirements
4. Ponytail's minimalism guidance
5. Individual implementation preference

Ponytail must never justify removing required validation, security controls, tests, error handling, or accessibility. A validator may identify unnecessary complexity, but must not reject a correct implementation only because another correct implementation could use fewer lines.

Graphify must not replace source inspection. Agents must inspect the actual source files before material code changes; when the graph conflicts with source, source wins.

RTK must not hide information needed to diagnose a failure. Rerun the command without compression, use a more detailed RTK mode, or inspect the underlying log when the summary is insufficient.

## Phase Routing

Load this policy when the task-routing table calls for tooling, then apply only the relevant capability:

| Workflow activity | Ponytail | Graphify | RTK |
|---|---|---|---|
| Exploration | Optional | High: map structure and impact before broad scanning | High for verbose discovery commands |
| Proposal | Optional | High: identify affected components | Normal |
| Spec | Low | Useful for terminology and boundaries | Normal |
| Design | Useful: prefer existing capabilities | High: inspect relationships and blast radius | Normal |
| Implementation | High | High, followed by source inspection | High |
| Validation and review | Medium: flag needless complexity without failing correct code | High: check affected paths and references | High, with diagnostic fallback |

The three-stage workflow maps these activities as follows: Exploration and Proposal use Graphify-led discovery; Design uses Graphify plus focused Ponytail review; Implementation activates Ponytail and RTK strongly; validation and review use all three with correctness and diagnosability taking precedence.

## Repository Lifecycle

For a new project, the environment command follows this order:

```text
detect -> install only with explicit approval -> configure -> initialize -> verify
```

Initialization is idempotent. It preserves existing instruction files and merges only a marked adapter block. It installs project-scoped Graphify adapters when the CLI is available, builds the initial graph, and uses `graphify update .` for an existing graph rather than rebuilding from scratch. A commit hook may be enabled when the user asks for automatic refresh; otherwise refresh after substantial structural changes with `graphify update .`.

Native agent integrations are preferred where upstream supports them. The shared adapter remains the fallback for agents that only consume repository instructions. Missing tooling produces a warning and does not stop normal development:

- Graphify unavailable: inspect targeted source files normally.
- Ponytail unavailable: apply the minimalism rules in this file.
- RTK unavailable: run the normal CLI command and preserve full diagnostics.

## Configuration Ownership

The workflow owns policy and thin adapters. Ponytail, Graphify, and RTK own their generated hooks, skills, indexes, and host-specific files. Do not hand-edit generated files when the upstream CLI provides an update or uninstall command. Do not overwrite user instruction files or settings; preserve them and merge only the managed adapter block.
