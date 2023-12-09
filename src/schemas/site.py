from typing import Optional
from typing_extensions import TypedDict

from pydantic import BaseModel


class Site(BaseModel):
    """Модель сайта"""
    id: int
    name: str
    description: Optional[str]
    url: str


class SiteDict(TypedDict):
    """Словарь принимаемых аргументов"""
    name: str
    description: Optional[str]
    url: str
