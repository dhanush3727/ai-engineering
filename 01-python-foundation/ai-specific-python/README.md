# AI-Specific Python Library:
## Numpy(Numerical python):
`Numpy` is a library for working with numerical data efficiently. Python has lists, but Numpy provides specialized arrays and optimized mathematical operations.

### How does it work?
Install it inside your active `.venv`,  `python -m pip install numpy`. Example
```py
import numpy as np

equipment_hours = np.array([1200, 1800, 2400, 3000])

print(equipment_hours)
print(equipment_hours.mean())
print(equipment_hours.max())
```
- `np.array()` creates a Numpy array.
- `.mean()` calculates the average.
- `.max()` finds the highest value.

## Pandas:
`Pandas` is a python library used to work with structured data, such as tables, CSV files, and datasets. Think of it as working with Excel data using python.

### How does it work?
Install the pandas: `python -m pip install pandas`.
```py
import pandas as pd

data = {
    "equipment": ["Pump", "Motor", "Compressor"],
    "hours": [1200, 2500, 3200],
    "status": ["Active", "Active", "Maintenance"]
}

df = pd.DataFrame(data)

print(df)
```
Here, 
- `DataFrame` creates a table.
- Each column represents a field.
- Each row represents a record.

## Pydantic:
`Pydantic` is a python library used to validate data and enforce its structure using type annotations. Think of it like Zod in TypeScript.

### How does it work?
Install it: `python -m pip install pydantic`.
```py
from pydantic import BaseModel

class Equipment(BaseModel):
    name: str
    operating_hours: int
    status: str

equipment = Equipment(
    name="Industrial Pump",
    operating_hours=2500,
    status="Active"
)

print(equipment)
print(equipment.model_dump())
```
- `BaseModel`: Base class used to define a Pydantic model.
- `name: str`: Declares the expected filed types.
- `model_dump()`: Converts the validated model into a Python dictionary.
- Invalid data raises a `ValidationError`.

