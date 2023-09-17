#!/usr/bin/python3
'''List all City objects from the database hbtn_0e_101_usa'''
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from model_city import Base, City
from sys import argv


if __name__ == '__main__':

    username, password, db_name = argv[1], argv[2], argv[3]
    engine = create_engine(
            'mysql+mysqldb://{}:{}@localhost/{}'.format(
                username, password, db_name
                ), pool_pre_ping=True
            )
    session = Session(engine)
    cities = session.query(City).order_by(City.id).all()
    for city in cities:
        s_name = city.s_name
        print("{}: {} -> {}".format(
            city.id,
            city.name,
            s_name
            ))
    session.close()
