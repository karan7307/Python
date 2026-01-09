"""
Working with Tuples in Python
==============================
This program demonstrates tuple operations.
Tuples are ordered, immutable collections (cannot be changed after creation).
"""

# Creating tuples
coordinates = (10, 20)
rgb_color = (255, 0, 0)
mixed_tuple = (1, "hello", 3.14, True)
single_item = (42,)                 # Note: comma is required for single item
empty_tuple = ()

print("=== Creating Tuples ===")
print("Coordinates:", coordinates)
print("RGB Color:", rgb_color)
print("Mixed tuple:", mixed_tuple)
print("Single item tuple:", single_item)
print("Empty tuple:", empty_tuple)

# Accessing tuple elements
point = (100, 200, 300)
print("\n=== Accessing Elements ===")
print("Point:", point)
print("X coordinate:", point[0])
print("Y coordinate:", point[1])
print("Z coordinate:", point[2])
print("Last element:", point[-1])

# Tuple length
print("\n=== Tuple Length ===")
print("Length of point:", len(point))

# Tuple unpacking
x, y, z = point
print("\n=== Tuple Unpacking ===")
print("x =", x)
print("y =", y)
print("z =", z)

# Why use tuples? They are immutable
print("\n=== Immutability Demo ===")
print("Original coordinates:", coordinates)
# coordinates[0] = 30  # This would cause an error!
print("Tuples cannot be changed after creation")

# Tuple methods (only 2 methods since tuples are immutable)
numbers = (1, 2, 3, 2, 4, 2, 5)
print("\n=== Tuple Methods ===")
print("Numbers:", numbers)
print("Count of 2:", numbers.count(2))
print("Index of 4:", numbers.index(4))

# Tuple operations
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
print("\n=== Tuple Operations ===")
print("Tuple 1:", tuple1)
print("Tuple 2:", tuple2)
print("Concatenation:", tuple1 + tuple2)
print("Repetition:", tuple1 * 3)

# Converting between lists and tuples
my_list = [1, 2, 3, 4, 5]
my_tuple = tuple(my_list)
back_to_list = list(my_tuple)

print("\n=== List and Tuple Conversion ===")
print("Original list:", my_list)
print("Converted to tuple:", my_tuple)
print("Back to list:", back_to_list)

# Practical use case: returning multiple values from a function
def get_student_info():
    """Returns student information as a tuple"""
    name = "Alice"
    age = 20
    grade = "A"
    return (name, age, grade)  # Or just: return name, age, grade

print("\n=== Practical Use Case ===")
student_data = get_student_info()
print("Student data (tuple):", student_data)

# Unpacking the returned tuple
student_name, student_age, student_grade = get_student_info()
print(f"Name: {student_name}, Age: {student_age}, Grade: {student_grade}")

# When to use tuples vs lists?
print("\n=== When to Use Tuples ===")
print("Use tuples when:")
print("  1. Data should not change (coordinates, RGB values)")
print("  2. Returning multiple values from a function")
print("  3. Using as dictionary keys (lists can't be keys)")
print("  4. Slightly faster than lists")
