from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from Tables.homeGames import HomeGames
from .cfg import engineStr
from .csvActions import getPeopleData, getNewData, getHomeData
from datetime import datetime
import os


def parse_date(date_str):
    try:
        return datetime.strptime(date_str, "%Y-%m-%d").date() if date_str else None
    except ValueError:
        return None


def fillHomeGame():
    engine = create_engine(engineStr)
    Session = sessionmaker(bind=engine)
    session = Session()

    try:


        BASE_DIR = os.path.dirname(os.path.abspath(__file__))
        batting_post_csv_path = os.path.join(BASE_DIR, 'lahman_1871-2023_csv', 'HomeGames.csv')
        currData = getHomeData(batting_post_csv_path)

        for row in currData:
            new_person = HomeGames(
                teamID=row[2],
                parkID=row[3],
                yearID=row[0],
                firstGame=parse_date(row[4]) if row[4] else None,
                lastGame=parse_date(row[5]) if row[5] else None,
                games=row[6] if row[6] else None,
                openings=row[7] if row[7] else None,
                attendance=row[8] if row[8] else None,

            )
            session.add(new_person)

        session.commit()
        print("home games updated")
    except Exception as e:
        session.rollback()
    finally:
        session.close()
