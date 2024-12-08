from sqlalchemy import Column, SmallInteger, VARCHAR
from sqlalchemy.dialects.mysql import INTEGER
from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    pass


class CollegePlaying(Base):
    __tablename__ = 'collegeplaying'
    collegeplaying_id = Column(INTEGER(11), primary_key=True, autoincrement=True)
    playerID = Column(VARCHAR(9), nullable=False)
    schoolID = Column(VARCHAR(15), nullable=True)
    yearID = Column(SmallInteger, nullable=True)
