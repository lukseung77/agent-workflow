# foundation-consumers Specification

## Purpose
Define the reusable foundation product boundary and the common installation,
customization, and reviewed-update process used by every consumer, including
the repository that develops the foundation.

## Requirements
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
