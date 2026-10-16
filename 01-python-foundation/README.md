# Phase 1: Python for AI Engineering
## Variables & Basic types
### Variables:
In python we create a varibles like this:
```py
name = "Dhanush"
```
Python doesn't require you to declare the type. Python is dynamically typed. But later when we learn python for AI engineering, we'll use type hints like
```py
name: str = "Dhanush"
age: int = 22
```

### Primitive/basic types:
In python the types are `str`, `int`, `float`, `bool`, and `Nonetype`. We can check a value's type using `type()`.
Ex:
```py
print(type(age)) # <class 'int'>
```

### Printing:
In JavaScript we use `console.log()` for printing. But in python we use `print()`. In JavaScript we use `template literals(``)` to combine variables and string. But python we use `f-string`
Ex:
```py
print(f"My name is {name}")
```

### Python Indentation(space):
In JavaScript we use `{}` for block of code, but in the python we use indentation(space) for block of code.
Ex:
```py
if age >= 18:
    print("adult")
```
but,
```py
if age >= 18:
print("adult")
```
This is invalid

## Strings
A string is text
```py
name = "Dhanush"
job = 'Software Developer'
```
Python supports single and double quotes

### String indexing
Python use zero based indexing and can also use negative indexes
```py
print(name[1])
print(name[-1])
```

### String slicing
In python string slicing is `string[start:end:step]`
Ex:
```py
print(name[0:3])
```
Start in included, end is excluded, so `0`,`1`,`2` is included `3` index is excluded.
In the string slicing:
* start: starting point of the string
* end: ending point of the string and excluded
* step: interval between index


### Strings are immutable
We can't modify strings directly that is 
```py
name = "Dhanush"
name[0] = "X"
```
This will fail because strings are immutable, instead of
```py
name = "Dhanush"
name = "X" + name[1:]
print(name) # Xhanush
```

### String methods
* `upper()`: It change the text into upper case. Ex: `text.upper()`, output is `DHANUSH`
* `lower()`: It change the text into lower case. Ex: `text.lower()`, output is `dhanush`
* `strip()`: It removes whitespace from both ends. we can also use `lstrip()` & `rstrip` that is `left side` and `right side`.
* `replace()`: Replace part of strin or character.
* `split()`: It converts a string into a list.
* `join()`: It combines multiple strings into one string.
* `startswith()`: This is return a boolean value that check that text start with.
* `endswith()`: This is return a boolean value that check that text end with.

## Lists
A python list stores multiple values in a single variable like JavaScript array. 
Ex:
```py
languages = ["Python", "JavaScript", "Java"]
```

### Creating a list
A list uses square brackets. Python lists cna contain different types
Ex:
```py
numbers = [10, 50, 30, 60]
names = ["Charu", "Dhanush", "Bhavana"]
mixed = ["Python", 10, True, 2.4]
```

### Indexing
Python lists zero based indexing like strings, negative indexing also works.
```py
languages = ["Python", "JavaScript", "TypeScript"]

print(languages[0]) # Python
print(languages[1]) # JavaScript
print(languages[-1]) # TypeScript
```

### Slicing
In python list we can slice a spcific portion from list. `[start:end]` start is included, end is excluded
Ex:
```py
languages = ["Python", "JavaScript", "TypeScript", "Java"]

print(languages[0:2]) #['Python', 'JavaScript']
print(languages[:2])
print(languages[2:])
print(languages[::-1])
```

### Lists are mutable
In string we can't modify a specific position but in list we can modify the specific position
Ex:
```py
languages = ["Python", "JavaScript", "TypeScript"]
languages[0] = "Java"
print(languages) # ['Java', 'JavaScript', 'TypeScript']
```

### Adding items
#### append() method
In list we use `append()` method for adds an item to the end.
Ex:
```py
languages = ["Python", "JavaScript"]
languages.append("TypeScript")
print(languages) # ['Python', 'JavaScript', 'TypeScript']
```

#### insert() method
Use `insert()` method to add an item at a specific position
```py
languages = ["Python", "TypeScript"]
languages.insert(1, "JavaScript")
print(languages) # ['Python', 'JavaScript', 'TypeScript']
```

### Removing items
#### remove() method
Use `remove()` method to removes a specific value
Ex:
```py
languages = ["Python", "JavaScript", "TypeScript"]
languages.remove("JavaScript")
print(languages) # ['Python', 'TypeScript']
```

#### pop() method
`pop()` removes an item by index and returns the removed value.
Ex:
```py
languages = ["Python", "JavaScript", "TypeScript"]
removed = languages.pop(1)
print(removed) # JavaScript
print(languages) # ['Python', 'TypeScript']
```
Without an index `pop()` removes last item.

### Length of list
Use `len()` to find the length of the list
Ex:
```py
languages = ["Python", "JavaScript", "TypeScript"]
print(len(languages)) # 3
```

### List iteration
To print list element we use for loop
```py
languages = ["Python", "JavaScript", "TypeScript"]
for language in languages:
    print(language)
```

#### range()
We can iterate some specific range using `range()`
```py
for number in range(5):
    print(number)
```
It runs default in `0` so the output is: `0`,`1`,`2`,`3`,`4`.

#### enumerate()
When using `enumerate` we can get the index and element
```py
for index, language in enumerate(languages):
    print(index, language)
```
output is:
```text
0 Python
1 JavaScript
2 TypeScript
```

## Tuples
A python tuples stores multiple values in a single varible it is very similar to lists, but one important difference is the tuples are immutable that we can't modify tuples value like lists but inside a tuple there is any mutable object then we can only modify that object.

### Creating a tuple
```py
coordinates = (10, 20)
print(coordinates) # (10, 20)
print(type(coordinates)) # <class 'tuple'>
```

### Tuple unpacking
The tuple unpacking is we can get the tuple elements one by one like JavaScript destructuring
Ex:
```py
point = (10, 20)

x, y = point

print(x) # 10
print(y) # 20
```

## Sets
A set is a collection of unique values. When you care about whether something exists, but you don't care about duplicates or positions. Sets automatically removes duplicates

### Create a set
```py
languages = {"Python", "JavaScript", "TypeScript"}

print(languages) # {'Python', 'JavaScript', 'TypeScript'}
print(type(languages)) # <class 'set'>
```

### Adding values
```py
languages = {"Python", "JavaScript"}

languages.add("TypeScript")

print(languages) # {'Python', 'JavaScript', 'TypeScript'}
```

### Removing values
```py
languages = {"Python", "JavaScript", "TypeScript"}
languages.remove("JavaScript")
```
But if the value doesn't exist then set return the error so we can use
```py
languages.discard("Rust")
```

### Check elements
```py
languages = {"Python", "JavaScript", "TypeScript"}
print("Python" in languages) # True
print("Rust" in languages) # False
```

### Set Operations
```py
frontend = {"React.js", "Next.js", "JavaScript", "TypeScript"}
backend = {"Node.js", "Express.js", "JavaScript", "TypeScript"}
```
#### Union - everything from both sets
```py
all_technologies = frontend | backend
print(all_technologies) # {'TypeScript', 'Node.js', 'JavaScript', 'Next.js', 'React.js', 'Express.js'}
```
#### Intersection - values common to both
```py
common = frontend & backend
print(common) # {'TypeScript', 'JavaScript'}
```
#### Difference - values in one set but not the other
```py
frontend_only = frontend - backend
print(frontend_only) # {'Next.js', 'React.js'}
```

## Dictonaries
A dictionary stores data as key value pairs like objects in JavaScript. Dictionary can contain different types.

### Creating Dictonaries
```py
user = {
    "name": "Dhanush",
    "age": 22
}
```

### Accessing Values
In the dictionary we can get the value using the key.
```py
print(user["name"])
print(user["age"])
```

### Adding new key and updating a value
```py
user["role"] = "Software Developer"
user["age"] = 23
print(user)
```

### Removing a key
We can use `del` or `.pop()`. `pop()` removes the key and gives you the value that was removed.
```py
del user["role"]
age = user.pop("age")

print(age)
print(user)
```

### Checking whether a key exists
```py
print("name" in user) # TRUE
print("email" in user) # FALSE
```

### `.get()`
If we check using `in` if the key was not there then it print the error. So we can use `.get()`
```py
print(user.get("email")) # None
```

### Getting keys and values
```py
print(user.keys())
print(user.values())
```

### Looping through a dictionary
We can use `.items()` to print the dictionary keys and values.
```py
for key, value in user.items():
    print(f"{key}: {value}")
```

### Dictionary Comprehensions
A dictionary comprehensions is a concise way to create a dictionary from an iterable.
```py
numbers = [1, 2, 3, 4, 5]
squares = {
    num: num * num
    for num in numbers
}
print(squares)

# Using conditions
even_squares = {
    number: number * number
    for number in numbers
    if number % 2 == 0
}

print(even_squares)

# Trnasforming an existing dictionary
uppercase_skills = {
    category: skill.upper()
    for category, skill in skills.items()
}
```

## Conditions
```py
# if condition
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
```
Python false values are:
```text
False
None
0
""
[]
{}
set()
```
other than this all values are true.

## Loops
### for loop
```py
# for loop in range
for i in range(6):
    print(i)

technologies = ["Python", "React", "Node.js"]
for technology in technologies:
    print(technology)
```
`range()`:
- In the for loop we use the `range` for print sequence values.
- The range `range(start, stop)` it is include the start and exclude the stop.
- We can also use `range(start, stop, step)` the step is default set as 1. So it is add `+1`.
- If we set the step as 2 then add the `+2` for every iterate.
- To reverse the sequence the use the step as `-1`.

`enumerate()`:
- It is used to print the index and value. Ex:
```py
# enumerate - print index and value together
equipment = ["motor", "pump", "compressor"]
for index, item in enumerate(equipment):
    print(index, item)

# can also choose the starting index
for number, item in enumerate(equipment, start=1):
    print(number, item)
```

### While loop
```py
attempt = 1
while attempt <= 3:
    print(f"Attempt {attempt}")
    attempt += 1
```

## Functions
```py
# Without parameter
def greet():
    print("Hello Dhanush")
greet()

# With parameter
def greeting(name):
    print(f"Hello, {name}")
greeting("Dhanush")
```
### Default paramter:
A default parameter is a paramter that already has a value if the caller does not provide one. Required parameters should come before default parameters. Ex,
`def search(query, limit=5):` Valid
`def search(limit=5, query):` Invalid
```py
# Default paramter
def search_document(query, limit=5):
    print(f"Searching for {query} with limit {limit}")
search_document("motor")
search_document("motor", 10)
```

### Keyword arguments
In the keyword argument, you explicitly tell python which parameter gets the value.
```py
# Keyword Arguments
def task(title, priority):
    print(title, priority)
task(priority="high", title="Replace")
```
We can also use positional + keyword together like
`task("Replace motor", priority="high")` - This is valid
`task(title="Replace motor", "high")` - This is invalid

### *args
The `*` is important it collect all arguments and make it in tuples
```py
def process(*args):
    print(type(args))
    print(args)
process("Motor", "Pump", "Generator")
```
`*args` with normal parameters:
You can have normal parameters before `*args`.
```py
def process_equipment(category, *equipment):
    print(f"Category: {category}")

    for item in equipment:
        print(f"Processing {item}")
process_equipment(
    "Critical",
    "Motor",
    "Pump",
    "Compressor"
)
```

### **kwargs
This is keyword arguments it becomes the arguments dictionary
```py
def create_equipment(**kwargs):
    print(kwargs)
create_equipment(name="Motor", status="active", location="Plant A")

def show_equipment(**details):
    for key, value in details.items():
        print(f"{key}: {value}")
show_equipment(name="Motor", status="active", location="Plant A")
```

### Lambda functions
A *lambda functions* is a small, anonymous function written in a single expression. The pattern is `lambda parameter: expression`. The expression's result is automatically returned.
Ex:
```py
square = lambda num: num * num
print(square(2))
```

## Comprehension
### List Comprehension
A list comprehension is a compact way to create a new list from an existing iterable.
The pattern is `[expression for item in iterable if condition]`.
```py
numbers = [1,2,3,4,5]
squares = [num * num for num in numbers]
print(squares)

# with condition
even_numbers = [num for num in numbers if num % 2 ==0]
print(even_numbers)
```

### Dictionary Comprehension
A dictionary comprehension creates a new dictionary from an iterable. The pattern is
```
{
    key_expression: value_expression
    for item in iterable
    if condition
}
```
Ex:
```py
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
```

### Set Comprehension
A set comprehension creates a new set from an iterable. The pattern is
```
{
    expression
    for expression in iterable
    if condition
}
```
Ex:
```py
scores = [0.92, 0.41, 0.87, 0.41, 0.95]
unique_score = {
    score
    for score in scores
    if score >= 0.8
}
print(unique_score)
```

## Exceptions
An exception is an event that occurs during program execution to indicate that an operation has failed or encountered an unexpected situation.
```py
equipment = {
    "name": "Motor",
    "hours": 123
}

print("Step 1")
print(equipment["location"])
print("Step 2")
```
In this code the `Step 1` will run but the `Step 2` won't run because of `KeyError`.

### try/except
```py
try:
    print(equipment["status"])
except:
    print("Equipment status is unavailable")
```
We can handle the different type of exception like,
`KeyError`: The key is missing
`ValueError`: Value has the wrong format
`TypeError`: Operation receives an incompatible type
Ex:
```py
equipment_records = [
    {"name": "Motor", "hours": "120"},
    {"name": "Pump", "hours": "unknown"},
    {"name": "Compressor"},
    {"name": "Generator", "hours": None},
    {"name": "Fan", "hours": "85"}
]

def process_equipment(records):
    result = []
    for equipment in records:
        try:
            hours = int(equipment["hours"])
            result.append({
                "name": equipment["name"],
                "hours": hours
            })
        except KeyError:
            print(f"Missing hours field for {equipment['name']}")
        except ValueError:
            print(f"Invalid hours value for {equipment['name']}")
        except TypeError:
            print(f"Invalid data type for {equipment['name']}")

    return result
print(process_equipment(equipment_records))
```

### else
`else` is to run code only when `try` block completes without raising an exception.
```py
user = {
    "name": "Dhanush",
    "age": 22
}
try:
    age = int(user["age"])
except KeyError:
    print("Age field is missing")
except ValueError:
    print("Age value is invalie")
except TypeError:
    print("Age has an invalid type")
else:
    print(f"Successfully print {user['name']}: {age}")
```
In this example if the age is alphabetic then the `else` won't run but if the age is int the `else` will run.

### finally
The `finally` block runs when python leaves the try/except structure, whether an exception occured or not.
Ex:
```py
user = {
    "name": "Dhanush",
    "age": 22
}
try:
    age = int(user["age"])
except ValueError:
    print("Invalid age")
else:
    print(f"Processed {user['name']}: {age}")
finally:
    print("User processing attempt finished")
```
In this example the `finally` will must.

### raise
The `raise` is used to raise an exception, signal that an error has occurred.
Ex:
```py
def validate_hours(hours):
    if hours < 0:
        raise ValueError("Operating hours cannot be negative")
    return hours
try:
    result = validate_hours(-50)
    print(result)
except ValueError as error:
    print(f"Invalid hour {error}")
```
Here,
`except`: catches an exception if its type matches.
`ValueError`: specifies which type of exception to catch.
`as error`: assigns the caught exception object to the variable `error`, so you can inspect or use it.

### re-raise
In python, re-raise a caught exception using a bare `raise` inside an `except` block, preserving the original traceback and context. For example,
```py
def eqiupment_fun():
    try:
        hours = int("unknown")
        print(hours)
    except ValueError as error:
        print(f"Import failed: {error}")
        raise
try:
    eqiupment_fun()
except ValueError as error:
    print(f"Caller received the error: {error}")
```
This means raise the currently handled exception again. Python prints the error message, then re-raises the original exception. If no outer handler catches it, the exception propagates outward and the operation fails.

### Nested try/except
```py
def example():
    try:
        print("Starting import")

        try:
            int("unknown")
        except ValueError:
            print(f"Invalid hours value")

        print("Import function continues")
    except Exception:
        print("Unexpected import failure")
example()
```
The output is
```text
Starting import
Invalid hours value
Import function continues
```
Let's trace why:
- The outer `try` starts the import.
- The inner `try` attempts to convert `"unknown"` to an integer.
- Python raises `ValueError`.
- The inner `except` catches it, so the exception is handled locally.
- Execution continues after the inner `try/except`, still inside the outer `try`.
- The outer `except` doesn't run because no exception escaped the outer `try`.

What happens if the inner handler re-raises the exception?
```py
def example_raise():
    try:
        print("Starting import")

        try:
            int("unknown")
        except ValueError:
            print("Invalid hours value")
            raise
        print("Import function continues")
    except ValueError:
        print("Outer handler: import failed")
example_raise()
```
Why didn't `"Import function continues"` print?
Because the inner `raise` propagated the exception to the outer handler. Python skipped the remaining statements in the outer `try` and transferred control to the matching outer `except`.

### Exception chaining
In python we use `raise ... from ...` for exception chaining.
```py
equipment_records = [
    {"name": "Motor", "hours": "120"},
    {"name": "Pump", "hours": "unknown"},
    {"name": "Fan", "hours": "85"}
]

class EquipmentImportError(Exception):
    pass


def parse_hours(equipment):
    try:
        hours = int(equipment["hours"])
        return {
            "name": equipment["name"],
            "hours": hours
        }
    except ValueError as error:
        raise EquipmentImportError(
            f"Failed to import hours for {equipment['name']}"
        ) from error


valid_equipment = []

for equipment in equipment_records:
    try:
        validated_equipment = parse_hours(equipment)
        valid_equipment.append(validated_equipment)
    except EquipmentImportError as error:
        print(error)

print(valid_equipment)
```

### Best Practice
#### Catch specific exceptions, not everything
```py
try:
    hours = int(equipment['hours'])
except ValueError:
    print("Operating hours must be a valid integer")
except KeyError:
    print("Operating hours are missing")
```