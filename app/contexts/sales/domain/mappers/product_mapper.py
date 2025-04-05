from shared.domain.mapper import Mapper
from entities.product_entity import Product

class ProductMapper(Mapper[Product]):
    """A Mapper for Product Entities."""
    
    def to_domain(self, entity: Product) -> Product:
        return Product()
    
    def map_to_entity(self, domain: Product) -> Product:
        return super().map_to_entity(domain)