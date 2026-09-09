# Deployment

## Local

- `docker compose up --build` starts the Phase 1 platform
- `Makefile` exposes common development commands

## Services

- web on `http://localhost:3000`
- api on `http://localhost:8000`
- ml-service on `http://localhost:8100`
- postgres on `localhost:5432`
- neo4j browser on `http://localhost:7474`
- opensearch on `http://localhost:9200`
- minio on `http://localhost:9001`

## Production Direction

Future deployment should split the app services from infrastructure, move secrets into a real secret manager, and use managed observability and backup tooling.
