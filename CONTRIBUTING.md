# Contributing

## Setup

1. Copy `.env.example` to `.env`.
2. Run `pnpm install`.
3. Run `python -m pip install -e .[dev]`.
4. Start services with `docker compose up --build` or use the `Makefile` targets.

## Validation

- `pnpm lint`
- `pnpm typecheck`
- `pnpm test`
- `pytest`

## Rules

- preserve provenance on transformed data
- avoid merging entities on names alone
- keep graph logic out of presentation components
