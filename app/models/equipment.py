from peewee import SQL, BigAutoField, CharField, DateTimeField, ForeignKeyField, DateField
from .user import User
from .connection_builder import BaseModel

class Equipment(BaseModel):
    created_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    creation_date = DateField(null=True)
    id = BigAutoField()
    mac = CharField(null=True, unique=True)
    name = CharField(null=True)
    updated_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    user = ForeignKeyField(column_name='user_id', field='id', model=User, null=True)

    class Meta:
        table_name = 'equipment'
