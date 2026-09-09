install:
	pnpm install
	python -m pip install -e .[dev]

dev:
	pnpm --filter @axiom-atlas/web dev

api:
	uvicorn axiom_atlas_api.main:app --reload --app-dir apps/api/src

ml:
	uvicorn axiom_atlas_ml.main:app --reload --app-dir apps/ml-service/src --port 8100

worker:
	dramatiq axiom_atlas_worker.tasks

test:
	pnpm test
	pytest

lint:
	pnpm lint
	ruff check .

typecheck:
	pnpm typecheck

compose:
	docker compose up --build
