#!/usr/bin/python3
"""Start link class to table in database\
   script that prints the State object with the name passed as\
   argument from the database hbtn_0e_6_usa
"""
import sys
from model_state import Base, State

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
    enter = False
    Session = sessionmaker(bind=engine)
    session = Session()
    for st in session.query(State.id).filter(State.name == sys.argv[4]):
        enter = True
        print(st.id)
    if enter is False:
        print("Not found")
