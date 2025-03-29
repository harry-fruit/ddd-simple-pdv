from shared.domain.repository import Repository
from entities.customer_entity import Customer
from uuid import UUID

class CustomerRepository(Repository[Customer, UUID]):
    """A Repository interface for Customer Entities."""
    pass