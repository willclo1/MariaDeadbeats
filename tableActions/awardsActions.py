from Tables.Awards import Awards
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from cfg import engineStr
from tableActions.csvActions import getNewData


def fillAwards():

    engine = create_engine(engineStr)
    Session = sessionmaker(bind=engine)
    session = Session()
    try:
        currData = getNewData("lahman_1871-2023_csv/AwardsManagers.csv")
        additionalAwardsData = getNewData("lahman_1871-2023_csv/AwardsPlayers.csv")

        totalData = additionalAwardsData + currData

        for row in totalData:
            new_row = Awards(
                awardID=row[1],
                yearID = row[2],
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