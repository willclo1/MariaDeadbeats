from sqlalchemy import Integer, Column, VARCHAR, Date
from sqlalchemy.orm import DeclarativeBase

class Base(DeclarativeBase):
    pass

class People(Base):
    __tablename__ = 'people'
    playerID = Column(VARCHAR(9), primary_key=True, nullable=False)
    birthYear = Column(Integer, nullable=True)
    birthMonth = Column(Integer, nullable=True)
    birthDay = Column(Integer, nullable=True)
    birthCountry = Column(VARCHAR(255), nullable=True)
    birthState = Column(VARCHAR(255), nullable=True)
    birthCity = Column(VARCHAR(255), nullable=True)
    deathYear = Column(Integer, nullable=True)
    deathMonth = Column(Integer, nullable=True)
    deathDay = Column(Integer, nullable=True)
    deathCountry = Column(VARCHAR(255), nullable=True)
    deathState = Column(VARCHAR(255), nullable=True)
    deathCity = Column(VARCHAR(255), nullable=True)
    nameFirst = Column(VARCHAR(255), nullable=True)
    nameLast = Column(VARCHAR(255), nullable=True, index=True)
    nameGiven = Column(VARCHAR(255), nullable=True)
    weight = Column(Integer, nullable=True)
    height = Column(Integer, nullable=True)
    bats = Column(VARCHAR(255), nullable=True)
    throws = Column(VARCHAR(255), nullable=True)
    debutDate = Column(Date, nullable=True)
    finalGameDate = Column(Date, nullable=True)