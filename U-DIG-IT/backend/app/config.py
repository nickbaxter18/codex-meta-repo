from functools import lru_cache
from pathlib import Path
from typing import List

from pydantic import AnyHttpUrl, Field, model_validator
from pydantic_settings import BaseSettings, SettingsConfigDict


def _parse_duration(value: str | int | float | None, default_minutes: int) -> int:
    if value is None:
        return default_minutes

    if isinstance(value, (int, float)):
        return int(value)

    token = value.strip().lower()
    multiplier = 1
    if token.endswith("ms"):
        multiplier = 1 / (60 * 1000)
        token = token[:-2]
    elif token.endswith("s"):
        multiplier = 1 / 60
        token = token[:-1]
    elif token.endswith("m"):
        multiplier = 1
        token = token[:-1]
    elif token.endswith("h"):
        multiplier = 60
        token = token[:-1]
    elif token.endswith("d"):
        multiplier = 60 * 24
        token = token[:-1]

    try:
        return int(float(token) * multiplier)
    except ValueError as exc:
        raise ValueError(f"Invalid duration value: {value}") from exc


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=Path(__file__).resolve().parents[1] / ".env", env_file_encoding="utf-8")

    app_name: str = Field(default="U-DIG-IT API")
    environment: str = Field(default="development", alias="BACKEND_ENVIRONMENT")
    log_level: str = Field(default="info", alias="BACKEND_LOG_LEVEL")

    database_url: str = Field(default="sqlite:///./u_dig_it.db", alias="DATABASE_URL")
    sentry_dsn: str | None = Field(default=None, alias="BACKEND_SENTRY_DSN")

    cors_origins: List[AnyHttpUrl] | List[str] = Field(default_factory=lambda: ["http://localhost:5173", "http://localhost:3000"], alias="CORS_ORIGIN")

    jwt_secret: str = Field(default="change-me", alias="JWT_SECRET")
    jwt_algorithm: str = "HS256"
    jwt_expires_in_minutes: int = Field(default=60 * 24, alias="JWT_EXPIRES_IN")
    refresh_token_secret: str = Field(default="change-me-refresh", alias="REFRESH_TOKEN_SECRET")
    refresh_token_expires_in_minutes: int = Field(default=60 * 24 * 14, alias="REFRESH_TOKEN_EXPIRES_IN")

    storage_provider: str | None = Field(default=None, alias="STORAGE_PROVIDER")
    storage_bucket: str | None = Field(default=None, alias="STORAGE_BUCKET")

    mixpanel_api_key: str | None = Field(default=None, alias="MIXPANEL_API_KEY")
    segment_write_key: str | None = Field(default=None, alias="SEGMENT_JS_WRITE_KEY")

    class Config:
        populate_by_name = True

    @model_validator(mode="after")
    def _normalize_durations(self) -> "Settings":
        if isinstance(self.cors_origins, str):
            self.cors_origins = [origin.strip() for origin in self.cors_origins.split(",") if origin.strip()]

        self.jwt_expires_in_minutes = _parse_duration(self.jwt_expires_in_minutes, 60 * 24)
        self.refresh_token_expires_in_minutes = _parse_duration(self.refresh_token_expires_in_minutes, 60 * 24 * 14)
        return self


@lru_cache
def get_settings() -> Settings:
    return Settings()


settings = get_settings()
