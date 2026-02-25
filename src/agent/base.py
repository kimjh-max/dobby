"""Base agent interface."""

from abc import ABC, abstractmethod
from typing import Any


class BaseAgent(ABC):
    """Abstract base class for all agents."""

    @abstractmethod
    async def run(self, query: str, **kwargs) -> Any:
        """Execute the agent with a given query."""
        ...
