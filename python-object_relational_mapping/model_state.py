#!/usr/bin/python3

from sqlalchemy import Integer, Column, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class State(Base):
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, nullable=False)
    name = Colums(String(128), nullable=False)
