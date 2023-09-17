#!/usr/bin/python3
'''Class of a city'''
from sqlalchemy import Column, Integer, String, ForeignKey
from model_state import Base

Base = declarative_base()


class City(Base):
    '''City in database'''
    __tablename__ = "cities"
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states_id'), nullable=False)
