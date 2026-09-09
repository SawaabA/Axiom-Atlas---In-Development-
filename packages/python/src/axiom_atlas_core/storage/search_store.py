from __future__ import annotations

from typing import Any
from urllib.parse import urlparse

from opensearchpy import OpenSearch, RequestsHttpConnection, helpers

from axiom_atlas_core.models import GraphNode
from axiom_atlas_core.settings import settings


def _host_config() -> dict[str, Any]:
    parsed = urlparse(settings.opensearch_url)
    use_ssl = parsed.scheme == "https"
    return {
        "host": parsed.hostname or "localhost",
        "port": parsed.port or (443 if use_ssl else 9200),
        "use_ssl": use_ssl,
    }


class SearchStore:
    def __init__(self) -> None:
        self.client = OpenSearch(
            hosts=[_host_config()],
            use_ssl=_host_config()["use_ssl"],
            verify_certs=False,
            ssl_assert_hostname=False,
            ssl_show_warn=False,
            connection_class=RequestsHttpConnection,
        )

    def ensure_index(self) -> None:
        if self.client.indices.exists(index=settings.search_index_name):
            return
        self.client.indices.create(
            index=settings.search_index_name,
            body={
                "settings": {"number_of_shards": 1, "number_of_replicas": 0},
                "mappings": {
                    "properties": {
                        "id": {"type": "keyword"},
                        "type": {"type": "keyword"},
                        "title": {"type": "text"},
                        "summary": {"type": "text"},
                        "tags": {"type": "keyword"},
                        "search_text": {"type": "text"},
                        "license": {"type": "keyword"},
                        "languages": {"type": "keyword"},
                        "msc_codes": {"type": "keyword"},
                        "community_id": {"type": "keyword"},
                    }
                },
            },
        )

    def index_nodes(self, nodes: list[GraphNode]) -> None:
        self.ensure_index()
        actions = []
        for node in nodes:
            metadata = node.metadata
            actions.append(
                {
                    "_index": settings.search_index_name,
                    "_id": node.id,
                    "_source": {
                        "id": node.id,
                        "type": node.type,
                        "title": node.title,
                        "summary": node.summary,
                        "tags": node.tags,
                        "search_text": " ".join(
                            [
                                node.title,
                                node.summary,
                                " ".join(node.tags),
                                " ".join(str(value) for value in metadata.values()),
                            ]
                        ),
                        "license": metadata.get("license"),
                        "languages": metadata.get("languages", []),
                        "msc_codes": metadata.get("msc_codes", []),
                        "community_id": metadata.get("community_id"),
                    },
                }
            )
        if actions:
            helpers.bulk(self.client, actions)

    def search(self, query: str, entity_type: str | None = None, size: int = 20) -> list[str]:
        self.ensure_index()
        filters = []
        if entity_type:
            filters.append({"term": {"type": entity_type}})
        response = self.client.search(
            index=settings.search_index_name,
            body={
                "size": size,
                "query": {
                    "bool": {
                        "must": [
                            {
                                "multi_match": {
                                    "query": query,
                                    "fields": ["title^4", "summary^2", "search_text", "tags^2"],
                                }
                            }
                        ],
                        "filter": filters,
                    }
                },
            },
        )
        return [hit["_id"] for hit in response["hits"]["hits"]]
