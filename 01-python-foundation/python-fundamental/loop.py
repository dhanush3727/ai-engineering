# Loop
# for loop
for i in range(6):
    print(i)

technologies = ["Python", "React", "Node.js"]
for technology in technologies:
    print(technology)

# for loop range with step
for i in range(1, 10, 2):
    print(i)

# Exercise 1
numbers = [10, 20, 30, 40, 50]
for number in numbers:
    print(number)

# Exercise 2
for number in numbers:
    print(f"Number: {number}")

# Exercise 3
numbers = [1, 2, 3, 4, 5]
for num in numbers:
    print(num * num)

# Exercise 4
for i in range(1,6):
    print(i)

# Exercise 5 - Maintenance schedule
start_day = 1
end_day = 15
for day in range(start_day, end_day + 1, 2):
    print(f"Inspection: Day {day}")

# Exercise 6 - Reverse countdown
for count in range(10, 0, -1):
    print(f"reverse: {count}")

# Exercise 7 - Process every 3rd record
for record in range(3, 20, 3):
    print(f"Processing record {record}")

# Exercise 8
for count in range(10, 1, -2):
    print(count)

# enumerate - print index and value together
equipment = ["motor", "pump", "compressor"]
for index, item in enumerate(equipment):
    print(index, item)

# can also choose the starting index
for number, item in enumerate(equipment, start=1):
    print(number, item)

# Exercise 9
equipments = ["Motor", "Pump", "Compressor", "Generator"]
for equipId, equipment in enumerate(equipments, start=1):
    print(f"Equipment {equipId}: {equipment}")

# Exercise 10
technologies = ["React", "TypeScript", "Next.js", "Python", "PostgreSQL"]
for index, item in enumerate(technologies):
    if item == "Python":
        print(f"Python is at position {index}")

# Exercise 11
documents = [
    "Maintenance schedule for Motor A",
    "Pump failure history",
    "Compressor inspection report",
    "Generator service record"
]
for number, doc in enumerate(documents, start=1):
    print(f"Processing document {number}: {doc}")

# While loop
# Exercise 12
attempt = 1
while attempt <= 3:
    print(f"Attempt {attempt}")
    attempt += 1

# Exercise 13
steps_remaining = 5
while steps_remaining >= 1:
    print(f"Steps remaining: {steps_remaining}")
    steps_remaining -= 1

# Exercise 14
battery = 100
while battery > 0:
    print(f"Battery: {battery}%")
    battery -= 20

# Break - Stop the entire loop
# Continue - Skip the current iteration
# Exercise 15
documents = [
    "doc_1",
    "doc_2",
    "doc_3",
    "doc_4",
    "doc_5"
]
for index, item in enumerate(documents):
    if item == "doc_4":
        break
    print(f"Processing {item}")

# Exercise 16
documents = [
    "doc_1",
    "invalid",
    "doc_2",
    "invalid",
    "doc_3"
]
for index, item in enumerate(documents):
    if item == "invalid":
        continue
    print(f"Processing {item}")

# Exercise 17
numbers = [10, 20, 30, 40, 50]
for index, num in enumerate(numbers):
    if num == 30:
        continue
    if num == 50:
        break
    print(num)

# Exercise 18
equipment = ["Motor", "Pump", "Generator"]
days = ["Monday", "Wednesday", "Friday"]
for machine in equipment:
    for day in days:
        print(f"{machine} - {day}")

# Exercise 19
equipment = [
    "Motor",
    "Pump",
    "invalid",
    "Compressor",
    "Generator"
]
for equip in equipment:
    if equip == "invalid":
        continue
    if equip == "Generator":
        break
    print(f"Processing {equip}")

# Exercise 20
record = 5
while record <= 25:
    print(f"Processing record {record}")
    record += 5

# Exercise 21
attempt = 1
while attempt <= 4:
    print(f"Attempt {attempt}")
    attempt += 1
print('Operation stopped')

# Exercise 22
scores = [0.91, 0.42, 0.85, 0.31, 0.95]
for score in scores:
    if score < 0.5:
        continue
    print(f"Relevant score: {score}")
    if score >= 0.9:
        break
    