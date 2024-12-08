from sqlalchemy import create_engine
from cfg import engineStr
from sqlalchemy.orm import sessionmaker
from Tables.UserLogs import Base, UserLogs

def create_user_logs_table():
    engine = create_engine(engineStr, echo=True)
    Base.metadata.create_all(engine)
    session = sessionmaker(bind=engine)

    try:
        session = session()
        session.commit()
        print("User Logs table created!")

    except Exception as e:
        session.rollback()
        print("An error occurred: {e}")

    finally:
        session.close()
create_user_logs_table()