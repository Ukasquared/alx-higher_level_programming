#!/usr/bin/python3
""" class definition of a State and an instance Base = declarative_base()"""
from sqlalchemy import Column, Integer, String
from sqlalchemy import Foreignkey
from model_state import Base


class City(Base):
    """create state table"""
    __tablename__ = 'cities'
    id = Column(Integer, autoincrement=True,
                primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, Foreignkey('states.id'), nullable=False)