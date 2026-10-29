from typing import TypedDict
from typing import Literal

# Type Hints: Way to declare a what type of data.
def calculate_maintenance_cost(hours_worked: float, coust_per_hour: float) -> float:
    return hours_worked * coust_per_hour
print(calculate_maintenance_cost(12.5, 80.0))

# None value
def display_equipment_info(name: str, operating_hours: int) -> None:
    print(f"{name}: {operating_hours}")
result = display_equipment_info("Motor", 120)
print(result)

# Optional value
def find_equipment_location(equipment_name: str) -> str | None:
    if equipment_name == "Motor":
        return "Factory Floor"
    elif equipment_name == "Pump":
        return "Water Room"
    return None
print(find_equipment_location("Pump"))
print(find_equipment_location("Fan"))

# Optional parameter
def create_maintenance_record(equipment_name: str, priority: str = "Medium") -> dict[str, str]:
    return {
        'name': equipment_name,
        'priority': priority
    }
print(create_maintenance_record("Motor"))
print(create_maintenance_record("Pump", "High"))

# Collection type hints
equipment_name:list[str] = ["Motor", "Pump", "Fan"]

operating_hours: dict[str, int] = {
    "Motor": 120,
    "Pump": 85
}

def get_maintenance_hours(equipment_names: list[str]) -> dict[str, int]: 
    all_equipment: dict[str, int] = {
        "Motor" : 120,
        "Pump": 85,
        "Fan": 60
    }

    result: dict[str, int] = {}

    for name in equipment_names:
        if name in all_equipment:
            result[name] = all_equipment[name]

    return result
print(get_maintenance_hours(["Motor", "Fan"]))

# Tuple and Set type hints
def get_equipment_summary() -> tuple[str, int]:
    return ("Pump", 85)

def get_equipment_categories() -> set[str]:
    return {"Mechanical", "Electrical", "Mechanical"}

print(get_equipment_summary())
print(get_equipment_categories())

# TypedDict: Which keys it should contain and the type of value associated with each key.
class MaintenanceRecord(TypedDict):
    equipment: str
    priority: str
    hours: int

def get_maintenance_record() -> MaintenanceRecord:
    return {
        "equipment": "Motor",
        "priority": "High",
        "hours": 120
    }
print(get_maintenance_record())

# Literal: lets you restrict a variable or parameter to specific allowed values.
MaitenancePriority = Literal["Low", "Medium", "High"]
def set_priority(priority: MaitenancePriority) -> None:
    print(f"Equipment priority is {priority}")
set_priority("High")

# Union type
def format_hours(hours: int | float) -> str:
    return f"Operating hours: {hours}"
print(format_hours(120))
print(format_hours(85.5))

# Type Aliases: gives a reusble name to an existing type.
type EquipmentId = int | str
def format_equipment_id(equipment_id: EquipmentId) -> str:
    return f"Equipment ID: {equipment_id}"
print(format_equipment_id(101))

# Type narrowing: checking a value's type so Python's type checker can understand which type you're working with.
def format_hour(hours: int | str) -> str:
    if isinstance(hours, str):
        return hours.upper()
    return f"Hours: {hours}"
print(format_hour(120))
print(format_hour("Unknown"))