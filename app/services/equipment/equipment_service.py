from .equipment_service_deps import equipment_service_deps
from app.logger import get_logger
from app.dtos.equipment_dto import EquipmentDto
from app.models import Equipment, User
logger = get_logger(__name__)

class EquipmentService:
    deps = None
     
    def __init__(self, deps) -> None:
        self.deps = deps
        self.logger = logger
        
    async def get_all(self, user: User):
        equipment_model: Equipment = self.deps['equipment']
        equipments = list(equipment_model.select().where(equipment_model.user == user.id).to_dicts)
        return equipments
    
    async def get_by_mac(self, mac: str, user):
        equipment_model: Equipment = self.deps['equipment']
        equipment = equipment_model.get_or_none(equipment_model.mac == mac and equipment_model.user == user.id)
        return equipment
        
    async def update(self, body: EquipmentDto):
        # TODO: editar equipo por mac + user_id 
        pass
    
    async def register(self, body: EquipmentDto, user: User):
        # TODO: Registrar equipo, el arduino enviara su mac, (el dispositivo debe estar registrado previamente)
        equipment_model: Equipment = self.deps['equipment']
        
        equipment_model.create(
            mac=body.mac,
            name=body.name,
            user=user.id
        )
        
        return {'register': True}
    
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
    
EquipmentServiceSingleton = EquipmentService(equipment_service_deps)
