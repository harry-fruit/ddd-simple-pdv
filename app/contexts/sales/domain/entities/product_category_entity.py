from shared.domain.entity import Entity
import uuid


class ProductCategory(Entity):
    """A Domain Entity representing a Product Category in the system."""

    def __init__(self, id: uuid.UUID, unique_key: str, name: str):
        self.id = id
        self.name = name
        self.unique_key = unique_key

    def __repr__(self):
        return f"ProductCategory(id={self.id}, name={self.name}, unique_key={self.unique_key})"