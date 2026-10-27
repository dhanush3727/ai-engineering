# Enum: Lets you define a fixed set of named values.
from enum import Enum

class MaintenancePriority(Enum):
    LOW = "Low"
    MEDIUM = "Medium"
    HIGH = "High"
maintenance_priority = MaintenancePriority.HIGH
print(maintenance_priority)
print(maintenance_priority.value)