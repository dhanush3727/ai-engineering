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
