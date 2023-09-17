#!/usr/bin/python3
'''List all State objects that contain the letter a from hbtn_0e_6_usa'''
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv
from model_state import Base, State


if __name__ == '__main__':

    username, password, db_name = argv[1], argv[2], argv[3]
    engine = create_engine(
            'mysql+mysqldb://{}:{}@localhost/{}'.format(
                username, password, db_name
                ), pool_pre_ping=True
            )
    Session = sessionmaker(bind=engine)
    session = Session()
    Base.metadata.create_all(engine)
    res = session.query(State).filter(
            State.name.like('%a%')
            ).order_by(State.id).all()
    for state in res:
        print("{}: {}".format(state.id, state.name))
    session.close()
