#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Table, ForeignKey
from sqlalchemy.orm import relationship


# Define the association table for the Many-To-Many relationship
association_table = Table('place_amenity', BaseModel.metadata,
                         Column('place_id', String(60), ForeignKey('places.id'),
                                primary_key=True, nullable=False),
                         Column('amenity_id', String(60), ForeignKey('amenities.id'),
                                primary_key=True, nullable=False)
                         )


class Amenity(BaseModel):
    """ Amenity class """
    __tablename__ = 'amenities'
    
    name = Column(String(128), nullable=False)

    # Establish the Many-To-Many relationship with Place
    place_amenities = relationship("Place", secondary=association_table, back_populates="amenities")