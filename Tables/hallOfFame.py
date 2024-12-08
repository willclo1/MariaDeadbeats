from sqlalchemy import Integer, Column, SmallInteger, VARCHAR
from sqlalchemy.dialects.mysql import INTEGER
from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    pass


class HallOfFame(Base):
    __tablename__ = 'halloffame'
    halloffame_ID = Column(INTEGER(12), primary_key=True, autoincrement=True)
    playerID = Column(VARCHAR(9), nullable=False)
    yearID = Column(SmallInteger, nullable=False)
    votedBy = Column(VARCHAR(64), nullable=False)
    ballots = Column(SmallInteger, nullable=True)
    needed = Column(SmallInteger, nullable=True)
    votes = Column(SmallInteger, nullable=True)
    inducted = Column(VARCHAR(1), nullable=True)
    category = Column(VARCHAR(20), nullable=True)
    note = Column(VARCHAR(25), nullable=True)
