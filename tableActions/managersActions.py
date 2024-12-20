from sqlalchemy.exc import IntegrityError
from sqlalchemy.sql.sqltypes import NULLTYPE

from Tables.Managers import Managers
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from .csi3335f2024 import engineStr
from .csvActions import getNewData
import os


def fillManagers():
    engine = create_engine(engineStr)
    Session = sessionmaker(bind=engine)
    session = Session()

    try:
        BASE_DIR = os.path.dirname(os.path.abspath(__file__))
        batting_post_csv_path = os.path.join(BASE_DIR, 'lahman_1871-2023_csv', 'Managers.csv')
        currData = getNewData(batting_post_csv_path)

        for row in currData:
            new_record = Managers(
                playerID=row[0],
                yearID=int(row[1]),
                teamID=row[2],
                inSeason=row[4],
                manager_G=row[5] if row[5] is not None else None,
                manager_W=row[6] if row[6] is not None else None,
                manager_L=row[7] if row[7] is not None else None,
                teamRank=row[8] if row[8] is not None else None,
                plyrMgr=row[9] if row[9] is not None else None,
                half=None
            )
            session.add(new_record)

        session.commit()
        print("managers updated")
    except Exception as e:
        session.rollback()
        print(f"An error occurred: {e}")
    finally:
        session.close()
