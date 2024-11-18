from Tables.hallOfFame import HallOfFame
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from cfg import engineStr
from tableActions.csvActions import getNewData


def fillHallOfFame():

    engine = create_engine(engineStr)
    Session = sessionmaker(bind=engine)
    session = Session()

    currData = getNewData("lahman_1871-2023_csv/HallOfFame.csv")

    for row in currData:
        new_row = HallOfFame(
            playerID=row[0],
            yearID=row[1],
            votedBy=row[2],
            ballots=row[3],
            needed=row[4],
            votes=row[5],
            inducted=row[6],
            category=row[7],
            note=row[8]
        )
        print(new_row.playerID, "Added")
        session.add(new_row)


    session.rollback()
    session.close()


fillHallOfFame()