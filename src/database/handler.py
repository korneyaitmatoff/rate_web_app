from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker


class PostgresqlHandler:
    def __init__(self):
        self.url = f"postgresql://tavern:tavern@45.9.43.40:5432/app"
        self.engine = create_engine(url=self.url)
        self.session = None

    def __enter__(self):
        self.create_session()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type:
            raise Exception(
                f'Произошла ошибка во время работы с БД!\n'
                f'\tТип:      {exc_type}\n'
                f'\tЗначение: {exc_val}\n'
                f'\tСтек:     {exc_tb}'
            )

        self.close_session()

    def create_session(self):
        self.session = sessionmaker(bind=self.engine)()

    def close_session(self):
        self.session.close()

    def test_connection(self):
        self.session.execute(text("SELECT 1;"))
