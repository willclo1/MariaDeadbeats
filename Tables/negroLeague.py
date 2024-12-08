from sqlalchemy import Integer, Column, String, SmallInteger, CHAR, VARCHAR
from sqlalchemy.dialects.mysql import INTEGER
from sqlalchemy.orm import DeclarativeBase


# No new divisions in 2023, no update required

class Base(DeclarativeBase):
    pass


class NegroLeague(Base):
    __tablename__ = 'negroLeague'
    negroLeague_id = Column(INTEGER(11), primary_key=True, autoincrement=True)
    playerName = Column(VARCHAR(255), nullable=False)
    position = Column(CHAR(2), nullable=True)
    startYear = Column(SmallInteger, nullable=True)
    endYear = Column(SmallInteger, nullable=True)
