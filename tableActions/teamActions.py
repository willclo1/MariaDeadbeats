from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import SQLAlchemyError
from .csvActions import getNewData
from .csi3335f2024 import engineStr
from Tables.Teams import Teams
import math
import os

def fillTeams():
    engine = create_engine(engineStr)
    Session = sessionmaker(bind=engine)
    session = Session()

    try:

        BASE_DIR = os.path.dirname(os.path.abspath(__file__))
        batting_post_csv_path = os.path.join(BASE_DIR, 'lahman_1871-2023_csv', 'Teams.csv')
        currData = getNewData(batting_post_csv_path)

        # Loop through rows and add them to the Teams table
        for row in currData:
            team_projW = float(row[14])/float(row[26])
            team_projW = team_projW ** 1.83
            team_projW = team_projW / (team_projW + 1)
            team_projW = math.floor(team_projW * 162)
            team_projL = 162 - team_projW

            new_team = Teams(
                yearID=row[0],
                lgID=row[1],
                teamID=row[2],
                franchID=row[3],
                divID=row[4],
                team_rank=row[5],
                team_G=row[6],
                team_G_home=row[7] if row[7] else None,
                team_W=row[8],
                team_L=row[9],
                DivWin=row[10],
                WCWin=row[11],
                LgWin=row[12],
                WSWin=row[13],
                team_R=row[14],
                team_AB=row[15],
                team_H=row[16],
                team_2B=row[17],
                team_3B=row[18],
                team_HR=row[19],
                team_BB=row[20],
                team_SO=row[21],
                team_SB=row[22],
                team_CS=row[23],
                team_HBP=row[24],
                team_SF=row[25],
                team_RA=row[26],
                team_ER=row[27],
                team_ERA=row[28] if row[28] else None,
                team_CG=row[29],
                team_SHO=row[30],
                team_SV=row[31],
                team_IPouts=row[32],
                team_HA=row[33],
                team_HRA=row[34],
                team_BBA=row[35],
                team_SOA=row[36],
                team_E=row[37],
                team_DP=row[38],
                team_FP=row[39] if row[39] else None,
                team_name=row[40],
                park_name=row[41] if row[41] else None,
                team_attendance=row[42],
                team_BPF=row[43],
                team_PPF=row[44],
                team_projW=team_projW,
                team_projL=team_projL

            )
            session.add(new_team)

        session.commit()
        print("teams data updated")
    except Exception as e:
        session.rollback()
        print(f"An error occurred: {e}")
    finally:
        session.close()
