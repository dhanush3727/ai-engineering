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