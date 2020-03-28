#!/usr/bin/python3
"""Start link class to table in database\
   Script that lists all State objects from the database hbtn_0e_6_usa
"""
import sys
from model_state import Base, State
from model_city import City
from sqlalchemy import (create_engine)

if __name__ == "__main__":
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(
            sys.argv[1],
            sys.argv[2],
            sys.argv[3]),
        pool_pre_ping=True)
    Base.metadata.create_all(engine)

    from sqlalchemy.orm import sessionmaker
    Session = sessionmaker(bind=engine)
    session = Session()
    for city, state in session.query(
            City, State).join(
            State, State.id == City.state_id):
        print("{}: ({}) {}".format(state.name, city.id, city.name))
