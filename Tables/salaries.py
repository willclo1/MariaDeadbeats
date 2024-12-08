from sqlalchemy import Column, SmallInteger, CHAR, VARCHAR, Double
from sqlalchemy.dialects.mysql import INTEGER
from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    pass


class Salaries(Base):
    __tablename__ = 'salaries'
    salaries_ID = Column(INTEGER(12), primary_key=True, autoincrement=True)
    playerID = Column(VARCHAR(9), nullable=False)
    yearId = Column(SmallInteger, nullable=False)
    teamID = Column(CHAR(3), nullable=False)
    salary = Column(Double, nullable=True)
