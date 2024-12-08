from sqlalchemy import Integer, Column, SmallInteger, CHAR, VARCHAR, Date
from sqlalchemy.dialects.mysql import INTEGER
from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    pass


class HomeGames(Base):
    __tablename__ = 'homegames'
    homegames_ID = Column(INTEGER(12), primary_key=True, autoincrement=True)
    teamID = Column(CHAR(3), nullable=False)
    parkID = Column(VARCHAR(255), nullable=False)
    yearID = Column(SmallInteger, nullable=False)
    firstGame = Column(Date, nullable=True)
    lastGame = Column(Date, nullable=True)
    games = Column(Integer, nullable=True)
    openings = Column(Integer, nullable=True)
    attendance = Column(Integer, nullable=True)
