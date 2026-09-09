# Graph Schema

## Supported Relationships in Phase 1

- `(Paper)-[:USES_SOFTWARE]->(Software)`
- `(Software)-[:IMPLEMENTS]->(Algorithm)`
- `(Software)-[:MEMBER_OF]->(ResearchCommunity)`
- `(Software)-[:HAS_REPOSITORY]->(Repository)`
- `(Paper)-[:ASSOCIATED_WITH]->(ResearchCommunity)`

## Required Relationship Metadata

- source provenance
- evidence string
- confidence
- retrieval timestamp
- imported versus inferred status

## Expansion Path

Later phases extend the schema with:

- `CITES`
- `CLASSIFIED_AS`
- `DEPENDS_ON`
- `RELATED_TO`
- `AUTHORED`
- `LICENSED_UNDER`
