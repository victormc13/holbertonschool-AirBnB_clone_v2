#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, Float, ForeignKey, Table
from sqlalchemy.orm import relationship

# Define the association table for the Many-To-Many relationship
place_amenity = Table('place_amenity', Base.metadata,
                     Column('place_id', String(60), ForeignKey('places.id'),
                            primary_key=True, nullable=False),
                     Column('amenity_id', String(60), ForeignKey('amenities.id'),
                            primary_key=True, nullable=False)
                     )


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = 'places'
    
    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    
    # Add a relationship to City and User, and Review
    city = relationship("City", back_populates="places")
    user = relationship("User", back_populates="places")
    reviews = relationship("Review", back_populates="place", cascade="all, delete-orphan")
    
    # Define the relationship with Amenity as secondary to place_amenity
    amenities = relationship("Amenity", secondary=place_amenity, back_populates="place_amenities", viewonly=False)

    # Getter attribute for amenities
    @property
    def amenities(self):
        """Getter attribute that returns the list of Amenity instances based on amenity_ids"""
        from models import storage
        amenity_list = []
        for amenity_id in self.amenity_ids:
            amenity = storage.get("Amenity", amenity_id)
            if amenity:
                amenity_list.append(amenity)
        return amenity_list

    # Setter attribute for amenities
    @amenities.setter
    def amenities(self, amenity):
        """Setter attribute that handles append method for adding an Amenity.id to amenity_ids"""
        if amenity.__class__.__name__ == "Amenity":
            self.amenity_ids.append(amenity.id)