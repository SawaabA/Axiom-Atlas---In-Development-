from fastapi import FastAPI, HTTPException

from axiom_atlas_core.repository import get_repository

app = FastAPI(
    title="Axiom Atlas ML Service",
    version="0.1.0",
    summary="Explainable baseline recommendations for mathematical software.",
)


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok", "service": "ml-service"}


@app.get("/v1/recommend/software/{software_id:path}")
def recommend_software(software_id: str) -> dict[str, object]:
    repository = get_repository()
    node = repository.get_node(software_id)
    if not node or node.type != "software":
        raise HTTPException(status_code=404, detail="Software not found")
    return {
        "source": software_id,
        "provider": "baseline-explainable",
        "results": [item.model_dump() for item in repository.recommend_software(software_id)],
    }
