#!/usr/bin/python3
'''List all City objects from the database hbtn_0e_101_usa'''
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, relationship
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
    Session = sessionmaker(bind=engine)
    session = Session()
    cities = session.query(City).order_by(City.id)
    for city in cities:
        s_name = city.s_name
        print("{}: {} -> {}".format(
            city.id,
            city.name,
            s_name
            ))
    session.close()
