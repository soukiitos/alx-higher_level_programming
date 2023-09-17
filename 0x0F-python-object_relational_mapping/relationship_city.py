#!/usr/bin/python3
'''City class'''
from sqlalchemy import Column, Integer, String, ForeignKey
from relationship_state import Base


class City(Base):
    '''The class City inherits from Base'''
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('state.id'), nullable=False)
