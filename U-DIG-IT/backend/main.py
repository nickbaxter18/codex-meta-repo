from __future__ import annotations

import logging

import sentry_sdk
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from sentry_sdk.integrations.fastapi import FastApiIntegration
from sentry_sdk.integrations.starlette import StarletteIntegration
from sqlmodel import Session

from app.config import settings
from app.database import get_engine, init_db
from app.routers import analytics, auth, catalog, health, reservations
from app.services.seed_data import seed_initial_data

logging.basicConfig(level=getattr(logging, settings.log_level.upper(), logging.INFO))
logger = logging.getLogger("u-dig-it")


if settings.sentry_dsn:
    sentry_sdk.init(
        dsn=settings.sentry_dsn,
        integrations=[FastApiIntegration(), StarletteIntegration()],
        traces_sample_rate=1.0,
        environment=settings.environment,
    )

app = FastAPI(title=settings.app_name, version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.cors_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.on_event("startup")
def on_startup() -> None:
    init_db()
    engine = get_engine()
    with Session(engine) as session:
        seed_initial_data(session)
        logger.info("Database and seed data ready")


@app.get("/", tags=["core"])
def root() -> dict[str, str]:
    return {"message": "Welcome to U-DIG-IT equipment rental API"}


app.include_router(health.router)
app.include_router(auth.router)
app.include_router(catalog.router)
app.include_router(reservations.router)
app.include_router(analytics.router)
