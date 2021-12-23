#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy.ext.declarative import declarative_base
import models
from sqlalchemy.orm import relationship, backref
from sqlalchemy.sql.schema import Column, ForeignKey, Table
from sqlalchemy.sql.sqltypes import String, Integer, Float

from os import getenv
from models.review import Review
from models.amenity import Amenity


column_amenity = Column('amenity_id', String(60), ForeignKey('amenities.id'))
place_amenity = Table('place_amenity', Base.metadata,
                      Column('place_id', String(60), ForeignKey('places.id')),
                      column_amenity)

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
        reviews = relationship("Review", backref="place",
                               cascade="all, delete, delete-orphan")
        amenities = relationship('Amenity', secondary='place_amenity',
                                 back_populates='place_amenities',
                                 viewonly=False)

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
        amenity_ids = []

