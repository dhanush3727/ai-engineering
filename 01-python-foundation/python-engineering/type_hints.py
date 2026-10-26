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

# 