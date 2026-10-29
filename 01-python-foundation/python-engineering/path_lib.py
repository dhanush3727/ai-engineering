# pathlib - It working with file and folder path.
from pathlib import Path

file_path = Path("data") / "equipment.json"
print(file_path)
print(file_path.name)
print(file_path.suffix)
print(file_path.is_dir())
print(file_path.is_file())
if file_path.exists():
    print("Equipment file exists")
else:
    print("Equipment file not exist")

# Task
mainthence_file = Path("01-python-foundation") / "python-engineering" / "data" / "maintenance.json"
print(mainthence_file)
print(mainthence_file.name)
print(mainthence_file.suffix)
if mainthence_file.exists():
    print("Maintenance record exists")
else:
    print("Maintenance record not found")

mainthence_file.parent.mkdir(parents=True, exist_ok=True)
mainthence_file.touch(exist_ok=True)
print(mainthence_file.exists())