from sqlalchemy import Column, VARCHAR
from sqlalchemy.orm import DeclarativeBase

class Base(DeclarativeBase):
    pass

class Parks(Base):
    __tablename__ = 'parks'
    parkID = Column(VARCHAR(255), primary_key=True, nullable=False)
    park_alias = Column(VARCHAR(255), nullable=True)
    park_name = Column(VARCHAR(255), nullable=True)
    city = Column(VARCHAR(255), nullable=True)
    state = Column(VARCHAR(255), nullable=True)
    country = Column(VARCHAR(255), nullable=True)