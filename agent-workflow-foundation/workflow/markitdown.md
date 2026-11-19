# MarkItDown For Agent Context

Use MarkItDown when source material is bulky or agent-unfriendly and the goal is to extract readable Markdown for review, summarization, or source-of-truth updates with lower token consumption.

Reference: https://github.com/microsoft/markitdown

## Good Fits

- PDFs, DOCX, PPTX, XLSX, HTML, email, ZIP, EPUB, audio transcripts, and other large external inputs
- product briefs, contracts, reports, exported tickets, design notes, or planning documents
- one-time conversion before asking agents to inspect or summarize content
- preprocessing even when an agent can read the binary directly, if the converted Markdown will reduce repeated context loading

## Installation

Use the MarkItDown entry in `third-party/origins.json` and its current official
instructions. Select only needed document extras and record the actual installed
version in the consuming project's local tooling inventory.

## Workflow Placement

1. Keep the original document in the project if licensing and privacy allow.
2. Track the original document in `agent-workflow-local/references/reference.md`.
3. Convert it to Markdown in `agent-workflow-local/references/markitdown/`.
4. Ask the lead agent to summarize only the decision-relevant content.
5. Move confirmed decisions into source-of-truth files.
6. Link back to the converted Markdown for traceability.

## Reference Registry

Every project that uses MarkItDown keeps a registry at:

```text
agent-workflow-local/references/reference.md
```

The registry tracks original reference files and their converted Markdown outputs.
It is operational metadata, not product source of truth. Downstream agents may
update rows for references they inspect or convert; the lead owns cleanup and
conflict resolution. Project-specific restrictions follow the local rules.

Recommended compact columns:

| Field | Purpose |
|---|---|
| Reference ID | Stable ID such as `REF-001` |
| Status | `active`, `obsolete`, `missing`, or `stale` |
| User label | Human-friendly name or request phrase |
| Source path | Most recent verified source path |
| Source SHA-256 | Identity of the original contents |
| Markdown path | Converted Markdown path, if any |
| Markdown SHA-256 | Identity of the converted contents |
| Notes | Extraction caveats, prior paths, or useful conversion provenance |

Existing wider registries remain valid; migrate columns only when useful. Size,
mtime, converter version, and processing date are optional notes, not mandatory
startup data. Retain both hashes: the converted file can change independently
of its source.

Use hashes as the identity check. Do not rely on filename, extension, title, or location alone; users and other apps can rename, move, or alter files outside the agent workflow.

## Converted Markdown Location

Store all converted Markdown under:

```text
agent-workflow-local/references/markitdown/
```

Use names that include a source hash prefix or suffix:

```text
<source-stem>--<sha256-12>.md
```

If two files share a filename but have different hashes, keep both converted Markdown files. If a source file is moved but its hash matches a registry row, update the path fields instead of creating a duplicate reference.

## Read And Conversion Rules

- Before reading a reference file, check `agent-workflow-local/references/reference.md`.
- If a current conversion exists and both source and converted-content hashes match, read the converted Markdown first; otherwise mark it stale and recheck before decision work.
- If the source hash differs from the registry, mark the row `stale`, regenerate the Markdown, and update the row before using it for decision work.
- If the source file has never been processed and local conversion is appropriate, run MarkItDown, store the output in the converted Markdown folder, and record the source and Markdown hashes in the registry.
- If conversion fails or misses important content, record the failure or caveat in the registry and use a targeted fallback such as direct binary inspection, OCR, or a user question.
- Treat converted Markdown as source material, not confirmed requirements.

## Ambiguous User References

Users often name files approximately. When a user asks agents to reference a file:

1. Search active registry rows and active project files first.
2. Match by user label, filename stem, path fragments, document title, and hash-backed registry history.
3. If multiple active files plausibly match, list the candidates with paths and ask the user which one they meant.
4. Do not choose between plausible matches silently.

## Obsolete And Moved Files

Files under `_OLD` are obsolete by default unless the user explicitly asks for old or obsolete material.

- Do not read or convert `_OLD` files during normal reference lookup.
- Continue tracking discovered `_OLD` files in the registry with status `obsolete` when practical.
- If an active reference moves into `_OLD`, mark it `obsolete` and keep its last known hash and converted Markdown path.
- If no active match exists and an `_OLD` file may be relevant, ask the user before using it.

## Token Discipline

- Do not paste full converted documents into chat by default.
- Ask agents to read sections by heading or line range when possible.
- Summarize large conversions into a short extraction note.
- Use direct binary reads, OCR, or cloud extraction only for spot checks or when local conversion misses decision-relevant content.
