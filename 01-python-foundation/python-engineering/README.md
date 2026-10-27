# Python for AI Engineering - Python Engineering
## Type Hints:
A way to declare what type of data a variable, function parameter, or return value is expected to have in python. Python does not automatically enforce type hints at runtime. Type hints describe the intended types; tools such as `Pyright` and `mypy` can check whether your code follows those expectations.
```py
def calculate_maintenance_cost(hours_worked: float, coust_per_hour: float) -> float:
    return hours_worked * coust_per_hour
print(calculate_maintenance_cost(12.5, 80.0))
print(calculate_maintenance_cost(12.5, "80.0"))
```

### Collection type hints:
In Python, collection type hints tell the type checker what kinds of values a list, dictionary, or other collection is expected to contain.
Ex:
```py
equipment_name:list[str] = ["Motor", "Pump", "Fan"]

operating_hours: dict[str, int] = {
    "Motor": 120,
    "Pump": 85
}
```

### `TypedDict`:
`TypedDict` lets you define the expected structure of a dictionary, which keys it should contain and the type of value associated with each key. We must import the `TypedDict`.
Ex:
```py
from typing import TypedDict

class EquipmentRecord(TypedDict):
    name: str
    hours: int
    location: str

equipment: EquipmentRecord = {
    "name": "Motor",
    "hours": 120,
    "location": "Factory floor"
}
```

### `Literal`:
`Literal` lets you restrict a variable or parameter to specific allowed values
Ex:
```py
from typing import Literal

Priority = Literal["Low", "Medium", "High"]

def create_task(priority: Priority) -> None:
    print(f"Priority: {priority}")
```

### Type narrowing:
Type narrowing means checking a value's type so python's type checker can understand which type you're working with. Use `isinstance()` to check the type.


## `dataclass`:
A dataclass is a convenient way to create a python class that mainly stores data.
Ex:
```py
from dataclasses import dataclass

@dataclass
class Equipment:
    name: str
    hours: int

motor = Equipment("Motor", 120)
```

## Enum:
An enum lets you define a fixed set of named values.
Ex:
```py
from enum import Enum

class Priority(Enum):
    LOW = "Low"
    MEDIUM = "Medium"
    HIGH = "High"

task_priority = Priority.HIGH
```