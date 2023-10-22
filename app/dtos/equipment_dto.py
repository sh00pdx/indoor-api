from pydantic import BaseModel

class EquipmentDto(BaseModel):
    user_id: int
    mac: str
    name: str 
