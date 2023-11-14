from pydantic import BaseModel


class User(BaseModel):
    """Модель пользователя"""
    name: str
    login: str
    password: str
