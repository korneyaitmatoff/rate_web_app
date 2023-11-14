from typing import List
from src.schemas.user import User


class UserRepository:
    def get_user(self) -> User:
        ...

    def get_users(self) -> List[User]:
        ...

    def create_user(self, data):
        print(data)
