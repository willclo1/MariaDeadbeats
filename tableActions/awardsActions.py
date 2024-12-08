from Tables.Awards import Awards
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from .csi3335f2024 import engineStr
from .csvActions import getNewData
import os


def fillAwards():
    engine = create_engine(engineStr)
    Session = sessionmaker(bind=engine)
    session = Session()
    try:
        BASE_DIR = os.path.dirname(os.path.abspath(__file__))

        awards_managers_csv_path = os.path.join(BASE_DIR, 'lahman_1871-2023_csv', 'AwardsManagers.csv')
        awards_players_csv_path = os.path.join(BASE_DIR, 'lahman_1871-2023_csv', 'AwardsPlayers.csv')

        currData = getNewData(awards_managers_csv_path)
        additionalAwardsData = getNewData(awards_players_csv_path)

        totalData = additionalAwardsData + currData

        for row in totalData:
            new_row = Awards(
                awardID=row[1],
                yearID=row[2],
                playerID=row[0],
                lgID=row[3],
                tie=row[4],
                notes=row[5] if row[5] else None
            )
            session.add(new_row)
        session.commit()
        print("Awards table updated")
    except Exception as e:
        session.rollback()
        print(e)
    finally:
        session.close()
