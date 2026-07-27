# Diagrams

Use this file only when a user asks for diagrams or a project-local rule requires diagram artifacts.

## Sequence Diagrams

- If the user explicitly asks for a sequence diagram, use PlantUML sequence-diagram syntax as the default source format and rendering engine.
- Reference syntax: `https://plantuml.com/en/sequence-diagram`.
- The user may override the diagram format or rendering engine.
- Store diagram source as a durable source-of-truth artifact when it describes confirmed behavior.
- Project-local files should define any required diagram naming, stage placement, or mandatory diagram rules.
