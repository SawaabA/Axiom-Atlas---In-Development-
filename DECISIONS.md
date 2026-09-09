# Decisions

## 2026-08-04

- Adopted a polyglot monorepo with `pnpm` and Turborepo for frontend packages, and Python packaging for backend services.
- Chose FastAPI plus Dramatiq for clear service boundaries without committing to premature heavy orchestration.
- Used a documented local graph fixture to avoid fake UI while live-source ingestion is still incomplete.
- Kept the first atlas graph bounded and neighborhood-based to avoid a frontend architecture that assumes full-graph rendering.
- Chose Zenodo as the first real public source because it is accessible without credentials and exposes machine-consumable metadata through a stable public API.
- Implemented backend reads with a hybrid repository so the application can prefer real backend data while retaining fixture fallback during Phase 2 stabilization.
- Added a math-relevance filter on Zenodo software records because raw `resource_type.type:software` results are too broad for the product domain.
