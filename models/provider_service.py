
import models
from models.base_model import BaseModel, Base
import sqlalchemy
from sqlalchemy import Column, String, Integer, Float, ForeignKey, Table
from sqlalchemy.orm import relationship


class ProviderService(BaseModel,Base):
    __tablename__ = "provider_services"
    service_name = Column(String(128), nullable=False)
    category_id= Column(String(128), ForeignKey('service_categories.id'), nullable=False)


    def __init__(self, *args, **kwargs):
        """initialize"""
        super().__init__(*args, **kwargs)
