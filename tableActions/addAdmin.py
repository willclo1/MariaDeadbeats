from sqlalchemy import create_engine, text
from cfg import engineStr
from werkzeug.security import generate_password_hash
from datetime import datetime, timezone



def execute_sql(engine, statement):
    with engine.connect() as conn:
        conn.execute(text(statement))
        conn.commit()

def create_admin_user():
    ADMIN_USER_USERNAME = 'admin'
    ADMIN_USER_EMAIL = 'admin@admin.com'
    ADMIN_USER_PASSWORD = 'guestPassword123'
    ADMIN_USER_PASSWORD_HASH = generate_password_hash(ADMIN_USER_PASSWORD)

    engine = create_engine(engineStr)

    try:
        # Check if the user already exists
        user_exists_query = f"SELECT EXISTS(SELECT * FROM Users WHERE username = '{ADMIN_USER_USERNAME}');"
        with engine.connect() as conn:
            user_exists = conn.execute(text(user_exists_query)).scalar()

        if user_exists:
            print(f"User '{ADMIN_USER_USERNAME}' already exists. Deleting the user...")
            delete_user_sql = f"DELETE FROM USERS where username = 'admin';"
            execute_sql(engine, delete_user_sql)
            print(f"User '{ADMIN_USER_USERNAME}' deleted successfully.")

        time_of_last_access = datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S')

        # Create the guest user
        create_user_sql = (f" INSERT INTO Users (username, email, password_hash, is_admin, time_of_last_access)"
                           f" VALUES ('{ADMIN_USER_USERNAME}','{ADMIN_USER_EMAIL}', '{ADMIN_USER_PASSWORD_HASH}', 1 , '{time_of_last_access}' );")
        execute_sql(engine, create_user_sql)
        print(f"ADMIN USER: '{ADMIN_USER_USERNAME}' created successfully.")


    except Exception as e:
        print(f"An error occurred: {e}")

create_admin_user()