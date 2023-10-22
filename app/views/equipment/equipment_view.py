from .equipment_deps import equipment_deps
from app.logger import get_logger 
from app.dtos import EquipmentDto

logger = get_logger(__name__)
    
class EquipmentView:
    deps: equipment_deps

    def __init__(self, deps: equipment_deps):
        self.deps = deps
        self.logger = logger
        
    async def get_all(self, body: EquipmentDto):
        # TODO: buscar todos los equipos del usuario (sin configuracion)
        pass
    
    async def get_by_mac(self, body: EquipmentDto):
        # TODO: buscar equipo por mac + user_id (con configuracion)
        pass
        
    async def update(self, body: EquipmentDto):
        # TODO: editar equipo por mac + user_id 
        pass
    
    async def register(self, body: EquipmentDto):
        # TODO: Registrar equipo
        pass
    
    async def register_config(self, body: EquipmentDto):
        # TODO: Registrar configuracion de equipo especifico
        pass
    
    async def register_medition(self, body: EquipmentDto):
        # TODO: Registrar equipo medicion de equipo especifico
        pass
    
    async def activate_config(self, body: EquipmentDto):
        # TODO: activar configuracion especifica (desactiva todas las siguientes)
        pass
    
    async def get_medition(self, body: EquipmentDto):
        # TODO: traer mediciones de equipo especifico por rango de fecha
        pass
    
    
EquipmentViewSingleton = EquipmentView(equipment_deps)
