from __future__ import annotations

from .models import GraphNode, Recommendation, RecommendationExplanation


def _recommend_from_candidates(
    source: GraphNode, candidates: list[GraphNode], limit: int = 3
) -> list[Recommendation]:
    source_algorithms = set(source.metadata.get("algorithms", []))
    source_msc = set(source.metadata.get("msc_codes", []))
    source_community = source.metadata.get("community_id")

    recommendations: list[Recommendation] = []
    for candidate in candidates:
        if candidate.type != "software" or candidate.id == source.id:
            continue

        candidate_algorithms = set(candidate.metadata.get("algorithms", []))
        candidate_msc = set(candidate.metadata.get("msc_codes", []))
        shared_algorithms = sorted(source_algorithms & candidate_algorithms)
        shared_msc = sorted(source_msc & candidate_msc)
        shared_community = source_community and source_community == candidate.metadata.get("community_id")

        score = 0.0
        signals: list[str] = []
        path = [source.title]
        evidence = [source.provenance.evidence]

        if shared_algorithms:
            score += 5 + len(shared_algorithms)
            algorithm_label = shared_algorithms[0].split(":", maxsplit=1)[-1].replace("-", " ")
            signals.append(f"Shared algorithm: {algorithm_label}")
            path.extend(["implements shared algorithm", candidate.title])
        if shared_msc:
            score += len(shared_msc) * 1.5
            signals.append(f"Shared MSC coverage: {', '.join(shared_msc)}")
        if shared_community:
            score += 2
            signals.append("Same research community")
        if score <= 0:
            continue

        explanation = RecommendationExplanation(
            plain_language=(
                f"{candidate.title} is recommended because it overlaps with {source.title} "
                f"through real graph signals: {', '.join(signals).lower()}."
            ),
            path=path,
            evidence=evidence + [candidate.provenance.evidence],
            signals=signals,
        )
        recommendations.append(Recommendation(node=candidate, score=score, explanation=explanation))

    return sorted(recommendations, key=lambda item: item.score, reverse=True)[:limit]


def recommend_related_software(node_id: str, limit: int = 3) -> list[Recommendation]:
    from .repository import load_dataset, node_index

    dataset = load_dataset()
    index = node_index()
    source = index[node_id]
    return _recommend_from_candidates(source, dataset.nodes, limit=limit)


def recommend_related_software_from_nodes(
    source: GraphNode, candidates: list[GraphNode], limit: int = 3
) -> list[Recommendation]:
    return _recommend_from_candidates(source, candidates, limit=limit)
