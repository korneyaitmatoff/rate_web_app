from fastapi import FastAPI
from fastapi import APIRouter

class Server:
    def __init__(self):
        self.app = FastAPI()
    
    def register_routes(self, route: APIRouter):
        self.app.add_route()