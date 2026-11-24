# foundation-consumers Specification

## Purpose
Define the reusable foundation product boundary and the common installation,
customization, and reviewed-update process used by every consumer, including
the repository that develops the foundation.

## Requirements
### Requirement: Communication core and project-owned processes

The foundation core SHALL handle communication between agents and the user,
including clarification, role boundaries, durable decisions, review messages,
queues, and handoffs. Grill-Me and its grilling dependency SHALL be core interview
capabilities, separately installed and truthfully verified. Project templates
SHALL own their processes, stages, gates, integration requirements, source-root
defaults, and handoff mode. The core SHALL NOT require OpenSpec, GitHub, or a
universal software-development stage model for every project type.

#### Scenario: Proposal project uses its own process

- **WHEN** a Proposal PT Making template is selected
- **THEN** its stages validate without enabling SW gates or requiring OpenSpec/GitHub

### Requirement: Explicit project type and template selection

New-project setup SHALL ask for a project type and then its template, reusing
explicit user answers. A project type SHALL support one or more templates.
The installer SHALL validate and record the selected pair and requirements
before writes, derive the source root from the template unless overridden, and
guide required installation rather than silently installing or configuring tools.
Selection SHALL remain distinct from installed, configured, and verified state.
Existing consumers SHALL retain their local process, artifacts, and history on
update or migration without being assigned a project type implicitly.

#### Scenario: Missing or mismatched choices

- **WHEN** new initialization lacks a valid type/template pair
- **THEN** it reports the required choice and creates no project files

#### Scenario: Existing consumer predates project templates

- **WHEN** it updates without explicit type/template selection
- **THEN** its record is legacy-unselected and its local source root and stage remain unchanged

### Requirement: Initial SW Development template

The SW Development type SHALL provide an OpenSpec/GitHub template using OpenSpec
as the overall development process and GitHub for the repository. It SHALL own
its development stages and review/approval gates, and select additional tools,
skills, or plugins for demonstrated project needs. Repository creation and
publication SHALL follow actual authorization rather than template selection.

#### Scenario: SW template initialization

- **WHEN** the OpenSpec/GitHub template is selected
- **THEN** setup records both requirements and core Grill-Me without claiming installation or creating a remote repository

### Requirement: Full Proposal PT Making template with manual handoff

The Proposal PT Making type SHALL provide a full-scope template using MarkItDown
for RFP/supporting-data read-in, ChatGPT for RFP analysis and TOC/per-slide
planning, and the user's Claude PowerPoint plugin for slide production. Handoffs
between ChatGPT and Claude SHALL initially be manual. Slide briefs SHALL include
TOC, per-slide title, key message, contents, and drawing/layout prompts. The
process SHALL include final review and revision against RFP requirements. The
exact plugin SHALL remain unverified until identified in its actual host.

#### Scenario: Planning is handed to Claude

- **WHEN** the user approves a ChatGPT slide brief
- **THEN** the user manually transfers its identified revision to Claude and returns the deck, deviations, and questions for review

#### Scenario: Slide-production plugin is not yet identified

- **WHEN** setup cannot verify the exact Claude PowerPoint plugin
- **THEN** it records that unresolved prerequisite and permits independent planning without claiming slide production capability

### Requirement: Separate product and operational instance

The repository SHALL publish a reusable foundation boundary containing rules,
templates, first-party tooling/skills, and third-party origins. Project-local
values, collaboration history, and maintainer-specific authority SHALL remain
outside that product. The source project SHALL consume the same local scaffold.

#### Scenario: New project installs from a source repository

- **WHEN** a source repository contains both a foundation and its own project state
- **THEN** installation copies only the foundation and creates a separate consumer instance

#### Scenario: Foundation repository initializes itself

- **WHEN** the source and installed foundation directory are the same
- **THEN** the common installer registers that product in place and instantiates the same templates

### Requirement: Preserve customization during reviewed updates

Updates SHALL offer a read-only plan, retain populated local values, and apply
only when no unresolved conflict remains. Rendered template baselines SHALL
support three-way merging; explicit reviewed local deviations MAY be retained.

#### Scenario: Independent local and upstream edits

- **WHEN** local customization and new defaults change non-overlapping template content
- **THEN** update merges both and retains the consumer's task state and host instructions

#### Scenario: Conflicting changes or modified upstream deletion

- **WHEN** an upstream update conflicts with local content
- **THEN** apply reports the conflicting paths and writes none of the planned update files

### Requirement: Third-party origin registry

The foundation SHALL reference official third-party origins instead of bundling
implementations. Authorized setup SHALL select needed compatible stable tools
and record actual verified version/origin and configuration in the consumer.

#### Scenario: Stable release cannot be resolved

- **WHEN** an optional installer cannot resolve a stable source release
- **THEN** it reports the limitation rather than silently installing development HEAD

#### Scenario: Existing manual plugin verification

- **WHEN** a convenience inventory pass cannot inspect a native plugin
- **THEN** it preserves prior verified plugin metadata and reports unknown state where no verification exists

### Requirement: Product-only export and acceptance evidence

Exports SHALL include only manifest product content. Maintenance validation SHALL
check the product boundary and this repository's ordinary consuming instance.

#### Scenario: Release package is exported

- **WHEN** the export command packages the foundation
- **THEN** the package contains local scaffold templates but none of the source project's populated configuration or history
