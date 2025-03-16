from abc import ABC, abstractmethod
from typing import Any
import uuid


class Entity(ABC):
    """A Base Domain Entity."""

    # def __init__(self, id: uuid.UUID | None = None, **kwargs: Any):
    #     """Assigns a new UUID if not provided."""
    #     self.id = id or uuid.uuid4()

    
