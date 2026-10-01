# List Comprehension - It is compact way to create new list
numbers = [1,2,3,4,5]
squares = [num * num for num in numbers]
print(squares)

# with condition
even_numbers = [num for num in numbers if num % 2 ==0]
print(even_numbers)

# Exercise 1
documents = ["motor", "pump", "compressor"]
upper_document = [doc.upper() for doc in documents]
print(upper_document)

# Exercise 2
scores = [0.92, 0.41, 0.87, 0.32, 0.95, 0.61]
new_scores = [score for score in scores if score >= 0.8]
print(new_scores)

# Exercise 3
numbers = [1,2,3,4,5,6,7,8]
even_squares = [num * num for num in numbers if num % 2 ==0]
print(even_squares)

# Dictionary Comprehension - A dictionary comprehension creates a new dictionary from an iterable.
scores = {
    "doc_1": 0.92,
    "doc_2": 0.41,
    "doc_3": 0.87
}
percentages = {
    doc: score * 100
    for doc, score in scores.items()
    if score >= 0.8
}
print(percentages)

# Exercise 1
equipment = {
    "motor": "active",
    "pump": "maintenance",
    "compressor": "active"
}
transform_equipment = {
    key.upper(): value
    for key, value in equipment.items()
}
print(transform_equipment)

# Exercise 2
scores = {
    "doc_1": 0.92,
    "doc_2": 0.41,
    "doc_3": 0.87,
    "doc_4": 0.32,
    "doc_5": 0.95
}
filter_scores = {
    doc: score
    for doc, score in scores.items()
    if score >=0.8
}
print(filter_scores)

# Exercise 3
equipment_hours = {
    "motor": 120,
    "pump": 80,
    "compressor": 200,
    "generator": 50
}
hours = {
    equip: hour * 2
    for equip, hour in equipment_hours.items()
    if hour >= 100
}
print(hours)