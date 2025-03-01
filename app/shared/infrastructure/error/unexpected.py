from infrastructure.error.base_error import BaseError


class UnexpectedError(BaseError):
    """Raised when an unexpected error occurs."""

    def __init__(self, original_exception: Exception):
        super().__init__(f"An unexpected error occurred: {str(original_exception)}")