from fastapi import APIRouter, Request
from app.dtos import EquipmentDto
from app.views.equipment.equipment_view import EquipmentViewSingleton

router = APIRouter()

@router.post("/register")
async def register(body: EquipmentDto):
    pass

@router.post("/signup")
async def login(body: EquipmentDto):
    pass
