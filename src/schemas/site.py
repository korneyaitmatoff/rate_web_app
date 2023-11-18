from typing import Optional
from pydantic import BaseModel


class Site(BaseModel):
    """Модель сайта"""
    name: str
    description: Optional[str]
    url: str
