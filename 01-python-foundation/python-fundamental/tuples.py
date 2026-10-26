# Tuples
coordinates = (10, 20)
user = ("Dhanush", 22, True)
print(coordinates)
print(user)
print(type(coordinates))

# Create a tuple with one element use comma
numbers = (10,)
print(type(numbers)) # <class 'tuple'>
# if there is no comma then it take as int
numbers =(10)
print(type(numbers)) # <class 'int'>

# Tuples are immutable that is we can't modify the tuple like list.
# Otherwise tuples same like list
equipment = ("motor", "pump", "compressor")
# equipment[0] = "Generator" # It return error

# Tuple unpacking
name, age, boolean = user
print(name)
print(age)
print(boolean)

# Exercise 1
equipment = ("Motor", "Pump", "Compressor", "Generator")
print(f"Print first equipment: {equipment[0]}")
print(f"Print last equipment: {equipment[-1]}")
print(f"Print first two equipment: {equipment[0:2]}")
print(f"Print the length: {len(equipment)}")
print("Pump" in equipment)

# Exercise 2
equipment = ("Motor", "Pump", "Compressor")
first, second, third = equipment
print(first)
print(second)
print(third)

# Exercise 3
equipment[0] = "Generator"