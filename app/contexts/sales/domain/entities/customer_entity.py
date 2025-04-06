from domain.entities.customer_address import CustomerAddress
from shared.domain.entities.user_entity import User
from shared.domain.entity import Entity
from shared.either import Either, Success, Failure
from shared.errors.unexpected_error import UnexpectedError
from uuid import UUID


Response = Either[None, BaseException]

class Customer(Entity):
    """A Domain Entity representing a Customer in the system."""

    customer_id: int | None
    name: str
    address: list[CustomerAddress]
    user: User

    def __init__(
            self, 
            customer_id: UUID, 
            name: str, 
            addresses: list[CustomerAddress], 
            user: User
        ):
        self.customer_id = customer_id
        self.name = name
        self.user = user
        self.addresses = addresses

    def add_address(self, address: CustomerAddress) -> Response:
        """Business rule to add an address to the customer."""
        try:
            self.addresses.append(address)
            return Success(None)
        except Exception as e:
            return Failure(UnexpectedError(e))

    def remove_address(self, address: CustomerAddress) -> Response:
        """Business rule to remove an address from the customer."""
        try:
            self.addresses.remove(address)
            return Success(None)
        except Exception as e:
            return Failure(UnexpectedError(e))

    def change_name(self, new_name: str) -> Response:
        """Business rule to update name."""
        try:
            self.name = new_name
            return Success(None)
        except Exception as e:
            return Failure(UnexpectedError(e))

    def __repr__(self):
        return f"Customer(customer_id={self.customer_id}, name={self.name}, address={self.address}, user={self.user})"
