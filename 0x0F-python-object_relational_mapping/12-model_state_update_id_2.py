#!/usr/bin/python3
"""Start link class to table in database\
   Script that adds the State object “Louisiana”\
   to the database hbtn_0e_6_usa
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
    Session = sessionmaker(bind=engine)
    session = Session()
    changed_st = session.query(State).filter_by(id=2).first()
    changed_st.name = 'New Mexico'
    session.commit()
