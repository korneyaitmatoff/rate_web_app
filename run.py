from src import server


def create_app():
    """Запуск сервера"""
    return server().get_app()
