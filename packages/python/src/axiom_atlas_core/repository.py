from __future__ import annotations

import json
from functools import lru_cache
from pathlib import Path

from axiom_atlas_core.models import GraphDataset, GraphNeighborhood, GraphNode, SearchResult
from axiom_atlas_core.recommender import recommend_related_software_from_nodes
from axiom_atlas_core.search import search_entities
from axiom_atlas_core.settings import settings
from axiom_atlas_core.storage.neo4j_store import Neo4jStore
from axiom_atlas_core.storage.search_store import SearchStore


def _root_dir() -> Path:
    return Path(__file__).resolve().parents[4]


def fixture_path() -> Path:
    return (_root_dir() / settings.fixture_data_path).resolve()


@lru_cache(maxsize=1)
def load_fixture_dataset() -> GraphDataset:
    with fixture_path().open("r", encoding="utf-8") as handle:
        payload = json.load(handle)
    return GraphDataset.model_validate(payload)


def load_dataset() -> GraphDataset:
    return load_fixture_dataset()


def node_index() -> dict[str, GraphNode]:
    dataset = load_fixture_dataset()
    return {node.id: node for node in dataset.nodes}


class Repository:
    def __init__(self) -> None:
        self.neo4j = Neo4jStore()
        self.search_store = SearchStore()

    def _backend_enabled(self) -> bool:
        return settings.data_backend in {"backend", "hybrid"}

    def summary(self) -> dict[str, object]:
        if self._backend_enabled():
            try:
                counts = self.neo4j.summary_counts()
                if counts:
                    return {
                        "dataset": "Zenodo Software Ingestion",
                        "version": "backend",
                        "generated_at": "live",
                        "counts": counts,
                        "provider": "backend",
                    }
            except Exception:
                pass

        dataset = load_fixture_dataset()
        counts: dict[str, int] = {}
        for node in dataset.nodes:
            counts[node.type] = counts.get(node.type, 0) + 1
        return {
            "dataset": dataset.dataset_name,
            "version": dataset.dataset_version,
            "generated_at": dataset.generated_at,
            "counts": counts,
            "provider": "fixture",
        }

    def search(self, query: str, entity_type: str | None = None) -> list[SearchResult]:
        if self._backend_enabled():
            try:
                ids = self.search_store.search(query, entity_type=entity_type)
                if ids:
                    nodes = self.neo4j.fetch_nodes_by_ids(ids)
                    return [
                        SearchResult(node=node, score=float(len(ids) - index), reasons=["OpenSearch match"])
                        for index, node in enumerate(nodes)
                    ]
            except Exception:
                pass
        return search_entities(query, entity_type=entity_type)

    def list_nodes_by_type(self, entity_type: str) -> list[GraphNode]:
        if self._backend_enabled():
            try:
                nodes = self.neo4j.fetch_nodes_by_type(entity_type)
                if nodes:
                    return nodes
            except Exception:
                pass
        return [node for node in load_fixture_dataset().nodes if node.type == entity_type]

    def get_node(self, node_id: str) -> GraphNode | None:
        if self._backend_enabled():
            try:
                node = self.neo4j.fetch_node(node_id)
                if node is not None:
                    return node
            except Exception:
                pass
        return node_index().get(node_id)

    def get_neighborhood(self, node_id: str, limit: int) -> GraphNeighborhood | None:
        if self._backend_enabled():
            try:
                neighborhood = self.neo4j.fetch_neighborhood(node_id, limit=limit)
                if neighborhood is not None:
                    return neighborhood
            except Exception:
                pass

        dataset = load_fixture_dataset()
        index = {node.id: node for node in dataset.nodes}
        if node_id not in index:
            return None
        selected_edges = []
        selected_node_ids = {node_id}
        for edge in dataset.edges:
            if edge.source == node_id or edge.target == node_id:
                selected_edges.append(edge)
                selected_node_ids.add(edge.source)
                selected_node_ids.add(edge.target)
            if len(selected_edges) >= limit:
                break
        nodes = [index[selected_id] for selected_id in selected_node_ids]
        return GraphNeighborhood(center=index[node_id], nodes=nodes, edges=selected_edges)

    def recommend_software(self, node_id: str, limit: int = 3):
        source = self.get_node(node_id)
        if source is None or source.type != "software":
            return []
        candidates = self.list_nodes_by_type("software")
        return recommend_related_software_from_nodes(source, candidates, limit=limit)


@lru_cache(maxsize=1)
def get_repository() -> Repository:
    return Repository()
