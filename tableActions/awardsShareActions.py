from Tables.awardsShare import AwardsShare
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from cfg import engineStr
from tableActions.csvActions import getNewData


def fillAwardsShare():

    engine = create_engine(engineStr)
    Session = sessionmaker(bind=engine)
    session = Session()

    currData = getNewData("lahman_1871-2023_csv/AwardsSharePlayers.csv")
    additionalAwardsData = getNewData("lahman_1871-2023_csv/AwardsShareManagers.csv")

    totalData = additionalAwardsData + currData

    for row in totalData:
        new_row = AwardsShare(
            awardID=row[0],
            yearID = row[1],
            playerID=row[3],
            lgID=row[2],
            pointsWon=row[4],
            pointsMax=row[5],
            votesFirst=row[6]
        )
        print(new_row.playerID, "Added")
        session.add(new_row)


    #session.rollback()

    session.commit()


    session.close()

fillAwardsShare()