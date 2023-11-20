import uuid
from .database import Base
from sqlalchemy import Column, String, Text, Numeric
from sqlalchemy.dialects.postgresql import UUID


class Product(Base):
    __tablename__ = 'Products'
    id = Column(UUID(as_uuid=True), primary_key=True, nullable=False,
                default=uuid.uuid4)
    name = Column(String,  nullable=False)
    weight = Column(Numeric, nullable=False)
    description = Column(Text, nullable=False)
