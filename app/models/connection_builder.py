from peewee import Model, MySQLDatabase

from ..config import DATABASE  # pylint:disable=relative-beyond-top-level

database = MySQLDatabase(
    database=DATABASE["name"],
    **{
        "charset": "utf8",
        "sql_mode": "PIPES_AS_CONCAT",
        "use_unicode": True,
        "host": DATABASE["host"],
        "user": DATABASE["user"],
        "passwd": DATABASE["pass"],
        "port": DATABASE["port"],
    },
)


# pylint: disable=too-few-public-methods
class BaseModel(Model):
    class Meta:
        database = database
