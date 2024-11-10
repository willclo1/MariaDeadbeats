from sqlalchemy import Column, SmallInteger, VARCHAR, CHAR, Integer
from sqlalchemy.orm import DeclarativeBase

class Base(DeclarativeBase):
    pass

class Managers(Base):
    __tablename__ = 'managers'
    managers_ID = Column(Integer, primary_key=True, autoincrement=True)
    playerID = Column(VARCHAR(9), nullable=False)
    yearID = Column(SmallInteger, nullable=False)
    teamID = Column(CHAR(3), nullable=False)
    inSeason = Column(SmallInteger, nullable=False)
    manager_G = Column(SmallInteger, nullable=True)
    manager_W = Column(SmallInteger, nullable=True)
    manager_L = Column(SmallInteger, nullable=True)
    teamRank = Column(SmallInteger, nullable=True)
    plyrMgr = Column(VARCHAR(1), nullable=True)
    half = Column(SmallInteger, nullable=True)