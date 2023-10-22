from peewee import SQL, BigAutoField, CharField, DateTimeField

from .connection_builder import BaseModel

class User(BaseModel):
    created_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    email = CharField(null=True)
    id = BigAutoField()
    name = CharField(null=True)
    password = CharField(null=True)
    updated_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    username = CharField(null=True)

    class Meta:
        table_name = 'user'
