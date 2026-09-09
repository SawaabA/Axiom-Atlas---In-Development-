from __future__ import annotations

import json
from typing import Any

from neo4j import GraphDatabase
from neo4j.exceptions import Neo4jError

from axiom_atlas_core.models import GraphDataset, GraphEdge, GraphNeighborhood, GraphNode, Provenance
from axiom_atlas_core.settings import settings


def _label_for_type(entity_type: str) -> str:
    mapping = {
        "software": "Software",
        "paper": "Paper",
        "algorithm": "Algorithm",
        "community": "ResearchCommunity",
        "repository": "Repository",
    }
    return mapping.get(entity_type, "Entity")


def _serialize_node(node: GraphNode) -> dict[str, Any]:
    return {
        "id": node.id,
        "type": node.type,
        "title": node.title,
        "summary": node.summary,
        "url": node.url,
        "tags": node.tags,
        "metadata_json": json.dumps(node.metadata),
        "provenance_source": node.provenance.source,
        "provenance_evidence": node.provenance.evidence,
        "provenance_confidence": node.provenance.confidence,
        "provenance_retrieved_at": node.provenance.retrieved_at,
    }


def _deserialize_node(properties: dict[str, Any]) -> GraphNode:
    return GraphNode(
        id=properties["id"],
        type=properties["type"],
        title=properties["title"],
        summary=properties.get("summary", ""),
        url=properties.get("url", ""),
        tags=properties.get("tags", []),
        metadata=json.loads(properties.get("metadata_json", "{}")),
        provenance=Provenance(
            source=properties.get("provenance_source", "unknown"),
            evidence=properties.get("provenance_evidence", ""),
            confidence=float(properties.get("provenance_confidence", 0.0)),
            retrieved_at=properties.get("provenance_retrieved_at", ""),
        ),
    )


class Neo4jStore:
    def __init__(self) -> None:
        self.driver = GraphDatabase.driver(
            settings.neo4j_url,
            auth=(settings.neo4j_username, settings.neo4j_password),
        )

    def ensure_schema(self) -> None:
        queries = [
            "CREATE CONSTRAINT node_id_unique IF NOT EXISTS FOR (n:Entity) REQUIRE n.id IS UNIQUE",
        ]
        with self.driver.session() as session:
            for query in queries:
                try:
                    session.run(query).consume()
                except Neo4jError:
                    continue

    def upsert_dataset(self, dataset: GraphDataset) -> None:
        self.ensure_schema()
        with self.driver.session() as session:
            for node in dataset.nodes:
                properties = _serialize_node(node)
                label = _label_for_type(node.type)
                session.run(
                    (
                        f"MERGE (n:Entity:{label} {{id: $id}}) "
                        "SET n += $properties"
                    ),
                    id=node.id,
                    properties=properties,
                ).consume()

            for edge in dataset.edges:
                session.run(
                    (
                        "MATCH (source:Entity {id: $source_id}) "
                        "MATCH (target:Entity {id: $target_id}) "
                        f"MERGE (source)-[rel:{edge.type} {{id: $id}}]->(target) "
                        "SET rel.evidence = $evidence, rel.confidence = $confidence"
                    ),
                    id=edge.id,
                    source_id=edge.source,
                    target_id=edge.target,
                    evidence=edge.evidence,
                    confidence=edge.confidence,
                ).consume()

    def summary_counts(self) -> dict[str, int]:
        with self.driver.session() as session:
            result = session.run(
                "MATCH (n:Entity) RETURN n.type AS type, count(*) AS count"
            )
            return {record["type"]: int(record["count"]) for record in result}

    def fetch_nodes_by_type(self, entity_type: str) -> list[GraphNode]:
        label = _label_for_type(entity_type)
        with self.driver.session() as session:
            result = session.run(
                f"MATCH (n:Entity:{label}) RETURN n ORDER BY n.title ASC"
            )
            return [_deserialize_node(dict(record["n"])) for record in result]

    def fetch_node(self, node_id: str) -> GraphNode | None:
        with self.driver.session() as session:
            record = session.run(
                "MATCH (n:Entity {id: $node_id}) RETURN n LIMIT 1",
                node_id=node_id,
            ).single()
            if record is None:
                return None
            return _deserialize_node(dict(record["n"]))

    def fetch_nodes_by_ids(self, node_ids: list[str]) -> list[GraphNode]:
        if not node_ids:
            return []
        with self.driver.session() as session:
            result = session.run(
                "MATCH (n:Entity) WHERE n.id IN $node_ids RETURN n",
                node_ids=node_ids,
            )
            nodes = [_deserialize_node(dict(record["n"])) for record in result]
            order = {node_id: index for index, node_id in enumerate(node_ids)}
            return sorted(nodes, key=lambda node: order.get(node.id, 0))

    def fetch_all_nodes(self) -> list[GraphNode]:
        with self.driver.session() as session:
            result = session.run("MATCH (n:Entity) RETURN n")
            return [_deserialize_node(dict(record["n"])) for record in result]

    def fetch_neighborhood(self, node_id: str, limit: int) -> GraphNeighborhood | None:
        with self.driver.session() as session:
            record = session.run(
                (
                    "MATCH (center:Entity {id: $node_id}) "
                    "OPTIONAL MATCH (center)-[rel]-(neighbor:Entity) "
                    "RETURN center, "
                    "collect(DISTINCT neighbor)[..$limit] AS neighbors, "
                    "collect(DISTINCT {"
                    "id: rel.id, "
                    "source: startNode(rel).id, "
                    "target: endNode(rel).id, "
                    "type: type(rel), "
                    "evidence: rel.evidence, "
                    "confidence: rel.confidence"
                    "})[..$limit] AS edges"
                ),
                node_id=node_id,
                limit=limit,
            ).single()
            if record is None:
                return None
            center = _deserialize_node(dict(record["center"]))
            neighbors = [
                _deserialize_node(dict(node)) for node in record["neighbors"] if node is not None
            ]
            edges = [
                GraphEdge.model_validate(edge)
                for edge in record["edges"]
                if edge.get("id") is not None
            ]
            unique_nodes = {center.id: center, **{node.id: node for node in neighbors}}
            return GraphNeighborhood(center=center, nodes=list(unique_nodes.values()), edges=edges)
