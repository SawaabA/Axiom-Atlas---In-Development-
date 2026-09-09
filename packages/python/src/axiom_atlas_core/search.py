from __future__ import annotations

from .models import GraphNode, SearchResult


def _score_node(node: GraphNode, query: str) -> SearchResult | None:
    query_lower = query.lower().strip()
    haystack = " ".join(
        [
            node.title,
            node.summary,
            " ".join(node.tags),
            " ".join(str(value) for value in node.metadata.values()),
        ]
    ).lower()
    if query_lower not in haystack and not all(part in haystack for part in query_lower.split()):
        return None

    reasons: list[str] = []
    score = 0.0

    if query_lower in node.title.lower():
        score += 4
        reasons.append("Title match")
    if any(query_lower in tag.lower() for tag in node.tags):
        score += 2
        reasons.append("Tag match")
    if query_lower in node.summary.lower():
        score += 1.5
        reasons.append("Summary match")
    if not reasons:
        reasons.append("Metadata match")
        score += 1

    return SearchResult(node=node, score=score, reasons=reasons)


def search_entities(query: str, entity_type: str | None = None) -> list[SearchResult]:
    from .repository import load_dataset

    dataset = load_dataset()
    results = []
    for node in dataset.nodes:
        if entity_type and node.type != entity_type:
            continue
        scored = _score_node(node, query)
        if scored:
            results.append(scored)
    return sorted(results, key=lambda item: item.score, reverse=True)
