from sqlalchemy import Integer, Column, SmallInteger, CHAR, VARCHAR, Double
from sqlalchemy.dialects.mysql import INTEGER
from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    pass


class Teams(Base):
    __tablename__ = 'teams'
    teams_ID = Column(INTEGER(12), primary_key=True, autoincrement=True)
    teamID = Column(CHAR(3), nullable=False)
    yearID = Column(SmallInteger, nullable=False)
    lgID = Column(CHAR(2), nullable=True)
    divID = Column(CHAR(1), nullable=True)
    franchID = Column(VARCHAR(3), nullable=True)
    team_name = Column(VARCHAR(50), nullable=True)
    team_rank = Column(SmallInteger, nullable=True)
    team_G = Column(SmallInteger, nullable=True)
    team_G_home = Column(SmallInteger, nullable=True)
    team_W = Column(SmallInteger, nullable=True)
    team_L = Column(SmallInteger, nullable=True)
    DivWin = Column(VARCHAR(1), nullable=True)
    WCWin = Column(VARCHAR(1), nullable=True)
    LgWin = Column(VARCHAR(1), nullable=True)
    WSWin = Column(VARCHAR(1), nullable=True)
    team_R = Column(SmallInteger, nullable=True)
    team_AB = Column(SmallInteger, nullable=True)
    team_H = Column(SmallInteger, nullable=True)
    team_2B = Column(SmallInteger, nullable=True)
    team_3B = Column(SmallInteger, nullable=True)
    team_HR = Column(SmallInteger, nullable=True)
    team_BB = Column(SmallInteger, nullable=True)
    team_SO = Column(SmallInteger, nullable=True)
    team_SB = Column(SmallInteger, nullable=True)
    team_CS = Column(SmallInteger, nullable=True)
    team_HBP = Column(SmallInteger, nullable=True)
    team_SF = Column(SmallInteger, nullable=True)
    team_RA = Column(SmallInteger, nullable=True)
    team_ER = Column(SmallInteger, nullable=True)
    team_ERA = Column(Double, nullable=True)
    team_CG = Column(SmallInteger, nullable=True)
    team_SHO = Column(SmallInteger, nullable=True)
    team_SV = Column(SmallInteger, nullable=True)
    team_IPouts = Column(Integer, nullable=True)
    team_HA = Column(SmallInteger, nullable=True)
    team_HRA = Column(SmallInteger, nullable=True)
    team_BBA = Column(SmallInteger, nullable=True)
    team_SOA = Column(SmallInteger, nullable=True)
    team_E = Column(SmallInteger, nullable=True)
    team_DP = Column(SmallInteger, nullable=True)
    team_FP = Column(Double, nullable=True)
    park_name = Column(VARCHAR(50), nullable=True)
    team_attendance = Column(Integer, nullable=True)
    team_BPF = Column(SmallInteger, nullable=True)
    team_PPF = Column(SmallInteger, nullable=True)
    team_projW = Column(SmallInteger, nullable=True)
    team_projL = Column(SmallInteger, nullable=True)
