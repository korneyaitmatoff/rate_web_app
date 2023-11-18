from typing import List

from fastapi import APIRouter
from src.schemas.user import User
from src.depends import get_user_service

router = APIRouter(prefix='/user', tags=['user'])


@router.get("", responses={400: {"description": "Bad request"}}, response_model=List[User],
            description="Получение списка пользователей")
def get_all_users():
    return get_user_service().get_users()


@router.post("", responses={400: {"description": "Bad request"}}, response_model=User,
             description="Создание пользователя")
def create_user(user: User):
    return get_user_service().create_user(data=user)
