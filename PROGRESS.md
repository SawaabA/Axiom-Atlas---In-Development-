# Progress

## Current Phase

Phase 2 complete and early Phase 3 in progress

## Completed

- repository scaffolded into web, API, worker, ML service, frontend packages, and shared Python core
- seed graph dataset added with typed nodes, edges, and provenance
- FastAPI endpoints added for health, summary, search, communities, software, recommendations, and graph neighborhoods
- worker and ML service foundations added
- homepage, discovery, atlas, software, community, and workspace routes created
- Docker Compose stack and CI workflow added
- Zenodo adapter added with live HTTP ingestion, math-relevance filtering, raw payload preservation, and normalization
- Postgres ingestion job/checkpoint/raw-record persistence added
- Neo4j graph upserts and OpenSearch indexing added
- backend-first repository layer added with fixture fallback
- search page, ingestion admin page, and provenance display added for early Phase 3 product usage
- live Docker-networked Zenodo sync executed on August 4, 2026 with 50 fetched records, 68 normalized backend nodes, 50 software nodes, 16 repository nodes, and 2 community nodes

## Passing Verification

- `pnpm lint`
- `pnpm typecheck`
- `pnpm test`
- `pytest`
- `docker compose config`
- `pnpm build`
- `docker compose run --build --rm --no-deps api ...ZenodoIngestionService().run()`

## Current Blockers

- Zenodo query relevance is improved but still broad; additional filtering or source enrichment is needed before claiming a high-quality mathematical-software corpus
- Full `docker compose up` is blocked on this machine by an unrelated service already binding Redis port `6379`
- Direct host-to-container Postgres password auth on this Windows environment was inconsistent, so live ingestion was validated on the Docker network instead

## Next Tasks

- refine mathematical-software relevance scoring and add paper extraction from Zenodo metadata where reliable
- expose backend search/entity results through a fully running local API and web stack
- add end-to-end tests for ingestion admin, search, and real entity detail flows
