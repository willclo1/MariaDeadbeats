from Tables.allStarFull import AllStarFull
from Tables.appearances import Appearances
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from cfg import cfg
from tableActions.csvActions import getNewData


def fillAllStartFull():
    engineStr = "mysql+pymysql://" + cfg.get("user") + ":" + cfg.get("password") + "@" + cfg.get(
        "host") + ":3306/" + cfg.get("db")

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

fillAllStartFull()