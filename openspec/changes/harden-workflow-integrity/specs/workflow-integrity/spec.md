## ADDED Requirements

### Requirement: Collaboration syntax integrity

Collaboration parsing SHALL recognize item headers and metadata only outside
fenced code and HTML comments, and SHALL read metadata only in an item's initial
field block. Level 1–3 headings SHALL end an item; deeper headings SHALL remain
body content.

#### Scenario: Example cannot change work state

- **WHEN** an item contains fenced headers or commented status fields
- **THEN** no example item appears and the item's header status remains authoritative

#### Scenario: Standing section survives archival

- **WHEN** a resolved item precedes a standing section heading
- **THEN** archival moves the complete item and retains the standing section

### Requirement: Reliable work discovery and review evidence

Queues SHALL compare timestamp instants, support the Gemini alias, and exclude
archives from active work. Lint SHALL warn on unknown agent names while allowing
explicit extensions. Formal completion checks SHALL use numbered archives for
review evidence.

#### Scenario: Timestamp offsets differ

- **WHEN** two active items use different timezone offsets
- **THEN** their displayed order follows actual newest-first chronology

#### Scenario: Review evidence has been archived

- **WHEN** a completed named review is moved to a numbered archive
- **THEN** completion checking still finds its evidence without making it active work

#### Scenario: Focused retrieval of completed review evidence

- **WHEN** an agent retrieves an item by ID or lists items referencing a request
- **THEN** lookup includes all live and numbered-archive items regardless of status
  or recipient, matches complete request IDs, and rejects ambiguous item IDs

#### Scenario: Routine archive threshold

- **WHEN** resolved content reaches the default twenty-thousand-byte threshold
- **THEN** archival is eligible while unresolved items and standing sections remain live

### Requirement: Honest and resilient optional tooling

Optional tooling SHALL distinguish shared adapter presence, unrequested agents,
and unknown plugin state. Initialization SHALL preserve user instruction text,
refresh valid managed blocks, reject malformed blocks, and continue independent
integrations after optional subprocess failures.

#### Scenario: One optional command fails to launch

- **WHEN** an optional CLI raises an OS error or times out
- **THEN** the report records a warning and independent tooling checks continue

#### Scenario: Workflow root changes

- **WHEN** initialization runs with a new workflow root and a valid existing block
- **THEN** the managed pointer updates and surrounding user text is preserved

### Requirement: Repeatable maintenance validation

Repository maintenance SHALL provide a single command for unit tests,
collaboration lint, and available OpenSpec validation without installing tools
or changing host configuration. CI SHALL require the OpenSpec check.

#### Scenario: Local OpenSpec is absent

- **WHEN** maintenance validation runs without the OpenSpec CLI
- **THEN** it explicitly reports the skipped check and fails only if that check was required
