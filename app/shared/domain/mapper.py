from abc import ABC, abstractmethod
from typing import Generic, TypeVar

T = TypeVar('T')

class Mapper(ABC, Generic[T]):
    """A Mapper interface."""
    
    @abstractmethod
    def to_domain(self, entity: T) -> T:
        pass

    @abstractmethod
    def map_to_entity(self, domain: T) -> T:
        pass