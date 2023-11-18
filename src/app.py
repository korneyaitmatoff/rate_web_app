from fastapi import FastAPI
from fastapi import APIRouter

from src.database.handler import DatabaseHandler


class Server:
    """Класс для управления сервером"""
    db_handler: DatabaseHandler

    def __init__(self):
        self.app = FastAPI()
        self.db_handler = DatabaseHandler()
        self.test_db_connection()

    def register_routes(self, router: APIRouter):
        """Метод для регистрации роутов"""
        self.app.include_router(router)

    def test_db_connection(self):
        """Регистрация и проверка соединения"""
        self.db_handler.test_connection()

    def get_app(self):
        """Получить объект приложени"""
        return self.app
