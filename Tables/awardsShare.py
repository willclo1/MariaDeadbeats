from sqlalchemy import Integer, Column, String, SmallInteger, CHAR, VARCHAR
from sqlalchemy.dialects.mysql import INTEGER, DOUBLE
from sqlalchemy.orm import DeclarativeBase

class Base(DeclarativeBase):
    pass
class AwardsShare(Base):
    __tablename__ = 'awardsshare'
    awardshare_id = Column(INTEGER(12), primary_key=True, autoincrement=True)
    awardID = Column(VARCHAR(255), nullable=False)
    yearID = Column(SmallInteger, nullable=False)
    playerID = Column(VARCHAR(9), nullable=False)
    lgID = Column(CHAR(2), nullable=False)
    pointsWon = Column(DOUBLE, nullable=True)
    pointsMax = Column(SmallInteger, nullable=True)
    votesFirst = Column(DOUBLE, nullable=True)