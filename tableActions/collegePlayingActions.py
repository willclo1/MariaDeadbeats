from sqlalchemy import create_engine
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import sessionmaker
from Tables.collegePlaying import CollegePlaying
from cfg import engineStr
from tableActions.csvActions import getNewData

def fillBattingPost():

    engine = create_engine(engineStr)
    Session = sessionmaker(bind=engine)
    session = Session()

    try:
        currData = getNewData("lahman_1871-2023_csv/CollegePlaying.csv")

        for row in currData:
            new_record = CollegePlaying(
                playerID=row[0],
                schoolID=row[1],
                yearID=int(row[2])
            )
            session.add(new_record)
            print(f"Added record for playerID: {row[0]}, yearID: {row[1]}")

        session.commit()
        print("All 2023 records successfully added to the batting table.")

    except IntegrityError as e:
        session.rollback()
        print(f"An integrity error occurred: {e}")
    except Exception as e:
        session.rollback()
        print(f"An error occurred: {e}")
    finally:
        session.close()

fillBattingPost()
