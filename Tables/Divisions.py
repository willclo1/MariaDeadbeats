from sqlalchemy import Integer, Column, String, SmallInteger, CHAR, VARCHAR
from sqlalchemy.dialects.mysql import INTEGER
from sqlalchemy.orm import DeclarativeBase

class Base(DeclarativeBase):
    pass

class Divisions(Base):
    __tablename__ = 'divisions'
    divisions_ID = Column(INTEGER(11), primary_key=True, autoincrement=True)
    divID = Column(CHAR(2), nullable=False)
    lgID = Column(CHAR(2), nullable=False)
    division_name = Column(VARCHAR(50), nullable=False)
    division_active = Column(CHAR(1), nullable=False)
