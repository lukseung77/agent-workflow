## ADDED Requirements

### Requirement: Shared capability policy

The workflow SHALL define one shared policy that treats Ponytail as
implementation discipline, Graphify as repository intelligence, and RTK as
execution efficiency, with explicit precedence for OpenSpec, project
architecture, correctness, security, and tests.

#### Scenario: Implementation uses minimalism safely

- **WHEN** an agent implements an accepted change
- **THEN** it applies Ponytail's YAGNI and reuse guidance without removing
  required behavior, validation, security, accessibility, or tests

#### Scenario: Graph conflicts with source

- **WHEN** Graphify's index disagrees with an inspected repository file
- **THEN** the agent treats the repository source as authoritative

#### Scenario: Compressed output is insufficient

- **WHEN** RTK's summary does not contain enough information to diagnose a
  command failure
- **THEN** the agent reruns or inspects the underlying command output at the
  required detail level

### Requirement: Idempotent project bootstrap

The environment command SHALL detect available agents and tools, configure
available project-scoped integrations, initialize or update the Graphify index,
and verify the result without requiring any optional tool for normal workflow
operation.

#### Scenario: Clean project

- **WHEN** initialization runs in a new software project with detected tools
- **THEN** it creates a thin shared-rule adapter, configures supported
  project-scoped adapters, builds a Graphify index, and reports verification

#### Scenario: Repeated initialization

- **WHEN** initialization runs more than once
- **THEN** existing user instructions are preserved, the managed adapter is not
  duplicated, and an existing Graphify index uses its incremental update path

#### Scenario: Tool is unavailable

- **WHEN** Ponytail, Graphify, or RTK is absent or cannot be verified
- **THEN** initialization reports a useful warning and leaves normal development
  available through shared rules or standard repository/CLI inspection

### Requirement: Safe installation and host integration

The bootstrap SHALL use validated upstream-supported installation/configuration
mechanisms, SHALL never pipe an arbitrary remote installer into a shell, and
SHALL require explicit approval flags for package installation or agent-wide
hooks/plugins.

#### Scenario: Missing package without approval

- **WHEN** a tool is missing and initialization runs without installation
  approval
- **THEN** no package installation occurs and the report gives the user the
  supported next action

#### Scenario: Partial installation failure

- **WHEN** one optional installation or agent integration fails
- **THEN** the failure is reported and other independent supported components
  continue configuring

#### Scenario: Existing configuration

- **WHEN** the project already has `AGENTS.md` content or generated tool files
- **THEN** the bootstrap preserves existing content and avoids duplicate managed
  adapters

### Requirement: Phase-aware integration and diagnostics

The workflow SHALL route Graphify, Ponytail, and RTK by the existing
Exploration, Proposal, and Implementation stages and by validation/review
activities, and SHALL provide a doctor report without exposing secrets.

#### Scenario: Phase routing

- **WHEN** agents work in Exploration, Proposal, Design, Implementation, or
  Validation/Review
- **THEN** the shared policy identifies the relevant capability intensity and
  does not require loading every tool into every prompt

#### Scenario: Environment doctor

- **WHEN** a user runs the diagnostic command
- **THEN** it reports detected agents, Ponytail rules, Graphify, Graphify index,
  and RTK status with warnings for unsupported integrations and no secret values
