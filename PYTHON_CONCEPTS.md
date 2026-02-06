# Python Concepts Reference Guide 📚

Quick reference for important Python concepts with examples.

---

## 🔷 Data Types

### Numeric Types
```python
# Integers
age = 25
count = -10

# Floats
price = 19.99
pi = 3.14159

# Complex
complex_num = 3 + 4j
```

### Strings
```python
# String creation
name = "Python"
message = 'Hello'
multiline = """This is
a multiline
string"""

# String methods
text = "HELLO"
text.lower()      # "hello"
text.replace('L', 'X')  # "HEXXO"
```

### Collections
```python
# Lists (mutable, ordered)
fruits = ["apple", "banana", "cherry"]
fruits.append("date")
fruits[0]  # "apple"

# Tuples (immutable, ordered)
coordinates = (10, 20)
x, y = coordinates

# Dictionaries (key-value pairs)
person = {"name": "John", "age": 30}
person["name"]  # "John"

# Sets (unique, unordered)
colors = {"red", "blue", "green"}
colors.add("yellow")
```

---

## 🔷 Control Structures

### Conditionals
```python
# If-else
if age >= 18:
    print("Adult")
elif age >= 13:
    print("Teenager")
else:
    print("Child")

# Ternary operator
status = "Adult" if age >= 18 else "Minor"
```

### Loops
```python
# For loop
for i in range(5):
    print(i)

for fruit in fruits:
    print(fruit)

# While loop
count = 0
while count < 5:
    print(count)
    count += 1

# Loop control
for i in range(10):
    if i == 5:
        break      # Exit loop
    if i == 2:
        continue   # Skip iteration
```

### Comprehensions
```python
# List comprehension
squares = [x**2 for x in range(5)]  # [0, 1, 4, 9, 16]

# Dictionary comprehension
person_dict = {i: f"person{i}" for i in range(3)}

# Set comprehension
unique_squares = {x**2 for x in [1, 1, 2, 2, 3]}

# With condition
evens = [x for x in range(10) if x % 2 == 0]
```

---

## 🔷 Functions

### Basic Functions
```python
def greet(name):
    """This function greets someone."""
    return f"Hello, {name}!"

greet("Alice")
```

### Function Arguments
```python
# Positional arguments
def add(a, b):
    return a + b

add(5, 3)

# Default arguments
def power(base, exponent=2):
    return base ** exponent

power(3)      # 9
power(3, 3)   # 27

# *args (variable positional)
def sum_all(*args):
    return sum(args)

sum_all(1, 2, 3, 4)

# **kwargs (variable keyword)
def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_info(name="John", age=30)
```

### Lambda Functions
```python
square = lambda x: x ** 2
square(5)  # 25

# With map, filter
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x**2, numbers))
evens = list(filter(lambda x: x % 2 == 0, numbers))
```

---

## 🔷 Object-Oriented Programming

### Classes and Objects
```python
class Dog:
    # Class variable
    species = "Canis familiaris"
    
    # Constructor
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    # Instance method
    def bark(self):
        return f"{self.name} says Woof!"
    
    # String representation
    def __str__(self):
        return f"Dog({self.name}, {self.age})"

# Creating object
my_dog = Dog("Buddy", 3)
print(my_dog.bark())
```

### Inheritance
```python
class Animal:
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        return f"{self.name} makes a sound"

class Dog(Animal):
    def speak(self):
        return f"{self.name} barks"

dog = Dog("Max")
print(dog.speak())  # "Max barks"
```

### Polymorphism
```python
class Cat(Animal):
    def speak(self):
        return f"{self.name} meows"

animals = [Dog("Rex"), Cat("Whiskers")]
for animal in animals:
    print(animal.speak())  # Different sounds
```

---

## 🔷 Error Handling

### Try-Except
```python
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero!")
except Exception as e:
    print(f"Error: {e}")
finally:
    print("This always runs")
```

### Raising Exceptions
```python
def validate_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative")
    return age

try:
    validate_age(-5)
except ValueError as e:
    print(f"Invalid input: {e}")
```

---

## 🔷 File Handling

### Reading and Writing
```python
# Writing to file
with open("data.txt", "w") as file:
    file.write("Hello, World!")

# Reading from file
with open("data.txt", "r") as file:
    content = file.read()
    print(content)

# Reading line by line
with open("data.txt", "r") as file:
    for line in file:
        print(line.strip())
```

### Working with JSON
```python
import json

# Writing JSON
data = {"name": "John", "age": 30}
with open("data.json", "w") as file:
    json.dump(data, file)

# Reading JSON
with open("data.json", "r") as file:
    data = json.load(file)
```

---

## 🔷 Modules and Imports

### Importing
```python
# Import entire module
import math
print(math.pi)

# Import specific function
from math import sqrt
print(sqrt(16))

# Import with alias
import pandas as pd
from numpy import array as arr

# Import all (avoid in production)
from math import *
```

### Creating Modules
```python
# mymodule.py
def greet(name):
    return f"Hello, {name}!"

# main.py
from mymodule import greet
print(greet("Alice"))
```

---

## 🔷 Useful Built-in Functions

| Function | Description | Example |
|----------|-------------|---------|
| `len()` | Length of object | `len([1,2,3])` → 3 |
| `max()` | Maximum value | `max([1,5,3])` → 5 |
| `min()` | Minimum value | `min([1,5,3])` → 1 |
| `sum()` | Sum of items | `sum([1,2,3])` → 6 |
| `sorted()` | Sorted list | `sorted([3,1,2])` → [1,2,3] |
| `enumerate()` | Index and value | `for i, v in enumerate([a,b])` |
| `zip()` | Combine lists | `zip([1,2], [a,b])` → [(1,a), (2,b)] |
| `range()` | Sequence of numbers | `range(5)` → [0,1,2,3,4] |
| `type()` | Type of object | `type(5)` → <class 'int'> |
| `isinstance()` | Check type | `isinstance(5, int)` → True |

---

## 🔷 String Methods Cheat Sheet

```python
text = "Hello World"

text.lower()           # "hello world"
text.upper()           # "HELLO WORLD"
text.capitalize()      # "Hello world"
text.replace("World", "Python")  # "Hello Python"
text.split()           # ["Hello", "World"]
" ".join(["A", "B"])   # "A B"
text.startswith("H")   # True
text.endswith("d")     # True
text.find("World")     # 6
text.count("l")        # 3
text.strip()           # Remove whitespace
```

---

## 🔷 List Methods Cheat Sheet

```python
lst = [1, 2, 3]

lst.append(4)          # [1, 2, 3, 4]
lst.extend([5, 6])     # [1, 2, 3, 4, 5, 6]
lst.insert(0, 0)       # [0, 1, 2, 3, 4, 5, 6]
lst.remove(3)          # Remove element
lst.pop()              # Remove and return last
lst.pop(0)             # Remove and return first
lst.index(2)           # 2 (index of element)
lst.count(1)           # 1 (count of element)
lst.sort()             # Sort in place
sorted(lst)            # Return sorted copy
lst.reverse()          # Reverse in place
lst.copy()             # Shallow copy
lst.clear()            # Remove all elements
```

---

## 🔷 Common Patterns

### List Flattening
```python
nested = [[1, 2], [3, 4], [5, 6]]
flat = [item for sublist in nested for item in sublist]
```

### Dictionary Merging
```python
dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}
merged = {**dict1, **dict2}
```

### Swapping Variables
```python
a, b = 5, 10
a, b = b, a  # a=10, b=5
```

### Multiple Assignment
```python
x, y, z = [1, 2, 3]
a, *rest, z = [1, 2, 3, 4, 5]  # a=1, rest=[2,3,4], z=5
```

---

## 🔷 Decorators (Advanced)

```python
def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("Before function call")
        result = func(*args, **kwargs)
        print("After function call")
        return result
    return wrapper

@my_decorator
def say_hello(name):
    print(f"Hello, {name}!")

say_hello("Alice")
```

---

## 📝 Notes

- **Mutable vs Immutable**: Lists, dicts, sets are mutable. Strings, tuples, ints are immutable.
- **Pass by Reference**: Objects are passed by reference in Python.
- **Indentation Matters**: Python uses indentation for code blocks.
- **Naming Conventions**: Use snake_case for variables and functions, PascalCase for classes.

---

**Quick Learning Tip:** The best way to learn Python is by doing. Write code every day! 🚀

*Reference Created: February 2026*
