# Data Model

## Canonical Node Types

- `software`
- `paper`
- `algorithm`
- `community`
- `repository`

## Canonical Fields

Each node includes:

- `id`
- `type`
- `title`
- `summary`
- `url`
- `tags`
- `metadata`
- `provenance`

Each edge includes:

- `id`
- `source`
- `target`
- `type`
- `evidence`
- `confidence`

## Current Storage Split

- Neo4j: planned canonical graph store
- PostgreSQL: planned application and audit data
- OpenSearch: planned search and autocomplete indexes
- MinIO: planned raw payloads, snapshots, and artifacts
- Local fixture JSON: current Phase 1 seed dataset
