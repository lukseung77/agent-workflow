# MarkItDown For Agent Context

Use MarkItDown when source material is bulky or agent-unfriendly and the goal is to extract readable Markdown for review, summarization, or source-of-truth updates with lower token consumption.

Reference: https://github.com/microsoft/markitdown

## Good Fits

- PDFs, DOCX, PPTX, XLSX, HTML, email, ZIP, EPUB, audio transcripts, and other large external inputs
- product briefs, contracts, reports, exported tickets, design notes, or planning documents
- one-time conversion before asking agents to inspect or summarize content
- preprocessing even when an agent can read the binary directly, if the converted Markdown will reduce repeated context loading

## Basic Use

Install in an isolated environment:

```sh
python -m venv .venv
source .venv/bin/activate
pip install 'markitdown[all]'
```

Convert a file:

```sh
markitdown source.pdf -o source.md
```

Use narrower optional dependencies when possible:

```sh
pip install 'markitdown[pdf,docx,pptx,xlsx]'
```

## Workflow Placement

1. Keep the original document in the project if licensing and privacy allow.
2. Convert it to Markdown in a references or imports folder.
3. Ask the lead agent to summarize only the decision-relevant content.
4. Move confirmed decisions into source-of-truth files.
5. Link back to the converted Markdown for traceability.

## Token Discipline

- Do not paste full converted documents into chat by default.
- Ask agents to read sections by heading or line range when possible.
- Summarize large conversions into a short extraction note.
- Treat converted Markdown as source material, not automatically accepted requirements.
- Use direct binary reads, OCR, or cloud extraction only for spot checks or when local conversion misses decision-relevant content.
