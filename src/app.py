from fastapi import FastAPI
from fastapi import APIRouter

from src.database.handler import PostgresqlHandler


class Server:
    db: PostgresqlHandler

    def __init__(self):
        self.app = FastAPI()
        self.register_db_connection()

    def register_routes(self, router: APIRouter):
        self.app.include_router(router)

    def register_db_connection(self):
        db = PostgresqlHandler()
        db.create_session()
        db.test_connection()

    def get_app(self):
        return self.app
