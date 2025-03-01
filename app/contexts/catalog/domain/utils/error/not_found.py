from infrastructure.error.base_error import BaseError


class NotFoundError(BaseError):
    """Raised when a resource is not found."""

    def __init__(self, resource: str, resource_id: str):
        super().__init__(f"{resource} with ID {resource_id} was not found.")
