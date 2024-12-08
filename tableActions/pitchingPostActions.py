from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from Tables.pitchingPost import PitchingPost
from .cfg import engineStr
from .csvActions import getPeopleData, getNewData
import os

def fillPostPitching():
    engine = create_engine(engineStr)
    Session = sessionmaker(bind=engine)
    session = Session()

    try:


        BASE_DIR = os.path.dirname(os.path.abspath(__file__))
        batting_post_csv_path = os.path.join(BASE_DIR, 'lahman_1871-2023_csv', 'PitchingPost.csv')
        currData = getNewData(batting_post_csv_path)

        for row in currData:
            new_row = PitchingPost(
                playerID = row[0],
                yearID = row[1],
                teamID = row[3],
                round = row[2],
                p_W = row[5] if row[5] else None,
                p_L = row[6] if row[6] else None,
                p_G = row[7] if row[7] else None,
                p_GS = row[8] if row[8] else None,
                p_CG = row[9] if row[9] else None,
                p_SHO = row[10] if row[10] else None,
                p_SV = row[11] if row[11] else None,
                p_IPOuts = row[12] if row[12] else None,
                p_H = row[13] if row[13] else None,
                p_ER = row[14] if row[14] else None,
                p_HR = row[15] if row[15] else None,
                p_BB = row[16] if row[16] else None,
                p_SO = row[17] if row[17] else None,
                p_BAOpp= row[18] if row[18] else None,
                p_ERA = row[19] if row[19] else None,
                p_IBB= row[20] if row[20] else None,
                p_WP = row[21] if row[21] else None,
                p_HBP = row[22] if row[22] else None,
                p_BK = row[23] if row[23] else None,
                p_BFP = row[24] if row[24] else None,
                p_GF = row[25] if row[25] else None,
                p_R =row[26] if row[26] else None,
                p_SH = row[27] if row[27] else None,
                p_SF = row[28] if row[28] else None,
                p_GIDP= row[29] if row[29] else None
            )
            session.add(new_row)

        session.commit()
        print("postseason pitching data added")
    except Exception as e:
        session.rollback()
        print(f"An error occurred: {e}")

    finally:
        session.close()
