#!/usr/bin/python3
"""
List all State objects, and corresponding City objects,
contained in the database hbtn_0e_101_usa
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from model_city import City
from model_state import Base, State
from sys import argv


if __name__ == '__main__':
    username, password, db_name = argv[1], argv[2], argv[3]
    engine = create_engine(
            'mysql+mysqldb://{}:{}@localhost/{}'.format(
                username, password, db_name
                ), pool_pre_ping=True
            )
    session = Session(engine)
    s_cities = session.query(State, City).join(City).order_by(
            State.id, City.id).all()
    for state, city in s_cities:
        if city.id == 1:
            print("{}: {}".format(state.id, state.name))
        print("\t{}: {}".format(city.id, city.name))
    session.close()
