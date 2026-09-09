FROM python:3.10-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY pyproject.toml README.md ./
COPY packages/python ./packages/python
COPY apps/worker ./apps/worker
COPY data ./data

RUN pip install --no-cache-dir -e .

CMD ["dramatiq", "axiom_atlas_worker.tasks"]
