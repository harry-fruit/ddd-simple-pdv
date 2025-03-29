from shared.domain.repository import Repository
from entities.brand_entity import Brand
from uuid import UUID

class BrandRepository(Repository[Brand, UUID]):
    """A Repository interface for Brand Entities."""
    pass
