# Defined Terms

Use this file when writing or reviewing project documents that reference formally defined domain terms.

## Rule

Any term that has been formally defined in the project's domain model or source-of-truth files is a **defined term**.

Whenever an agent refers to a defined term in collaboration files, exploration files, proposals, or other project documents, format it as:

```md
<span style="color: #0066cc">**TERM NAME**</span>
```

Rules:

- Use all capital letters for defined terms.
- Apply the format every time the term is used, not just on first use.
- Do not invent defined terms before the project has confirmed them in the domain model or source-of-truth files.
- When a new term is confirmed, add it to the domain model or equivalent source-of-truth file before using the format.

GitHub strips inline `style` attributes, so the color may not render there. The bold all-caps text still preserves the signal.

Example:

```md
The rider creates a <span style="color: #0066cc">**RIDE PLAN**</span> and attaches a <span style="color: #0066cc">**ROUTE PLAN**</span>.
```
