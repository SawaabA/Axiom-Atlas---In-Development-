from __future__ import annotations

import json
from pathlib import Path
from urllib.parse import urlparse

import boto3
from botocore.exceptions import BotoCoreError, ClientError

from axiom_atlas_core.settings import settings


def _root_dir() -> Path:
    return Path(__file__).resolve().parents[5]


def _normalize_endpoint(endpoint: str) -> str:
    if endpoint.startswith("http://") or endpoint.startswith("https://"):
        return endpoint
    return f"http://{endpoint}"


class ObjectStore:
    def __init__(self) -> None:
        self.local_root = _root_dir() / "data" / "raw"
        self.local_root.mkdir(parents=True, exist_ok=True)
        endpoint_url = _normalize_endpoint(settings.minio_endpoint)
        self.s3 = boto3.client(
            "s3",
            endpoint_url=endpoint_url,
            aws_access_key_id=settings.minio_access_key,
            aws_secret_access_key=settings.minio_secret_key,
        )

    def _ensure_bucket(self) -> None:
        existing = self.s3.list_buckets().get("Buckets", [])
        if any(bucket["Name"] == settings.minio_bucket for bucket in existing):
            return
        self.s3.create_bucket(Bucket=settings.minio_bucket)

    def put_json(self, key: str, payload: dict[str, object]) -> str:
        body = json.dumps(payload, indent=2).encode("utf-8")
        try:
            self._ensure_bucket()
            self.s3.put_object(
                Bucket=settings.minio_bucket,
                Key=key,
                Body=body,
                ContentType="application/json",
            )
            return f"s3://{settings.minio_bucket}/{key}"
        except (BotoCoreError, ClientError, ValueError):
            local_path = self.local_root / key
            local_path.parent.mkdir(parents=True, exist_ok=True)
            local_path.write_bytes(body)
            return f"file://{local_path.as_posix()}"
