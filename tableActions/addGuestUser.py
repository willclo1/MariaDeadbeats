from sqlalchemy import create_engine, text
from cfg import engineStr

def create_guest_user():
    """
    Creates a guest user with read-only access. Deletes the user if it already exists.
    """

    GUEST_USERNAME = 'guest_user'
    GUEST_PASSWORD = 'guestPassword123'
    DATABASE_NAME = 'mariadeadbeats'

    engine = create_engine(engineStr)

    def execute_sql(statement):
        with engine.connect() as conn:
            conn.execute(text(statement))
            conn.commit()

    try:
        # Check if the user already exists
        user_exists_query = f"SELECT EXISTS(SELECT 1 FROM mysql.user WHERE user = '{GUEST_USERNAME}' AND host = 'localhost');"
        with engine.connect() as conn:
            user_exists = conn.execute(text(user_exists_query)).scalar()

        if user_exists:
            print(f"User '{GUEST_USERNAME}' already exists. Deleting the user...")
            delete_user_sql = f"DROP USER '{GUEST_USERNAME}'@'localhost';"
            execute_sql(delete_user_sql)
            print(f"User '{GUEST_USERNAME}' deleted successfully.")

        # Create the guest user
        create_user_sql = f"CREATE USER '{GUEST_USERNAME}'@'localhost' IDENTIFIED BY '{GUEST_PASSWORD}';"
        execute_sql(create_user_sql)
        print(f"User '{GUEST_USERNAME}' created successfully.")

        # Grant the user permissions
        grant_user_sql = f"GRANT SELECT,INSERT, UPDATE ON {DATABASE_NAME}.* TO '{GUEST_USERNAME}'@'localhost';"
        execute_sql(grant_user_sql)
        print(f"User '{GUEST_USERNAME}' successfully granted permissions.")

    except Exception as e:
        print(f"An error occurred: {e}")

create_guest_user()

