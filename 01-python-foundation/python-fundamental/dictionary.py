# Dictonaries
user = {
    "name": "Dhanush",
    "age": 22,
    "is_working": True,
    "skills": ["React", "TypeScript", "Python"],
    "profile": {
        "job": "Software Developer",
        "experience": 2
    }
}
print(user)
print(type(user)) # <class 'dict'>

# Accessing values
print(user["name"])
print(user["age"])
print(user["skills"])

# Adding new key
user["status"] = "Single"
print(user)

# updating value
user["age"] = 23
user["skills"][0] = "Next"
print(user)

# removing a key
del user["is_working"]
age = user.pop("age")
print(user)
print(age)

# Checking whether a key exists
print("age" in user) # False
print("name" in user) # True

# .get()
# print(user["email"]) # it return error because there is no email key
print(user.get("email"))

# Getting keys and values
print(user.keys()) # dict_keys(['name', 'skills', 'profile', 'status'])
print(user.values()) # dict_values(['Dhanush', ['Next', 'TypeScript', 'Python'], {'job': 'Software Developer', 'experience': 2}, 'Single'])

# Looping through a dictionary
for key, value in user.items():
    print(f"{key}: {value}")

# Exercise 1: Basic dictionary
user = {
    "name": "Dhanush",
    "age": 22,
    "role": "Software Developer",
    "experience": 2
}
print(user["name"])
print(user["role"])
user["experience"] = 3
user["is_learning_ai"] = True
print("email" in user)
print(user.get("email", "Not Provided"))

# Exercise 2: Nested dictionary
equipment = {
    "name": "Motor",
    "status": "Running",
    "location": {
        "building": "A",
        "floor": 2
    }
}
print(equipment["name"])
print(equipment["status"])
print(equipment["location"]["building"])
print(equipment["location"]["floor"])

# Exercise 3: Looping
skills = {
    "frontend": "React",
    "backend": "NestJS",
    "database": "PostgreSQL",
    "language": "TypeScript"
}
for key, value in skills.items():
    print(f"{key}: {value}")


# Dictionary Comprehensions
# Exercise 1
numbers = [1, 2, 3, 4, 5]
squares = {
    num: num * num
    for num in numbers
}
print(squares)

# Exercise 2
uppercase_skills = {
    category: skill.upper()
    for category, skill in skills.items()
}
print(uppercase_skills)

# Exercise 3: Transforming an exising dictionary
scores = {
    "doc_1": 0.92,
    "doc_2": 0.41,
    "doc_3": 0.87,
    "doc_4": 0.32
}
relevant_documents = {
    doc: score
    for doc, score in scores.items()
    if score >= 0.8
}
print(relevant_documents)