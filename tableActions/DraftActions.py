from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from Tables.Draft import Draft
from Tables.People import People
from .csvActions import getDraftData
from .cfg import engineStr
import os



def fillDraft():

    engine = create_engine(engineStr)
    Session = sessionmaker(bind=engine)
    session = Session()

    try:

        BASE_DIR = os.path.dirname(os.path.abspath(__file__))
        batting_post_csv_path = os.path.join(BASE_DIR, 'lahman_1871-2023_csv', 'draft_1965_2019.csv')
        currData = getDraftData(batting_post_csv_path)

        for draft_row in currData:
            person_query = session.query(People).filter(
                People.nameFirst == draft_row["nameFirst"],
                People.nameLast == draft_row["nameLast"]
            )

            if draft_row.get("birth_date"):
                person_query = person_query.filter(People.birthYear == draft_row["birth_date"].year)
            if draft_row.get("bats"):
                person_query = person_query.filter(People.bats == draft_row["bats"])
            if draft_row.get("throws"):
                person_query = person_query.filter(People.throws == draft_row["throws"])
            if draft_row.get("weight"):
                person_query = person_query.filter(People.weight == draft_row["weight"])

            person = person_query.first()

            if person:
                draft_entry = Draft(
                    playerID=person.playerID,
                    nameFirst=person.nameFirst,
                    nameLast=person.nameLast,
                    yearID=draft_row["year"],
                    round=draft_row["round"],
                    pick=draft_row["pick"],
                    description=draft_row["description"]
                )
                session.merge(draft_entry)

        session.commit()
        print("Draft table updated successfully.")
    except Exception as e:
        session.rollback()
        print(f"An error occurred: {e}")
    finally:
        session.close()