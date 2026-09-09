from __future__ import annotations

from dataclasses import dataclass
from typing import Any

from axiom_atlas_core.models import GraphDataset
from axiom_atlas_core.settings import settings
from axiom_atlas_core.sources.zenodo import ZenodoAdapter
from axiom_atlas_core.storage.neo4j_store import Neo4jStore
from axiom_atlas_core.storage.object_store import ObjectStore
from axiom_atlas_core.storage.postgres import (
    get_checkpoint,
    list_ingestion_jobs,
    set_checkpoint,
    start_ingestion_job,
    store_raw_record,
    update_ingestion_job,
)
from axiom_atlas_core.storage.search_store import SearchStore


@dataclass
class IngestionResult:
    job_id: str
    records_fetched: int
    records_normalized: int
    records_failed: int
    checkpoint: dict[str, Any]
    dataset: GraphDataset


class ZenodoIngestionService:
    def __init__(self) -> None:
        self.adapter = ZenodoAdapter()
        self.object_store = ObjectStore()
        self.neo4j = Neo4jStore()
        self.search = SearchStore()

    def run(self) -> IngestionResult:
        checkpoint = get_checkpoint(self.adapter.source_name)
        start_page = int(checkpoint.get("page", 1))
        job_id = start_ingestion_job(self.adapter.source_name)
        current_page = start_page
        total_fetched = 0
        total_normalized = 0
        total_failed = 0
        latest_dataset = GraphDataset(
            generated_at="",
            dataset_name="Zenodo Software Ingestion",
            dataset_version="0",
            nodes=[],
            edges=[],
        )

        try:
            while current_page and current_page <= settings.zenodo_max_pages:
                page = self.adapter.fetch_page(page=current_page)
                total_fetched += len(page.records)
                for record in page.records:
                    source_record_id = str(record.get("id"))
                    storage_key = f"{settings.raw_payload_prefix}/page-{current_page}/{source_record_id}.json"
                    storage_uri = self.object_store.put_json(storage_key, record)
                    store_raw_record(
                        self.adapter.source_name,
                        source_record_id,
                        storage_uri,
                        record,
                    )

                latest_dataset = self.adapter.normalize_records(page.records)
                total_normalized += len(latest_dataset.nodes)
                self.neo4j.upsert_dataset(latest_dataset)
                self.search.index_nodes(latest_dataset.nodes)
                checkpoint = {"page": current_page + 1}
                set_checkpoint(self.adapter.source_name, checkpoint)

                if page.next_page is None:
                    break
                current_page = page.next_page

            update_ingestion_job(
                job_id,
                status="completed",
                records_fetched=total_fetched,
                records_normalized=total_normalized,
                records_failed=total_failed,
                checkpoint=checkpoint,
            )
            return IngestionResult(
                job_id=job_id,
                records_fetched=total_fetched,
                records_normalized=total_normalized,
                records_failed=total_failed,
                checkpoint=checkpoint,
                dataset=latest_dataset,
            )
        except Exception as exc:
            total_failed += 1
            update_ingestion_job(
                job_id,
                status="failed",
                records_fetched=total_fetched,
                records_normalized=total_normalized,
                records_failed=total_failed,
                checkpoint=checkpoint,
                error_message=str(exc),
            )
            raise


def list_ingestion_jobs_view() -> list[dict[str, Any]]:
    return list_ingestion_jobs()
