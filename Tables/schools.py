from sqlalchemy import Column, VARCHAR
from sqlalchemy.orm import DeclarativeBase

class Base(DeclarativeBase):
    pass

class Schools(Base):
    __tablename__ = 'schools'
    schoolId = Column(VARCHAR(15), primary_key=True, nullable=False)
    school_name = Column(VARCHAR(255), nullable=True)
    school_city = Column(VARCHAR(55), nullable=True)
    school_state = Column(VARCHAR(55), nullable=True)
    school_country = Column(VARCHAR(55), nullable=True)