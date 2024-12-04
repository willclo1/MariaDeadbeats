from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
from Tables.Pitching import Pitching
from Tables.People import People  # Assuming you have a People table model
from cfg import engineStr
from tableActions.csvActions import getPeopleData, getNewData, getAllData


def add_column_to_pitching():
    engine = create_engine(engineStr)
    with engine.connect() as conn:
        try:
            # Add the p_WAR and p_NH columns to the Pitching table
            conn.execute(text("ALTER TABLE Pitching ADD COLUMN p_WAR FLOAT"))
            conn.execute(text("ALTER TABLE Pitching ADD COLUMN p_NH BOOLEAN DEFAULT FALSE"))
            print("Columns 'p_WAR', 'p_NH' added successfully to the Pitching table.")
        except Exception as e:
            print(f"An error occurred while altering the table: {e}")


def fillPitching():
    engine = create_engine(engineStr)
    Session = sessionmaker(bind=engine)
    session = Session()

    try:
        add_column_to_pitching()
        currData = getNewData("lahman_1871-2023_csv/Pitching.csv")
        warData = getAllData("lahman_1871-2023_csv/jeffbagwell_war_historical_2023.csv")
        noHitterData = getAllData("lahman_1871-2023_csv/no_hitters_and_perfect_games.csv")

        # Add current pitching data
        for row in currData:
            new_row = Pitching(
                playerID=row[0],
                yearID=row[1],
                teamID=row[3],
                stint=row[2],
                p_W=row[5] if row[5] else None,
                p_L=row[6] if row[6] else None,
                p_G=row[7] if row[7] else None,
                p_GS=row[8] if row[8] else None,
                p_CG=row[9] if row[9] else None,
                p_SHO=row[10] if row[10] else None,
                p_SV=row[11] if row[11] else None,
                p_IPOuts=row[12] if row[12] else None,
                p_H=row[13] if row[13] else None,
                p_ER=row[14] if row[14] else None,
                p_HR=row[15] if row[15] else None,
                p_BB=row[16] if row[16] else None,
                p_SO=row[17] if row[17] else None,
                p_BAOpp=row[18] if row[18] else None,
                p_ERA=row[19] if row[19] else None,
                p_IBB=row[20] if row[20] else None,
                p_WP=row[21] if row[21] else None,
                p_HBP=row[22] if row[22] else None,
                p_BK=row[23] if row[23] else None,
                p_BFP=row[24] if row[24] else None,
                p_GF=row[25] if row[25] else None,
                p_R=row[26] if row[26] else None,
                p_SH=row[27] if row[27] else None,
                p_SF=row[28] if row[28] else None,
                p_GIDP=row[29] if row[29] else None,
            )
            session.add(new_row)

        # Update WAR data
        for row in warData:
            player_id = row[2]
            year_id = int(row[3])
            war_value = float(row[39]) if row[39] != 'NA' else None

            session.query(Pitching).filter(
                Pitching.playerID == player_id, Pitching.yearID == year_id
            ).update({"p_WAR": war_value})

        # Add no-hitter data by joining with People
        for row in noHitterData:
            year_id = int(row[0])
            player_name = row[1].strip()
            team_name = row[2].strip()
            person = session.query(People).filter(People.nameFirst + " " + People.nameLast == player_name).first()

            if person:
                session.query(Pitching).filter(
                    Pitching.yearID == year_id,
                    Pitching.teamID == team_name,
                    Pitching.playerID == person.playerID
                ).update({"p_NH": True})

        # Commit all changes
        session.commit()
        print("Pitching data and no-hitter data added successfully")

    except Exception as e:
        session.rollback()
        print(f"An error occurred: {e}")

    finally:
        session.close()