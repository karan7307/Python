"""
VARIABLES AND DATA TYPES IN PYTHON
===================================

What are Variables?
-------------------
Variables are containers that store data values. 
Think of them as labeled boxes where you can keep different types of information.

Python has several built-in data types:
1. Integer (int) - Whole numbers
2. Float - Decimal numbers
3. String (str) - Text
4. Boolean (bool) - True or False
5. List - Collection of items
6. Dictionary (dict) - Key-value pairs
"""

# ============================================
# NUMBERS (Integers and Floats)
# ============================================

# Integer - whole numbers without decimal points
age = 20
print("Age:", age)
print("Type of age:", type(age))  # type() tells us what kind of data it is

# Float - numbers with decimal points
height = 5.9
print("\nHeight:", height)
print("Type of height:", type(height))

# You can do math with numbers
students = 30
present = 28
absent = students - present
print("\nTotal students:", students)
print("Present:", present)
print("Absent:", absent)


# ============================================
# STRINGS (Text)
# ============================================

# Strings are text enclosed in quotes (single or double)
name = "Alice"
greeting = 'Hello'
print("\n" + greeting + ", " + name + "!")

# You can combine (concatenate) strings with +
first_name = "John"
last_name = "Doe"
full_name = first_name + " " + last_name
print("Full name:", full_name)

# String length
message = "Python is fun!"
print("Message:", message)
print("Length of message:", len(message))


# ============================================
# BOOLEANS (True or False)
# ============================================

# Booleans represent truth values
is_student = True
has_graduated = False

print("\nIs student?", is_student)
print("Has graduated?", has_graduated)

# Booleans are often used in conditions
is_learning_python = True
if is_learning_python:
    print("Keep practicing!")


# ============================================
# LISTS (Collections)
# ============================================

# Lists store multiple items in a single variable
fruits = ["apple", "banana", "orange", "mango"]
print("\nFruits list:", fruits)
print("First fruit:", fruits[0])  # Lists start counting from 0
print("Second fruit:", fruits[1])
print("Number of fruits:", len(fruits))

# Lists with numbers
scores = [85, 90, 78, 92, 88]
print("\nScores:", scores)
print("Highest score:", max(scores))
print("Lowest score:", min(scores))


# ============================================
# DICTIONARIES (Key-Value Pairs)
# ============================================

# Dictionaries store data in key-value pairs
student_info = {
    "name": "Emma",
    "age": 21,
    "grade": "A",
    "is_active": True
}

print("\nStudent Information:")
print("Name:", student_info["name"])
print("Age:", student_info["age"])
print("Grade:", student_info["grade"])


# ============================================
# TYPE CONVERSION
# ============================================

# You can convert between different data types
number_as_string = "100"
actual_number = int(number_as_string)  # Convert string to integer
print("\nString '100' converted to integer:", actual_number)
print("Now we can do math: 100 + 50 =", actual_number + 50)

# Convert integer to string
score = 95
score_text = str(score)
message = "Your score is " + score_text
print(message)


# ============================================
# PRACTICE PROBLEMS
# ============================================

print("\n" + "="*50)
print("PRACTICE PROBLEMS")
print("="*50)

"""
Try these exercises:

1. Create a variable called 'city' and assign your city name to it.
   Then print it.

2. Create two number variables and store your age and a friend's age.
   Calculate and print the age difference.

3. Create a list of 5 favorite movies and print the list.
   Then print only the first and last movie.

4. Create a dictionary to store information about your favorite book:
   title, author, year, and pages.
   Print each piece of information.

5. Create a string variable with a number like "25", convert it to 
   an integer, multiply by 2, and print the result.
"""

print("\nTry solving the practice problems above!")
print("Write your solutions in a new file or below this code.")
