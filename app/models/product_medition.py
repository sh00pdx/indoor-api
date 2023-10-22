from peewee import SQL, BigAutoField, DateTimeField, DecimalField, ForeignKeyField, IntegerField
from .equipment import Equipment
from .connection_builder import BaseModel

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
