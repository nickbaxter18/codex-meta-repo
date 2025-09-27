from collections.abc import Generator
from typing import Any

from sqlmodel import Session, SQLModel, create_engine

from .config import settings


def _build_engine() -> Any:
    connect_args: dict[str, Any] = {}
    if settings.database_url.startswith("sqlite"):
        connect_args = {"check_same_thread": False}
    echo = settings.environment.lower() in {"development", "dev", "local"}
    return create_engine(settings.database_url, connect_args=connect_args, echo=echo)


def get_engine() -> Any:
    return _engine


_engine = _build_engine()


def init_db() -> None:
    SQLModel.metadata.create_all(_engine)


def get_session() -> Generator[Session, None, None]:
    with Session(_engine) as session:
        yield session
