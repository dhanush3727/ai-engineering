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

# else
user = {
    "name": "Dhanush",
    "age": 22
}
try:
    age = int(user["age"])
except KeyError:
    print("Age field is missing")
except ValueError:
    print("Age value is invalie")
except TypeError:
    print("Age has an invalid type")
else:
    print(f"Successfully print {user['name']}: {age}")

# finally
try:
    age = int(user["age"])
except ValueError:
    print("Invalid age")
else:
    print(f"Processed {user['name']}: {age}")
finally:
    print("User processing attempt finished")

# raise
def validate_hours(hours):
    if hours < 0:
        raise ValueError("Operating hours cannot be negative")
    return hours
try:
    result = validate_hours(-50)
    print(result)
except ValueError as error:
    print(f"Invalid hour {error}")

# re-raise
def eqiupment_fun():
    try:
        hours = int("unknown")
        print(hours)
    except ValueError as error:
        print(f"Import failed: {error}")
        raise
try:
    eqiupment_fun()
except ValueError as error:
    print(f"Caller received the error: {error}")

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

# Exercise 2
def validate_equipment(records):
    result = []
    for equipment in records:
        try:
            hours = int(equipment["hours"])
        except KeyError:
            print(f"Missing hours field for {equipment['name']}")
        except ValueError:
            print(f"Invalid hours value for {equipment['name']}")
        except TypeError:
            print(f"Invalid data type for {equipment['name']}")
        else:
            result.append({
                "name": equipment["name"],
                "hours": hours
            })

    return result
print(validate_equipment(equipment_records))

# Exercise 3
def import_equipment(records):
    result = []
    for equipment in records:
        try:
            hours = int(equipment["hours"])
        except KeyError:
            print(f"Missing hours field for {equipment['name']}")
        except ValueError:
            print(f"Invalid hours value for {equipment['name']}")
        except TypeError:
            print(f"Invalid data type for {equipment['name']}")
        else:
            result.append({
                "name": equipment["name"],
                "hours": hours
            })
        finally:
            print(f"Finished attempting: {equipment["name"]}")
    return result
print(import_equipment(equipment_records))

# Exercise 4
def import_equipment(records):
    result = []
    for equipment in records:
        try:
            hours = int(equipment['hours'])
            if hours < 0:
                raise ValueError("Operating hours cannot be negative")
        except ValueError as error:
            print(error)
        else: 
            result.append({
                "name": equipment['name'],
                "hours": hours
            })
        
    return result

equipment_records = [
    {"name": "Motor", "hours": "120"},
    {"name": "Pump", "hours": "-10"},
    {"name": "Compressor", "hours": "unknown"},
    {"name": "Fan", "hours": "85"},
    {"name": "Generator", "hours": "0"}
]
print(import_equipment(equipment_records))