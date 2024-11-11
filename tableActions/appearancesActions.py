from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from Tables.appearances import Appearances
from cfg import cfg
from tableActions.csvActions import getNewData


def fillAppearances():
    engineStr = "mysql+pymysql://" + cfg.get("user") + ":" + cfg.get("password") + "@" + cfg.get(
        "host") + ":3306/" + cfg.get("db")

    engine = create_engine(engineStr)
    Session = sessionmaker(bind=engine)
    session = Session()

    currData = getNewData("lahman_1871-2023_csv/Appearances.csv")
    for row in currData:
        new_row = Appearances(
            playerID=row[3],
            yearID=row[0],
            teamId=row[1],
            G_all=row[4],
            GS=row[5],
            G_batting=row[6],
            G_defense=row[7],
            G_p=row[8],
            G_c=row[9],
            G_1b=row[10],
            G_2b=row[11],
            G_3b=row[12],
            G_ss=row[13],
            G_lf=row[14],
            G_cf=row[15],
            G_rf=row[16],
            G_of=row[17],
            G_dh=row[18],
            G_ph=row[19],
            G_pr=row[20]
        )
        print(new_row.playerID , "Added")
        session.add(new_row)
    session.rollback()

fillAppearances()


