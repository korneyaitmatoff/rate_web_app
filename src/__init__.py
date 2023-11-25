from typing import List

from fastapi import FastAPI

from src.app import App
from src.database import tables
from src.repositories import UserRepository
from src.services.user_service import UserService
from src.schemas.user import User
from src.routes.user import UserRouter

server = (app := App(server=FastAPI())).get_app()

# сервисы
user_service = UserService(repository=UserRepository(table=tables.User, database_handler=app.db_handler))

# роуты
USER_ROUTES = [
    {
        "path": "",
        "responses": {400: {"description": "Bad request"}},
        "response_model": List[User],
        "description": "Получение списка пользователей", "methods": ['GET'],
        "endpoint": user_service.get_users
    },
    {
        "path": "/{user_id}",
        "responses": {400: {"description": "Bad request"}},
        "response_model": User,
        "description": "Получение пользователя по id", "methods": ['GET'],
        "endpoint": user_service.get_user_by_id
    },
    {
        "path": "",
        "responses": {400: {"description": "Bad request"}},
        "response_model": User,
        "description": "Создание пользователя", "methods": ['POST'],
        "endpoint": user_service.create_user
    },
    {
        "path": "/{user_id}",
        "responses": {400: {"description": "Bad request"}},
        "description": "Удаление пользователя", "methods": ['PUT'],
        "endpoint": user_service.delete_user
    },
    {
        "path": "/{user_id}",
        "responses": {400: {"description": "Bad request"}},
        "response_model": User,
        "description": "Изменение данных пользователя", "methods": ['PATCH'],
        "endpoint": user_service.edit_user
    },
]

# роутеры
user_router = UserRouter(service=user_service, routes=USER_ROUTES).get_router()

app.register_routes([
    user_router,
])
