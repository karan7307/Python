"""
Basic Variables in Python
==========================
This program demonstrates how to create and use variables in Python.
Variables are containers for storing data values.
"""

# Creating variables with different data types
name = "Alice"              # String variable
age = 20                    # Integer variable
height = 5.6               # Float variable
is_student = True          # Boolean variable

# Printing variables
print("=== Student Information ===")
print("Name:", name)
print("Age:", age)
print("Height:", height, "feet")
print("Is Student:", is_student)

# You can change variable values
print("\n=== After one year ===")
age = age + 1              # Increasing age by 1
print("Age:", age)

# Multiple variables in one line
x, y, z = 10, 20, 30
print("\n=== Multiple Variables ===")
print("x =", x)
print("y =", y)
print("z =", z)

# Same value to multiple variables
a = b = c = 100
print("\n=== Same Value to Multiple Variables ===")
print("a =", a)
print("b =", b)
print("c =", c)

# Variable naming rules demonstration
student_name = "Bob"       # Good: descriptive and uses snake_case
_private_var = 42          # Good: starts with underscore (convention for private)
# 2nd_student = "Charlie"  # Bad: cannot start with number (commented out)

print("\n=== Variable Naming ===")
print("Student Name:", student_name)
print("Private Variable:", _private_var)
