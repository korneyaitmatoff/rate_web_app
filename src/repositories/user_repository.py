from typing import List, Type

from sqlalchemy.orm import DeclarativeMeta

from src.schemas.user import User
from src.repositories.repository import Repository


class UserRepository(Repository):
    table: Type[DeclarativeMeta]

    def __init__(self, table: Type[DeclarativeMeta]):
        super().__init__()
        self.table = table

    def get_user(self, id: int) -> User:
        return self.read(id=id)

    def get_users(self, filters: tuple = (), limit: int = 100) -> List[User]:
        return self.read_all(filters=filters, limit=limit)

    def create_user(self, data: dict):
        return self.create(data=data)
