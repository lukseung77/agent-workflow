# Proposal PT Making — ChatGPT And Claude Manual Handoff

This initial template covers the full proposal presentation process. ChatGPT
handles RFP analysis and presentation planning; the user manually transfers the
approved slide instructions to Claude for PowerPoint production and returns
results for review. No cross-app session launch, plugin call, or automated
transfer is required or implied.

## Required Capabilities And Sources

- Core Grill-Me, including grilling, for requested clarification interviews.
- MarkItDown for the RFP and supporting document read-in, following
  `workflow/markitdown.md`. Preserve original sources, extraction caveats, and
  source references. Check tables, figures, and mandatory instructions against
  originals when extraction is incomplete; a conversion is not acceptance evidence.
- ChatGPT for requirement analysis, TOC planning, and per-slide instructions.
- The user's Claude PowerPoint plugin for producing slides. Its exact identity,
  official origin, host setup, and capabilities must be established during guided
  setup before slide production. Do not invent its name, installer, commands, or
  verified status. Planning may continue while this prerequisite is unresolved.

The default source root is `proposal/`. Keep the analysis, outline, slide brief,
review notes, and output locations indexed there and in project facts. Converted
references remain in the core reference location. OpenSpec and GitHub are not
required by this template. Additional capabilities depend on actual project gaps.

## Stages And Gates

These are initial template defaults, refined through project-local rules when the
real RFP or production workflow requires it. They do not inherit SW stage gates
or require concurrence from a fixed agent roster.

1. **RFP Analysis:** ChatGPT extracts objectives, audience, deliverables,
   evaluation criteria, submission constraints, and mandatory requirements.
   Produce a requirement matrix linking source locations to planned responses;
   distinguish source requirements, user decisions, assumptions, and missing data.
   Gate: the user confirms the interpretation and resolves material ambiguities.
2. **TOC Planning:** ChatGPT develops the proposal narrative, TOC, sequence, and
   a complete brief for every slide using the handoff format below.
   Gate: the user approves the outline and slide briefs; mandatory requirements
   have coverage or an explicit unresolved gap. Clearly mark unsupported claims.
3. **Slide Creation:** the user transfers the approved brief and necessary
   reference assets to Claude and uses the PowerPoint plugin to create a draft.
   Return the draft and production questions/limitations manually.
   Gate: the produced deck corresponds to the approved brief, is available for
   inspection, and omissions or deviations are recorded before final review.
4. **Final Review:** compare the rendered deck with the requirement matrix,
   approved narrative, and slide briefs. Check factual accuracy, evidence,
   consistency, readability, diagrams, layout, slide count, and RFP constraints.
   Send focused revision instructions back through the same manual handoff.
   Gate: material gaps are resolved and the user accepts the final deliverable.
   Save the editable PowerPoint and any additional formats actually required.

Record stage outcomes and the next owner in collaboration files and current
state. Returning a deck or transferring a file does not establish approval.
Human submission/publication is separate from deck acceptance. Freshness reviews
run on explicit requests; this template adds no automatic stage-review trigger.

## Manual Handoff Contract

Use `templates/project-types/proposal-pt-making/slide-handoff.md` for the actual
brief stored under the project's source root. It includes the TOC, slide IDs,
titles, key messages, content, and drawing/layout prompts. Link each mandatory
requirement and factual claim to its source or mark it as needing evidence.

Label each handoff with its revision, approval state, source references, expected
output, sender, recipient, and pending questions. The user transfers the approved
version; later revisions identify changed slide IDs. Claude's returned deck must
identify the brief revision used, deviations, and unresolved questions so ChatGPT
can review the actual result. Maintain one accepted brief and preserve decision
history. The same format supports targeted corrections without resending all
source documents.
