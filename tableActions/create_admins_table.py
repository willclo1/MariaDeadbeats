from sqlalchemy import create_engine
from cfg import engineStr
from sqlalchemy.orm import sessionmaker
from Tables.Admins import Base, Admins

def create_admins_table():
    engine = create_engine(engineStr, echo=True)
    Base.metadata.create_all(engine)
    session = sessionmaker(bind=engine)

    try:
        session = session()
        session.commit()
        print("Admins table created!")

    except Exception as e:
        session.rollback()
        print("An error occurred: {e}")

    finally:
        session.close()
