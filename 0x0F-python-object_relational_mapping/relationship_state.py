#!/usr/bin/python3
'''State class'''
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from model_city import Base, City

Base = declarative_base()


class State(Base):
    '''The class State inherits from Base'''
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
    cities = relationship(
            "City",
            backref="state",
            cascade="all, delete-orphan"
            )
