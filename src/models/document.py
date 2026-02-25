"""Document data models."""

from pydantic import BaseModel


class Document(BaseModel):
    """Represents a loaded document chunk."""

    content: str
    metadata: dict = {}
    source: str = ""
