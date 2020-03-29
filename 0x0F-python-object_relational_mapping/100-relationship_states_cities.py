#!/usr/bin/python3
"""Start link class to table in database\
   Script that lists all State objects from the database hbtn_0e_6_usa
"""
import sys
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy.orm import relationship, aliased, backref
from sqlalchemy import (create_engine)
#state = aliased(State)

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
    Base.metadata.create_all(engine)
    cal = State(name="California")
    cal.cities = [City(name="San Francisco")]
    session.add(cal)
    session.commit()
    session.close()
