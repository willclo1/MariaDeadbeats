from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from Tables.Draft import Draft
from Tables.People import People
from csvActions import getDraftData
from cfg import engineStr
import csv


def fillDraft():
    """
    Populate the Draft table using data from the draft CSV and the People table.
    Uses additional attributes like weight, bats, throws, and birth_date for accurate mapping.
    """
    engine = create_engine(engineStr)
    Session = sessionmaker(bind=engine)
    session = Session()

    try:
        # Load draft data from CSV
        draft_data = getDraftData("lahman_1871-2023_csv/draft_1965_2019.csv")

        for draft_row in draft_data:
            # Retrieve player data using additional attributes for disambiguation
            person_query = session.query(People).filter(
                People.nameFirst == draft_row["nameFirst"],
                People.nameLast == draft_row["nameLast"]
            )

            # Apply additional filters to resolve ambiguous cases
            if draft_row.get("birth_date"):
                person_query = person_query.filter(People.birthYear == draft_row["birth_date"].year)
            if draft_row.get("bats"):
                person_query = person_query.filter(People.bats == draft_row["bats"])
            if draft_row.get("throws"):
                person_query = person_query.filter(People.throws == draft_row["throws"])
            if draft_row.get("weight"):
                person_query = person_query.filter(People.weight == draft_row["weight"])

            person = person_query.first()  # Fetch the first match

            if person:
                draft_entry = Draft(
                    playerID=person.playerID,
                    nameFirst=person.nameFirst,
                    nameLast=person.nameLast,
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
