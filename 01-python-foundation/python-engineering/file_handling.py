# file handling:
from pathlib import Path

report_path = Path("01-python-foundation") / "python-engineering" / "maintenance.txt"
report_path.parent.mkdir(parents=True, exist_ok=True)

report = "Equipment: Motor\nPriority: High\n"

with open(report_path, "w", encoding="utf-8") as file:
    file.write(report)

with open(report_path, "r", encoding="utf-8") as file:
    saved_path = file.read()

print(saved_path)