from decouple import config

DATABASE = {
    "host": config("DB_HOST", "localhost"),
    "port": int(config("DB_PORT", default=3306)),
    "name": config("DB_NAME", default="indoor"),
    "user": config("DB_USER", "root"),
    "pass": config("DB_PASS", None),
}

ENV = config("ENVIRONMENT", default="qa")
