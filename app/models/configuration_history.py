from peewee import SQL, BigAutoField, CharField, DateTimeField, ForeignKeyField
from .configuration import Configuration
from .connection_builder import BaseModel

class ConfigurationHistory(BaseModel):
    configuration = ForeignKeyField(column_name='configuration_id', field='id', model=Configuration, null=True)
    created_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    id = BigAutoField()
    new_state = CharField(null=True)
    updated_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])

    class Meta:
        table_name = 'configuration_history'