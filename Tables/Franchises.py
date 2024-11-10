from sqlalchemy import Integer, Column, SmallInteger, VARCHAR, CHAR
from sqlalchemy.dialects.mysql import INTEGER
from sqlalchemy.orm import DeclarativeBase

class Base(DeclarativeBase):
    pass
class Franchises(Base):
    __tablename__ = 'franchises'
    franchID = Column(VARCHAR(3), primary_key=True, autoincrement=True)
    franchName = Column(VARCHAR(50), nullable=True)
    active = Column(CHAR(1), nullable=True)
    NAassoc = Column(VARCHAR(3), nullable=True)