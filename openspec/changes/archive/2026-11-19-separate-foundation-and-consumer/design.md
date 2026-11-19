## Context

The foundation is product source, analogous to application source code. Its
project-local scaffold serves both other projects and this repository itself.
Reviews and reusable rule changes target that product by default; one project's
custom values are not silently promoted to defaults.

## Goals / Non-Goals

Goals: one distributable boundary, one setup/update mechanism, preserved local
customizations, portable origins, and evidence from both self and independent consumers.

Non-goals: publishing to GitHub, installing host plugins, deciding previously
deferred stage/format policies, or merging conflicting local requirements automatically.

## Decisions

1. The manifest enumerates product roots. Source repository acquisition selects
   only its foundation child. Export never includes root project state or history.
2. Local templates render project identity and roles once. The local installation
   state records source/fingerprint, product hashes, and rendered template bases;
   it is operational metadata excluded from normal prompt reads.
3. Updates review before apply. Unmodified product files update or delete safely;
   customized product files that also changed upstream require reconciliation.
   Local template updates use a three-way Git merge when necessary. Any unresolved
   conflict prevents all planned writes. Explicit keep-local selections record
   reviewed deviations without replacing the local content.
4. The source repository registers its foundation in place using the same tool,
   then customizes its local maintainer rules. No special startup bypass exists.
5. Tool origins are first-class data. Supported convenience installers resolve
   stable upstream packages/tags when requested and retain explicit compatibility
   selectors. Exact verified version output and host status stay in local inventory.

## Risks / Trade-offs

- File writes are individually atomic; updates are not multi-file crash transactions.
  Consumers should retain version control or a backup before apply.
- Automatic template merging needs Git. Without it, overlapping customization is
  reported for manual reconciliation instead of introducing another dependency.
- Source acquisition and third-party installation require permitted network access.
  Local integration tests do not prove remote or native host integration.
- Operational installation metadata must be preserved for future comparisons.

## Migration Plan

Preserve existing history and the pre-restructure working tree snapshot at
`/private/tmp/agent-workflow-before-foundation-r1e1p2b6.tgz`. Move product files,
instantiate this consumer, review/apply its own update, then run regression,
boundary, queue, and OpenSpec validation. Existing consumers retain their old
copies until deliberately migrated. The new source package has no root workflow
compatibility copies that could become a second product source of truth.
