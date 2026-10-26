# Python for AI Engineering - Python Engineering
## Type Hints:
A way to declare what type of data a variable, function parameter, or return value is expected to have in python. Python does not automatically enforce type hints at runtime. Type hints describe the intended types; tools such as `Pyright` and `mypy` can check whether your code follows those expectations.
```py
def calculate_maintenance_cost(hours_worked: float, coust_per_hour: float) -> float:
    return hours_worked * coust_per_hour
print(calculate_maintenance_cost(12.5, 80.0))
print(calculate_maintenance_cost(12.5, "80.0"))
```