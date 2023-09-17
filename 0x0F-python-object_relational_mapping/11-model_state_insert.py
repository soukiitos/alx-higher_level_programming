#!/usr/bin/python3
'''Add the State object “Louisiana” to the database hbtn_0e_6_usa'''
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
    s_add = State(name="Louisiana")
    session.add(s_add)
    session.commit()
    print(s_add.id)
    session.close()
