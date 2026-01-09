"""
Basic Functions in Python
==========================
This program demonstrates how to create and use functions.
"""

# Simple function without parameters
def greet():
    """Prints a greeting message"""
    print("Hello, World!")

print("=== Simple Function ===")
greet()  # Call the function

# Function called multiple times
print("\n=== Calling Function Multiple Times ===")
def say_hello():
    print("Hello!")

say_hello()
say_hello()
say_hello()

# Function with a parameter
print("\n=== Function with Parameter ===")
def greet_person(name):
    """Greets a person by name"""
    print(f"Hello, {name}!")

greet_person("Alice")
greet_person("Bob")
greet_person("Charlie")

# Function with multiple parameters
print("\n=== Multiple Parameters ===")
def introduce(name, age):
    """Introduces a person with name and age"""
    print(f"My name is {name} and I am {age} years old.")

introduce("Alice", 20)
introduce("Bob", 22)

# Function with calculation
print("\n=== Function with Calculation ===")
def calculate_square(number):
    """Calculates the square of a number"""
    square = number ** 2
    print(f"The square of {number} is {square}")

calculate_square(5)
calculate_square(10)
calculate_square(7)

# Function that prints a pattern
print("\n=== Function for Pattern ===")
def print_stars(count):
    """Prints a line of stars"""
    print("*" * count)

print_stars(5)
print_stars(10)
print_stars(3)

# Function with return value
print("\n=== Function with Return ===")
def add_numbers(a, b):
    """Returns the sum of two numbers"""
    return a + b

result1 = add_numbers(5, 3)
result2 = add_numbers(10, 20)

print(f"5 + 3 = {result1}")
print(f"10 + 20 = {result2}")

# Using return value in expressions
total = add_numbers(15, 25) + add_numbers(10, 5)
print(f"(15 + 25) + (10 + 5) = {total}")

# Function with multiple operations
print("\n=== Calculator Functions ===")
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Cannot divide by zero"

x, y = 10, 5
print(f"{x} + {y} = {add(x, y)}")
print(f"{x} - {y} = {subtract(x, y)}")
print(f"{x} * {y} = {multiply(x, y)}")
print(f"{x} / {y} = {divide(x, y)}")

# Function with conditional logic
print("\n=== Function with Conditions ===")
def check_even_odd(number):
    """Checks if a number is even or odd"""
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"

print(f"7 is {check_even_odd(7)}")
print(f"10 is {check_even_odd(10)}")
print(f"15 is {check_even_odd(15)}")

# Function with loop
print("\n=== Function with Loop ===")
def print_numbers(n):
    """Prints numbers from 1 to n"""
    for i in range(1, n + 1):
        print(i, end=" ")
    print()

print("Numbers 1 to 5:")
print_numbers(5)
print("Numbers 1 to 10:")
print_numbers(10)

# Function returning maximum
print("\n=== Finding Maximum ===")
def find_max(a, b):
    """Returns the larger of two numbers"""
    if a > b:
        return a
    else:
        return b

print(f"Max of 15 and 20: {find_max(15, 20)}")
print(f"Max of 50 and 30: {find_max(50, 30)}")

# Function with list parameter
print("\n=== Function with List ===")
def print_list(items):
    """Prints all items in a list"""
    for item in items:
        print(f"  - {item}")

fruits = ["apple", "banana", "orange"]
print("Fruits:")
print_list(fruits)

numbers = [1, 2, 3, 4, 5]
print("\nNumbers:")
print_list(numbers)

# Function returning sum of list
print("\n=== Sum of List ===")
def calculate_sum(numbers):
    """Returns the sum of numbers in a list"""
    total = 0
    for num in numbers:
        total += num
    return total

my_numbers = [10, 20, 30, 40, 50]
print(f"Numbers: {my_numbers}")
print(f"Sum: {calculate_sum(my_numbers)}")

# Docstrings
print("\n=== Function Docstrings ===")
def example_function(param):
    """
    This is a docstring.
    It explains what the function does.
    
    Parameters:
        param: Description of parameter
    
    Returns:
        Description of return value
    """
    return param * 2

print("Function name:", example_function.__name__)
print("Function docstring:", example_function.__doc__)

# Multiple functions working together
print("\n=== Functions Working Together ===")
def celsius_to_fahrenheit(celsius):
    """Converts Celsius to Fahrenheit"""
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    """Converts Fahrenheit to Celsius"""
    return (fahrenheit - 32) * 5/9

temp_c = 25
temp_f = celsius_to_fahrenheit(temp_c)
print(f"{temp_c}°C = {temp_f}°F")

temp_f = 77
temp_c = fahrenheit_to_celsius(temp_f)
print(f"{temp_f}°F = {temp_c}°C")
