from __future__ import annotations

import re
from dataclasses import dataclass
from datetime import datetime, timezone
from typing import Any

import httpx

from axiom_atlas_core.models import GraphDataset, GraphEdge, GraphNode, Provenance
from axiom_atlas_core.settings import settings


TAG_RE = re.compile(r"<[^>]+>")
MATH_TERMS = {
    "math",
    "mathematical",
    "mathematics",
    "algebra",
    "geometry",
    "topology",
    "numerical",
    "equation",
    "solver",
    "symbolic",
    "finite element",
    "pde",
    "homology",
    "number theory",
    "optimization",
    "analysis",
    "simulation",
}


def _strip_html(value: str | None) -> str:
    if not value:
        return ""
    return re.sub(r"\s+", " ", TAG_RE.sub(" ", value)).strip()


def _safe_slug(value: str) -> str:
    cleaned = re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-")
    return cleaned or "unknown"


def _extract_repository_url(record: dict[str, Any]) -> str | None:
    metadata = record.get("metadata", {})
    for related in metadata.get("related_identifiers", []) or []:
        identifier = related.get("identifier", "")
        if "github.com/" in identifier.lower():
            return identifier
    return None


def _extract_languages(metadata: dict[str, Any]) -> list[str]:
    keywords = metadata.get("keywords") or []
    known = []
    for keyword in keywords:
        if keyword.lower() in {"python", "julia", "matlab", "c++", "fortran", "r"}:
            known.append(keyword)
    return known


def _is_math_relevant(title: str, description: str, keywords: list[Any]) -> bool:
    haystack = " ".join([title, description, " ".join(str(keyword) for keyword in keywords)]).lower()
    return any(term in haystack for term in MATH_TERMS)


@dataclass
class ZenodoPage:
    records: list[dict[str, Any]]
    total: int
    next_page: int | None


class ZenodoAdapter:
    source_name = "zenodo"

    def __init__(self) -> None:
        self.client = httpx.Client(timeout=settings.zenodo_timeout_seconds)

    def fetch_page(self, *, page: int) -> ZenodoPage:
        response = self.client.get(
            settings.zenodo_api_base_url,
            params={
                "q": settings.zenodo_query,
                "size": settings.zenodo_page_size,
                "page": page,
                "sort": "mostrecent",
            },
        )
        response.raise_for_status()
        payload = response.json()
        hits = payload.get("hits", {})
        records = hits.get("hits", [])
        total_raw = hits.get("total", 0)
        total = total_raw if isinstance(total_raw, int) else int(total_raw.get("value", 0))
        next_page = page + 1 if records and page < settings.zenodo_max_pages else None
        return ZenodoPage(records=records, total=total, next_page=next_page)

    def normalize_records(self, records: list[dict[str, Any]]) -> GraphDataset:
        nodes: list[GraphNode] = []
        edges: list[GraphEdge] = []

        for record in records:
            metadata = record.get("metadata", {})
            record_id = str(record.get("id"))
            description = _strip_html(metadata.get("description"))
            title = metadata.get("title") or f"Zenodo record {record_id}"
            doi = record.get("doi") or metadata.get("doi")
            repository_url = _extract_repository_url(record)
            languages = _extract_languages(metadata)
            keywords = metadata.get("keywords") or []
            communities = metadata.get("communities") or []

            if not _is_math_relevant(title, description, keywords):
                continue

            software_id = f"software:zenodo:{record_id}"
            software_node = GraphNode(
                id=software_id,
                type="software",
                title=title,
                summary=description or "Software record ingested from Zenodo.",
                url=record.get("doi_url") or record.get("links", {}).get("self_html", ""),
                tags=[str(keyword) for keyword in keywords][:12],
                metadata={
                    "zenodo_record_id": record_id,
                    "doi": doi,
                    "publication_date": metadata.get("publication_date"),
                    "version": metadata.get("version"),
                    "license": (metadata.get("license") or {}).get("id")
                    if isinstance(metadata.get("license"), dict)
                    else metadata.get("license"),
                    "languages": languages,
                    "community_id": None,
                    "source": "zenodo",
                },
                provenance=Provenance(
                    source="zenodo",
                    evidence=f"Zenodo record {record_id}",
                    confidence=1.0,
                    retrieved_at=datetime.now(timezone.utc).isoformat(),
                ),
            )
            nodes.append(software_node)

            if repository_url:
                repo_id = f"repository:{_safe_slug(repository_url)}"
                repo_node = GraphNode(
                    id=repo_id,
                    type="repository",
                    title=repository_url.replace("https://", "").replace("http://", ""),
                    summary=f"Repository linked from Zenodo record {record_id}.",
                    url=repository_url,
                    tags=["github"] if "github.com" in repository_url.lower() else ["repository"],
                    metadata={"host": "GitHub" if "github.com" in repository_url.lower() else "Web"},
                    provenance=software_node.provenance,
                )
                nodes.append(repo_node)
                edges.append(
                    GraphEdge(
                        id=f"edge:{software_id}:has-repository:{repo_id}",
                        source=software_id,
                        target=repo_id,
                        type="HAS_REPOSITORY",
                        evidence=f"Related identifier in Zenodo record {record_id}",
                        confidence=1.0,
                    )
                )

            for community in communities:
                identifier = community.get("identifier") or community.get("id")
                if not identifier:
                    continue
                community_id = f"community:zenodo:{_safe_slug(identifier)}"
                community_title = community.get("title") or identifier
                nodes.append(
                    GraphNode(
                        id=community_id,
                        type="community",
                        title=community_title,
                        summary=f"Zenodo community {community_title}.",
                        url=f"https://zenodo.org/communities/{identifier}/",
                        tags=["zenodo-community"],
                        metadata={"zenodo_identifier": identifier},
                        provenance=software_node.provenance,
                    )
                )
                edges.append(
                    GraphEdge(
                        id=f"edge:{software_id}:member-of:{community_id}",
                        source=software_id,
                        target=community_id,
                        type="MEMBER_OF",
                        evidence=f"Zenodo community membership on record {record_id}",
                        confidence=1.0,
                    )
                )

        deduped_nodes = {node.id: node for node in nodes}
        return GraphDataset(
            generated_at=datetime.now(timezone.utc).isoformat(),
            dataset_name="Zenodo Software Ingestion",
            dataset_version=datetime.now(timezone.utc).strftime("%Y%m%d%H%M%S"),
            nodes=list(deduped_nodes.values()),
            edges=edges,
        )
