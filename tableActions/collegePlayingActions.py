from sqlalchemy import create_engine
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import sessionmaker
from Tables.collegePlaying import CollegePlaying
from cfg import engineStr
from tableActions.csvActions import getNewData

def fillCollegePlaying():

    engine = create_engine(engineStr)
    Session = sessionmaker(bind=engine)
    session = Session()

    try:
        currData = getNewData("lahman_1871-2023_csv/CollegePlaying.csv")

        for row in currData:
            new_record = CollegePlaying(
                playerID=row[0],
                schoolID=row[1] if row[1] != '' else None,
                yearID=int(row[2]) if row[2] != '' else None,
            )
            session.add(new_record)


        session.commit()
        print("College playing updated")
    except Exception as e:
        session.rollback()
        print(f"An error occurred: {e}")
    finally:
        session.close()
