## Why

The repository mixed its delivered reusable workflow with its own agent
collaboration, maintainer authority, and project state. The human defined the
product as agent-workflow-foundation and requested that this project consume
the same local scaffold and update mechanism as other projects. Third-party
tools and skills should be referenced by official origin rather than bundled.

## What Changes

- Move reusable product source into agent-workflow-foundation with an explicit
  distribution manifest and product-only export.
- Group the local scaffold under foundation templates and instantiate this
  repository's agent-workflow-local and host files using the common installer.
- Keep maintainer-specific policies, records, product specs, tests, and history
  in this consuming project, outside the distributable product.
- Support local/repository sources, reviewed updates, template merges, and
  conflict detection while preserving populated values and project state.
- Register official third-party origins and record verified versions locally.

## Capabilities

### New Capabilities

- `foundation-consumers`: product distribution, self-consumption, scaffold
  customization, and reviewed updates.

### Modified Capabilities

- None. Existing collaboration integrity and optional-tooling requirements
  continue to apply from their new product paths.

## Impact

Product entry paths move under agent-workflow-foundation. Repository validation
stays at scripts/validate.py. Historical records are preserved without rewriting
their reviewed snapshots. Root host files and this repository's own local
configuration use the new product path. No third-party package or host plugin is
installed as part of this restructure; GitHub publication remains separate.
