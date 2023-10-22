from decouple import Csv, config

DATABASE = {
    "host": config("DB_HOST"),
    "port": int(config("DB_PORT", default=3306)),
    "name": config("DB_NAME", default="indoor"),
    "user": config("DB_USER"),
    "pass": config("DB_PASS"),
}

ENV = config("ENVIRONMENT", default="qa")
