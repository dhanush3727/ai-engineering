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

## `pathlib`:
`pathlib` is Python module for working with file and folder paths. It makes it easier to create paths, check whether files exist, and read file information without manually joining path strings.
Ex:
```py
from pathlib import Path

# Create path object
mainthence_file = Path("01-python-foundation") / "python-engineering" / "data" / "maintenance.json"
print(mainthence_file)
print(mainthence_file.name)
print(mainthence_file.suffix)
if mainthence_file.exists():
    print("Maintenance record exists")
else:
    print("Maintenance record not found")

# Create the exact path using the path object
mainthence_file.parent.mkdir(parents=True, exist_ok=True)
mainthence_file.touch(exist_ok=True)
print(mainthence_file.exists())
```
In this example,
- `parent`: Gets the directory containing the file.
- `mkdir()`: Creates a directory.
- `parents=True` tells python to create all missing parent folders in the path.
- `exist_ok=True` in `mkdir()` tells python not to raise an error if the directory already exists.
- `touch(exist_ok=True)` creates an empty file if it don't exist.

## `datetime`:
`datetime` is a built-in Python module for working with date, times and time differences.
Ex:
```py
from datetime import datetime

breakdown_time = datetime.now()
print(breakdown_time)
print(breakdown_time.year)
print(breakdown_time.strftime("%d-%m-%y"))
```

## JSON:
JSON is a format to storing and exchanging structured data between application. The methods or,
- `json.dumps()`: convert python object into JSON string.
- `json.loads()`: convert JSON string into python object.
- `json.dump()`: write python data to a JSON file.
- `json.load()`: Read data from JSON file.

## Environment Variable:
Create and load env variables in python
Step 1: Install the package in your activated virtual environment.
```bash
pip install python-dotenv
```
Step2: Create a `.env` file in your project directory.
```env
APP_NAME=Maintix
```
Step 3: Load the file in python
```py
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    raise ValueError("OPENAI_API_KEY is missing")

print("API key loaded successfully")
```

## Logging:
Logging lets your application record what happens while it runs, such a successful operations, warnings and errors. The levels are
- `DEBUG`: Detailed information for debugging
- `INFO`: Normal application events
- `WARNING`: Something unexpected may need attention
- `ERROR`: An operation failed
- `CRITICAL`: A severe failure
Ex:
```py
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def summarize_breakdown(equipment_name: str) -> str:
    logger.info("Summarizing breakdown for %s", equipment_name)

    if not equipment_name:
        logger.error("Equipment name is missing")
        raise ValueError("Equipment name is required")

    return f"Breakdown report for {equipment_name}"

result = summarize_breakdown("Pump")
print(result)
```

## File handling:
```py
from pathlib import Path

report_path = Path("01-python-foundation") / "python-engineering" / "maintenance.txt"
report_path.parent.mkdir(parents=True, exist_ok=True)

report = "Equipment: Motor\nPriority: High\n"

with open(report_path, "w", encoding="utf-8") as file:
    file.write(report)

with open(report_path, "r", encoding="utf-8") as file:
    saved_path = file.read()

print(saved_path)
```
Here, `pathlib` builds the path and creates the directory, while file handling writed and reads the report. The important file modes are:
- `"r"`: Read and existing file.
- `"w"`: Write; creates the file or replaces its existing contents.
- `"a"`: Append content to the end.
- `"x"`: Create a new file; fail if it already exists.

## HTTP Request:
Install the requests using the command `python -m pip install requests`.
```py
import requests

url = "https://httpbin.org/post"

equipment = {
    "name": "Industrial Pump",
    "hours": 2500,
    "issue": "Unusual vibration"
}

try:
    response = requests.post(url, json=equipment, timeout=10)
    response.raise_for_status()

    result = response.json()
    print(result["json"])

except requests.RequestException as error:
    print(f"Request failed: {error}")
```
Here `httpbin.org` is a testing service, not a real AI API,
- `request.post()`: sends a POST request.
- `json=equipment`: converts the python dictionary to JSON and sends it in the request body.
- `timeout=10`: Maximum number of seconds the program will wait for the server to respond.
- `raise_for_status()`: parses the returned JSON.
- `except` handles request-related failures, including connection errors and timouts.

## async/await:
