from app.models import Equipment, Configuration, ProductMedition

equipment_service_deps = {
    "models":{
        'equipment': Equipment,
        'configuration': Configuration,
        'producto_medition': ProductMedition,
    }
}
