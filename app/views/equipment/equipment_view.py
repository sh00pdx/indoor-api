from .equipment_deps import equipment_deps
from app.logger import get_logger 
from app.dtos import EquipmentDto, MeditionDto
from app.middleware.error_handler import error_handler_decorator
from app.models import User
logger = get_logger(__name__)
    
class EquipmentView:
    deps: equipment_deps

    def __init__(self, deps: equipment_deps):
        self.deps = deps
        self.logger = logger
        
    async def get_all(self, user: User):
        return await self.deps['services']['EquipmentServiceSingleton'].get_all(user)

    
    async def get_by_mac(self, mac: str, user: User):
        return await self.deps['services']['EquipmentServiceSingleton'].get_by_mac(mac, user)
        
    async def update(self, body: EquipmentDto):
        # TODO: editar equipo por mac + user_id 
        pass
    
    @error_handler_decorator()
    async def register(self, body: EquipmentDto, user: User):
        # TODO: Registrar equipo
        return await self.deps['services']['EquipmentServiceSingleton'].register(body, user)
    
    @error_handler_decorator()
    async def register_config(self, body: EquipmentDto):
        return await self.deps['services']['EquipmentServiceSingleton'].register_config(body)

    
    @error_handler_decorator()
    async def register_medition(self, body: MeditionDto):
        return await self.deps['services']['EquipmentServiceSingleton'].register_medition(body)
    
    async def activate_config(self, body: EquipmentDto):
        # TODO: activar configuracion especifica (desactiva todas las siguientes)
        pass
    
    async def get_medition(self, body: EquipmentDto):
        # TODO: traer mediciones de equipo especifico por rango de fecha
        pass
    
    
EquipmentViewSingleton = EquipmentView(equipment_deps)
