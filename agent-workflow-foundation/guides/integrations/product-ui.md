# Product Flow And UI Integrations

Apply `workflow/tooling.md` for the common lifecycle. Select tools
by product need; a source-only or CLI product may require none of these.

| Registry ID | Setup and trigger | Representative verification | Fallback / retirement |
|---|---|---|---|
| `wireflow-review` | Install the upstream skill and its required resources using the origin's current setup guide when navigation/state flows are unsettled. | Render one critical path and a cancel/back/retry path. Distinguish brief requirements from proposed screens; put accepted decisions in specs. Record output location and source revision. | Use a simple flow diagram. Generated wireframes do not become a second source of requirements. |
| `astryx` | Add the official component packages to a compatible application using its package manager. Check current React peer requirements and beta maturity against existing components before choosing it. | Build a representative form/dialog with project tokens; check keyboard interaction, mobile layout, production build, and dependency compatibility. Commit application lockfile changes deliberately. | Keep the existing design system or use accessible native components. Remove application dependencies only after replacing their usages. |
| `anti-ui-slop` | Install the selected free skill from uizze/uizze for a UI direction/finish review. Its authenticated MCP is a separate optional service selection. | Review a real screen against product goals, existing tokens, responsive states, and usability. Inspect rendered changes rather than accepting style labels as evidence. | Ordinary design review. Disable only selected skills or MCP settings; no paid reference service is required for the free skill. |
| `unslop` | Install the selected upstream skill/plugin for a focused redesign of an existing screen, checking attribution terms. Prefer one aesthetic reviewer for the task. | Compare before/after screens and verify functionality, brand fit, keyboard use, and reduced motion. Use existing browser tooling; do not activate optional image/story-video generation as part of ordinary UI review. | Targeted manual refinement. Remove only the installed skill/plugin and separately recorded configuration. |
| `web-design-guidelines` | Install only this skill from vercel-labs/agent-skills for implementation review. Inspect the current upstream guideline source when running it. | Review affected UI files and confirm actionable findings in a rendered screen, including keyboard, responsive, loading, empty, and error behavior. | Use project accessibility/usability checks. Do not claim source review alone certifies conformance. |
| `21st-mcp` | Follow the current 21st MCP setup linked by the Magic MCP origin. Configure the selected host and account with explicit service scope; avoid a new legacy proxy by default. | Discover actual tools, retrieve a suitable component/reference, inspect terms and dependencies, and build/test any adopted code in the application. Record endpoint/client and service constraints. | Reuse local components or primary examples. Remove only its MCP entry; account/subscription retirement is separate. |

Use Wireflow Review for behavior before aesthetic refinement. Astryx is an
application dependency, while 21st MCP is a service; they are not interchangeable
prompt skills. Anti-UI Slop and unslop are alternatives for the primary aesthetic
pass; Web Design Guidelines has a separate implementation-review role.
Anatomy, Diorama, Line Art Animation, and Canvas Design are outside this integration set.
