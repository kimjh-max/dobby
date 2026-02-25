"""Docs Agent - main agent implementation."""

from .base import BaseAgent


class DocsAgent(BaseAgent):
    """Agent for document search, Q&A, and generation."""

    async def run(self, query: str, **kwargs):
        raise NotImplementedError
