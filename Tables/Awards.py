from sqlalchemy import Integer, Column, String, SmallInteger, CHAR, VARCHAR
from sqlalchemy.dialects.mysql import INTEGER
from sqlalchemy.orm import DeclarativeBase

class Base(DeclarativeBase):
    pass

class Awards(Base):
    __tablename__ = 'awards'
    awards_id = Column(INTEGER(12), primary_key=True, autoincrement=True)
    awardID = Column(VARCHAR(255), nullable=False)
    yearID = Column(SmallInteger, nullable=False)
    playerID = Column(VARCHAR(9), nullable=False)
    lgID = Column(CHAR(2), nullable=False)
    tie = Column(VARCHAR(1), nullable=True)
    notes =Column(VARCHAR(100), nullable=True)
