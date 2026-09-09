from axiom_atlas_core.search import search_entities


def test_search_finds_symbolic_software() -> None:
    results = search_entities("symbolic algebra", entity_type="software")
    assert results
    assert results[0].node.type == "software"
