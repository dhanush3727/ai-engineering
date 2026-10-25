# Inheritance: It allows one class to reuse and extend the attributes and methods of another class.
class Equipment:
    def __init__(self, name, hours):
        self.name = name
        self.hours = hours

    def get_details(self):
        return f"{self.name}: {self.hours} hours"

class Motor(Equipment):
    # This runs the parent's constructor to initialize the inherited attributes.
    def __init__(self, name, hours, power_kw):
        super().__init__(name, hours)
        self.power_kw = power_kw

    def maitnenace_due(self):
        return 200 - self.hours

    # Method overriding: A child class can define a method with the same name as it's parent's method.
    def get_details(self):
        return f"Motor {self.name}: {self.hours} operating hours"

class Pump(Equipment):
    def additional_hours(self, hours):
        self.hours += hours

    def get_details(self):
        return f"Pump {self.name}"

class Truck(Equipment):
    def get_details(self):
        # super(): reuse the parent's behavior and extend it
        parent_details = super().get_details()
        return f"{parent_details} - Truck"

class Screw(Equipment):
    def get_details(self):
        return super().get_details() + " - Screw"

motor = Motor("A1", 120, 140)
pump = Pump("B1", 85)
truck = Truck("T1", 40)
screw = Screw("S1", 50)
print(motor.power_kw)
print(motor.get_details())
print(motor.maitnenace_due())
print(pump.get_details())
print(truck.get_details())
print(screw.get_details())

# Exercise 1
class AirCompressor(Equipment):
    def __init__(self, name, hours, power):
        super().__init__(name, hours)
        self.power = power

    def get_power(self):
        return self.power

    def get_details(self):
        return f"{super().get_details()}, Power: {self.power}"

air_compressor = AirCompressor("A1", 120, 5)
print(air_compressor.name)
print(air_compressor.hours)
print(air_compressor.get_power())
print(air_compressor.get_details())