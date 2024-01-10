#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from models import storage_t
from models.city import City
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """ State class """
    if storage_t == 'db':
        __tablename__ = 'states'
        name = Column(String(128), nullable=False)
        cities = relationship('City',
                              backref='state',
                              cascade='all, delete, delete-orphan')
    else:
        name = ""

    def __init__(self, *args, **kwargs):
        """Initializes a State instance"""
        super().__init__(*args, **kwargs)

    if storage_t != 'db':
        @property
        def cities(self):
            """Getter for list of city instances related to the state"""
            from models import storage
            city_list = []
            all_cities = storage.all(City)
            for city in all_cities.values():
                if city.state_id == self.id:
                    city_list.append(city)

            return city_list
