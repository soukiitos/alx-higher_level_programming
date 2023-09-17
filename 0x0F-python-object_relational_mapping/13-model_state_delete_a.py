#!/usr/bin/python3
"""
Delete all State objects with a name containing the letter a
from the database hbtn_0e_6_usa
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from sys import argv


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
    delete_s = session.query(State).filter(State.name.like('%a%')).all()
    for del_s in delete_s:
        session.delete(del_s)
    session.commit()
    session.close()
