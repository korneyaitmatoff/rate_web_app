from src.repositories.user_repository import UserRepository
from src.services.user_service import UserService


def get_user_service():
    return UserService(repository=UserRepository())
