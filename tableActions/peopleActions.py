from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from Tables.People import People
from .csi3335f2024 import engineStr
from .csvActions import getPeopleData
from datetime import datetime
import os


def parse_date(date_str):
    try:
        return datetime.strptime(date_str, "%Y-%m-%d").date() if date_str else None
    except ValueError:
        return None


def fillPeople():
    engine = create_engine(engineStr)
    Session = sessionmaker(bind=engine)
    session = Session()

    try:
        BASE_DIR = os.path.dirname(os.path.abspath(__file__))
        batting_post_csv_path = os.path.join(BASE_DIR, 'lahman_1871-2023_csv', 'People.csv')
        currData = getPeopleData(batting_post_csv_path)


        for row in currData:
            new_person = People(
                playerID=row[1],  # Map "playerID" column
                birthYear=int(row[2]) if row[2] else None,
                birthMonth=int(row[3]) if row[3] else None,
                birthDay=int(row[4]) if row[4] else None,
                birthCountry=row[6] if row[6] else None,
                birthState=row[7] if row[7] else None,
                birthCity=row[5] if row[5] else None,
                deathYear=int(row[8]) if row[8] else None,
                deathMonth=int(row[9]) if row[9] else None,
                deathDay=int(row[10]) if row[10] else None,
                deathCountry=row[11] if row[11] else None,
                deathState=row[12] if row[12] else None,
                deathCity=row[13] if row[13] else None,
                nameFirst=row[14],
                nameLast=row[15],
                nameGiven=row[16],
                weight=int(row[17]) if row[17] else None,
                height=int(row[18]) if row[18] else None,
                bats=row[19],
                throws=row[20],
                debutDate=parse_date(row[21]),
                finalGameDate=parse_date(row[23])
            )
            session.merge(new_person)

        session.commit()
        print("People table updated")
    except Exception as e:
        session.rollback()
        print(f"An error occurred: {e}")
    finally:
        session.close()

