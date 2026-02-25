"""Application configuration."""

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """Global settings loaded from environment variables."""

    APP_NAME: str = "Dobby Docs Agent"
    DEBUG: bool = False

    # LLM
    LLM_PROVIDER: str = "anthropic"
    LLM_MODEL: str = "claude-sonnet-4-20250514"
    LLM_API_KEY: str = ""

    # Embedding
    EMBEDDING_MODEL: str = "text-embedding-3-small"

    # Vector Store
    VECTOR_STORE_TYPE: str = "chroma"
    VECTOR_STORE_PATH: str = "data/vectordb"

    # API
    API_HOST: str = "0.0.0.0"
    API_PORT: int = 8000

    model_config = {"env_file": ".env", "env_file_encoding": "utf-8"}


settings = Settings()
