from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


class PostgresqlHandler:
    def __init__(self):
        self.url = f"postgresql+psycopg2://postgres:postgres@locahost/postgres"
        self.engine = create_engine(url=self.url)
        self.session = None

    def __enter__(self):
        self.create_session()

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type:
            raise Exception(f"DATABASE ERROR: \n{exc_type}\n{exc_val}\n{exc_tb}")

        self.close_session()

    def create_session(self):
        self.session = sessionmaker(bind=self.engine)()

    def close_session(self):
        self.session.close()
