from sqlalchemy.exc import IntegrityError
from sqlalchemy.sql.sqltypes import NULLTYPE

from Tables.Managers import Managers
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from cfg import engineStr
from tableActions.csvActions import getNewData

def fillManagers():

    engine = create_engine(engineStr)
    Session = sessionmaker(bind=engine)
    session = Session()

    try:
        currData = getNewData("lahman_1871-2023_csv/Managers.csv")

        for row in currData:
            new_record = Managers(
                playerID=row[0],
                yearID=int(row[1]),
                teamID = row[2],
                inSeason=row[4],
                manager_G=row[5],
                manager_W=row[6],
                manager_L= row[7],
                teamRank=row[8],
                plyrMgr=row[9],
                half=NULLTYPE
            )
            session.add(new_record)
            print(f"Added record for playerID: {row[0]}, yearID: {row[1]}")

        #session.commit()
        print("All 2023 records successfully added to the batting table.")

    except IntegrityError as e:
        session.rollback()
        print(f"An integrity error occurred: {e}")
    except Exception as e:
        session.rollback()
        print(f"An error occurred: {e}")
    finally:
        session.close()

fillManagers()
