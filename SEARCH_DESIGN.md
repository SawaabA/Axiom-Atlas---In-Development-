# Search Design

## Current Phase 1 Search

- lexical title, tag, summary, and metadata matching
- API endpoint: `/v1/search`
- fixture-backed fallback for frontend rendering

## Intended Hybrid Ranking

Later phases combine:

- BM25
- semantic embeddings
- graph proximity
- community overlap
- repository quality indicators
- user preferences

## Query Interpretation

The UI is structured for removable chips even though the full natural-language query parser is not yet implemented.
