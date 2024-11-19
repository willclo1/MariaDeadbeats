from sqlalchemy import create_engine
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import sessionmaker
from Tables.seriesPost import SeriesPost
from cfg import engineStr
from tableActions.csvActions import getNewData

def fillSeriesPost():

    engine = create_engine(engineStr)
    Session = sessionmaker(bind=engine)
    session = Session()

    try:
        currData = getNewData("lahman_1871-2023_csv/SeriesPost.csv")

        for row in currData:
            new_record = SeriesPost(
                teamIDwinner=row[2],
                teamIDloser=row[4],
                yearID=row[0],
                round=row[1],
                wins=row[6] if row[6] else None,
                losses=row[7] if row[7] else None,
                ties=row[8] if row[8] else None,

            )
            session.add(new_record)

        session.commit()
        print("series post data updated")

    except Exception as e:
        session.rollback()
        print(f"An error occurred: {e}")
    finally:
        session.close()
