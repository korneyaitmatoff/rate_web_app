from src import create_server


def create_app():
    """Запуск сервера"""
    return create_server().get_app()
