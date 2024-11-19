from Tables.allStarFull import AllStarFull
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from cfg import engineStr
from tableActions.csvActions import getNewData



def fillAllStartFull():
    engine = create_engine(engineStr)
    Session = sessionmaker(bind=engine)
    session = Session()
    try:
        currData = getNewData("lahman_1871-2023_csv/AllstarFull.csv")
        for row in currData:
            new_row = AllStarFull(
                playerID = row[0],
                lgID = row[5],
                teamID = row[4],
                yearID = row[1],
                gameID = row[3] if row[3] else None,
                GP = row[6] if row[6] else None,
                startingPos = row[7] if row[7] else None
            )
            session.add(new_row)
        session.commit()
        print("AllStar data added")

    except Exception as e:
        session.rollback()
        print(e)
    finally:
        session.close()