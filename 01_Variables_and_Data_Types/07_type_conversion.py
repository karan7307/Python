"""
Type Conversion in Python
==========================
This program demonstrates how to convert between different data types.
"""

# Checking data types
name = "Alice"
age = 20
height = 5.6
is_student = True

print("=== Checking Data Types ===")
print(f"name = {name}, type = {type(name)}")
print(f"age = {age}, type = {type(age)}")
print(f"height = {height}, type = {type(height)}")
print(f"is_student = {is_student}, type = {type(is_student)}")

# Converting to integer
float_number = 3.14
string_number = "42"

print("\n=== Converting to Integer ===")
print(f"int(3.14) = {int(float_number)}")           # Removes decimal part
print(f"int('42') = {int(string_number)}")          # String to integer
print(f"int(True) = {int(True)}")                   # Boolean to integer
print(f"int(False) = {int(False)}")

# Converting to float
integer_number = 10
string_float = "3.14"

print("\n=== Converting to Float ===")
print(f"float(10) = {float(integer_number)}")
print(f"float('3.14') = {float(string_float)}")
print(f"float(True) = {float(True)}")

# Converting to string
number = 42
pi = 3.14159
flag = True

print("\n=== Converting to String ===")
print(f"str(42) = '{str(number)}'")
print(f"str(3.14159) = '{str(pi)}'")
print(f"str(True) = '{str(flag)}'")

# Converting to boolean
print("\n=== Converting to Boolean ===")
print(f"bool(1) = {bool(1)}")           # Non-zero numbers are True
print(f"bool(0) = {bool(0)}")           # Zero is False
print(f"bool('hello') = {bool('hello')}")  # Non-empty strings are True
print(f"bool('') = {bool('')}")            # Empty string is False
print(f"bool([1,2,3]) = {bool([1,2,3])}")  # Non-empty list is True
print(f"bool([]) = {bool([])}")            # Empty list is False

# Converting between list, tuple, and set
my_list = [1, 2, 3, 4, 5]
my_tuple = (1, 2, 3, 4, 5)
my_set = {1, 2, 3, 4, 5}

print("\n=== Converting Collections ===")
print("Original list:", my_list)
print("List to tuple:", tuple(my_list))
print("List to set:", set(my_list))

print("\nOriginal tuple:", my_tuple)
print("Tuple to list:", list(my_tuple))
print("Tuple to set:", set(my_tuple))

# Practical example: User input (always comes as string)
print("\n=== Practical Example: User Input ===")
print("User input always comes as a string!")
print("If you need a number, you must convert it.")

# Example (without actual input for demo)
user_input_demo = "25"  # Simulating input()
print(f"Input: '{user_input_demo}' (type: {type(user_input_demo)})")
age = int(user_input_demo)
print(f"Converted: {age} (type: {type(age)})")

# Common mistakes and how to avoid them
print("\n=== Common Type Conversion Mistakes ===")

# Mistake 1: Trying to convert invalid strings
try:
    result = int("hello")
except ValueError as e:
    print(f"Error: Can't convert 'hello' to int - {e}")

# Mistake 2: Not considering decimal points
try:
    result = int("3.14")
except ValueError as e:
    print(f"Error: Can't convert '3.14' directly to int - {e}")
    print("Solution: Convert to float first, then to int")
    result = int(float("3.14"))
    print(f"int(float('3.14')) = {result}")

# Safe conversion with error handling
def safe_int_conversion(value):
    """Safely convert a value to integer"""
    try:
        return int(value)
    except ValueError:
        print(f"Cannot convert '{value}' to integer!")
        return None

print("\n=== Safe Conversion Examples ===")
print(f"safe_int_conversion('42') = {safe_int_conversion('42')}")
print(f"safe_int_conversion('hello') = {safe_int_conversion('hello')}")

# ASCII conversions
print("\n=== ASCII Conversions ===")
print(f"ord('A') = {ord('A')}")  # Character to ASCII code
print(f"chr(65) = '{chr(65)}'")  # ASCII code to character
