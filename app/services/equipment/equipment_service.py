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
        equipment_model: Equipment = self.deps['models']['equipment']
        equipments = list(equipment_model.select().where(equipment_model.user == user.id))
        return equipments
    
    async def get_by_mac(self, mac: str, user):
        equipment_model: Equipment = self.deps['models']['equipment']
        equipment = equipment_model.get_or_none(equipment_model.mac == mac and equipment_model.user == user.id)
        return equipment
        
    async def update(self, body: EquipmentDto):
        # TODO: editar equipo por mac + user_id 
        pass
    
    async def register(self, body: EquipmentDto, user: User):
        # TODO: Registrar equipo, el arduino enviara su mac, (el dispositivo debe estar registrado previamente)
        equipment_model: Equipment = self.deps['models']['equipment']
        
        equipment_model.create(
            mac=body.mac,
            name=body.name,
            user=user.id
        )
        
        return {'success': True}
    
    async def register_config(self, body: EquipmentConfigDto):
        config_model: Configuration = self.deps['models']['configuration']
        
        config_model.create(
            #config=body.config,
            description=body.description,
            equipment=body.equipment,
            name=body.name
        )
        
        return {'success': True}
    
    async def register_medition(self, body: MeditionDto):
        medition_model: ProductMedition = self.deps['models']['producto_medition']
        
        medition = medition_model.create(
            equipment=body.equipment,
            ambient_humidity=body.ambient_humidity,
            ambient_temperature=body.ambient_temperature,
            soil_humidity=body.soil_humidity
        )
        
        config_model: Configuration = self.deps['models']['configuration']
        config = config_model.get(config_model.equipment == body.equipment and config_model.state == 'active')
        config = config.config
        
        activate_irrigation = False
        
        if config.get('soil_low_humidity') >= body.soil_humidity:
            activate_irrigation = True
            
        if config.get('soil_max_humidity') <= body.soil_humidity:
            activate_irrigation = False
                    
        response = {
            'activate_irrigation': activate_irrigation
        }
        
        medition.order_sent = response
        medition.save()
        
        return response
    
    async def activate_config(self, body: EquipmentDto):
        # TODO: activar configuracion especifica (desactiva todas las siguientes)
        pass
    
    async def get_medition(self, user):
        medition_model: ProductMedition = self.deps['models']['producto_medition']
        meditions = list(medition_model.select().where(medition_model.equipment == 1).order_by(medition_model.id.desc()).limit(10).dicts())
        return meditions
    
EquipmentServiceSingleton = EquipmentService(equipment_service_deps)
