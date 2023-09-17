#!/usr/bin/python3
"""
Create the State “California” with the City “San Francisco”
from the database hbtn_0e_100_usa
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from relationship_city import City
from relationship_state import State
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
    cal = State(name="California")
    sanf = City(name="San Francisco")
    cal.cities.append(sanf)
    session.add(cal)
    session.add(sanf)
    session.commit()
    session.close()
