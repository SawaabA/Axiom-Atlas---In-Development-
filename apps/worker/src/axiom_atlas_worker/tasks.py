from __future__ import annotations

import json

import dramatiq
from dramatiq.brokers.redis import RedisBroker

from axiom_atlas_core.ingestion import ZenodoIngestionService
from axiom_atlas_core.repository import fixture_path, load_dataset
from axiom_atlas_worker.settings import settings


dramatiq.set_broker(RedisBroker(url=settings.redis_url))


@dramatiq.actor
def ingest_seed_dataset() -> dict[str, int | str]:
    dataset = load_dataset()
    output_path = fixture_path().resolve().parents[1] / "processed" / "last_ingestion_summary.json"
    output_path.parent.mkdir(parents=True, exist_ok=True)
    summary = {
        "dataset_name": dataset.dataset_name,
        "dataset_version": dataset.dataset_version,
        "node_count": len(dataset.nodes),
        "edge_count": len(dataset.edges),
    }
    output_path.write_text(json.dumps(summary, indent=2), encoding="utf-8")
    return summary


@dramatiq.actor
def ingest_zenodo_records() -> dict[str, int | str | dict[str, object]]:
    result = ZenodoIngestionService().run()
    return {
        "job_id": result.job_id,
        "records_fetched": result.records_fetched,
        "records_normalized": result.records_normalized,
        "records_failed": result.records_failed,
        "checkpoint": result.checkpoint,
    }
