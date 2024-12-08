from sqlalchemy import Integer, Column, String, SmallInteger, CHAR, VARCHAR
from sqlalchemy.dialects.mysql import INTEGER
from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    pass


class Draft(Base):
    __tablename__ = 'draft'
    drafts_id = Column(INTEGER(11), primary_key=True, autoincrement=True)
    playerID = Column(VARCHAR(9), nullable=False)
    yearID = Column(SmallInteger, nullable=False)
    nameFirst = Column(VARCHAR(255), nullable=True)
    nameLast = Column(VARCHAR(255), nullable=True, index=True)
    round = Column(SmallInteger, nullable=True)
    pick = Column(SmallInteger, nullable=True)
    description = Column(VARCHAR(255), nullable=True)
