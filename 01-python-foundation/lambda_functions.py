# Lambda Functions is a small, anonymous function written in a single expression
square = lambda num: num * num
print(square(10))

# Exercise 1
square = lambda num: num * num
print(square(7))

# Exercise 2
is_relevant = lambda score: score >= 0.8
print(is_relevant(0.92))
print(is_relevant(0.41))

# Exercise 3
equipment = [
    {"name": "Motor", "hours": 120},
    {"name": "Pump", "hours": 80},
    {"name": "Compressor", "hours": 200}
]
equipment.sort(key=lambda item: item["hours"])
for item in equipment:
    print(item["name"])