# Grill Me Integration

Grill Me is the foundation's supported upstream skill for an explicitly
requested assumption-challenging interview. Recommend it during project setup
when interactive planning is wanted. Its origin and dependencies are recorded
in `third-party/origins.json`; install upstream files in the consuming project,
never inside the foundation product. Catalog inclusion is not installation.

## Skill-Specific Setup

Use `workflow/tooling.md` for the common lifecycle. Install
`skills/productivity/grill-me` and `skills/productivity/grilling` from the same
reviewed revision of the registry origin. Verify the wrapper and dependency are
discoverable in the selected host. Hosts without the wrapper's Skill API load the
installed `grilling/SKILL.md` directly. Record actual invocation separately from
download success. `grill-with-docs` has additional dependencies and is a separate
selection. Do not edit upstream files to implement foundation pacing.

## Interview Behavior

When the user asks to be grilled about a plan, idea, or design, use the installed
skill with the following foundation integration rules:

- `workflow/question-model.md` owns interview pacing and evidence-based question
  selection, adapting upstream multi-question rounds without modifying them.
- Existing project authority governs research and delegation. A skill grants no
  additional permissions.
- Confirm expressly requested interview conclusions before dependent implementation;
  independent authorized work continues without a new interview approval gate.
- Use the host's actual invocation syntax or plain-language trigger. If the
  upstream skills are unavailable, follow `workflow/question-model.md` and say
  that foundation guidance is being used, rather than claiming a native skill ran.

These are first-party integration rules. The upstream implementation remains
unmodified and separately installed; project-local restrictions can specialize
this integration using the ordinary precedence rules.
