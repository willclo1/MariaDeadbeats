from sqlalchemy import Column, SmallInteger, CHAR, VARCHAR
from sqlalchemy.dialects.mysql import INTEGER
from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    pass


class SeriesPost(Base):
    __tablename__ = 'seriesPost'
    seriespost_ID = Column(INTEGER(12), primary_key=True, autoincrement=True)
    teamIDwinner = Column(CHAR(3), nullable=False)
    teamIDloser = Column(CHAR(3), nullable=False)
    yearID = Column(SmallInteger, nullable=False)
    round = Column(VARCHAR(5), nullable=False)
    wins = Column(SmallInteger, nullable=True)
    losses = Column(SmallInteger, nullable=True)
    ties = Column(SmallInteger, nullable=True)
