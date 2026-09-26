# Conditions
# if condition
age = 18
if age >= 18:
    print("Adult")
else:
    print("Minor")

score = 75
if score >= 90:
    print("A")
elif score >= 75:
    print("B")
elif score >= 60:
    print("C")
else:
    print("D")

# Comparison operators
print(age == 22)
print(age != 18)
print(age > 20)
print(age < 30)
print(age >= 22)
print(age <= 25)

# and, or, not
experience = 2
if age >= 18 and experience >= 2:
    print("Eligible")

role = "admin"
if role == "admin" or role == "manager":
    print("Can access dashboard")

is_logged_in = False
if not is_logged_in:
    print("Please login")

# Conditions with collections
skills = ["React", "Python", "TypeScript"]
if "Python" in skills:
    print("Python found")

allowed_roles = {"ADMIN", "MANAGER", "ENGINEER"}
role = "ENGINEER"
if role in allowed_roles:
    print("Access granted")

user = {
    "name": "Dhanush",
    "role": "ENGINEER"
}
if "role" in user:
    print("Role exists")

# Exercise 1
age = 22
if age >= 18:
    print("Adult")
else:
    print("Minor")

# Exercise 2
experience = 2
is_skilled = True
if experience >= 2 and is_skilled:
    print("Eligible")
else:
    print("Not Eligible")

# Exercise 3
score = 82
if score >= 90:
    print("Excellent")
elif score >= 75:
    print("Good")
elif score >= 60:
    print("Average")
else:
    print("Needs improvement")

# Exercise 4
documents = {
    "doc_1": 0.92,
    "doc_2": 0.41,
    "doc_3": 0.87
}
threshold = 0.8
for doc, score in documents.items():
    if score >= threshold:
        print(f"{doc} is relevant")
    else:
        print(f"{doc} is not relevant")