from axiom_atlas_core.recommender import recommend_related_software


def test_recommender_returns_shared_algorithm_match() -> None:
    recommendations = recommend_related_software("software:sagemath")
    assert recommendations
    assert any("Shared algorithm" in signal for signal in recommendations[0].explanation.signals)
