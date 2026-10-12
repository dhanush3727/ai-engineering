# Exception
equipment = {
    "name": "Motor",
    "hours": 123
}

# try and exception
try:
    print(equipment["status"])
except:
    print("Equipment status is unavailable")

print("Continue processing")

equipment = {
    "name": "Pump",
    "hours": "None"
}
try:
    hours = int(equipment["hours"])
    print(hours)
except KeyError:
    print("Missing equipment field")
except ValueError:
    print("Invalid hours value")
except TypeError:
    print("Invalid data type")

# Exercise 1
equipment_records = [
    {"name": "Motor", "hours": "120"},
    {"name": "Pump", "hours": "unknown"},
    {"name": "Compressor"},
    {"name": "Generator", "hours": None},
    {"name": "Fan", "hours": "85"}
]

def process_equipment(records):
    result = []
    for equipment in records:
        try:
            hours = int(equipment["hours"])
            result.append({
                "name": equipment["name"],
                "hours": hours
            })
        except KeyError:
            print(f"Missing hours field for {equipment['name']}")
        except ValueError:
            print(f"Invalid hours value for {equipment['name']}")
        except TypeError:
            print(f"Invalid data type for {equipment['name']}")

    return result
print(process_equipment(equipment_records))