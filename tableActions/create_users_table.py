from sqlalchemy import create_engine
from cfg import engineStr
from sqlalchemy.orm import sessionmaker
from Tables.Users import Base, Users

def create_users_table():
    engine = create_engine(engineStr, echo=True)
    Base.metadata.create_all(engine)
    session = sessionmaker(bind=engine)

    try:
        session = session()
        session.commit()
        print("User table created!")

    except Exception as e:
        session.rollback()
        print("An error occurred: {e}")

    finally:
        session.close()
