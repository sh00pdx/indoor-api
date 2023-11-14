from .equipment_service_deps import equipment_service_deps
from app.logger import get_logger
from app.dtos import EquipmentDto, EquipmentConfigDto, MeditionDto
from app.models import Equipment, User, Configuration, ProductMedition
import matplotlib.pyplot as plt
from io import BytesIO
from fastapi.responses import StreamingResponse

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
        #TODO: debe desactivar todas las configuraciones previa y dejar activa la nueva
        config_model.create(
            #config=body.config,
            description=body.description,
            equipment=body.equipment,
            name=body.name
        )
        
        return {'success': True}
    
    async def register_medition(self, body: MeditionDto):
        medition_model: ProductMedition = self.deps['models']['producto_medition']
        #TODO: Cambiar order_sent, se deben añadir mas columnas y ser del tipo ENUM
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
       
        if config.get('soil_low_humidity') <= body.soil_humidity:
            activate_irrigation = True
            
        if config.get('soil_max_humidity') >= body.soil_humidity:
            activate_irrigation = False
                    
        response = {
            'activate_irrigation': activate_irrigation
        }
        
        medition.order_sent = activate_irrigation
        medition.save()
        
        return response
    
    async def activate_config(self, body: EquipmentDto):
        # TODO: activar configuracion especifica (desactiva todas las siguientes)
        pass
    
    async def get_medition(self, user):
        medition_model: ProductMedition = self.deps['models']['producto_medition']
        meditions = list(
            medition_model.select(
                medition_model.soil_humidity, medition_model.ambient_humidity, medition_model.order_sent
            )
            .where(medition_model.equipment == 1)
            .order_by(medition_model.id.desc())
            .limit(50)
            .dicts()
        )

        soil_humidity_values = [float(medition['soil_humidity']) for medition in meditions]
        ambient_humidity_values = [float(medition['ambient_humidity']) for medition in meditions]
        order_sent_labels = ['Riego' if m['order_sent'] else '' for m in meditions]
        # Creamos la figura y el eje
        fig, ax1 = plt.subplots()       

        # Graficamos la humedad del suelo con color azul
        ax1.plot(soil_humidity_values, color='blue', marker='o', label='Soil Humidity')     

        # Creamos un segundo eje para las otras mediciones
        ax2 = ax1.twinx()       

        # Graficamos la humedad ambiental con color verde
        ax2.plot(ambient_humidity_values, color='green', marker='x', label='Ambient Humidity')      

        # Graficamos la temperatura ambiental con color rojo

        # Añadimos títulos y etiquetas
        ax1.set_title('Soil and Ambient Conditions Over Time')
        ax1.set_xlabel('Measurement Number')
        ax1.set_ylabel('Soil Humidity', color='blue')
        ax2.set_ylabel('Ambient Conditions', color='green')     

        # Añadimos las leyendas
        ax1.legend(loc='upper left')
        ax2.legend(loc='upper right')       

        # Añadimos las etiquetas de 'order_sent' al gráfico con un zorder más alto para que se dibuje por encima
        for i, (label, y_value) in enumerate(zip(order_sent_labels, soil_humidity_values)):
            ax1.text(i, y_value, f'{label}', color='red', fontsize=14, ha='center', va='bottom', zorder=3)
    
        # Ajustamos los límites si es necesario
        """ ax1.set_ylim([220, 250])
        ax2.set_ylim([40, 50])      """ 

        # Guardamos el gráfico en un buffer en lugar de un archivo
        buf = BytesIO()
        plt.savefig(buf, format='png')
        buf.seek(0)  # Regresamos al inicio del buffer      

        # Devolvemos el buffer como una respuesta StreamingResponse
        return StreamingResponse(buf, media_type="image/png")
    
EquipmentServiceSingleton = EquipmentService(equipment_service_deps)
