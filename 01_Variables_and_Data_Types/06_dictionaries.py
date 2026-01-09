"""
Working with Dictionaries in Python
====================================
This program demonstrates dictionary operations.
Dictionaries store data in key-value pairs.
"""

# Creating dictionaries
student = {
    "name": "Alice",
    "age": 20,
    "grade": "A",
    "subjects": ["Math", "Science", "English"]
}

empty_dict = {}

print("=== Creating Dictionaries ===")
print("Student:", student)
print("Empty dictionary:", empty_dict)

# Accessing values
print("\n=== Accessing Values ===")
print("Student name:", student["name"])
print("Student age:", student["age"])
print("Student subjects:", student["subjects"])

# Using get() method (safer - doesn't error if key doesn't exist)
print("\n=== Using get() Method ===")
print("Grade:", student.get("grade"))
print("City:", student.get("city", "Not specified"))  # Default value

# Adding and modifying entries
student["city"] = "New York"        # Add new key-value pair
student["age"] = 21                 # Modify existing value

print("\n=== After Adding/Modifying ===")
print("Student:", student)

# Removing entries
del student["city"]                 # Remove specific key
print("\n=== After Deleting City ===")
print("Student:", student)

removed_grade = student.pop("grade")  # Remove and return value
print("\n=== After Popping Grade ===")
print("Removed grade:", removed_grade)
print("Student:", student)

# Dictionary methods
person = {
    "name": "Bob",
    "age": 25,
    "job": "Engineer"
}

print("\n=== Dictionary Methods ===")
print("All keys:", person.keys())
print("All values:", person.values())
print("All items:", person.items())

# Looping through dictionary
print("\n=== Looping Through Dictionary ===")
for key in person:
    print(f"{key}: {person[key]}")

print("\nUsing items():")
for key, value in person.items():
    print(f"{key}: {value}")

# Checking if key exists
print("\n=== Checking Keys ===")
print("Is 'name' in dictionary?", "name" in person)
print("Is 'salary' in dictionary?", "salary" in person)

# Nested dictionaries (dictionary inside dictionary)
classroom = {
    "student1": {"name": "Alice", "grade": "A"},
    "student2": {"name": "Bob", "grade": "B"},
    "student3": {"name": "Charlie", "grade": "A"}
}

print("\n=== Nested Dictionary ===")
print("Classroom:", classroom)
print("Student1 name:", classroom["student1"]["name"])
print("Student2 grade:", classroom["student2"]["grade"])

# Dictionary comprehension
squares_dict = {x: x**2 for x in range(1, 6)}
print("\n=== Dictionary Comprehension ===")
print("Squares dictionary:", squares_dict)

# Copying dictionaries
original = {"a": 1, "b": 2}
copied = original.copy()

print("\n=== Copying Dictionary ===")
print("Original:", original)
print("Copied:", copied)

# Merging dictionaries
dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}
merged = {**dict1, **dict2}  # Python 3.5+

print("\n=== Merging Dictionaries ===")
print("Dictionary 1:", dict1)
print("Dictionary 2:", dict2)
print("Merged:", merged)

# Practical example: Phone book
phone_book = {
    "Alice": "555-1234",
    "Bob": "555-5678",
    "Charlie": "555-9012"
}

print("\n=== Phone Book Example ===")
print("Alice's number:", phone_book["Alice"])
print("All contacts:", phone_book)

# Adding a new contact
phone_book["Diana"] = "555-3456"
print("After adding Diana:", phone_book)
