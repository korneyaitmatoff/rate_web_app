from pydantic import BaseModel


class User(BaseModel):
    """Модель пользователя"""
    name: str
    login: str
    password: str


class AuthUser(BaseModel):
    """Модель пользователя для авторизации"""
    login: str
    password: str
