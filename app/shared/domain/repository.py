from abc import ABC, abstractmethod
from typing import Generic, TypeVar, Optional

T = TypeVar('T')
ID = TypeVar('ID')

class Repository(ABC, Generic[T, ID]):
    
    @abstractmethod
    def get_by_id(self, id: ID) -> Optional[T]:
        pass

    @abstractmethod
    def list(self) -> list[T]:
        pass

    @abstractmethod
    def add(self, entity: T) -> T:
        pass

    @abstractmethod
    def update(self, entity: T) -> T:
        pass

    @abstractmethod
    def delete(self, id: ID) -> None:
        pass