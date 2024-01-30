from datetime import datetime

from sqlalchemy import Column, VARCHAR, TIMESTAMP, Integer, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(VARCHAR)
    login = Column(VARCHAR)
    password = Column(VARCHAR)
    created_at = Column(TIMESTAMP, default=datetime.utcnow)


class Site(Base):
    __tablename__ = 'sites'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(VARCHAR)
    description = Column(VARCHAR, default=None)
    url = Column(VARCHAR)
    user_id = Column(Integer, ForeignKey(User.id))
    created_at = Column(TIMESTAMP, default=datetime.utcnow)
