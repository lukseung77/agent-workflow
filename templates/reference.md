# Reference Registry

Operational index for external reference files and MarkItDown conversions.

This file tracks file identity and conversion status. It is not product source of truth. Confirmed decisions belong in source-of-truth files.

## Rules

- Use SHA-256 hashes to identify file contents; do not rely on filenames alone.
- Store converted Markdown in `agent-workflow-local/references/markitdown/`.
- Any agent may update the row for a reference file it just inspected or converted.
- The lead agent owns registry cleanup, duplicate reconciliation, and canonical location tracking.
- Treat `_OLD` files as `obsolete` unless the user explicitly asks for old material.
- If a user request could refer to multiple files, ask which candidate they meant before using one.

## References

| Reference ID | Status | User label | Original path | Last seen path | Source SHA-256 | Source size | Source mtime | Markdown path | Markdown SHA-256 | MarkItDown version | Processed at | Notes |
|--------------|--------|------------|---------------|----------------|----------------|-------------|--------------|---------------|--------------------|--------------------|--------------|-------|
| REF-001 | active |  |  |  |  |  |  |  |  |  |  |  |
