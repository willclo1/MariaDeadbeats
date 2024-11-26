# Modify for your own database connection/account
cfg = {"host" : "localhost", "user": "nicholasnolen", "password" : "", "db" : "MariaDeadbeats"}
engineStr = "mysql+pymysql://" + cfg.get("user") + ":" + cfg.get("password") + "@" + cfg.get(
        "host") + ":3306/" + cfg.get("db")