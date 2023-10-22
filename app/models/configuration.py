from peewee import SQL, BigAutoField, CharField, DateTimeField, TextField, ForeignKeyField
from playhouse.mysql_ext import JSONField
from .equipment import Equipment
from .connection_builder import BaseModel

class Configuration(BaseModel):
    config = JSONField()  # json
    created_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    description = TextField(null=True)
    equipment = ForeignKeyField(column_name='equipment_id', field='id', model=Equipment, null=True)
    id = BigAutoField()
    name = CharField(null=True)
    state = CharField(null=True)
    updated_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])

    class Meta:
        table_name = 'configuration'