# Reference And Discovery Integrations

Use `workflow/tooling.md` for installation/inventory lifecycle and
`workflow/markitdown.md` for reference-conversion handling.

| Registry ID | Setup and trigger | Representative verification | Fallback / retirement |
|---|---|---|---|
| `markitdown` | Install the official package with only the extras required by incoming document types. Use when a bulky external reference needs searchable text. | Convert a sample document; compare headings, meaningful tables, and extracted values with its source. Record converter version, source identity, and output location. Extraction is not visual-layout verification. | Read the source with an appropriate document tool. Remove generated extracts only when reproducible and no longer referenced. |
| `context7` | Configure the current official MCP/client integration when library APIs need version-specific documentation. Select access credentials/service scope explicitly; preserve existing MCP settings. | Resolve the actual project library/version, retrieve a focused answer, inspect its cited source, and check an example against the installed API. Record client/endpoint and verification date; do not invent a hosted server version. | Use official library documentation directly. Remove only the selected MCP entry and separately retire credentials if appropriate. |
| `find-skills` | Install only the discovery skill from vercel-labs/skills through its supported host installer when the curated integrations leave a concrete gap. | Verify host discovery and search for one named capability. Inspect the returned candidate's official origin, dependencies, and compatibility before selecting it. | Search primary sources manually. Discovery results do not install or authorize a candidate. Remove the discovery skill independently of any later selected skill. |

Do not send private repository content to a documentation/discovery service
when a library name and focused query suffice. Keep primary references and
accepted requirements authoritative over retrieved summaries. SkillSpector
inspection, when useful for a candidate, is routed through
`guides/integrations/security.md` rather than treating search ranking as trust.
