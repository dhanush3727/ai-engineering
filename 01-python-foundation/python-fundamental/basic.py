# Variables
name = "Dhanush"
age = 22
salary = 13500.65
isJobless = False
isMarried = None
print(name, age)
print(f"My name is {name}. I am {age} years old")

# types
print(type(name)) # <class 'str'>
print(type(age)) # <class 'int'>
print(type(salary)) # <class 'float'>
print(type(isJobless)) # <class 'bool'>
print(type(isMarried)) # <class 'NoneType'>

# Python Indentation(space)
if age>= 18:
    print("Adult")
else:
    print("Child")

# Small exercise - print about your self
experience = 2
job = "Software Developer"
is_working = True
print(type(name))
print(type(age))
print(type(experience))
print(type(job))
print(type(is_working))
print(f"My name is {name}. "
      f"I am {age} years old. "
      f"I am a {job} and I have {experience} years of experience."
      )