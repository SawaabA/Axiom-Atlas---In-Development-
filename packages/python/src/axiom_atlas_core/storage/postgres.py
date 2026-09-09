from __future__ import annotations

import uuid
from contextlib import contextmanager
from datetime import datetime, timezone
from typing import Any, Iterator

from sqlalchemy import JSON, DateTime, Integer, String, Text, create_engine
from sqlalchemy.orm import DeclarativeBase, Mapped, Session, mapped_column, sessionmaker

from axiom_atlas_core.settings import settings


class Base(DeclarativeBase):
    pass


class IngestionJob(Base):
    __tablename__ = "ingestion_jobs"

    id: Mapped[str] = mapped_column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    source_name: Mapped[str] = mapped_column(String(64), index=True)
    status: Mapped[str] = mapped_column(String(32), index=True)
    started_at: Mapped[datetime] = mapped_column(DateTime(timezone=True))
    finished_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True), nullable=True)
    records_fetched: Mapped[int] = mapped_column(Integer, default=0)
    records_normalized: Mapped[int] = mapped_column(Integer, default=0)
    records_failed: Mapped[int] = mapped_column(Integer, default=0)
    checkpoint: Mapped[dict[str, Any]] = mapped_column(JSON, default=dict)
    error_message: Mapped[str | None] = mapped_column(Text, nullable=True)


class SourceCheckpoint(Base):
    __tablename__ = "source_checkpoints"

    source_name: Mapped[str] = mapped_column(String(64), primary_key=True)
    cursor: Mapped[dict[str, Any]] = mapped_column(JSON, default=dict)
    updated_at: Mapped[datetime] = mapped_column(DateTime(timezone=True))


class RawRecord(Base):
    __tablename__ = "raw_records"

    id: Mapped[str] = mapped_column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    source_name: Mapped[str] = mapped_column(String(64), index=True)
    source_record_id: Mapped[str] = mapped_column(String(128), index=True)
    storage_uri: Mapped[str] = mapped_column(Text)
    payload_json: Mapped[dict[str, Any]] = mapped_column(JSON)
    retrieved_at: Mapped[datetime] = mapped_column(DateTime(timezone=True))


engine = create_engine(settings.postgres_url, future=True, pool_pre_ping=True)
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False, future=True)


def utcnow() -> datetime:
    return datetime.now(timezone.utc)


def ensure_postgres_schema() -> None:
    Base.metadata.create_all(bind=engine)


@contextmanager
def session_scope() -> Iterator[Session]:
    ensure_postgres_schema()
    session = SessionLocal()
    try:
        yield session
        session.commit()
    except Exception:
        session.rollback()
        raise
    finally:
        session.close()


def start_ingestion_job(source_name: str) -> str:
    with session_scope() as session:
        job = IngestionJob(
            source_name=source_name,
            status="running",
            started_at=utcnow(),
            checkpoint={},
        )
        session.add(job)
        session.flush()
        return job.id


def update_ingestion_job(
    job_id: str,
    *,
    status: str,
    records_fetched: int,
    records_normalized: int,
    records_failed: int,
    checkpoint: dict[str, Any],
    error_message: str | None = None,
) -> None:
    with session_scope() as session:
        job = session.get(IngestionJob, job_id)
        if not job:
            return
        job.status = status
        job.records_fetched = records_fetched
        job.records_normalized = records_normalized
        job.records_failed = records_failed
        job.checkpoint = checkpoint
        job.error_message = error_message
        if status in {"completed", "failed"}:
            job.finished_at = utcnow()


def get_checkpoint(source_name: str) -> dict[str, Any]:
    ensure_postgres_schema()
    with SessionLocal() as session:
        checkpoint = session.get(SourceCheckpoint, source_name)
        return checkpoint.cursor if checkpoint else {}


def set_checkpoint(source_name: str, cursor: dict[str, Any]) -> None:
    with session_scope() as session:
        checkpoint = session.get(SourceCheckpoint, source_name)
        if checkpoint is None:
            checkpoint = SourceCheckpoint(
                source_name=source_name,
                cursor=cursor,
                updated_at=utcnow(),
            )
            session.add(checkpoint)
        else:
            checkpoint.cursor = cursor
            checkpoint.updated_at = utcnow()


def store_raw_record(
    source_name: str,
    source_record_id: str,
    storage_uri: str,
    payload_json: dict[str, Any],
) -> None:
    with session_scope() as session:
        record = RawRecord(
            source_name=source_name,
            source_record_id=source_record_id,
            storage_uri=storage_uri,
            payload_json=payload_json,
            retrieved_at=utcnow(),
        )
        session.add(record)


def list_ingestion_jobs(limit: int = 20) -> list[dict[str, Any]]:
    ensure_postgres_schema()
    with SessionLocal() as session:
        jobs = (
            session.query(IngestionJob)
            .order_by(IngestionJob.started_at.desc())
            .limit(limit)
            .all()
        )
        return [
            {
                "id": job.id,
                "source_name": job.source_name,
                "status": job.status,
                "started_at": job.started_at.isoformat(),
                "finished_at": job.finished_at.isoformat() if job.finished_at else None,
                "records_fetched": job.records_fetched,
                "records_normalized": job.records_normalized,
                "records_failed": job.records_failed,
                "checkpoint": job.checkpoint,
                "error_message": job.error_message,
            }
            for job in jobs
        ]
