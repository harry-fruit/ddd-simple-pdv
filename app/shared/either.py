from typing import Generic, TypeVar, Union

T = TypeVar("T")  # Success type
E = TypeVar("E")  # Error type

class Either(Generic[T, E]):
    """Base class for Either pattern."""

    def is_success(self) -> bool:
        """Check if the result is a success."""
        return isinstance(self, Success)

    def is_failure(self) -> bool:
        """Check if the result is a failure."""
        return isinstance(self, Failure)

class Success(Either[T, E]):
    """Represents a successful result."""

    def __init__(self, value: T):
        self.value = value

    def __repr__(self):
        return f"Success({self.value})"

class Failure(Either[T, E]):
    """Represents a failed result."""

    def __init__(self, error: E):
        self.error = error

    def __repr__(self):
        return f"Failure({self.error})"
