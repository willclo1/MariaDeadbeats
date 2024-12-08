from sqlalchemy import Integer, Column, SmallInteger, CHAR, VARCHAR, Double
from sqlalchemy.dialects.mysql import INTEGER
from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    pass


class Batting(Base):
    __tablename__ = 'batting'
    batting_ID = Column(INTEGER(12), primary_key=True, autoincrement=True)
    playerID = Column(VARCHAR(9), nullable=False)
    yearId = Column(SmallInteger, nullable=False)
    teamID = Column(CHAR(3), nullable=False)
    stint = Column(SmallInteger, nullable=False)
    b_G = Column(SmallInteger, nullable=True)
    b_AB = Column(SmallInteger, nullable=True)
    b_R = Column(SmallInteger, nullable=True)
    b_H = Column(SmallInteger, nullable=True)
    b_2B = Column(SmallInteger, nullable=True)
    b_3B = Column(SmallInteger, nullable=True)
    b_HR = Column(SmallInteger, nullable=True)
    b_RBI = Column(SmallInteger, nullable=True)
    b_SB = Column(SmallInteger, nullable=True)
    b_CS = Column(SmallInteger, nullable=True)
    b_BB = Column(SmallInteger, nullable=True)
    b_WAR = Column(Double, nullable=True)
    b_SO = Column(SmallInteger, nullable=True)
    b_IBB = Column(SmallInteger, nullable=True)
    b_HBP = Column(SmallInteger, nullable=True)
    b_SH = Column(SmallInteger, nullable=True)
    b_SF = Column(SmallInteger, nullable=True)
    b_GIDP = Column(SmallInteger, nullable=True)
