from pydantic import BaseModel
from typing import Optional

class MeditionDto(BaseModel):
    ambient_humidity: Optional[float] = None 
    ambient_temperature: Optional[float] = None
    soil_humidity: Optional[float] = None 
    equipment: Optional[int] = None

