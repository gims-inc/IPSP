
import models
from models.base_model import BaseModel, Base
from models.town import Town
import sqlalchemy
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship


class Region(BaseModel, Base):
    """Representation of region """
    
    __tablename__ = 'regions'
    name = Column(String(128), nullable=False)
    towns = relationship("Town",
                              backref="region",
                              cascade="all, delete, delete-orphan")
    

    def __init__(self, *args, **kwargs):
        """initializes region"""
        super().__init__(*args, **kwargs)

    
    @property
    def towns(self):
        """getter for list of town instances related to the Region"""
        town_list = []
        all_towns = models.storage.all(Town)
        for town in all_towns.values():
            if town.state_id == self.id:
                town_list.append(town)
        return town_list
