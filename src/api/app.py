"""FastAPI application entry point."""

from fastapi import FastAPI

from src.api.router import router
from src.core.config import settings


def create_app() -> FastAPI:
    app = FastAPI(title=settings.APP_NAME, debug=settings.DEBUG)
    app.include_router(router)
    return app


app = create_app()
