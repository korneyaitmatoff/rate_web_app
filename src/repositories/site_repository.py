from typing import Type

from sqlalchemy.orm import DeclarativeMeta

from src.repositories.repository import Repository


class SiteRepository(Repository):
    table: Type[DeclarativeMeta]

    def __init__(self, table: Type[DeclarativeMeta]):
        """Инит экземпляра класса и его родителя

        Args:
            table: объект таблицы сущности
        """
        super().__init__(table=table)
