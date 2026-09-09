# Product Spec

## Product

Axiom Atlas is a discovery and recommendation platform for mathematical software, papers, algorithms, repositories, and research communities.

## Core Goals

- Support explainable search and recommendation flows grounded in graph relationships.
- Preserve provenance on imported and inferred facts.
- Support both beginner-friendly exploration and technically precise metadata inspection.
- Keep 3D graph exploration optional rather than mandatory.

## Phase 1 Scope

- Monorepo foundation with web, API, worker, and ML services.
- Local fixture aligned with the production graph schema.
- Search, entity detail, community detail, and recommendation views.
- Docker Compose stack with service health checks.

## Deferred Scope

- Live source ingestion from Zenodo and zbMATH.
- Persistent user accounts, collections, and workspaces.
- Neo4j-backed graph queries and OpenSearch hybrid ranking.
- Heterogeneous GNN training and evaluation.
