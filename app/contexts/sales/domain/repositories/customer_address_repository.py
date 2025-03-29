from shared.domain.repository import Repository
from entities.customer_address import CustomerAddress
from uuid import UUID

class CustomerAddressRepository(Repository[CustomerAddress, UUID]):
    """A Repository interface for CustomerAddress Entities."""
    pass
