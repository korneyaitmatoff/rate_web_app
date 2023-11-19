from src.app import Server
from src.database import tables
from src.routes import test_router
from src.repositories.user_repository import UserRepository
from src.repositories.site_repository import SiteRepository
from src.services.user_service import UserService
from src.services.site_service import SiteService


def create_server() -> Server:
    """Функция для создания сервера и его запуска"""
    server = Server()

    server.register_routes(router=test_router)

    return server


# Экземпляр сервера
server = create_server()

# Объявление сервисов сущностей
user_service = UserService(repository=UserRepository(tables.Site))
site_service = SiteService(repository=SiteRepository(tables.User))
