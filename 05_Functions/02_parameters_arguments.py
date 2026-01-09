"""
Parameters and Arguments in Python
===================================
This program demonstrates different ways to pass arguments to functions.
"""

# Positional arguments - order matters
print("=== Positional Arguments ===")
def introduce(name, age, city):
    print(f"I am {name}, {age} years old, from {city}")

introduce("Alice", 20, "New York")
introduce("Bob", 22, "London")

# Keyword arguments - order doesn't matter
print("\n=== Keyword Arguments ===")
introduce(age=25, name="Charlie", city="Paris")
introduce(city="Tokyo", age=30, name="Diana")

# Mixing positional and keyword arguments
print("\n=== Mixed Arguments ===")
introduce("Eve", age=28, city="Berlin")
# introduce(name="Frank", 35, "Rome")  # Error: positional after keyword

# Default parameters
print("\n=== Default Parameters ===")
def greet(name, message="Hello"):
    print(f"{message}, {name}!")

greet("Alice")                    # Uses default message
greet("Bob", "Hi")               # Custom message
greet("Charlie", message="Hey")  # Keyword argument

# Multiple default parameters
print("\n=== Multiple Defaults ===")
def create_profile(name, age=18, country="USA"):
    print(f"Name: {name}, Age: {age}, Country: {country}")

create_profile("Alice")
create_profile("Bob", 25)
create_profile("Charlie", 30, "Canada")
create_profile("Diana", country="UK")

# Function with calculations
print("\n=== Area Calculations ===")
def calculate_rectangle_area(length, width):
    """Calculate area of rectangle"""
    area = length * width
    return area

def calculate_circle_area(radius, pi=3.14159):
    """Calculate area of circle"""
    area = pi * radius ** 2
    return area

rect_area = calculate_rectangle_area(5, 3)
print(f"Rectangle (5×3) area: {rect_area}")

circle_area = calculate_circle_area(7)
print(f"Circle (radius 7) area: {circle_area:.2f}")

circle_area_precise = calculate_circle_area(7, pi=3.14159265359)
print(f"Circle (precise) area: {circle_area_precise:.2f}")

# Variable number of arguments (*args)
print("\n=== Variable Arguments (*args) ===")
def sum_all(*numbers):
    """Sum any number of arguments"""
    total = 0
    for num in numbers:
        total += num
    return total

print(f"Sum of 1, 2, 3: {sum_all(1, 2, 3)}")
print(f"Sum of 10, 20, 30, 40: {sum_all(10, 20, 30, 40)}")
print(f"Sum of 5: {sum_all(5)}")

# *args with other parameters
print("\n=== *args with Regular Parameters ===")
def make_sentence(prefix, *words):
    """Creates a sentence with a prefix"""
    sentence = prefix + " " + " ".join(words)
    return sentence

print(make_sentence("Hello:", "Python", "is", "awesome"))
print(make_sentence("I", "love", "programming"))

# Keyword arguments (**kwargs)
print("\n=== Keyword Arguments (**kwargs) ===")
def print_info(**info):
    """Print key-value pairs"""
    for key, value in info.items():
        print(f"{key}: {value}")

print("Student Info:")
print_info(name="Alice", age=20, grade="A", city="New York")

print("\nBook Info:")
print_info(title="Python Guide", author="John Doe", year=2024)

# Combining *args and **kwargs
print("\n=== Combining *args and **kwargs ===")
def flexible_function(*args, **kwargs):
    """Accepts any number of positional and keyword arguments"""
    print("Positional arguments:")
    for i, arg in enumerate(args, 1):
        print(f"  {i}. {arg}")
    
    print("Keyword arguments:")
    for key, value in kwargs.items():
        print(f"  {key} = {value}")

flexible_function(1, 2, 3, name="Alice", age=20)

# Practical: Student grade calculator
print("\n=== Student Grade Calculator ===")
def calculate_grade(name, *scores, bonus=0):
    """Calculate average grade with optional bonus"""
    if len(scores) == 0:
        return f"{name}: No scores provided"
    
    average = sum(scores) / len(scores) + bonus
    return f"{name}: Average = {average:.2f}"

print(calculate_grade("Alice", 85, 90, 88))
print(calculate_grade("Bob", 75, 80, 70, bonus=5))
print(calculate_grade("Charlie", 95, 92, 98, 90))

# Function with list as parameter
print("\n=== List as Parameter ===")
def find_max_min(numbers):
    """Find maximum and minimum in a list"""
    if not numbers:
        return None, None
    return max(numbers), min(numbers)

nums = [45, 23, 67, 89, 12, 34]
maximum, minimum = find_max_min(nums)
print(f"Numbers: {nums}")
print(f"Max: {maximum}, Min: {minimum}")

# Mutable default argument (be careful!)
print("\n=== Mutable Default Arguments ===")
def add_item(item, items=None):
    """Correct way to handle mutable defaults"""
    if items is None:
        items = []
    items.append(item)
    return items

list1 = add_item("apple")
list2 = add_item("banana")
print(f"List 1: {list1}")
print(f"List 2: {list2}")

# Type hints (Python 3.5+)
print("\n=== Type Hints (Optional) ===")
def greet_with_types(name: str, age: int) -> str:
    """Function with type hints"""
    return f"Hello {name}, you are {age} years old"

result = greet_with_types("Alice", 20)
print(result)

# Practical: Format name
print("\n=== Name Formatter ===")
def format_name(first, last, middle=""):
    """Format a person's name"""
    if middle:
        return f"{first} {middle} {last}"
    return f"{first} {last}"

print(format_name("John", "Doe"))
print(format_name("John", "Doe", "Paul"))
print(format_name("John", "Doe", middle="Smith"))

# Unpacking arguments
print("\n=== Unpacking Arguments ===")
def display_coordinates(x, y, z):
    print(f"Coordinates: ({x}, {y}, {z})")

coords = [10, 20, 30]
display_coordinates(*coords)  # Unpacking list

point = {"x": 5, "y": 15, "z": 25}
display_coordinates(**point)  # Unpacking dictionary
