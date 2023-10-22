from peewee import SQL, BigAutoField, CharField, DateTimeField, ForeignKeyField, IntegerField
from .configuration import Configuration
from .connection_builder import BaseModel

class ConfigurationResult(BaseModel):
    configuration = ForeignKeyField(column_name='configuration_id', field='id', model=Configuration)
    id = BigAutoField()
    result_date = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    result_quality = CharField(null=True)
    result_quantity = IntegerField(null=True)

    class Meta:
        table_name = 'configuration_result'