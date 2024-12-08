from sqlalchemy import Integer, Column, String, SmallInteger, CHAR, VARCHAR
from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    pass


class Appearances(Base):
    __tablename__ = 'appearances'
    appearances_ID = Column(Integer, primary_key=True, autoincrement=True)
    playerID = Column(VARCHAR(9), nullable=False)
    yearID = Column(SmallInteger, nullable=False)
    teamId = Column(CHAR(3), nullable=False)
    G_all = Column(SmallInteger, nullable=True)
    GS = Column(SmallInteger, nullable=True)
    G_batting = Column(SmallInteger, nullable=True)
    G_defense = Column(SmallInteger, nullable=True)
    G_p = Column(SmallInteger, nullable=True)
    G_c = Column(SmallInteger, nullable=True)
    G_1b = Column(SmallInteger, nullable=True)
    G_2b = Column(SmallInteger, nullable=True)
    G_3b = Column(SmallInteger, nullable=True)
    G_ss = Column(SmallInteger, nullable=True)
    G_lf = Column(SmallInteger, nullable=True)
    G_cf = Column(SmallInteger, nullable=True)
    G_rf = Column(SmallInteger, nullable=True)
    G_of = Column(SmallInteger, nullable=True)
    G_dh = Column(SmallInteger, nullable=True)
    G_ph = Column(SmallInteger, nullable=True)
    G_pr = Column(SmallInteger, nullable=True)
