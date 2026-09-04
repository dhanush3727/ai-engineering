# Lists
numbers = [10, 50, 30, 60]
names = ["Charu", "Dhanush", "Bhavana"]
mixed = ["Python", 10, True, 2.4]
print(numbers, names, mixed)

# Index
languages = ["Python", "JavaScript", "TypeScript"]
print(languages[0])
print(languages[-1])

# Slicing
programming_languages = ["Python", "JavaScript", "TypeScript", "Java"]
print(programming_languages[0:2])
print(programming_languages[:2])
print(programming_languages[2:])
print(programming_languages[::-1])

programming_languages[-1] = "C++"
print(programming_languages)

# Adding items
programming_languages.append("C#")
print(programming_languages)
programming_languages.insert(1, "Java")
print(programming_languages)

# Remove items
programming_languages.remove("Java")
print(programming_languages)
programming_languages.pop(3) # it removes 3rd index element
print(programming_languages)
programming_languages.pop() # It removes last element
print(programming_languages)

# Length
print(len(programming_languages))

# Other small concept
user_names = ["Rukku", "Dhanush", "Sadie"]
new_users = user_names
new_users.append("kayadu")
new_users.remove("Rukku")
print(user_names)
# both the user_names and new_users refer the same list

# Exercise 1
languages = ["Python", "JavaScript", "TypeScript"]
print(f"First element: {languages[0]}")
print(f"Last element: {languages[-1]}")
print(f"First two languages: {languages[0:2]}")
languages[1] = "Java"
print(languages)
languages.append("Go")
languages.insert(1, "Rust")
languages.remove("TypeScript")
last_element = languages.pop()
print(languages)
print(last_element)
print(len(languages))
print(f"Type: {type(languages)}")

# Exercise 2
languages = ["Python", "JavaScript", "TypeScript"]
other_languages = languages
other_languages.append("Rust")
print(languages)
print(other_languages)

# List iteration
languages = ["Python", "JavaScript", "TypeScript"]
for language in languages:
    print(language)

for language in languages:
    print(language.upper())

for item in languages:
    if item == "Python":
        print("This is python")


# range(): It runs a specific range
for number in range(5):
    print(number)

for number in range(1,6):
    print(number)

for number in range(0,10,3):
    print(number)

# enumerate(): Getting index. If we want index and value then
for index, language in enumerate(languages):
    print(index, language)

# Exercise 3
languages = ["Python", "JavaScript", "TypeScript", "Go", "Rust"]
# Print every language
for language in languages:
    print(language)

for language in languages:
    print(f"I am learning {language}")

for language in languages:
    if len(language) > 6:
        print(language)

for index,item in enumerate(languages):
    print(f"{index}: {item}")

documents = ["Python is a programming language","Machine learning uses data","Large language models process text","RAG combines retrieval with generation"]
for index,item in enumerate(documents):
    print(f"Document{index + 1}: {item}")

# While loop exercise
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
count = 1
while count <= 10:
    print(count)
    count += 1

for num in numbers:
    if num == 6:
        break
    print(num)

for num in numbers:
    if num % 2 != 0:
        print(num)