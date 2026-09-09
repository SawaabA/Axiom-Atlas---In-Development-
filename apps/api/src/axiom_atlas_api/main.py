from __future__ import annotations

from typing import Any

import httpx
from fastapi import FastAPI, HTTPException, Query

from axiom_atlas_api.settings import settings
from axiom_atlas_core.ingestion import ZenodoIngestionService, list_ingestion_jobs_view
from axiom_atlas_core.recommender import recommend_related_software
from axiom_atlas_core.repository import get_repository

app = FastAPI(
    title="Axiom Atlas API",
    version="0.1.0",
    summary="Search, graph, and entity APIs for mathematical software discovery.",
)


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok", "service": "api"}


@app.get("/v1/summary")
def summary() -> dict[str, Any]:
    return get_repository().summary()


@app.get("/v1/search")
def search(q: str = Query(..., min_length=2), entity_type: str | None = None) -> dict[str, Any]:
    results = get_repository().search(q, entity_type=entity_type)
    return {"query": q, "results": [result.model_dump() for result in results]}


@app.get("/v1/software")
def list_software() -> dict[str, Any]:
    software = get_repository().list_nodes_by_type("software")
    return {"items": [node.model_dump() for node in software]}


@app.get("/v1/software/{software_id:path}")
def get_software(software_id: str) -> dict[str, Any]:
    node = get_repository().get_node(software_id)
    if not node or node.type != "software":
        raise HTTPException(status_code=404, detail="Software not found")
    return node.model_dump()


@app.get("/v1/software/{software_id:path}/recommendations")
async def software_recommendations(software_id: str) -> dict[str, Any]:
    repository = get_repository()
    node = repository.get_node(software_id)
    if not node or node.type != "software":
        raise HTTPException(status_code=404, detail="Software not found")

    if settings.ml_service_url:
        try:
            async with httpx.AsyncClient(timeout=5.0) as client:
                response = await client.get(
                    f"{settings.ml_service_url}/v1/recommend/software/{software_id}"
                )
                response.raise_for_status()
                return response.json()
        except httpx.HTTPError:
            pass

    return {
        "source": software_id,
        "results": [item.model_dump() for item in repository.recommend_software(software_id)],
        "provider": "api-fallback",
    }


@app.get("/v1/communities")
def list_communities() -> dict[str, Any]:
    communities = get_repository().list_nodes_by_type("community")
    return {"items": [node.model_dump() for node in communities]}


@app.get("/v1/communities/{community_id:path}")
def get_community(community_id: str) -> dict[str, Any]:
    node = get_repository().get_node(community_id)
    if not node or node.type != "community":
        raise HTTPException(status_code=404, detail="Community not found")
    return node.model_dump()


@app.get("/v1/graph/neighborhood/{node_id:path}")
def neighborhood(node_id: str, limit: int = Query(default=12, ge=1, le=100)) -> dict[str, Any]:
    neighborhood_result = get_repository().get_neighborhood(node_id, limit=limit)
    if neighborhood_result is None:
        raise HTTPException(status_code=404, detail="Node not found")
    return neighborhood_result.model_dump()


@app.get("/v1/admin/ingestion/jobs")
def list_ingestion_jobs() -> dict[str, Any]:
    return {"items": list_ingestion_jobs_view()}


@app.post("/v1/admin/ingestion/zenodo/sync")
def run_zenodo_sync() -> dict[str, Any]:
    result = ZenodoIngestionService().run()
    return {
        "job_id": result.job_id,
        "records_fetched": result.records_fetched,
        "records_normalized": result.records_normalized,
        "records_failed": result.records_failed,
        "checkpoint": result.checkpoint,
        "dataset_version": result.dataset.dataset_version,
    }
