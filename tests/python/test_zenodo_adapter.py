from axiom_atlas_core.sources.zenodo import ZenodoAdapter


def test_zenodo_normalizer_creates_software_and_repository_nodes() -> None:
    adapter = ZenodoAdapter()
    dataset = adapter.normalize_records(
        [
            {
                "id": 123,
                "doi": "10.5281/zenodo.123",
                "doi_url": "https://doi.org/10.5281/zenodo.123",
                "metadata": {
                    "title": "Symbolic algebra toolkit",
                    "description": "<p>Mathematical software for symbolic algebra workflows.</p>",
                    "keywords": ["mathematics", "python"],
                    "license": {"id": "MIT"},
                    "related_identifiers": [
                        {
                            "identifier": "https://github.com/example/symbolic-algebra-toolkit",
                        }
                    ],
                    "communities": [{"identifier": "math-tools", "title": "Math Tools"}],
                },
            }
        ]
    )

    node_ids = {node.id for node in dataset.nodes}
    edge_ids = {edge.id for edge in dataset.edges}

    assert "software:zenodo:123" in node_ids
    assert "repository:https-github-com-example-symbolic-algebra-toolkit" in node_ids
    assert "community:zenodo:math-tools" in node_ids
    assert "edge:software:zenodo:123:has-repository:repository:https-github-com-example-symbolic-algebra-toolkit" in edge_ids


def test_zenodo_normalizer_skips_non_math_records() -> None:
    adapter = ZenodoAdapter()
    dataset = adapter.normalize_records(
        [
            {
                "id": 456,
                "metadata": {
                    "title": "Marketing automation workflow",
                    "description": "Customer segmentation and sales funnel software.",
                    "keywords": ["marketing", "crm"],
                },
            }
        ]
    )

    assert dataset.nodes == []
    assert dataset.edges == []
