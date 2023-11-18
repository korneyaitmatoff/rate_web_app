from typing import List
from src.schemas.user import User


class UserService:
    def __init__(self, repository):
        self.repository = repository

    def get_users(self) -> List[User]:
        return self.repository.get_users()

    def get_user(self) -> User:
        return self.repository.get_user()

    def create_user(self, data):
        return self.repository.create_user(data=data)
