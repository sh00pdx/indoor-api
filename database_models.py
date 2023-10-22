from peewee import *

database = MySQLDatabase('indoor', **{'charset': 'utf8', 'sql_mode': 'PIPES_AS_CONCAT', 'use_unicode': True, 'host': '127.0.0.1', 'port': 3306, 'user': 'root'})

class UnknownField(object):
    def __init__(self, *_, **__): pass

class BaseModel(Model):
    class Meta:
        database = database

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

class Configuration(BaseModel):
    config = UnknownField()  # json
    created_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    description = TextField(null=True)
    equipment = ForeignKeyField(column_name='equipment_id', field='id', model=Equipment, null=True)
    id = BigAutoField()
    name = CharField(null=True)
    state = CharField(null=True)
    updated_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])

    class Meta:
        table_name = 'configuration'

class ConfigurationHistory(BaseModel):
    configuration = ForeignKeyField(column_name='configuration_id', field='id', model=Configuration, null=True)
    created_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    id = BigAutoField()
    new_state = CharField(null=True)
    updated_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])

    class Meta:
        table_name = 'configuration_history'

class ConfigurationResult(BaseModel):
    configuration = ForeignKeyField(column_name='configuration_id', field='id', model=Configuration)
    id = BigAutoField()
    result_date = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    result_quality = CharField(null=True)
    result_quantity = IntegerField(null=True)

    class Meta:
        table_name = 'configuration_result'

class ProductMedition(BaseModel):
    ambient_humidity = DecimalField(null=True)
    ambient_temperature = DecimalField(null=True)
    created_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    equipment = ForeignKeyField(column_name='equipment_id', field='id', model=Equipment, null=True)
    id = BigAutoField()
    order_sent = IntegerField(null=True)
    record_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    soil_temperature = DecimalField(null=True)
    updated_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])

    class Meta:
        table_name = 'product_medition'

