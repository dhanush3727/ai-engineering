#JSON: A format for storing and exchanging data between application.
import json
from typing import TypedDict

class Equipment(TypedDict):
    name: str
    hours: int
    is_active: bool

equipment: Equipment = {
    'name': "Motor",
    'hours': 500,
    'is_active': True
}

# convert python -> json
json_data = json.dumps(equipment)
print(json_data)

# convert json -> python
python_data = json.loads(json_data)
print(python_data["name"])