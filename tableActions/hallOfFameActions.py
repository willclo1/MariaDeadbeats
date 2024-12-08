from Tables.hallOfFame import HallOfFame
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from .cfg import engineStr
from .csvActions import getNewData
import os


def fillHallOfFame():

    engine = create_engine(engineStr)
    Session = sessionmaker(bind=engine)
    session = Session()

    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    batting_post_csv_path = os.path.join(BASE_DIR, 'lahman_1871-2023_csv', 'HallOfFame.csv')
    currData = getNewData(batting_post_csv_path)
    try:
        for row in currData:
            new_row = HallOfFame(
                playerID=row[0],
                yearID=row[1],
                votedBy=row[2],
                ballots=row[3] if row[3] else None,
                needed=row[4] if row[4] else None,
                votes=row[5] if row[5] else None,
                inducted=row[6] if row[6] else None,
                category=row[7] if row[7] else None,
                note=row[8] if row[8] else None,
            )
            session.add(new_row)

        session.commit()
        print("hall of fame updated")
    except Exception as e:
        session.rollback()
        print(e)
    finally:
        session.close()
