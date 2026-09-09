from __future__ import annotations

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class CoreSettings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8", extra="ignore")

    data_backend: str = Field(default="hybrid", alias="DATA_BACKEND")
    fixture_data_path: str = Field(default="data/fixtures/seed_graph.json", alias="FIXTURE_DATA_PATH")
    postgres_url: str = Field(
        default="postgresql+psycopg://axiom:axiom@localhost:5432/axiom_atlas",
        alias="POSTGRES_URL",
    )
    neo4j_url: str = Field(default="bolt://localhost:7687", alias="NEO4J_URL")
    neo4j_username: str = Field(default="neo4j", alias="NEO4J_USERNAME")
    neo4j_password: str = Field(default="axiomatlas", alias="NEO4J_PASSWORD")
    opensearch_url: str = Field(default="http://localhost:9200", alias="OPENSEARCH_URL")
    minio_endpoint: str = Field(default="http://localhost:9000", alias="MINIO_ENDPOINT")
    minio_access_key: str = Field(default="minioadmin", alias="MINIO_ACCESS_KEY")
    minio_secret_key: str = Field(default="minioadmin", alias="MINIO_SECRET_KEY")
    minio_bucket: str = Field(default="axiom-atlas", alias="MINIO_BUCKET")
    minio_secure: bool = Field(default=False, alias="MINIO_SECURE")
    zenodo_api_base_url: str = Field(
        default="https://zenodo.org/api/records", alias="ZENODO_API_BASE_URL"
    )
    zenodo_query: str = Field(
        default=(
            "resource_type.type:software AND "
            "(description:mathematical OR keywords:mathematics "
            "OR title:mathematical OR description:numerical OR description:algebra)"
        ),
        alias="ZENODO_QUERY",
    )
    zenodo_page_size: int = Field(default=25, alias="ZENODO_PAGE_SIZE")
    zenodo_max_pages: int = Field(default=2, alias="ZENODO_MAX_PAGES")
    zenodo_timeout_seconds: float = Field(default=20.0, alias="ZENODO_TIMEOUT_SECONDS")
    raw_payload_prefix: str = Field(default="zenodo/raw", alias="RAW_PAYLOAD_PREFIX")
    search_index_name: str = Field(default="entities_v1", alias="SEARCH_INDEX_NAME")


settings = CoreSettings()
