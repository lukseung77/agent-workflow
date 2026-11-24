# SW Development — OpenSpec And GitHub

## Process And Sources

Use OpenSpec as the overall development process for specifications, scoped
changes, implementation, and validation. Follow the actual selected version's
official workflow; do not invent CLI commands or treat foundation stage names as
OpenSpec events. Use `templates/project-types/sw-development/stages.md` for
Exploration, Proposal, Implementation, review concurrence, and human transition
approval. Scope changes during implementation require a mini-proposal before
changing accepted requirements.

The default source root is `openspec/`, with accepted specifications, change
artifacts, and exploration material indexed in project facts. Existing project
structure takes precedence when deliberately retained during setup.

## Required Capabilities

- Core Grill-Me, including its grilling dependency, for requested clarification
  interviews under `workflow/grill-me.md`.
- OpenSpec for the development process. Follow `guides/tooling-operations.md`.
- GitHub for the project repository. Reuse the existing repository/access or guide
  setup; establish repository identity, visibility, and publication scope before
  remote creation or publication. The lead owns authorized sync; coordinate writes
  so multiple agents do not publish concurrently. Selection alone grants no push
  authority. Local work may proceed while repository setup is pending.

Select additional capabilities only for demonstrated project needs, such as
library references, browser acceptance checks, security review, or interface
design. Use `workflow/tooling.md` and the origin registry; do not install a fixed
engineering bundle for every project.

## Setup And Checks

Record required capabilities as selected and unverified until actual checks
pass. Use guided installation, preserve existing specs and host configuration,
and record missing prerequisites without claiming completion. Do not silently
replace required OpenSpec or GitHub with another process or repository service.
An unavailable CLI can leave accepted files readable while its required checks
remain explicitly outstanding.

Tool freshness reviews run on confirmed stage changes and explicit requests
under `workflow/tooling-review.md`. Implementation validation follows the accepted
change's criteria; repository CI and commands are project-specific.
