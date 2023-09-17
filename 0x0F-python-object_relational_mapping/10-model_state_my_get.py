#!/usr/bin/python3
"""
Print the State object with the name passed as argument
from the database hbtn_0e_6_usa
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from sys import argv


if __name__ == '__main__':

    username, password, db_name = argv[1], argv[2], argv[3]
    engine = create_engine(
            'mysl+mysqldb://{}:{}@localhost/{}'.format(
                username, password, db_name
                ), pool_pre_ping=True
            )
    Session = sessionmaker(bind=engine)
    session = Session()
    Base.metadata.create_all(engine)
    res = session.query(State).filter(State.name == argv[4]).first()
    if res:
        print("{}".format(res.id))
    else:
        print("Not found")
    session.close()
