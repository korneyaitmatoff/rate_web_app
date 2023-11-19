from src.services.service import Service
from src.repositories.repository import Repository


class UserService(Service):
    """Класс-сервис для работы с сущностью "Пользователь" """

    def __init__(self, repository: Repository):
        super().__init__(repository=repository)
