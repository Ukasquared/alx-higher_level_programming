#!/usr/bin/python3
import sys
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format
                       (sys.argv[1], sys.argv[2],
                        sys.argv[3]), pool_pre_ping=True)

Base = declarative_base()


class State(Base):
    __tablename__ = 'states'
    id = Column(Integer, autoincrement=True, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)


Base.metadata.create_all(engine)
