from sqlalchemy import create_engine, text
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.sync import update

from Tables.Batting import Batting
from .cfg import engineStr
import os
from .csvActions import getNewData, getAllData

def add_column_to_batting():
    engine = create_engine(engineStr)
    with engine.connect() as conn:
        try:
            # Add the b_WAR column to the Batting table
            conn.execute(text("ALTER TABLE Batting ADD COLUMN b_WAR FLOAT"))
            print("Column 'b_WAR' added successfully to the Batting table.")
        except Exception as e:
            print(f"An error occurred while altering the table: {e}")

def fillBatting():

    engine = create_engine(engineStr)
    Session = sessionmaker(bind=engine)
    session = Session()

    try:
        add_column_to_batting()


        BASE_DIR = os.path.dirname(os.path.abspath(__file__))


        batting_csv_path = os.path.join(BASE_DIR, 'lahman_1871-2023_csv', 'Batting.csv')
        war_data_csv_path = os.path.join(BASE_DIR, 'lahman_1871-2023_csv', 'jeffbagwell_war_historical_2023.csv')


        currData = getNewData(batting_csv_path)
        warData = getAllData(war_data_csv_path)

        for row in currData:
            new_record = Batting(
                playerID=row[0],
                yearId=int(row[1]),
                stint=int(row[2]),
                teamID=row[3],
                b_G=int(row[5]) if row[5] else None,
                b_AB=int(row[7]) if row[7] else None,
                b_R=int(row[8]) if row[8] else None,
                b_H=int(row[9]) if row[9] else None,
                b_2B=int(row[10]) if row[10] else None,
                b_3B=int(row[11]) if row[11] else None,
                b_HR=int(row[12]) if row[12] else None,
                b_RBI=int(row[13]) if row[13] else None,
                b_SB=int(row[14]) if row[14] else None,
                b_CS=int(row[15]) if row[15] else None,
                b_BB=int(row[16]) if row[16] else None,
                b_SO=int(row[17]) if row[17] else None,
                b_IBB=int(row[18]) if row[18] else None,
                b_HBP=int(row[19]) if row[19] else None,
                b_SH=int(row[20]) if row[20] else None,
                b_SF=int(row[21]) if row[21] else None,
                b_GIDP=int(row[22]) if row[22] else None,
            )
            session.add(new_record)

        for row in warData:
            player_id = row[2]
            year_id = int(row[3])
            if row[18] != 'NA':
                war_value = float(row[18])
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



