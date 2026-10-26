# Class
class Equipment:
    # This is a class attribute
    category = "Industrial Equipment"

    # When a new Equipment object is initialize python calls init automatically
    def __init__(self, name, hours):
        # Add validation inside class
        if hours < 0:
            raise ValueError("Operating hours cannot be negative")

        if not name.strip():
            raise ValueError("Equipment name cannot be empty")

        # This is a instance attribute
        self.name = name
        self.hours = hours

    # Class Methods
    @classmethod
    def get_category(cls):
        return cls.category

    # Static Methods
    @staticmethod
    def is_valid_name(name):
        return bool(name.strip()) # Strip removes the whitespaces from begining and end

    # Create method
    def remaining_hours(self):
        return 200 - self.hours

    # Modify an object's data
    def update_hours(self, additional_hours):
        if additional_hours < 0:
            raise ValueError("Additional operating hours cannot be negative")
        self.hours += additional_hours

print(Equipment.get_category())
print(Equipment.is_valid_name("Motor"))
print(Equipment.is_valid_name(" "))
motor = Equipment("Motor", 120)
print("Motor",motor.get_category())
motor.update_hours(15)
print(motor.hours)
try:
    motor.update_hours(-200)
except ValueError as error:
    print(error)
print(motor.hours)
print(motor.remaining_hours())

fan = Equipment("Fan", 60)
print(fan.remaining_hours())
print(fan.category)
fan.update_hours(100)
print(fan.hours)

try:
    motor = Equipment("Motor", -160)
except ValueError as error:
    print(error)

try:
    motor = Equipment("", 160)
except ValueError as error:
    print(error)

# Example
class Vehicle:
    # Class attribute: shared default information for the class
    category = "Transport"

    # Constructor: runs when a new Vehicle object is initialized
    def __init__(self, brand, speed):
        # Validate values before assigning instance attributes
        if not brand.strip():
            raise ValueError("Vehicle brand cannot be empty")

        if speed < 0:
            raise ValueError("Speed cannot be negative")

        # Instance attribute: each object has its own values
        self.brand = brand
        self.speed = speed

    # Instance method: uses self to access a specific object's data
    def get_details(self):
        return f"{self.brand} travels at {self.speed} km/h"

    def increase_speed(self, additional_speed):
        if additional_speed < 0:
            raise ValueError("Additional speed cannot be negative")

        self.speed += additional_speed

    # Class method: receives the class through cls
    @classmethod
    def create_new(cls, brand):
        # Creates a vehicle object with a default speed of 0
        return cls(brand, 0)

    # Static method: receives neither self nor cls automatically
    @staticmethod
    def is_valid_speed(speed):
        return speed >= 0

# Create two independent objects using the constructor 
car = Vehicle("Toyota", 100)
bike = Vehicle("Honda", 60)

# Access instance attributes
print(car.brand) # Toyota
print(bike.brand) # Honda

# Access class attribute
print(Vehicle.category)

# Call instance methods
print(car.get_details())   # Toyota travels at 100 km/h
print(bike.get_details())  # Honda travels at 60 km/h

# Modify one object's state
car.increase_speed(20)
print(car.speed)  # 120
print(bike.speed) # 60 — unchanged

# Use a class method to create an object
truck = Vehicle.create_new("Volvo")
print(truck.brand)  # Volvo
print(truck.speed)  # 0

# Use a static method to validate a value
print(Vehicle.is_valid_speed(80))   # True
print(Vehicle.is_valid_speed(-10))  # False

# 16. Handle validation errors
try:
    invalid_car = Vehicle("", 100)
except ValueError as error:
    print(error)  # Vehicle brand cannot be empty

try:
    bike.increase_speed(-20)
except ValueError as error:
    print(error)  # Additional speed cannot be negative

# Exercise 1
class Equipment:
    @classmethod
    def create_with_default_hours(cls, name):
        return cls(name, 100)

    def __init__(self, name, hours):
        self.name = name
        self.hours = hours

    @staticmethod
    def is_valid_hours(hours):
        if hours < 0:
            return False

        return True

pump = Equipment.create_with_default_hours("Pump")
print(pump.name)
print(pump.hours)
print(Equipment.is_valid_hours(120))
print(Equipment.is_valid_hours(-10))
motor = Equipment("Motor", -10)