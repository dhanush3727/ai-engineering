# Class
class Equipment:
    # This is a class attribute
    category = "Industrial Equipment"

    # Class Methods
    @classmethod
    def get_category(cls):
        return cls.category

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

    # Create method
    def remaining_hours(self):
        return 200 - self.hours

    # Modify an object's data
    def update_hours(self, additional_hours):
        if additional_hours < 0:
            raise ValueError("Additional operating hours cannot be negative")
        self.hours += additional_hours

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