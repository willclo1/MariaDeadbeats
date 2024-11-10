from sqlalchemy import Integer, Column, SmallInteger, CHAR, VARCHAR, Date
from sqlalchemy.dialects.mysql import INTEGER
from sqlalchemy.orm import DeclarativeBase

class Base(DeclarativeBase):
    pass
class Leagues(Base):
    __tablename__ = 'leagues'
    lgID = Column(CHAR(2), primary_key=True, autoincrement=True)
    league_name = Column(VARCHAR(50), nullable=False)
    league_active = Column(CHAR(1), nullable=False)


