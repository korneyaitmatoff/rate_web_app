from typing import List

from fastapi import FastAPI

from src.app import App
from src.database import tables
from src.repositories import UserRepository
from src.repositories import SiteRepository
from src.repositories import CommentRepository
from src.services.user_service import UserService
from src.services.site_service import SiteService
from src.services.comment_service import CommentService
from src.schemas.user import User
from src.schemas.site import Site
from src.schemas.comment import Comment
from src.routes.user import UserRouter
from src.routes.site import SiteRouter
from src.routes.comment import CommentRouter

server = (app := App(server=FastAPI())).get_app()

# Сервисы
user_service = UserService(repository=UserRepository(table=tables.User, database_handler=app.db_handler))
site_service = SiteService(repository=SiteRepository(table=tables.Site, database_handler=app.db_handler))
comment_service = CommentService(repository=CommentRepository(table=tables.Comment, database_handler=app.db_handler))

# Роутеры
app.register_routes([
    UserRouter(
        service=user_service,
        routes=[
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
            {
                "path": "/auth",
                "responses": {400: {"description": "Bad request"}},
                "response_model": int,
                "description": "Верификация данных аутентификации", "methods": ['POST'],
                "endpoint": user_service.auth
            },
        ]
    ).get_router(),
    SiteRouter(
        service=site_service,
        routes=[
            {
                "path": "",
                "responses": {400: {"description": "Bad request"}},
                "response_model": List[Site],
                "description": "Получение списка сайтов", "methods": ['GET'],
                "endpoint": site_service.get_sites
            },
            {
                "path": "/{site_id}",
                "responses": {400: {"description": "Bad request"}},
                "response_model": Site,
                "description": "Получение сайта по id", "methods": ['GET'],
                "endpoint": site_service.get_site_by_id
            },
            {
                "path": "",
                "responses": {400: {"description": "Bad request"}},
                "response_model": Site,
                "description": "Создание сайта", "methods": ['POST'],
                "endpoint": site_service.create_site
            },
            {
                "path": "/{site_id}",
                "responses": {400: {"description": "Bad request"}},
                "description": "Удаление сайта", "methods": ['PUT'],
                "endpoint": site_service.delete_site
            },
            {
                "path": "/{site_id}",
                "responses": {400: {"description": "Bad request"}},
                "response_model": Site,
                "description": "Изменение данных сайта", "methods": ['PATCH'],
                "endpoint": site_service.edit_site
            },
            {
                "path": "/user/{user_id}",
                "responses": {400: {"description": "Bad request"}},
                "response_model": list[Site],
                "description": "Получение списка сайтов по id пользователя", "methods": ['GET'],
                "endpoint": site_service.get_sites_by_user_id
            },
            {
                "path": "/data/{site_id}",
                "responses": {400: {"description": "Bad request"}},
                "description": "Всех данных сайта", "methods": ['GET'],
                "endpoint": site_service.get_site_data
            },
        ]
    ).get_router(),
    CommentRouter(
        service=comment_service,
        routes=[
            {
                "path": "/{site_id}",
                "responses": {400: {"description": "Bad request"}},
                "response_model": List[Comment],
                "description": "Получение списка комментариев сайта", "methods": ['GET'],
                "endpoint": comment_service.get_comments_by_site
            },
            {
                "path": "/{comment_id}",
                "responses": {400: {"description": "Bad request"}},
                "description": "Изменение комментария", "methods": ['PATCH'],
                "endpoint": comment_service.edit_comment
            },
            {
                "path": "/{comment_id}",
                "responses": {400: {"description": "Bad request"}},
                "description": "Удаление комментария", "methods": ['DELETE'],
                "endpoint": comment_service.delete_comment
            },
            {
                "path": "/{site_id}/{user_id}",
                "responses": {400: {"description": "Bad request"}},
                "description": "Добавление комментария", "methods": ['POST'],
                "endpoint": comment_service.add_site_comment
            },
        ]
    ).get_router()
])
