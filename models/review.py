#!/usr/bin/python3
""" Review module for the HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship


class Review(BaseModel, Base):
    """ Review classto store review information """
    __tablename__ = 'reviews'
    
    text = Column(String(1024), nullable=False)

    # ForeignKey to places.id
    place_id = Column(String(60), ForeignKey('places.id'), nullable=False)

    # ForeignKey to users.id
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)

    def __init__(self, *args, **kwargs):
        """Instantiates a new Review"""
        super().__init__(*args, **kwargs)
