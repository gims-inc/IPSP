
import models
from models.base_model import BaseModel, Base
import sqlalchemy
from sqlalchemy import Column, String, Integer, Float, ForeignKey, Table
from sqlalchemy.orm import relationship


class ServiceCategory(BaseModel,Base):

    __tablename__ = 'service_categories'
    category_name = Column(String(128), nullable=False)

    provider_services = relationship('ProviderService', backref='service_category')

    def __init__(self, *args, **kwargs):
        """initialize"""
        super().__init__(*args, **kwargs)
