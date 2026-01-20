"""
Gaian Service Configuration

Validates environment variables at startup using Pydantic Settings.
Fails fast if required configuration is missing.
"""

from functools import lru_cache
from typing import Optional

from pydantic import Field, field_validator
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """
    Application settings loaded from environment variables.

    Required variables will cause startup failure if missing.
    Optional variables have sensible defaults for development.
    """

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
        extra="ignore",
    )

    # -------------------------------------------------------------------------
    # Application
    # -------------------------------------------------------------------------
    app_env: str = Field(default="development", description="Environment name")
    app_debug: bool = Field(default=True, description="Debug mode")
    app_secret_key: str = Field(
        default="dev-secret-change-in-production",
        description="Secret key for signing"
    )

    # -------------------------------------------------------------------------
    # Gaian Service
    # -------------------------------------------------------------------------
    gaian_host: str = Field(default="0.0.0.0", description="Server host")
    gaian_port: int = Field(default=8000, description="Server port")
    gaian_log_level: str = Field(default="DEBUG", description="Log level")
    gaian_workers: int = Field(default=1, description="Uvicorn workers")

    # -------------------------------------------------------------------------
    # Database (Optional for Phase 1)
    # -------------------------------------------------------------------------
    database_url: Optional[str] = Field(
        default=None,
        description="PostgreSQL connection string"
    )
    database_pool_size: int = Field(default=5, description="Connection pool size")
    database_max_overflow: int = Field(default=10, description="Max overflow")

    # -------------------------------------------------------------------------
    # Redis (Optional for Phase 1)
    # -------------------------------------------------------------------------
    redis_url: str = Field(
        default="redis://localhost:6379/0",
        description="Redis URL"
    )
    redis_password: Optional[str] = Field(default=None, description="Redis password")

    # -------------------------------------------------------------------------
    # Qdrant (Optional for Phase 1)
    # -------------------------------------------------------------------------
    qdrant_host: str = Field(default="localhost", description="Qdrant host")
    qdrant_port: int = Field(default=6333, description="Qdrant port")
    qdrant_api_key: Optional[str] = Field(default=None, description="Qdrant API key")

    # -------------------------------------------------------------------------
    # Training Data
    # -------------------------------------------------------------------------
    training_data_path: str = Field(
        default="./data/training",
        description="Training data directory"
    )
    training_log_format: str = Field(default="jsonl", description="Log format")
    training_batch_size: int = Field(default=100, description="Batch size")

    # -------------------------------------------------------------------------
    # SILA Token
    # -------------------------------------------------------------------------
    sila_mock_enabled: bool = Field(default=True, description="Use mock SILA")
    sila_base_reward: float = Field(default=0.01, description="Base reward")

    # -------------------------------------------------------------------------
    # Security
    # -------------------------------------------------------------------------
    cors_origins: str = Field(
        default="http://localhost:3000,http://localhost:8080",
        description="CORS origins (comma-separated)"
    )

    # -------------------------------------------------------------------------
    # Feature Flags
    # -------------------------------------------------------------------------
    feature_uprising_biome: bool = Field(default=False)
    feature_theater_biome: bool = Field(default=False)
    feature_data_export: bool = Field(default=False)

    # -------------------------------------------------------------------------
    # Validators
    # -------------------------------------------------------------------------
    @field_validator("app_env")
    @classmethod
    def validate_app_env(cls, v: str) -> str:
        allowed = {"development", "staging", "production"}
        if v.lower() not in allowed:
            raise ValueError(f"app_env must be one of {allowed}")
        return v.lower()

    @field_validator("gaian_log_level")
    @classmethod
    def validate_log_level(cls, v: str) -> str:
        allowed = {"DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"}
        if v.upper() not in allowed:
            raise ValueError(f"gaian_log_level must be one of {allowed}")
        return v.upper()

    # -------------------------------------------------------------------------
    # Computed Properties
    # -------------------------------------------------------------------------
    @property
    def is_production(self) -> bool:
        return self.app_env == "production"

    @property
    def is_development(self) -> bool:
        return self.app_env == "development"

    @property
    def cors_origins_list(self) -> list[str]:
        return [origin.strip() for origin in self.cors_origins.split(",")]


@lru_cache
def get_settings() -> Settings:
    """
    Get cached settings instance.

    Uses lru_cache to ensure settings are only loaded once.
    Raises ValidationError if required variables are missing.
    """
    return Settings()


# Convenience export for direct import
settings = get_settings()
