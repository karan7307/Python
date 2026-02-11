"""
Basic for Loop in Python
=========================
This program demonstrates how to use for loops to repeat code.
"""

# Simple for loop
print("=== Simple for Loop ===")
for i in range(5):
    print(f"Iteration {i}")

# Looping through a list
print("\n=== Looping Through a List ===")
fruits = ["apple", "banana", "orange", "grape"]
for fruit in fruits:
    print(f"I like {fruit}")

# Looping through a string
print("\n=== Looping Through a String ===")
word = "Python"
for char in word:
    print(char)

# Counting from 1 to 10
print("\n=== Counting 1 to 10 ===")
for number in range(1, 11):
    print(number, end=" ")
print()  # New line

# Printing even numbers
print("\n=== Even Numbers (0-20) ===")
for num in range(0, 21, 2):
    print(num, end=" ")
print()

# Using loop with index
print("\n=== List with Index ===")
colors = ["red", "green", "blue", "yellow"]
for i in range(len(colors)):
    print(f"Index {i}: {colors[i]}")

# enumerate() - Better way to get index and value
print("\n=== Using enumerate() ===")
subjects = ["Math", "Science", "English"]
for index, subject in enumerate(subjects):
    print(f"{index + 1}. {subject}")

# Starting enumerate from 1
print("\n=== enumerate() Starting from 1 ===")
for index, subject in enumerate(subjects, start=1):
    print(f"{index}. {subject}")

# Looping through a tuple
print("\n=== Looping Through a Tuple ===")
coordinates = (10, 20, 30, 40)
for coord in coordinates:
    print(f"Coordinate: {coord}")

# Calculating sum using loop
print("\n=== Sum of Numbers ===")
numbers = [10, 20, 30, 40, 50]
total = 0
for num in numbers:
    total += num
print(f"Numbers: {numbers}")
print(f"Sum: {total}")

# Multiplication table
print("\n=== Multiplication Table of 5 ===")
for i in range(1, 11):
    print(f"5 × {i} = {5 * i}")

# Countdown
print("\n=== Countdown ===")
for i in range(5, 0, -1):
    print(i)
print("Blast off! 🚀")

# Pattern printing
print("\n=== Star Pattern ===")
for i in range(1, 6):
    print("* " * i)

# Shopping list with formatting
print("\n=== Shopping List ===")
shopping_items = ["milk", "bread", "eggs", "butter", "cheese"]
print("My Shopping List:")
print("-" * 30)
for item_num, item in enumerate(shopping_items, start=1):
    print(f"{item_num}. {item.capitalize()}")

# Looping through dictionary keys
print("\n=== Dictionary Keys ===")
student = {"name": "Alice", "age": 20, "grade": "A"}
for key in student:
    print(f"{key}: {student[key]}")

# Better way - using items()
print("\n=== Dictionary Items ===")
for key, value in student.items():
    print(f"{key}: {value}")

# Squaring numbers
print("\n=== Square Numbers ===")
for num in range(1, 6):
    square = num ** 2
    print(f"{num}² = {square}")

# Finding maximum in a list
print("\n=== Finding Maximum ===")
numbers = [45, 23, 78, 12, 67, 34]
max_num = numbers[0]
for num in numbers:
    if num > max_num:
        max_num = num
print(f"Numbers: {numbers}")
print(f"Maximum: {max_num}")

# Greeting multiple people
print("\n=== Greeting Multiple People ===")
names = ["Alice", "Bob", "Charlie", "Diana"]
for name in names:
    print(f"Hello, {name}! Welcome to Python.")
