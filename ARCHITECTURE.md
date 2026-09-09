# Architecture

## Overview

Axiom Atlas uses a polyglot monorepo:

- `apps/web`: Next.js App Router frontend
- `apps/api`: FastAPI service for entity, graph, and search APIs
- `apps/worker`: Dramatiq-based background ingestion worker
- `apps/ml-service`: FastAPI recommendation service
- `packages/python`: shared graph-domain models and baseline algorithms
- `packages/*`: shared frontend packages for types, UI, configuration, and API access

## Data Flow

1. Source adapters download raw records into object storage or local `data/raw`.
2. Normalization maps source records into canonical graph entities and typed relationships.
3. The worker stores normalized artifacts and later loads them into Neo4j, PostgreSQL, OpenSearch, and MinIO.
4. The API exposes search, detail, and graph-neighborhood endpoints.
5. The ML service computes explainable baseline recommendations using graph-derived signals.
6. The frontend renders discovery, atlas, and detail pages using API-first fetches with fixture fallback during Phase 1.

## Phase 1 Design Decisions

- Shared domain logic is centralized in Python so the API, worker, and ML service cannot drift on schema assumptions.
- The frontend reads from the API when available but falls back to the fixture for local page rendering and tests.
- The initial graph view only renders focused neighborhoods and never assumes the full graph can fit client-side.
