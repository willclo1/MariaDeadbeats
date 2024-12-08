from sqlalchemy import Integer, Column, SmallInteger, VARCHAR, CHAR
from sqlalchemy.dialects.mysql import INTEGER
from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    pass


class FieldingPost(Base):
    __tablename__ = 'fieldingpost'
    fieldingpost_ID = Column(INTEGER(12), primary_key=True, autoincrement=True)
    playerID = Column(VARCHAR(9), nullable=False)
    yearID = Column(SmallInteger, nullable=False)
    teamID = Column(CHAR(3), nullable=False)
    round = Column(VARCHAR(10), nullable=False)
    position = Column(VARCHAR(2), nullable=True)
    f_G = Column(SmallInteger, nullable=True)
    f_GS = Column(SmallInteger, nullable=True)
    f_InnOuts = Column(SmallInteger, nullable=True)
    f_PO = Column(SmallInteger, nullable=True)
    f_A = Column(SmallInteger, nullable=True)
    f_E = Column(SmallInteger, nullable=True)
    f_DP = Column(SmallInteger, nullable=True)
    f_TP = Column(SmallInteger, nullable=True)
    f_PB = Column(SmallInteger, nullable=True)
