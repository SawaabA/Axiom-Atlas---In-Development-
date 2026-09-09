# Ingestion Plan

## Source Priority

1. Zenodo mathematical software dataset
2. ICMS-related community data
3. zbMATH Open API
4. GitHub repository enrichment
5. Software Heritage enrichment

## Adapter Contract

Every adapter must support:

- pagination
- retries with exponential backoff
- rate limiting
- checkpoints
- raw-response preservation
- schema validation
- idempotent normalization

## Current Phase

Phase 2 uses a live Zenodo adapter with:

- query-based record retrieval from `https://zenodo.org/api/records`
- raw JSON preservation to MinIO-compatible storage with filesystem fallback
- ingestion job and checkpoint persistence in Postgres
- canonical node and edge upserts into Neo4j
- entity indexing into OpenSearch

The current default query is:

- `resource_type.type:software AND (description:mathematical OR keywords:mathematics OR title:mathematical OR description:numerical OR description:algebra)`

This is a practical starting point, not a final relevance model.
