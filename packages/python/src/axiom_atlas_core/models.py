from __future__ import annotations

from typing import Any, Literal

from pydantic import BaseModel, Field


EntityType = Literal[
    "software",
    "paper",
    "algorithm",
    "community",
    "repository",
]


class Provenance(BaseModel):
    source: str
    evidence: str
    confidence: float = Field(ge=0, le=1)
    retrieved_at: str


class GraphNode(BaseModel):
    id: str
    type: EntityType
    title: str
    summary: str
    url: str
    tags: list[str] = Field(default_factory=list)
    metadata: dict[str, Any] = Field(default_factory=dict)
    provenance: Provenance


class GraphEdge(BaseModel):
    id: str
    source: str
    target: str
    type: str
    evidence: str
    confidence: float = Field(ge=0, le=1)


class GraphDataset(BaseModel):
    generated_at: str
    dataset_name: str
    dataset_version: str
    nodes: list[GraphNode]
    edges: list[GraphEdge]


class SearchResult(BaseModel):
    node: GraphNode
    score: float
    reasons: list[str]


class RecommendationExplanation(BaseModel):
    plain_language: str
    path: list[str]
    evidence: list[str]
    signals: list[str]


class Recommendation(BaseModel):
    node: GraphNode
    score: float
    explanation: RecommendationExplanation


class GraphNeighborhood(BaseModel):
    center: GraphNode
    nodes: list[GraphNode]
    edges: list[GraphEdge]
