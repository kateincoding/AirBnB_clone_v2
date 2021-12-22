#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
import models
from sqlalchemy import Table, Column
from sqlalchemy import Integer, Float, String
from sqlalchemy.orm import relationship, backref
from os import getenv
from sqlalchemy import ForeignKey
from models.review import Review

if getenv('HBNB_TYPE_STORAGE') == 'db':
    class Place(BaseModel, Base):
        """ A place to stay """
        __tablename__ = 'places'
        city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
        user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
        name = Column(String(128), nullable=False)
        description = Column(String(1024), nullable=False)
        number_rooms = Column(Integer, nullable=False, default=0)
        number_bathrooms = Column(Integer, nullable=False, default=0)
        max_guest = Column(Integer, nullable=False, default=0)
        price_by_night = Column(Integer, nullable=False, default=0)
        latitude = Column(Float)
        longitude = Column(Float)
        reviews = relationship("Review", backref="place", cascade="all, delete, delete-orphan")

else:
    class Place(BaseModel):
        city_id = ''
        user_id = ''
        name = ''
        description = ''
        number_rooms = ''
        number_bathrooms = ''
        max_guest = ''
        price_by_night = ''
        latitude = ''
        longitude = ''
        reviews = models.storage.all(Review)
