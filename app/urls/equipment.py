from fastapi import APIRouter, Request
from app.dtos import EquipmentDto, EquipmentConfigDto, MeditionDto
from app.views.equipment.equipment_view import EquipmentViewSingleton
from app.models import User
from devtools import debug

router = APIRouter()

@router.get("/equipment")
async def get_all(request: Request):
    user: User = request.state.user
    return await EquipmentViewSingleton.get_all(user)

@router.get("/equipment/{mac}")
async def get_by_mac(request: Request, mac: str):
    user: User = request.state.user
    return await EquipmentViewSingleton.get_by_mac(mac, user)

""" @router.put("/equipment")
async def update(body: EquipmentDto):
    # TODO: editar equipo por mac + user_id 
    pass """

@router.post("/equipment")
async def register(request: Request, body: EquipmentDto):
    user: User = request.state.user
    debug(user)
    return await EquipmentViewSingleton.register(body, user)

@router.post("/equipment/config")
async def register_config(body: EquipmentConfigDto):
    return await EquipmentViewSingleton.register_config(body)

@router.post("/equipment/medition")
async def register_medition(body: MeditionDto):
    # TODO: Registrar equipo medicion de equipo especifico
    return await EquipmentViewSingleton.register_medition(body)

""" @router.put("/equipment/config/activate")
async def activate_config(body: EquipmentDto):
    # TODO: activar configuracion especifica (desactiva todas las siguientes)
    pass """

""" @router.get("/equipment/medition")
async def get_medition(body: EquipmentDto):
    # TODO: buscar todos los equipos del usuario (sin configuracion)
    pass """