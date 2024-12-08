from sqlalchemy import create_engine
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import sessionmaker
from Tables.battingPost import BattingPost
from .csi3335f2024 import engineStr
from .csvActions import getNewData
import os


def fillBattingPost():
    engine = create_engine(engineStr)
    Session = sessionmaker(bind=engine)
    session = Session()

    try:
        BASE_DIR = os.path.dirname(os.path.abspath(__file__))
        batting_post_csv_path = os.path.join(BASE_DIR, 'lahman_1871-2023_csv', 'BattingPost.csv')
        currData = getNewData(batting_post_csv_path)

        for row in currData:
            new_record = BattingPost(
                playerID=row[2],
                yearId=int(row[0]),
                teamID=row[3],
                round=row[1],
                b_G=int(row[5]) if row[5] else None,
                b_AB=int(row[6]) if row[6] else None,
                b_R=int(row[7]) if row[7] else None,
                b_H=int(row[8]) if row[8] else None,
                b_2B=int(row[9]) if row[9] else None,
                b_3B=int(row[10]) if row[10] else None,
                b_HR=int(row[11]) if row[11] else None,
                b_RBI=int(row[12]) if row[12] else None,
                b_SB=int(row[13]) if row[13] else None,
                b_CS=int(row[14]) if row[14] else None,
                b_BB=int(row[15]) if row[15] else None,
                b_SO=int(row[16]) if row[16] else None,
                b_IBB=int(row[17]) if row[17] else None,
                b_HBP=int(row[18]) if row[18] else None,
                b_SH=int(row[19]) if row[19] else None,
                b_SF=int(row[20]) if row[20] else None,
                b_GIDP=int(row[21]) if row[21] else None,
            )
            session.add(new_record)  # Add the record to the session

        session.commit()
        print("Batting Post updated")
    except Exception as e:
        session.rollback()
        print(f"An error occurred: {e}")
    finally:
        session.close()
