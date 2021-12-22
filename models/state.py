#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
import models
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import relationship
from models import city
from os import getenv


class State(BaseModel, Base):
    """ State class """
    if getenv('HBNB_TYPE_STORAGE') == 'db':
        __tablename__ = 'states'
        name = Column(String(128), nullable=False)
        cities = relationship('City')
    else:
        name = ''
        cities = models.storage.all(city.City)

