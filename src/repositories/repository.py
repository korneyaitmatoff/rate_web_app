from abc import ABC, abstractmethod
from typing import Type

from sqlalchemy.orm import DeclarativeMeta

from src.database.handler import DatabaseHandler
from src import server


class Repository(ABC):
    """Абстрактный класс для работы репозиториями"""
    db_engine: DatabaseHandler
    table: Type[DeclarativeMeta]

    def __init__(self, table: Type[DeclarativeMeta]):
        """Инит экземпляра класса

        Args:
            table: таблица сущности
        """
        self.db_engine = server.db
        self.table = table

    @abstractmethod
    def create(self, data: dict):
        """Создание объекта

        data: данные для создания записи
        """
        return self.db_engine.insert(table=self.table, data=data)

    @abstractmethod
    def read(self, filters: tuple = (), limit: int = 100):
        """Чтение из таблицы

        Args:
            filters: фильтр для выборки данных
            limit: ограничение по кол-ву записей
        """
        return self.db_engine.select(table=self.table, filters=filters, limit=limit)

    @abstractmethod
    def update(self, id: int, data: dict): ...

    @abstractmethod
    def delete(self, filters: tuple):
        """Удаление данных

        Args:
            filters: фильтр для выборки данных
        """
        self.db_engine.delete(table=self.table, filters=filters)
