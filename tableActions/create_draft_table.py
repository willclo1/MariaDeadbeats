from sqlalchemy import create_engine
from .cfg import engineStr
from sqlalchemy.orm import sessionmaker
from Tables.Draft import Base, Draft

def create_draft_table():
    engine = create_engine(engineStr, echo=True)
    Base.metadata.create_all(engine)
    session = sessionmaker(bind=engine)

    try:
        session = session()
        session.commit()
        print("Draft table created!")

    except Exception as e:
        session.rollback()
        print(f"An error occurred: {e}")

    finally:
        session.close()

