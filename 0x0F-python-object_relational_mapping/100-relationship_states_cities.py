#!/usr/bin/python3
"""
Create the State “California” with the City “San Francisco”
from the database hbtn_0e_100_usa
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_city import Base, City
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
    Session = sessionmaker(bind=engine)
    session = Session()
    cal = State(name="California")
    sanf = City(name="San Francisco")
    session.add(sanf, cal)
    session.commit()
