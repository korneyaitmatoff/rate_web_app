from src.app import Server
from src.database import tables
from src.routes import test_router, user_router
from src.repositories.user_repository import UserRepository
from src.repositories.site_repository import SiteRepository
from src.services.user_service import UserService
from src.services.site_service import SiteService


def create_server() -> Server:
    """Функция для создания сервера и его запуска"""
    server = Server()

    # Регистрация роутов
    server.register_routes(router=test_router)
    server.register_routes(router=user_router)

    return server


# Экземпляр сервера
server = create_server()


# Объявление сервисов сущностей
def user_service():
    return UserService(repository=UserRepository(tables.Site))


def site_service():
    return SiteService(repository=SiteRepository(tables.User))
