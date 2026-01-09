"""
Taking Multiple Inputs in Python
=================================
This program demonstrates different ways to take multiple inputs from users.
"""

# Taking multiple inputs one by one
print("=== Multiple Inputs One by One ===")
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
age = int(input("Enter your age: "))

print(f"\nHello, {first_name} {last_name}!")
print(f"You are {age} years old.")

# Taking multiple inputs in one line (space-separated)
print("\n=== Multiple Inputs in One Line ===")
print("Enter three numbers separated by spaces:")
numbers = input().split()  # Returns a list of strings
print("You entered:", numbers)

# Convert to integers
num1, num2, num3 = int(numbers[0]), int(numbers[1]), int(numbers[2])
print(f"Sum: {num1 + num2 + num3}")

# Better way: using map()
print("\n=== Using map() for Conversion ===")
print("Enter three numbers separated by spaces:")
a, b, c = map(int, input().split())
print(f"Numbers: {a}, {b}, {c}")
print(f"Average: {(a + b + c) / 3}")

# Taking multiple floats
print("\n=== Multiple Float Inputs ===")
print("Enter three decimal numbers separated by spaces:")
x, y, z = map(float, input().split())
print(f"Numbers: {x}, {y}, {z}")
print(f"Maximum: {max(x, y, z)}")
print(f"Minimum: {min(x, y, z)}")

# Student information collection
print("\n=== Student Information Form ===")
name = input("Enter student name: ")
roll_number = int(input("Enter roll number: "))
marks1 = float(input("Enter marks in Subject 1: "))
marks2 = float(input("Enter marks in Subject 2: "))
marks3 = float(input("Enter marks in Subject 3: "))

total_marks = marks1 + marks2 + marks3
average = total_marks / 3

print("\n--- Student Report ---")
print(f"Name: {name}")
print(f"Roll Number: {roll_number}")
print(f"Marks: {marks1}, {marks2}, {marks3}")
print(f"Total: {total_marks}")
print(f"Average: {average:.2f}")

# Taking a list of items
print("\n=== Shopping List ===")
print("Enter items separated by commas:")
items = input().split(",")
# Remove extra spaces from each item
items = [item.strip() for item in items]

print("\nYour shopping list:")
for i, item in enumerate(items, 1):
    print(f"{i}. {item}")

# Yes/No input
print("\n=== Yes/No Input ===")
response = input("Do you like Python? (yes/no): ").lower()
if response == "yes" or response == "y":
    print("Great! Keep learning!")
elif response == "no" or response == "n":
    print("Give it more time, you'll love it!")
else:
    print("Please answer yes or no")

# Menu-based input
print("\n=== Menu Selection ===")
print("Choose an operation:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
choice = int(input("Enter your choice (1-4): "))

if 1 <= choice <= 4:
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    
    if choice == 1:
        print(f"Result: {num1 + num2}")
    elif choice == 2:
        print(f"Result: {num1 - num2}")
    elif choice == 3:
        print(f"Result: {num1 * num2}")
    elif choice == 4:
        if num2 != 0:
            print(f"Result: {num1 / num2}")
        else:
            print("Error: Division by zero!")
else:
    print("Invalid choice!")

# Personal information collector
print("\n=== Personal Information ===")
data = {}
data['name'] = input("Full Name: ")
data['email'] = input("Email: ")
data['phone'] = input("Phone Number: ")
data['address'] = input("Address: ")

print("\n--- Information Summary ---")
for key, value in data.items():
    print(f"{key.capitalize()}: {value}")

# Quiz program
print("\n=== Quick Quiz ===")
score = 0

question1 = input("What is the capital of France? ").lower()
if question1 == "paris":
    print("Correct!")
    score += 1
else:
    print("Wrong! The answer is Paris.")

question2 = input("What is 5 + 7? ")
if question2 == "12":
    print("Correct!")
    score += 1
else:
    print("Wrong! The answer is 12.")

print(f"\nYour score: {score}/2")
