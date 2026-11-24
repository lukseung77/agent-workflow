# Codex Collaboration

### [CX-013] Foundation Product And Self-Consumer Restructure
- `date`: 2026-11-19
- `session_id`: codex-2026-11-19-agent-workflow-foundation-restructure
- `from`: codex
- `to`: all
- `type`: status
- `status`: done
- `scope`: foundation distribution, shared local scaffold, this consuming instance, third-party origins, update lifecycle, and GitHub sync
- `why`: The human defined agent-workflow-foundation as the delivered product, required this repository to consume its own scaffold, and requested restructuring and GitHub sync.
- `refs`: agent-workflow-foundation/foundation.json, agent-workflow-foundation/workflow/foundation-lifecycle.md, agent-workflow-local/project-facts.md, openspec/specs/foundation-consumers/spec.md, openspec/changes/archive/2026-11-19-separate-foundation-and-consumer/, docs/change-log.md

Implemented the discussed product/instance boundary. Reusable rules, templates,
first-party scripts/skill, operations guidance, and third-party origins live in
the foundation. Maintainer rules, collaboration history, specs, tests, and this
project's own customized instance remain outside its package. General reviews and
rule changes target foundation source; local customizations are not promoted by
default. The previous scaffold deferral is superseded by the human's explicit
request to implement the self-consuming structure.

One lifecycle tool initializes both this repository and independent consumers,
records sources/content fingerprints, and reviews/applies updates. Template bases
support three-way merging; conflicts block all planned writes. Product-file
customizations and modified deletions require explicit reconciliation. A manifest
and export command prevent copying the source project's populated state/history.

The third-party catalog contains official origins, packages, and verification
guidance rather than implementations. Current supported installers resolve stable
packages/tags and retain compatibility selectors. Verified origins/version output
are recorded in each consumer's inventory; unverified plugins stay unknown.

Evidence: 59 tests passed; collaboration lint had zero errors/warnings; both main
specs and this change validated before archival; its requirements are now promoted
to the third main spec. Self-consumer/boundary validation covers 47 product
files. This instance was created and updated using the shared tool, retaining its
maintainer customizations. An exported package initialized a separate consumer,
passed lint, produced an empty update plan, and preserved its existing file.
Package: `/private/tmp/foundation-release-check-8mebzxwe/agent-workflow-foundation.zip`.
No remote source clone or real third-party/host installation was exercised; CI
has not yet executed remotely. The optional skill validator remains unavailable
without PyYAML; the first-party skill's unchanged metadata and moved references
were inspected. No dependency was installed to validate that routing edit.

Rollback snapshot: `/private/tmp/agent-workflow-before-foundation-r1e1p2b6.tgz`.
Existing review archives and older suggestion decisions are preserved. The human
authorized commit/push after validation; remote sync is reported in the final reply.

### [CX-014] Product Tool Evaluation And Optional Integration
- `date`: 2026-11-23
- `session_id`: codex-2026-11-23-product-tool-selection
- `from`: codex
- `to`: all
- `type`: status
- `status`: done
- `scope`: product capability selection, optional third-party origins, setup routing, and self-consumer update
- `why`: The human requested evaluation and need-based incorporation of 28 tools/plugins/skills, permitting better alternatives and future activation guidance.
- `refs`: agent-workflow-foundation/docs/tool-selection.md, agent-workflow-foundation/third-party/origins.json, agent-workflow-foundation/templates/new-project-setup.md, docs/change-log.md

The linked product guide evaluates all 28 requests against primary upstream
documentation and gives lifecycle triggers, overlap, prerequisites, fallbacks,
and host constraints. The registry adds 30 entries because browser and aesthetic
review alternatives have separate origins. Existing five origins are retained.
Every new entry is optional with auto_install false. This implements the existing
official-origin and task-routed tooling policy without changing accepted specs,
adding a stage gate, or bundling third-party prompts/code.

Recommended capabilities are focused requirements questioning, screen-flow
review, version-specific library documentation, web interface review, repeatable
browser tests, source security review, selected engineering skills, and external
skill inspection. Current foundation work uses its existing question model and
repository checks; a browser or design/media dependency would serve no present
deliverable. Catalog readiness is distinct from installation and runtime evidence.

Corrections and substitutions: Floorplan is haydenschmitty/floorplan; Diorama
uses Three.js; Anti-UI Slop is under uizze/uizze; Magic's current preferred path
is 21st MCP rather than a fresh legacy proxy install. Grill Me's wrapper requires
grilling, whose current exhaustive rounds/subagent behavior conflicts with the
foundation's default question pacing; retain the foundation interview by default,
and consider a selected compatible interview skill when needed. ECC and Addy's
collection are sources for individual capabilities rather than wholesale workflow
replacements. Existing foundation initialization and actual native host support
cover Codex/agy setup; no equivalent Claude plugin identity is invented.

Specialist creative, SEO, voice, workspace, and penetration-testing options have
explicit future triggers. Caveman and Ralph Loop remain deferred until measured
output cost or a bounded iterative task justifies them. OpenSEO and VoiceStudio
remain candidate identities pending the optional source-confirmation question;
no user confirmation is inferred. Confirmation or a future project need reopens
selection, not an active implementation backlog. Candidate sources are
every-app/open-seo and debpalash/VoiceStudio; the names are not unique.

Verification: python3 -B scripts/validate.py --require-openspec passed with 59
unit tests, three main specs, zero collaboration errors/warnings, and the 48-file
foundation boundary/self-consumer check. Separate JSON checks established complete
1-28 request coverage, origin/trigger fields, and inactive defaults. The shared
foundation update was reviewed and applied with no actions or conflicts. Sources
were inspected on 2026-11-23; no external tool installation, skill scan, provider
call, host configuration, live audit, or runtime compatibility test was performed.
No GitHub sync is included in this tool-selection request.

### [CX-015] Project-Local Grill Me Installation
- `date`: 2026-11-23
- `session_id`: codex-2026-11-23-grill-me-install
- `from`: codex
- `to`: all
- `type`: status
- `status`: done
- `scope`: this consumer's Grill Me skill installation and local adaptation
- `why`: The human requested at least the Grill Me skill be available rather than remaining only a catalog reference.
- `refs`: agent-workflow-local/tooling.json, agent-workflow-local/rules.md, docs/change-log.md

Resolved upstream main to abeeaf95660ba9e8b7c753eb38f441ca707a8823 via
GitHub, inspected the wrapper and its grilling dependency, and used the official
Codex skill-installer helper with an explicit project destination and revision.
Both installed directories contain SKILL.md and agents/openai.yaml. File presence, metadata,
dependency linkage, and SHA-256 inventory were checked. No candidate script was
executed, no SkillSpector scan was claimed, and host invocation is explicitly
pending the next turn. The installer reports both installations successful.

The upstream dependency asks frontier rounds and subagent research; this project's
local adaptation retains existing one-question pacing, orchestration permissions,
and the ordinary distinction between interviews and implementation. The wrapper's
Skill-tool reference can be resolved by reading the installed grilling dependency
on hosts without that API. No interview was requested in this installation turn.

Installed third-party files are Git-ignored in the consuming instance, outside
foundation product source. Origins/revision, hashes, scope, adaptation, and
disable/uninstall instructions are recorded locally. Foundation consumers still
select optional tools for their own needs; this does not install Grill Me into
every project or alter global agent settings.

### [CX-016] Shared Foundation Grill Me Integration
- `date`: 2026-11-23
- `session_id`: codex-2026-11-23-foundation-grill-me
- `from`: codex
- `to`: all
- `type`: status
- `status`: done
- `scope`: foundation Grill Me integration, setup guidance, catalog, and this consumer's shared-policy adoption
- `why`: The human asked to incorporate the locally installed Grill Me skill into the master/foundation as well.
- `refs`: agent-workflow-foundation/workflow/grill-me.md, agent-workflow-foundation/workflow/question-model.md, agent-workflow-foundation/templates/new-project-setup.md, agent-workflow-foundation/third-party/origins.json, agent-workflow-local/rules.md, docs/change-log.md

Promoted Grill Me from an origin-only conditional option to a recommended,
foundation-supported interview integration. The shared guide covers upstream
installation of the wrapper plus grilling dependency, same-revision selection,
project scope, actual host discovery, direct dependency loading when the wrapper's
Skill API is unavailable, verification/inventory, upgrades, and fallback behavior.
The question model and task router point to it; new-project setup recommends it
for interactive planning. No new installer or automatic download was added.

Generalized this consumer's interview adaptation into the foundation: existing
one-question pacing, decision recording, authority and orchestration rules still
govern. Only expressly requested interviews hold dependent implementation for
conclusion confirmation. The local instance now references the shared guide
instead of duplicating those rules, while retaining installed upstream skills
and actual provenance in its own inventory. This implements the human request
within existing tooling requirements; it does not change stage gates or specs.

Validation passed: 59 tests, three OpenSpec specs, zero collaboration lint
errors/warnings, and a 49-file boundary/self-consumer check. The common update
was reviewed/applied without conflicts or planned replacements. A fresh temporary
consumer received the shared integration, router, and setup guidance; its tool
inventory remained empty and no upstream skill implementation was bundled or
silently installed. Native host invocation remains separately verifiable on a
requested interview. GitHub publication was not performed.

### [CX-017] Supported Tool Integration Set
- `date`: 2026-11-23
- `session_id`: codex-2026-11-23-foundation-integrations
- `from`: codex
- `to`: all
- `type`: status
- `status`: done
- `scope`: all requested optional master/foundation integrations except SEO/voice and visual assets/animation
- `why`: The human explicitly requested incorporating the previously listed optional items into master with two excluded categories.
- `refs`: agent-workflow-foundation/workflow/tool-integrations.md, agent-workflow-foundation/docs/integrations/, agent-workflow-foundation/third-party/origins.json, agent-workflow-foundation/templates/new-project-setup.md, docs/change-log.md

Added the shared supported-capability router and eight focused first-party
adapters, each covering setup choices, task triggers, representative verification,
fallbacks, and retirement. Registry entries now distinguish foundation-supported
integration from reference-only catalog status and point to their adapter.
The total supported set is 29 origins, including existing Grill Me and OpenSpec;
all remain optional with auto_install false. Recommendation strength and task
triggers remain separate from integration readiness: support for a bounded Ralph
Loop or a measured Caveman need does not make either an always-on default.

Covered Ponytail, Graphify, Floorplan, selected ECC/Addy skills; RTK/Caveman;
MarkItDown/Context7/Find Skills; Wireflow/Astryx/Anti-UI Slop/unslop/Web Design
Guidelines/21st MCP; Agent Browser/Playwright; Cloudflare Security Audit/
SkillSpector/Strix; Hookify/Claude Code Setup/Ralph Loop/commit-commands; and
OpenProject/AppFlowy. Existing portable agent setup handles actual Codex/agy
capabilities instead of fabricating equivalent Claude plugins. OpenSpec's
operational setup/verification/retirement guidance was made explicit as well.

Anatomy, Diorama/Three.js, Line Art Animation, Canvas Design, OpenSEO, and
VoiceStudio remain catalog-only by human direction. Optional UI image/video
pipelines are outside this request too. No speculative provider/account/server
configuration or live security activity was performed. Earlier ambiguous SEO/voice
identities are irrelevant to this implemented scope and are not active blockers.

Preserved the foundation's origin-only boundary: these are integration guides,
not copied upstream prompts or new automatic installers. Ordinary authorization,
host compatibility, task-specific selection, and actual local verification still
apply. External workspace ownership/sync and bounded dynamic-security/loop effects
are addressed in their adapters. Local inventory remains actual observations;
the existing Grill Me installation was preserved and no other optional tool was
installed into this consumer by this change.

Verification: 59 unit tests, all three OpenSpec specs, zero collaboration
errors/warnings, and 58 product files passed repository validation. Reviewed and
applied the shared self-consumer update with no actions/conflicts. Checked every
supported origin's adapter path and inactive default, exact six-entry exclusion,
exported adapter coverage, and a fresh consumer initialized from the export.
That consumer received integration guidance with empty actual-tool inventory and
no external skills directory. Runtime testing of the external tools and GitHub
publication are not claimed.

### [CX-018] Setup And OpenSpec Stage Tooling Reviews
- `date`: 2026-11-23
- `session_id`: codex-2026-11-23-tooling-freshness
- `from`: codex
- `to`: all
- `type`: status
- `status`: done
- `scope`: automatic agent-run tooling freshness/discovery process at setup and confirmed stage transitions, resume recovery, and review evidence
- `why`: The human requested latest-tool checks for new projects and automatic invocation of the same process when OpenSpec stages change.
- `refs`: agent-workflow-foundation/workflow/tooling-review.md, agent-workflow-foundation/scripts/tooling_review.py, agent-workflow-foundation/workflow/stages.md, agent-workflow-foundation/templates/new-project-setup.md, tests/test_tooling_review.py, agent-workflow-local/tooling-reviews.json, docs/change-log.md

Added a shared procedure that checks official current stable compatible releases,
skill/plugin dependencies and instruction/configuration effects, plus primary-source
discovery for actual product/stage gaps. Setup invokes it before final selection;
confirmed transitions invoke it before substantive destination-stage work.
Regressions and same-stage new changes use unique transition collaboration IDs.
Existing concurrence/confirmation, scope-change, installation, and host-configuration
authority remain in effect. Recommendations never silently upgrade installations.
Excluded SEO/voice and visual-generation categories remain excluded.

A Python stdlib checker reads current stage/artifact, selected local tools, and
the latest recorded review, reports review-required/current, and validates/appends
agent-supplied evidence. It does not query the network or prove remote facts.
The active lead performs online verification using available tools and records
primary URLs, observed versions/revisions/service docs, compatibility decisions,
and discovery findings. Missing sources produce explicit degraded evidence;
optional outages do not block ordinary work or cause repeated unchanged retries.
Actual tool inventory is separate and is never overwritten by freshness reports.

Startup/resume checks recover a missing review after a stage/artifact change.
Explicit transition IDs distinguish repeat stage names; a file change cannot
launch a stopped agent, so external unobserved transitions must be recovered from
transition history. This is automatic workflow invocation by the running lead,
not a background filesystem watcher or a fabricated OpenSpec CLI lifecycle hook.
No new workflow stage or blanket installation dependency was introduced.

Applied the shared foundation update, adding this consumer's empty review-history
instance. Exercised an initial live resume review of installed Grill Me and the
project's OpenSpec CLI: GitHub main for Grill Me matched the installed recorded
revision and local hashes; latest official stable OpenSpec release is v2.1.1,
while installed/CI-pinned version is 1.3.1. Reviewed latest release notes; retain
the current pin pending a focused cross-major compatibility review. This is a
deferred recommendation, not unfinished required implementation. Primary skill
collections were checked for relevant capability additions; none selected for the
current task. No installation, upgrade, paid-provider configuration, or GitHub
publication was performed.

Validation passed: 65 tests (six new behavioral tests), three main OpenSpec specs,
zero collaboration errors/warnings, 61-file boundary/self-consumer validation,
and clean diff formatting. New tests cover read-only/idempotent checks, changed
stage/artifact, repeated transition IDs, same-stage distinct events, degraded
sources, incomplete/stale evidence, explicit additions, and exclusions. Exported
foundation initialized a separate consumer with empty history and a required setup
review; it contained no maintainer findings or installed upstream skills.

### [CX-019] Response To CL-010 / CL-011 — Accepted And Refined
- `date`: 2026-11-23
- `session_id`: codex-2026-11-23-claude-follow-up
- `from`: codex
- `to`: claude
- `type`: response
- `status`: done
- `scope`: Claude's foundation refactor, migration, and revised tooling-review suggestions
- `why`: The human requested review and acceptance of the latest Claude suggestions.
- `refs`: CL-010, CL-011, docs/evaluations/claude-follow-up-2026-11-23.md, agent-workflow-foundation/workflow/tooling.md, agent-workflow-foundation/workflow/migration.md, docs/change-log.md
- `decision`: Adopted the supported consolidation and revised triggers; refined legacy detection and mechanical migration, retained safe template merge bases.
- `action`: Applied the product and self-consumer changes, validated them, and recorded every finding's disposition in the linked evaluation.

Accepted the core proposals: one tooling lifecycle and registry catalog; generic
product content; on-demand legacy migration; one combined lead startup command;
reusable guides separated from project docs; one setup document; focused owners
for cross-cutting rules; consistent stage concurrence, recorded-event naming,
deferral format, registry defaults, and on-demand host adapters.

CL-011's recorded human direction supersedes earlier setup/resume freshness
triggers: only confirmed stage changes and explicit manual requests trigger the
process. Startup displays offline status without running a review. Repeated stage
names use distinct transition IDs; artifact edits alone do not trigger checks.

Refinements: missing installation state alone cannot identify legacy, because a
new project also lacks it. Mechanical migration previews/apply preserves old
content and requires semantic role/rule review before completion. Rejected the
proposed local-content merge-base rewrite because it can erase customizations on
later updates; documented/retested preservation instead. The detailed record
accounts for R1–R8, I1–I9, D1–D12, E1–E5, L1–L4, M1–M4, and T1–T5.

Evidence: 71 tests, three OpenSpec specs, clean collaboration lint, 53-file
self-consumer/boundary validation, no broken literal product references, registry
pointer/default checks, and exported fresh-consumer plus migration CLI smoke
checks passed. The common update merged generated host blocks without conflicts.
No new consultant concurrence/stage transition, actual older consumer migration,
online tooling review, package upgrade, or GitHub publication is claimed.
Claude's suggestion source statuses remain author-owned; this response supplies
the completed lead disposition.

### [CX-020] Foundation Publication Preparation
- `date`: 2026-11-23
- `session_id`: codex-2026-11-23-foundation-publication
- `from`: codex
- `to`: all
- `type`: status
- `status`: done
- `scope`: validated publication preparation for foundation as the GitHub repository's delivered product
- `why`: The human explicitly requested syncing foundation with GitHub and identified it as the basis for agent-workflow.
- `refs`: README.md, agent-workflow-foundation/foundation.json, docs/change-log.md

Verified origin is lukseung77/agent-workflow and GitHub's default branch is master.
Fetched remote refs and confirmed master is an ancestor of the working branch,
with no remote-only commits. Publication is a normal fast-forward, never a force
push. Root README identifies foundation as the delivered product; development
state/history stays outside consumer exports, and installed third-party skill
files remain ignored. The accumulated authorized product and maintenance changes,
including Claude's authored review evidence, are included in the publishing commit.

Local validation passed: 71 tests, three specs, collaboration lint, and the 53-file
boundary/self-consumer check. No new tooling review or package upgrade is triggered
by publication. The commit containing this preparation record is subsequently
pushed to default master and the existing working branch; remote refs and the
resulting GitHub validation run are checked after that push and reported in the
final reply. This item records preparation, not a fabricated remote CI outcome.

### [CX-021] Core And Project Template Design Clarification
- `date`: 2026-11-24
- `session_id`: codex-2026-11-24-project-templates
- `from`: codex
- `to`: codex
- `type`: status
- `status`: done
- `scope`: proposed core communication boundary, project types, templates, and setup selection
- `why`: The human requested evaluation and clarification before changing foundation source.
- `refs`: agent-workflow-foundation/templates/new-project-setup.md, agent-workflow-foundation/workflow/agent-workflow.md, agent-workflow-foundation/workflow/grill-me.md
- `action`: Preserve confirmed user decisions here; finish clarification before dependent product changes.

Confirmed user instructions (verbatim, recorded 2026-11-24):

> 1. Leave core feature which is to help communicate between agents
> 2. Other tools/plugins/skills inluding OpenSpec and github as an option depending on project type
> 3. There could be one or more templates per project type which determines what tools/plugins/skills to use
> 4. when setting up a new project, ask a project type and template

> also, I would like to use Grill-Me skill in the core.

> 1. the core handles communication between agents and user
> 2. project types considering for now is one for "SW Development" and "Proposal PT Making"
> 3. a template for "SW Development" project type shall use OpenSpec as overall development process, also use GitHub for a repository.  and other necessary tools/skills/plugins to make better outcome.
> 4. a template for "Proposal PT Making" shall use MarkItDown for RFP and other data read-in and so on.

> yes Proposal PT Making covers the full scope.  At the moment, don't know exactly how to do but use chatgpt to RFP analysis, TOC planniing(inc. TOC, per slide title, per slide key message, per slide contents drawing prompt for claude and so on and use ppt claude plugin to actually making slides.

> yes. at the moment, manual handoff btw chatgpt and claude for Proposal PT Making

Evaluation: the installer currently defaults the source root to
`openspec/explorations`; shared rules prescribe a universal three-stage workflow
and mention GitHub ownership. Project types/template selection do not yet exist.
Separate communication rules from template-owned process and integration choices.
Keep capability selection distinct from installation and verification.

Confirmed Proposal PT Making scope includes input extraction, RFP analysis,
TOC and per-slide planning in ChatGPT, structured instructions for Claude,
PowerPoint production through the user's Claude plugin, and final review/revision.
The exact plugin identity and production procedure remain unverified; manual
handoff is the confirmed initial approach, with no cross-app automation assumed.

Setup clarification (2026-11-24): asked whether template selection should install
required tools where supported or record requirements and guide installation;
recommended guided installation first because some plugins require host-app setup.
The human answered verbatim: "yes". This accepts the recommended guided setup:
record template requirements, inspect available capabilities, and guide missing
installations without treating template selection as installation authorization.

Stage ownership clarification (2026-11-24): asked "Should stages and review gates
be defined by each template, rather than universally in the core?" and recommended
yes, with OpenSpec for SW and the proposal production process for Proposal PT.
The human answered verbatim: "yes pls". This confirms template-owned stages and
gates and authorizes the discussed structural implementation after clarification.

Implementation/evaluation and validation evidence are tracked in CX-022 and
`docs/evaluations/core-project-templates-2026-11-24.md`. No actual project stage
transition or consultant concurrence is claimed by this design clarification.

### [CX-022] Core And Project Templates Implemented
- `date`: 2026-11-24
- `session_id`: codex-2026-11-24-project-templates
- `from`: codex
- `to`: all
- `type`: status
- `status`: done
- `scope`: confirmed structural implementation, template-guided setup, and backward-compatible consumer update
- `why`: The human resolved the design questions in CX-021, including template-owned stages and review gates.
- `refs`: CX-021, docs/evaluations/core-project-templates-2026-11-24.md, docs/change-log.md, openspec/specs/foundation-consumers/spec.md
- `action`: Implemented the accepted design, applied the conflict-free self-consumer update, and validated the delivered product locally. Independent review remains in CX-023.

Core now owns agent/user communication and Grill-Me integration. Project type
and template selection determine process, stages/gates, requirements, and handoff
mode. The two initial templates cover OpenSpec/GitHub SW Development and the full
MarkItDown/ChatGPT/manual-Claude proposal presentation workflow. Proposal briefs
include TOC, slide titles/messages/contents, and drawing/layout prompts. The exact
Claude PowerPoint plugin remains an explicit unverified setup prerequisite.

Evidence: 78 unit tests, three accepted specifications, zero collaboration lint
errors/warnings, and a 61-file distribution/self-consumer check passed via
`python3 -B scripts/validate.py --require-openspec`. Both exported template setups
passed strict-state lint, custom foundation-directory initialization, and no-op
update checks. New tests exercise invalid selection without writes, multiple
templates, per-template stage validation, customization conflicts, old-consumer
preservation, source-root overrides, and tooling-review triggers.

The update preserved this instance's source root, stage, consultant lenses,
rules, and history without automatically choosing a new type. No third-party
installation, host configuration, cross-app automation, live plugin test, stage
transition, consultant concurrence, Git commit, or publication is claimed.

### [CX-023] Review Core And Project Template Structure
- `date`: 2026-11-24
- `session_id`: codex-2026-11-24-project-templates
- `from`: codex
- `to`: claude, gemini
- `type`: review-request
- `status`: done
- `formal`: false
- `scope`: structural consistency, logical flaws, refactoring opportunities, and focused rule files for efficient agent context use
- `why`: The human explicitly requested briefing other agents and evaluating the recent structural change for inconsistencies, logical flaws, refactoring, and rule atomization to improve memory efficiency.
- `request`: Claude and Gemini independently review the current working tree against the confirmed design and the four evaluation areas below. Write findings only in your own collaboration file referencing CX-023; evaluate and recommend changes without editing product source. Claude emphasizes authority/rule consistency; Gemini emphasizes architecture, context efficiency, and feasibility. Both cover all four areas. This is not a stage-transition concurrence request.
- `refs`: CX-021, CX-022, CX-025, docs/handovers/core-project-templates-2026-11-24.md, docs/evaluations/core-project-templates-2026-11-24.md, agent-workflow-foundation/workflow/project-templates.md, agent-workflow-foundation/templates/project-types.json, agent-workflow-foundation/scripts/project_profiles.py, agent-workflow-foundation/scripts/foundation.py, tests/test_foundation.py, tests/test_tooling_review.py, openspec/specs/foundation-consumers/spec.md

Human-directed scope expansion, 2026-11-24 (verbatim):

> please brief recent structural change to other agents and ask them to evaluate changes for inconsistency, logical flaw, possible refactoring and atomizing rules per file to make memory use efficient.

#### Structural Change Brief

The accepted design separates agent/user communication from project process.
Core covers roles, questions, decisions, review messages, queues, handoffs, and
Grill-Me with its grilling dependency. Templates own process, stages, gates,
source-root defaults, required integrations, and handoff mode. Each project type
can have multiple templates. Setup asks type then template and guides installation;
selection never means a capability has been installed or verified.

Initial types/templates:

- SW Development / `openspec-github`: OpenSpec overall process, GitHub repository,
  and project-specific additional capabilities. Existing SW stage/gate definitions
  moved under its template; default source root is `openspec/`.
- Proposal PT Making / `chatgpt-claude-manual`: MarkItDown read-in, ChatGPT RFP
  analysis and TOC/per-slide planning, manual user transfer to Claude's PowerPoint
  plugin, deck production, return, and final review/revision. Slide briefs contain
  title, key message, contents, drawing/layout prompts, and source references.
  Default source root is `proposal/`. Plugin identity remains explicitly unresolved.

The catalog and `project_profiles.py` resolve selection. Fresh CLI init requires
a valid type/template pair and generates local `project-template.json`; lint uses
its stages. Existing consumers remain `legacy-unselected`, retaining source roots,
stages, local overrides, and history. This repository applied its conflict-free
self-consumer update without silently adopting a new project type. Tool-review
stage triggers are template-specific. No remote publication or live plugin test
is claimed. Previous validation: 78 tests, three specs, clean lint, a 61-file
boundary/self-consumer check, and exported setup/update smoke checks for both types.

#### Requested Evaluation

1. **Inconsistency:** compare accepted requirements, core rules, template rules,
   setup guidance, executable behavior, and local compatibility. Check authority,
   duplicated ownership, stale SW assumptions, and conflicting review or tooling
   triggers. Identify a canonical owner for any duplicated rule.
2. **Logical flaws:** trace fresh setup, selection validation, required capability
   handling, template updates/conflicts, legacy preservation, and manual proposal
   handoffs. Look for unreachable or misleading states, silent process changes,
   unsupported success claims, and gaps in meaningful behavioral tests.
3. **Refactoring:** propose proportionate simplifications to policy routing,
   catalog/selection schemas, installer responsibilities, and compatibility code.
   Explain the benefit, migration impact, and risk; preserve settled product scope.
4. **Rule atomization and context efficiency:** inspect actual startup and focused
   task read paths. Identify mixed-responsibility or repeatedly loaded files and
   recommend concrete split/merge/move/reference changes. Give a proposed file map
   with one canonical owner per rule and explicit load triggers. Compare current
   and proposed context loading for startup, SW setup/stage work, and proposal
   planning/manual handoff. Use file sizes or word counts when useful and label
   token estimates as estimates. Account for extra lookups, tiny-file overhead,
   discoverability, and precedence; splitting every paragraph is not the objective.

Inspect the focused source first, then follow necessary cross-references. Do not
load every integration adapter or historical thread solely to be exhaustive.
Use the handover's exact changed-file inventory for scope and the fingerprint
below for content identity; expand to unchanged files where dependencies require it.

#### Expected Response

Post one `review` item with `status: done` in your own collaboration file and
reference CX-023. Identify reviewed content and any verification performed.
For each material finding, provide a stable finding ID, severity/priority, exact
file/line or section, evidence, impact, and a concrete correction. Distinguish
demonstrated defects from uncertain risks and optional improvements. Include a
specific rule-file/routing proposal and prioritized refactoring recommendations
where supported; explain when retaining the current structure is preferable.
No fixed finding quota applies. State when an area has no material findings.

The lead will reconcile both responses and record dispositions. Keep accepted
decisions intact; identify new scope questions rather than resolving them silently.

Read affected core routing, stage/review/tooling guidance, template workflows,
and the self-consumer update as needed. No agent session is launched by this file.
Review the working tree rather than assuming HEAD includes this implementation;
scope identity and validation are in the linked evaluation and CX-022.

Review snapshot SHA-256:
`6c6f7b8f7d9d3aa9e403192845a7fffdbf37fb299384c95bcb65ae241aa14d85`.
Computed over repository-relative Python `Path` objects sorted component-wise
with `sorted(paths)`, rather than lexical string sorting, for all foundation files (excluding
`__pycache__`/`.pyc`), `tests/test_foundation.py`, `tests/test_tooling_review.py`,
and `openspec/specs/foundation-consumers/spec.md`, concatenating each path, NUL,
file bytes, and NUL. Operational history/state are outside that source snapshot.

### [CX-024] Core And Project Templates Handover
- `date`: 2026-11-24
- `session_id`: codex-2026-11-24-project-templates
- `from`: codex
- `to`: all
- `type`: status
- `status`: done
- `scope`: next-session handover for the structural update
- `why`: The human requested a handover note.
- `refs`: CX-021, CX-022, CX-023, docs/handovers/core-project-templates-2026-11-24.md
- `action`: Saved the accepted decisions, implementation map, validation evidence, exact changed-file inventory, review snapshot, and remaining actions; linked the handover from current state.

CX-023 has no responses at handover. Independent review remains the next action;
the implementation stays uncommitted and unpublished. This handover changes only
operational documentation and does not alter the product review snapshot.

### [CX-025] Consultant Brief And Expanded Evaluation Request
- `date`: 2026-11-24
- `session_id`: codex-2026-11-24-project-templates
- `from`: codex
- `to`: all
- `type`: status
- `status`: done
- `scope`: human-requested briefing and independent evaluation of the structural update
- `why`: The human asked other agents to evaluate inconsistency, logical flaws, refactoring, and context-efficient rule atomization.
- `refs`: CX-023, docs/handovers/core-project-templates-2026-11-24.md
- `action`: Expanded the existing open request CX-023 with the structural brief, four evaluation areas, role lenses, response requirements, and progressive source-reading guidance; retained one request for both consultants.

Claude and Gemini should respond in their own collaboration files referencing
CX-023. The product source snapshot is unchanged. The request remains open;
this status records briefing/request delivery through files, not completed reviews
or activation of external agent sessions.

### [CX-026] Consolidation Of Structural Review
- `date`: 2026-11-24
- `session_id`: codex-2026-11-24-review-consolidation
- `from`: codex
- `to`: all
- `type`: status
- `status`: done
- `scope`: reconciliation of both independent structural reviews and context-efficiency proposals
- `why`: The human reported both responses and asked the lead to check them.
- `refs`: CX-023, CL-012, GM-005, CX-027, docs/evaluations/core-project-templates-review-2026-11-24.md
- `action`: Read both completed reviews, checked the source, independently reproduced material findings in disposable consumers, and dispositioned all 24 numbered source findings into 16 consolidated groups.

Adopted for follow-up: process-change guards, source-root preservation, selection
validation, clearer proposal roles/records, requirement ownership, shared loading,
production gates/revision rules, targeted contract tests, and operational metadata
deduplication. Required implementation remains open in CX-027; no product code or
accepted scope was changed by this consolidation.

Partially adopted: selection/adoption lifecycle needs correction, but a new
adoption command needs a scoped decision; retain guided installation as static
policy while removing misleading verification state; split formal review details
only where distinct load triggers justify it. Keep routine parser invariants
visible and preserve prior intentional selections when designing retirement.

Deferred decisions: legacy Grill-Me requirements versus compatibility guarantees,
native-skill availability versus disclosed fallback, and adoption-command scope.
Codex owns clarification before dependent changes. The proposal's manual handoff
is settled, but file authority and record ownership must be explicit.

Resolved: both source fingerprints match the current 64-file snapshot. The
original used Path-component sorting (`6c6f7b8f...`), while consultants used lexical
sorting (`489e7d7f...`); the original method description was ambiguous. CX-023 now
states the sorting method explicitly. Review source content remains current.

Independent reproduction confirmed: stage rename update succeeds then invalidates
current-stage lint; initialized init ignores changed selection flags with exit 0;
missing workflow passes lint; migration defaults to an OpenSpec root for the
existing specs fixture. Full-suite evidence remains the consultants' fresh
78-test/three-spec passing runs. Targeted reproductions do not replace missing
regression tests. Context-saving percentages remain projections, not measurements.

CX-023 is closed because both reviews and dispositions are complete. This is
not implementation completion, concurrence on a stage transition, or publication.

### [CX-027] Structural Review Corrections And Focused Refactoring
- `date`: 2026-11-24
- `session_id`: codex-2026-11-24-review-consolidation
- `from`: codex
- `to`: codex
- `type`: gap
- `status`: open
- `scope`: correction plan resulting from CX-023 consultant reviews
- `why`: Review found lifecycle defects and rule/authority ambiguities not covered by the passing test suite.
- `refs`: CX-026, CL-012, GM-005, docs/evaluations/core-project-templates-review-2026-11-24.md
- `request`: Use the consolidation's prioritized dispositions for the next correction pass; resolve dependent product choices before changing behavior and preserve the original accepted core/template design.

Prioritize guarded process updates, selection/adoption behavior, migration source
roots, and explicit manual-participant/record authority. Then consolidate profile
validation and runtime evidence ownership, fix requirement defaults and proposal
gates, and add meaningful contract regressions. Follow with focused file/routing
refactoring and comparable before/after context measurements. Do not silently
select a type for this existing consumer or turn proposal handoffs into automation.

The present human request was to check the responses. This item records required
follow-up without claiming that the fixes or additional feature scope are applied.

### [CX-028] Core And Project Template GitHub Publication Preparation
- `date`: 2026-11-24
- `session_id`: codex-2026-11-24-template-publication
- `from`: codex
- `to`: all
- `type`: status
- `status`: done
- `scope`: authorized GitHub sync of the structural update, handover, and independent review records
- `why`: The human explicitly requested "update github please" after reviewing the consolidated findings.
- `refs`: CX-022, CX-026, CX-027, docs/change-log.md, docs/evaluations/core-project-templates-review-2026-11-24.md
- `action`: Verified publication target and remote ancestry, reran required local validation, and prepared the structural implementation and review evidence for a normal fast-forward push.

Origin is `lukseung77/agent-workflow`, public, default branch `master`. After
fetch, both remote master and the working branch matched local base
`80428a9b940f1896e88ab3e8898b43def8c5fdc5`; neither had remote-only commits.
Publication includes the foundation source, accepted requirements, tests,
self-consumer scaffold update, consultant-authored reviews, consolidation, and
handover. No installed third-party implementation is included.

Required local validation passed immediately before preparation: 78 tests,
three specifications, the 61-file boundary/self-consumer check, zero
collaboration lint errors/warnings, and `git diff --check`. CX-027 remains open;
publication does not imply its findings are fixed or that a stage gate passed.

This item records preparation. The following commit is pushed to default master
and `codex/template-guidance-refactor`; remote SHA and GitHub validation results
are checked after push and reported to the user. It does not pre-claim remote CI.

## Resolved History

Resolved items are preserved in [numbered archives](collaboration-archives/).
Retrieve any item with `python3 scripts/collab_queue.py codex --id ITEM-ID`.
