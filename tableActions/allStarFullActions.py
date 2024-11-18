from Tables.allStarFull import AllStarFull
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from cfg import engineStr
from tableActions.csvActions import getNewData



def fillAllStartFull():
    engine = create_engine(engineStr)
    Session = sessionmaker(bind=engine)
    session = Session()

    currData = getNewData("lahman_1871-2023_csv/AllstarFull.csv")
    for row in currData:
        new_row = AllStarFull(
            playerID = row[0],
            lgID = row[5],
            teamID = row[4],
            yearID = row[1],
            gameID = row[3],
            GP = row[6],
            startingPos = row[7]
        )
        print(new_row.playerID , "Added")
        session.add(new_row)
    session.rollback()

    session.close()
fillAllStartFull()