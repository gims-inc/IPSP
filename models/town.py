
import models
from models.base_model import BaseModel, Base
import sqlalchemy
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship


class Town(BaseModel, Base):
    """Representation of town """
    
    __tablename__ = 'cities'
    region_id = Column(String(60), ForeignKey('regions.id'), nullable=False)
    name = Column(String(128), nullable=False)
   
    def __init__(self, *args, **kwargs):
        """initialize"""
        super().__init__(*args, **kwargs)
