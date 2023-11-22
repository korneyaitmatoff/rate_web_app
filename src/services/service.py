from abc import ABC, abstractmethod

from src.repositories.repository import Repository


class Service(ABC):
    repository: Repository

    def __init__(self, repository: Repository):
        """Инит экземпляра класа

        Args:
            repository: репозиторий сущности
        """
        self.repository = repository

    @abstractmethod
    def create(self, data: dict):
        """Саздание записи в бд"""
        return self.repository.create(data=data)

    @abstractmethod
    def read(self, id: int):
        """Чтение записи по id из бд"""
        return self.repository.read(filters=(
            self.repository.table.id == id,
        ))

    def update(self, id: int, data: dict): ...

    @abstractmethod
    def delete(self, filters: tuple):
        return self.repository.delete(filters=filters)
