import uuid

class Brand:
    """A Domain Entity representing a Brand in the system."""

    def __init__(self, id: uuid.UUID, name: str, unique_key: str):
        self.id = id
        self.name = name
        self.unique_key = unique_key

    def __repr__(self):
        return f"Brand(id={self.id}, name={self.name}, unique_key={self.unique_key})"