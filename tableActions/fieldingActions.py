from sqlalchemy import create_engine
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import sessionmaker
from Tables.Fielding import Fielding
from .csi3335f2024 import engineStr
from .csvActions import getNewData
import os

def fillFielding():

    engine = create_engine(engineStr)
    Session = sessionmaker(bind=engine)
    session = Session()

    try:


        BASE_DIR = os.path.dirname(os.path.abspath(__file__))
        batting_post_csv_path = os.path.join(BASE_DIR, 'lahman_1871-2023_csv', 'Fielding.csv')
        currData = getNewData(batting_post_csv_path)

        for row in currData:
            new_record = Fielding(
                playerID=row[0],
                yearID=int(row[1]),
                stint=int(row[2]),
                teamID=row[3],
                position=row[5],
                f_G=int(row[6]) if row[6] else None,
                f_GS=int(row[7]) if row[7] else None,
                f_InnOuts=int(row[8]) if row[8] else None,
                f_PO=int(row[9]) if row[9] else None,
                f_A=int(row[10]) if row[10] else None,
                f_E=int(row[11]) if row[11] else None,
                f_DP=int(row[12]) if row[12] else None,
                f_PB=int(row[13]) if row[13] else None,
                f_WP=int(row[14]) if row[14] else None,
                f_SB=int(row[15]) if row[15] else None,
                f_CS=int(row[16]) if row[16] else None,
                f_ZR=int(row[17]) if row[17] else None,
            )
            session.add(new_record)  # Add the record to the session

        session.commit()
        print("Fielding updated")

    except Exception as e:
        session.rollback()
        print(f"An error occurred: {e}")
    finally:
        session.close()

