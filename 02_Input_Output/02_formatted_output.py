"""
Formatted Output in Python
===========================
This program demonstrates different ways to format output for better presentation.
"""

# Basic string formatting
name = "Alice"
age = 20
grade = 85.5

print("=== Old Style Formatting (%) ===")
print("Name: %s, Age: %d, Grade: %.2f" % (name, age, grade))

print("\n=== Format Method ===")
print("Name: {}, Age: {}, Grade: {}".format(name, age, grade))
print("Name: {0}, Age: {1}, Grade: {2}".format(name, age, grade))
print("Grade: {2}, Name: {0}, Age: {1}".format(name, age, grade))

# F-strings (Python 3.6+) - Most recommended!
print("\n=== F-Strings (Recommended) ===")
print(f"Name: {name}, Age: {age}, Grade: {grade}")

# Formatting numbers
pi = 3.14159265359
large_number = 1234567890

print("\n=== Number Formatting ===")
print(f"Pi with 2 decimals: {pi:.2f}")
print(f"Pi with 4 decimals: {pi:.4f}")
print(f"Large number with commas: {large_number:,}")
print(f"Percentage: {0.856:.2%}")

# Alignment and padding
print("\n=== Text Alignment ===")
print(f"{'Left':<10}|")      # Left aligned (10 characters)
print(f"{'Right':>10}|")     # Right aligned
print(f"{'Center':^10}|")    # Center aligned

# Creating tables
print("\n=== Creating a Simple Table ===")
print(f"{'Name':<15} {'Age':>5} {'Grade':>8}")
print("-" * 30)
print(f"{'Alice':<15} {20:>5} {85.5:>8.2f}")
print(f"{'Bob':<15} {22:>5} {90.0:>8.2f}")
print(f"{'Charlie':<15} {19:>5} {78.3:>8.2f}")

# Expressions in f-strings
a = 10
b = 20

print("\n=== Expressions in F-Strings ===")
print(f"a = {a}, b = {b}")
print(f"Sum: {a + b}")
print(f"Product: {a * b}")
print(f"Average: {(a + b) / 2}")

# Multi-line formatted output
print("\n=== Receipt Example ===")
item1 = "Notebook"
price1 = 12.50
quantity1 = 3

item2 = "Pen"
price2 = 2.25
quantity2 = 5

print("=" * 40)
print(" " * 12 + "RECEIPT")
print("=" * 40)
print(f"{'Item':<20} {'Qty':>5} {'Price':>10}")
print("-" * 40)
print(f"{item1:<20} {quantity1:>5} ${price1 * quantity1:>9.2f}")
print(f"{item2:<20} {quantity2:>5} ${price2 * quantity2:>9.2f}")
print("-" * 40)
total = (price1 * quantity1) + (price2 * quantity2)
print(f"{'TOTAL:':<20} {' ':>5} ${total:>9.2f}")
print("=" * 40)

# Conditional formatting
score = 85
status = "Pass" if score >= 50 else "Fail"

print("\n=== Conditional Formatting ===")
print(f"Score: {score}, Status: {status}")
print(f"Grade: {'A' if score >= 90 else 'B' if score >= 80 else 'C'}")

# Pretty printing lists and dictionaries
student = {"name": "Alice", "age": 20, "grade": "A"}
subjects = ["Math", "Science", "English"]

print("\n=== Formatting Collections ===")
print(f"Student info: {student}")
print(f"Subjects: {subjects}")
print(f"Subjects as string: {', '.join(subjects)}")

# Progress bar example (visual formatting)
print("\n=== Progress Bar Example ===")
progress = 75
bar_length = 20
filled = int(bar_length * progress / 100)
bar = "█" * filled + "-" * (bar_length - filled)
print(f"Progress: [{bar}] {progress}%")
