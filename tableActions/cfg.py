# Modify for your own database connection/account
cfg = {"host" : "localhost", "user": "guest_user", "password" : "guestPassword123", "db" : "MariaDeadbeats"}
engineStr = "mysql+pymysql://" + cfg.get("user") + ":" + cfg.get("password") + "@" + cfg.get(
        "host") + ":3306/" + cfg.get("db")
API_KEY = "AIzaSyD_0DLUddBAgE3IuRWlp7HBQgTu0qq2Kik"