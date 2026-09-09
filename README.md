# Axiom Atlas

Axiom Atlas is a mathematical software discovery platform built as a monorepo with a Next.js frontend, Python backend services, shared graph-domain logic, and local infrastructure managed by Docker Compose.

## Status

As of August 4, 2026:

- Phase 1 foundation is complete
- Phase 2 Zenodo ingestion and backend persistence are implemented
- Early Phase 3 search and detail-product surfaces are implemented
- A live Docker-networked Zenodo ingestion run has been executed successfully against Postgres, Neo4j, OpenSearch, and MinIO-compatible storage

## Implemented Platform

This repository now contains:

- `apps/web`: Next.js application shell with discovery, atlas, software, community, and workspace pages
- `apps/api`: FastAPI service for health, search, graph neighborhoods, and sample entity APIs
- `apps/worker`: background ingestion worker foundation with Redis-backed task stubs
- `apps/ml-service`: FastAPI service exposing explainable baseline recommendations
- `packages/python`: shared domain models, fixture loading, graph queries, search, and recommendations
- `packages/python/src/axiom_atlas_core/sources/zenodo.py`: live Zenodo source adapter
- `packages/python/src/axiom_atlas_core/storage/*`: Postgres, Neo4j, OpenSearch, and object-storage integration
- `packages/*`: frontend shared packages
- `data/fixtures`: local schema-aligned seed dataset
- `docker-compose.yml`: local development platform with Postgres, Neo4j, Redis, OpenSearch, MinIO, and app services

## Quick Start

1. Copy `.env.example` to `.env`.
2. Install JavaScript dependencies with `pnpm install`.
3. Install Python dependencies with `python -m pip install -e .[dev]`.
4. Start the frontend locally with `pnpm --filter @axiom-atlas/web dev`.
5. Start the API locally with `uvicorn axiom_atlas_api.main:app --reload --app-dir apps/api/src`.
6. Start the full stack with `docker compose up --build`.

To run a Zenodo sync through the API after the backend services are up:

- `POST /v1/admin/ingestion/zenodo/sync`
- `GET /v1/admin/ingestion/jobs`

## Verification Commands

- `pnpm lint`
- `pnpm typecheck`
- `pnpm test`
- `pytest`
- `docker compose config`

## Notes

- The fixture dataset still exists as a fallback path, but the backend can now ingest and serve real Zenodo-backed records.
- The current Zenodo query is intentionally conservative but still imperfect for mathematical-software-only relevance.
- Human-only actions and later source integrations are tracked in `HUMAN_ACTIONS.md`.
