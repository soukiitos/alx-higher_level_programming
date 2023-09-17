#!/usr/bin/python3
"""
List all State objects, and corresponding City objects,
contained in the database hbtn_0e_101_usa
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from relationship_city import City
from relationship_state import Base, State
from sys import argv


if __name__ == '__main__':
    username, password, db_name = argv[1], argv[2], argv[3]
    engine = create_engine(
            'mysql+mysqldb://{}:{}@localhost/{}'.format(
                username, password, db_name
                ), pool_pre_ping=True
            )
    Base.metadata.create_all(engine)
    session = Session(engine)
    for state in session.query(State).order_by(State.id).all():
        print("{}: {}".format(state.id, state.name))
        for city in state.cities:
            print("\t{}: {}".format(city.id, city.name))
    session.close()
