#!/usr/bin/python3
"""  python file that contains the class definition of\
     a State and an instance Base = declarative_base():\
"""
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String
Base = declarative_base()


class State(Base):
    """ class of states column """

    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, unique=True, nullable=False)
    name = Column(String(128), nullable=False)

    cities = relationship(
        "City",
        back_populates='states',
        cascade=False)
