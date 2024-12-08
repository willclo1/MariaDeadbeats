from sqlalchemy import Integer, Column, String, Numeric, create_engine, SmallInteger
from sqlalchemy.dialects.mysql import *
from sqlalchemy.orm import DeclarativeBase, sessionmaker


class Base(DeclarativeBase):
    pass


class AllStarFull(Base):
    __tablename__ = 'allstarfull'
    allstarfull_id = Column(Integer, primary_key=True, autoincrement=True)
    playerID = Column(VARCHAR(9), nullable=False)
    lgID = Column(CHAR(2), nullable=False)
    teamID = Column(CHAR(3), nullable=False)
    yearID = Column(SMALLINT(6), nullable=False)
    gameID = Column(VARCHAR(12))
    GP = Column(SmallInteger)
    startingPos = Column(SmallInteger)
