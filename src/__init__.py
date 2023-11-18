from src.app import Server
from src.routes import test_router


def create_server() -> Server:
    server = Server()

    server.register_routes(router=test_router)

    return server


server = create_server()
