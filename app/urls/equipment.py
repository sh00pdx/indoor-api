from fastapi import APIRouter, Request
from app.dtos import EquipmentDto
from app.views.equipment.equipment_view import EquipmentViewSingleton
from app.models import User
router = APIRouter()

@router.get("/equipment")
async def get_all(body: EquipmentDto):
    # TODO: buscar todos los equipos del usuario (sin configuracion)
    pass

@router.get("/equipment/{mac}")
async def get_by_mac(mac: str, user: User):
   return await EquipmentViewSingleton.get_by_mac(mac, user)

@router.put("/equipment")
async def update(body: EquipmentDto):
    # TODO: editar equipo por mac + user_id 
    pass

@router.post("/equipment")
async def register(body: EquipmentDto):
    # TODO: Registrar equipo
    return await EquipmentViewSingleton.register(body)

@router.post("/equipment/config")
async def register_config(body: EquipmentDto):
    # TODO: Registrar configuracion de equipo especifico
    pass

@router.post("/equipment/medition")
async def register_medition(body: EquipmentDto):
    # TODO: Registrar equipo medicion de equipo especifico
    pass

@router.put("/equipment/config/activate")
async def activate_config(body: EquipmentDto):
    # TODO: activar configuracion especifica (desactiva todas las siguientes)
    pass

@router.get("/equipment/medition")
async def get_medition(body: EquipmentDto):
    # TODO: buscar todos los equipos del usuario (sin configuracion)
    pass