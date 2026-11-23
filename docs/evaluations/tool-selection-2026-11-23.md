# Product Tool Selection

Use this guide during setup, when a product requirement exposes a capability
gap, or when reviewing an installed tool update. It is a reference catalog,
not an always-loaded prompt or an instruction to install everything.
Machine-readable origins and activation triggers are in
`third-party/origins.json`. Recommendations are engineering judgments based on
the primary documentation reviewed on 2026-11-23; installation, runtime quality,
security, and host compatibility have not been certified by that review.
Recheck current upstream instructions before activation.

## Integration Status

All catalog entries except Anatomy, Diorama, Line Art Animation, Canvas Design,
OpenSEO, and VoiceStudio now have foundation-supported integration adapters.
Use `workflow/tool-integrations.md` to route setup, use, verification, updates,
and retirement to the appropriate focused guide. The excluded entries remain
reference-only; this request does not activate their optional media features
indirectly through another tool.

Integration support and the assessments below answer different questions:
conditional or deferred use still has a supported setup path, while its task
trigger remains selective. Support does not mean a tool is installed, required,
or runtime-verified in this project. Foundation updates never bulk-install them.

## Start From The Product

Use existing project and host capabilities first. For a typical web product,
consider this small set as needs arise:

| Activity | First choice | When an external capability helps |
|---|---|---|
| Clarify outcomes and challenge assumptions | `workflow/question-model.md`; supported Grill Me integration in `workflow/grill-me.md` | Use the installed upstream pair for an explicitly requested deeper interview; preserve foundation pacing. |
| Review screen transitions | Wireflow Review | Multiple screens, back/cancel/retry paths, or retained form state are unsettled. |
| Implement against a library | Official version-specific docs; Context7 if useful | An API is unfamiliar or current examples are needed. |
| Build UI | Existing components and tokens | Astryx is an option for a suitable new React product; component discovery is optional. |
| Check UI | Web Design Guidelines and the available browser | Add one aesthetic reviewer only when visual direction needs work. |
| Verify user journeys | Playwright for repeatable tests | Add critical-path tests to a web application; reuse the host browser or Agent Browser for interactive inspection. |
| Review security | Focused source review; Cloudflare guidance when helpful | Trust boundaries, authentication, sensitive data, or an explicit audit justify deeper checks. |
| Add a skill | Inspect its source and dependencies | SkillSpector can supplement that inspection before activation. |

These activities fit the existing Exploration, Proposal, and Implementation
stages. They add no stage, mandatory interview, or automatic approval gate.
A CLI/library-only product usually needs neither UI tooling nor a browser.
This foundation repository already has the questioning workflow; its catalog
work does not require installing browser, design, or media packages.

## Evaluation Of The Requested Options

**Recommended** means a useful capability to consider when its trigger occurs,
not enabled by default. **Conditional** means select only for a specific gap.
**Specialist** means a separate product or specialized deliverable justifies it.
**Deferred** means current defaults have a simpler fit; the listed trigger can
reopen the choice. **Needs confirmation** means the name alone does not establish
the intended project, so installation remains pending.

| # | Option and primary origin | Assessment and use condition |
|---|---|---|
| 1 | [Cloudflare security-audit](https://github.com/cloudflare/security-audit-skill) | Recommended for source-based security work. Guidance mode suits a focused question. Full audits require explicit scope and upstream sandbox and independent-agent prerequisites; do not silently turn every review into a full audit. |
| 2 | [Wireflow Review](https://github.com/JeongK7998/wireflow-review) | Recommended for multi-screen planning. Clickable low-fidelity flows expose missing steps before visual polish; accepted decisions still go into the project's specs. |
| 3 | [Floorplan](https://github.com/haydenschmitty/floorplan) | Conditional, especially for explaining an existing app to a nontechnical builder. Corrected `haydenschitty` to `haydenschmitty`. Overlaps Graphify's discovery role; choose a human-facing map or source-oriented index according to the task. |
| 4 | [Astryx](https://github.com/meta/astryx) | Conditional component library, not just a prompting skill. Current docs describe a beta React 19+ system. Assess compatibility and maturity before adopting; retain a suitable existing design system. |
| 5 | [Anatomy](https://github.com/wheresryan22/anatomy) | Specialist for interactive isometric technical illustrations. Useful for explanatory product visuals; not a general architecture review tool. |
| 6 | [Diorama](https://github.com/sloemo01/diorama) | Specialist for requested rotatable 3D scenes. The library is **Three.js**, presumably the intended “tree.js.” Consider mobile rendering, asset rights, and fallback behavior. |
| 7 | [ECC](https://github.com/affaan-m/ECC) | Conditional source of individual skills. Its broad harness, memory, hooks, and workflows overlap the foundation; a wholesale install would create competing conventions. |
| 8 | [Line Art Animation](https://github.com/JDhruv14/line-art-animation) | Specialist for SVG illustration and motion when the brief calls for it. Check reduced motion and performance rather than adding decorative animation by default. |
| 9 | [Grill Me / grilling](https://github.com/mattpocock/skills) | Recommended, with the supported setup and interview adapter in `workflow/grill-me.md`. Install the `grill-me` wrapper and `skills/productivity/grilling` dependency together. Foundation question pacing and authority govern the integration; `grill-with-docs` has additional dependencies and is not included by selecting this pair. |
| 10 | [Caveman](https://github.com/JuliusBrussee/caveman) | Deferred until measured verbosity/context cost needs more than concise output or RTK. Optional proxy configuration adds another integration surface. Never shorten executable code, contracts, or diagnostic evidence at the expense of correctness. |
| 11 | [Agent Browser](https://github.com/vercel-labs/agent-browser) / [Playwright](https://playwright.dev/docs/intro) | Playwright is recommended for repeatable web acceptance tests. Agent Browser is a conditional interactive driver when existing browser tooling is insufficient. Both can have distinct roles; neither is a compulsory duplicate of a working host browser. |
| 12 | [Find Skills](https://github.com/vercel-labs/skills/tree/main/skills/find-skills) | Conditional discovery when a concrete gap remains. Search results are candidates to inspect, not trusted installation recommendations. |
| 13 | [Anti-UI Slop](https://github.com/uizze/uizze) / [unslop](https://github.com/heydamir/unslop) | Conditional alternatives for product-grounded UI refinement. Corrected UIZZE origin. Start with one aesthetic reviewer; free UIZZE skills are separate from paid MCP services. unslop has attribution terms and optional browser/video/image dependencies. Preserve product identity and accessibility over stylistic preferences. |
| 14 | [Web Design Guidelines](https://github.com/vercel-labs/agent-skills/tree/main/skills/web-design-guidelines) | Recommended for web UI review. Complements rendered keyboard, responsive, and failure-state checks; it does not alone establish accessibility conformance. |
| 15 | [Canvas Design](https://github.com/anthropics/skills/tree/main/skills/canvas-design) | Specialist for static PNG/PDF compositions and visual assets. It is not an interactive app UI or HTML canvas development framework. |
| 16 | [OpenSEO candidate](https://github.com/every-app/open-seo) | Needs identity confirmation: multiple projects share this name. The candidate is an SEO platform; useful for search-led public products, with hosting and data/API costs to assess. Ordinary metadata and crawlability work can use existing tools. |
| 17 | [OpenProject](https://github.com/opf/openproject) | Specialist team project-management application. Integrate when the team uses it or needs its planning features; specify ownership of tasks and Git records to avoid competing queues. |
| 18 | [VoiceStudio candidate](https://github.com/debpalash/VoiceStudio) | Needs identity confirmation. The candidate is a local audio/voice production application, useful for voice products or media assets. Assess hardware, model storage, licenses, and deployment before adopting. |
| 19 | [AppFlowy](https://github.com/AppFlowy-IO/AppFlowy) | Specialist workspace application. Useful for a team's established knowledge workflow; it is not a necessary coding-agent dependency. Define documentation ownership and synchronization deliberately. |
| 20 | [SkillSpector](https://github.com/NVIDIA/SkillSpector) | Recommended capability when considering external skills or updates. Static and model-backed analyses have different prerequisites and costs; choose deliberately, triage findings, and retain source inspection. A scan is not proof of safety. |
| 21 | [Hookify](https://github.com/anthropics/claude-plugins-official/tree/main/plugins/hookify) | Conditional Claude Code hook authoring for repeated concrete problems. Review and test generated rules, preserve existing hooks, and document disable steps. Do not assume those hooks work in Codex or agy. |
| 22 | [Claude Code Setup](https://github.com/anthropics/claude-plugins-official/tree/main/plugins/claude-code-setup) | Conditional read-only automation recommender. For Codex and agy, use the foundation's existing setup and current native host facilities, assessing capabilities rather than claiming identical plugins exist. Recommendations and configuration are separate operations. |
| 23 | [Ralph Loop](https://github.com/anthropics/claude-plugins-official/tree/main/plugins/ralph-loop) | Deferred for bounded, testable tasks needing iterative repair. Require finite iterations/time/cost, cancellation, and a stagnation exit; the upstream unlimited default is unsuitable as a foundation default. Verify completion using real checks. |
| 24 | [commit-commands](https://github.com/anthropics/claude-plugins-official/tree/main/plugins/commit-commands) | Conditional Claude convenience plugin. Native git/gh already cover the portable need. Check each command's effects: commit, push/PR, and branch/worktree cleanup carry different authorization scopes. |
| 25 | [Addy Osmani Agent Skills](https://github.com/addyosmani/agent-skills) | Recommended source of selected engineering skills, not a mandatory bundle. Choose a specific interview, debugging, testing, or review skill and inspect dependencies/host support. Its `interview-me` option is a closer match to one-question pacing than exhaustive grilling. |
| 26 | [Context7](https://github.com/upstash/context7) | Recommended for current, version-specific library documentation when needed. Match the installed dependency, verify source references, and use official docs directly if unavailable. Check current service access limits. |
| 27 | [Magic MCP / 21st MCP](https://github.com/21st-dev/magic-mcp) | Conditional frontend component discovery/generation. Upstream now recommends **21st MCP**; Magic remains a compatibility proxy. Use the current upstream setup, assess account/subscription requirements, component terms, and design-system fit. |
| 28 | [Strix](https://github.com/usestrix/strix) | Specialist dynamic penetration testing. Use only for explicitly authorized targets/actions in an appropriate isolated environment with resource/model bounds. Ordinary source security review is the lighter starting point. |

## Activate A Selected Capability

1. Identify the product outcome and missing capability. Check existing host
   tools, dependencies, and local inventory before selecting another tool.
   Prefer one primary tool per overlapping role. Confirm ambiguous identities
   before installation; catalog candidates are not confirmed user selections.
2. Open the official origin and current install/license documentation. Resolve
   a current compatible release or commit, inspect the selected skill, required
   sibling skills, scripts, and configuration effects. SkillSpector is an
   optional inspection aid; unavailable scanning does not justify executing
   unreviewed code or claiming the bundle was scanned.
3. Follow existing installation and host-configuration opt-ins in
   `workflow/agent-tooling.md`. Prefer project scope when supported. Install
   outside foundation product source using the upstream-supported installer;
   do not copy third-party prompts or implementations into this distribution.
   Existing authorization applies; do not invent an extra approval round.
   Choose accounts, network/data exposure, paid services, model calls, and
   hardware prerequisites only as needed for the selected task.
4. Check the actual host supports discovery/invocation and any required hook,
   MCP transport, or sibling skill. Portable `SKILL.md` text does not make
   Claude slash commands and hooks portable. Recheck current native Codex/agy
   support rather than generating speculative configuration formats. Foundation
   `init` creates startup files; it does not install or certify host plugins.
5. Verify a small representative task and record evidence and exact local
   results in `agent-workflow-local/tooling.json`. Record a package version or
   Git revision, install scope, host, selected skill/dependencies, configuration
   locations (never credentials), and disable/uninstall instructions. For a
   hosted service, record endpoint/client identity and the verification date;
   do not invent a server version. Keep selected, installed, and verified states
   distinct. Use local rules for any deliberate project-specific adaptation.
6. Keep the tool only if it improves the intended outcome. When updating the
   foundation, new catalog entries remain inactive. When updating an installed
   tool, inspect upstream changes and rerun relevant verification; preserve local
   customizations and update actual inventory rather than silently taking a new
   prompt, hook, proxy, or workflow.

The environment bootstrap currently automates only its existing Ponytail,
Graphify, and RTK integrations. New catalog entries have `auto_install: false`;
they require the procedure above, not a generic bulk-install command. The local
inventory records actual consumer choices and observations; it is not a second
copy of the upstream candidate catalog.
