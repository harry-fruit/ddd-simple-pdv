from uuid import UUID

class Brand:
    """A Domain Entity representing a Brand in the system."""

    def __init__(self, brand_id: UUID, name: str, unique_key: str):
        self.brand_id = brand_id
        self.name = name
        self.unique_key = unique_key

    def __repr__(self):
        return f"Brand(brand_id={self.brand_id}, name={self.name}, unique_key={self.unique_key})"