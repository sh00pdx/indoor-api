from pydantic import BaseModel

class EquipmentDto(BaseModel):
    mac: str
    name: str 
