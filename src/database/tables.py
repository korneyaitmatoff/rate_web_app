from datetime import datetime

from sqlalchemy import Column, VARCHAR, TIMESTAMP, Integer
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Site(Base):
    __tablename__ = 'sites'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(VARCHAR)
    description = Column(VARCHAR, default=None)
    url = Column(VARCHAR)
    created_at = Column(TIMESTAMP, default=datetime.utcnow)


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(VARCHAR)
    login = Column(VARCHAR)
    password = Column(VARCHAR)
    created_at = Column(TIMESTAMP, default=datetime.utcnow)
