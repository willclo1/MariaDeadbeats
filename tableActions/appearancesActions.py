from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from Tables.appearances import Appearances
from cfg import engineStr
from tableActions.csvActions import getNewData


def fillAppearances():

    engine = create_engine(engineStr)
    Session = sessionmaker(bind=engine)
    session = Session()
    try:
        currData = getNewData("lahman_1871-2023_csv/Appearances.csv")
        for row in currData:
            new_row = Appearances(
                playerID=row[3],
                yearID=row[0],
                teamId=row[1],
                G_all=row[4] if row[4] else None,
                GS=row[5] if row[5] else None,
                G_batting=row[6] if row[6] else None,
                G_defense=row[7] if row[7] else None,
                G_p=row[8] if row[8] else None,
                G_c=row[9] if row[9] else None,
                G_1b=row[10] if row[10] else None,
                G_2b=row[11] if row[11] else None,
                G_3b=row[12] if row[12] else None,
                G_ss=row[13] if row[13] else None,
                G_lf=row[14] if row[14] else None,
                G_cf=row[15] if row[15] else None,
                G_rf=row[16] if row[16] else None,
                G_of=row[17] if row[17] else None,
                G_dh=row[18] if row[18] else None,
                G_ph=row[19] if row[19] else None,
                G_pr=row[20] if row[20] else None
            )
            session.add(new_row)
        session.commit()
        print("appearances updated")
    except Exception as e:
        session.rollback()
        print(e)
    finally:
        session.close()




