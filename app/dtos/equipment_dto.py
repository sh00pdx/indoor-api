from pydantic import BaseModel, Field, validator
from typing import Optional

class EquipmentDto(BaseModel):
    mac: str
    name: str 


class Config(BaseModel):
    soil_low_humidity: float = Field(..., example=30.0, description="Low soil humidity threshold value")
    soil_max_humidity: float = Field(..., example=80.0, description="Maximum soil humidity threshold value")

    @validator('soil_low_humidity', 'soil_max_humidity')
    def check_humidity_values(cls, value):
        if not isinstance(value, (int, float)):
            raise ValueError('The value must be numeric')
        return value

    class Config:
        schema_extra = {
            "example": {
                "soil_low_humidity": 30.0,  # Numeric type example for low soil humidity
                "soil_max_humidity": 80.0,  # Numeric type example for maximum soil humidity
            }
        }


class EquipmentConfigDto(BaseModel):
    config: Config
    description: Optional[str]
    equipment: int
    name: str
    
