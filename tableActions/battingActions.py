from sqlalchemy import create_engine
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.sync import update

from Tables.Batting import Batting
from cfg import engineStr
from tableActions.csvActions import getNewData, getAllData


def fillBatting():

    engine = create_engine(engineStr)
    Session = sessionmaker(bind=engine)
    session = Session()

    try:
        currData = getNewData("lahman_1871-2023_csv/Batting.csv")

        warData = getAllData("lahman_1871-2023_csv/jeffbagwell_war_historical_2023.csv")


        for row in currData:
            new_record = Batting(
                playerID=row[0],
                yearId=int(row[1]),
                stint=int(row[2]),
                teamID=row[3],
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
            session.add(new_record)

        for row in warData:
            player_id = row[2]
            year_id = int(row[3])
            if row[19] != 'NA':
                war_value = float(row[19])
            else:
                war_value = None

            session.query(Batting).filter(
                Batting.playerID == player_id, Batting.yearId == year_id
            ).update({"b_WAR": war_value})



        session.commit()
        print("Batting updated")
    except Exception as e:
        session.rollback()
        print(f"An error occurred: {e}")
    finally:
        session.close()  # Close the session
