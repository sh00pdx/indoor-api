from .equipment_service_deps import equipment_service_deps
from app.logger import get_logger
from app.dtos import EquipmentDto, EquipmentConfigDto, MeditionDto
from app.models import Equipment, User, Configuration, ProductMedition
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
        
        return {'success': True}
    
    async def register_config(self, body: EquipmentConfigDto):
        config_model: Configuration = self.deps['configuration']
        
        config_model.create(
            config=body.config,
            description=body.description,
            equipment=body.equipment,
            name=body.name
        )
        
        return {'success': True}
    
    async def register_medition(self, body: MeditionDto):
        medition_model: ProductMedition = self.deps['producto_medition']
        
        medition = medition_model.create(**body)
        
        config_model: Configuration = self.deps['configuration']
        config = config_model.get(config_model.equipment == body.equipment and config_model.state == 'active')
        config = config.get('config')
        
        response = {
            'activate_irrigation': True if config.get('soil_max_humidity', 2000) < body.soil_humidity and  config.get('sol_min_hidity', 0) > body.soil_humidity else False
        }
        
        medition.action = response
        medition.save()
        
        return response
    
    async def activate_config(self, body: EquipmentDto):
        # TODO: activar configuracion especifica (desactiva todas las siguientes)
        pass
    
    async def get_medition(self, body: EquipmentDto):
        # TODO: traer mediciones de equipo especifico por rango de fecha
        pass
    
EquipmentServiceSingleton = EquipmentService(equipment_service_deps)
