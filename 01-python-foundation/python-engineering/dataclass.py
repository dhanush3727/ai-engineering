# dataclass: convenient way to create a python class
from dataclasses import dataclass

@dataclass
class MaintenanceTask:
    equipment_name: str
    # Default values
    priority: str = "Medium"
    hours: int = 0

motor = MaintenanceTask("Motor", "High", 120)
pump = MaintenanceTask("Pump")
print(pump)
