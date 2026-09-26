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