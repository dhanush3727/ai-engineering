# Class
class Equipment:
    # This is a class attribute
    category = "Industrial Equipment"

    # When a new Equipment object is initialize python calls init automatically
    def __init__(self, name, hours):
        # This is a instance attribute
        self.name = name
        self.hours = hours

    # Create method
    def remaining_hours(self):
        return 200 - self.hours

motor = Equipment("Motor", 120)
print(motor.remaining_hours())

fan = Equipment("Fan", 60)
print(fan.remaining_hours())
print(fan.category)