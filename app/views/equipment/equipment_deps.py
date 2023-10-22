from app.services.equipment.equipment_service import EquipmentServiceSingleton

equipment_deps = {
    "services": {
        "EquipmentServiceSingleton": EquipmentServiceSingleton
    },
}
