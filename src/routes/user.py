from typing import List

from fastapi import APIRouter
from src.schemas.user import User
from src import user_service

router = APIRouter(prefix='/user', tags=['user'])


@router.get("/{id}", responses={400: {"description": "Bad request"}}, response_model=List[User],
            description="Получение пользователя")
def get(id):
    return user_service().read(id=id)


@router.post("", responses={400: {"description": "Bad request"}}, response_model=User,
             description="Создание пользователя")
def create(user: User):
    print(user)
