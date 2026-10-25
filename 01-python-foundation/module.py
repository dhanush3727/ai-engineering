from equipment import Equipment

# import an entire module
import calculator as calc

motor = Equipment("Motor", 120)
print(motor.get_details())
print(calc.add(10, 20))
print(calc.subtract(10, 5))