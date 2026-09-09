FROM python:3.10-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY pyproject.toml README.md ./
COPY packages/python ./packages/python
COPY apps/ml-service ./apps/ml-service
COPY data ./data

RUN pip install --no-cache-dir -e .

CMD ["uvicorn", "axiom_atlas_ml.main:app", "--host", "0.0.0.0", "--port", "8100", "--app-dir", "apps/ml-service/src"]
