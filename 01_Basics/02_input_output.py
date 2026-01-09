"""
INPUT AND OUTPUT IN PYTHON
==========================

Input: Getting data FROM the user
Output: Showing data TO the user
"""

# ============================================
# OUTPUT - Printing to the screen
# ============================================

print("Hello, World!")  # Basic print statement
print()  # Empty line for spacing

# Printing multiple items
print("Python", "is", "awesome!")

# Printing with variables
name = "Sarah"
print("Welcome,", name)

# Using f-strings (formatted strings) - Easy and modern way
age = 19
print(f"Hello! My name is {name} and I am {age} years old.")

# Printing with .format() method
city = "New York"
print("I live in {}.".format(city))

# Printing numbers and calculations
x = 10
y = 20
print(f"{x} + {y} = {x + y}")


# ============================================
# INPUT - Getting data from the user
# ============================================

# Basic input - input() always returns a string
print("\n" + "="*50)
print("Let's get some information from you!")
print("="*50 + "\n")

# Getting user's name
user_name = input("What is your name? ")
print(f"Nice to meet you, {user_name}!")

# Getting user's age (need to convert to integer)
user_age = input("How old are you? ")
print(f"You are {user_age} years old.")

# Converting input to integer for calculations
user_age_number = int(user_age)
years_to_30 = 30 - user_age_number
if years_to_30 > 0:
    print(f"You will be 30 years old in {years_to_30} years!")
elif years_to_30 == 0:
    print("You are exactly 30 years old!")
else:
    print(f"You turned 30 about {abs(years_to_30)} years ago!")


# ============================================
# SIMPLE INPUT/OUTPUT PROGRAMS
# ============================================

print("\n" + "="*50)
print("PROGRAM 1: GREETING PROGRAM")
print("="*50 + "\n")

# Get user information
first_name = input("Enter your first name: ")
favorite_color = input("What's your favorite color? ")
favorite_number = input("What's your favorite number? ")

# Display personalized message
print(f"\nHello {first_name}!")
print(f"Your favorite color is {favorite_color}.")
print(f"Your favorite number is {favorite_number}.")
print("Thank you for sharing!")


print("\n" + "="*50)
print("PROGRAM 2: SIMPLE CALCULATOR")
print("="*50 + "\n")

# Get two numbers from user
num1 = input("Enter first number: ")
num2 = input("Enter second number: ")

# Convert strings to numbers
number1 = float(num1)  # Using float to handle decimals
number2 = float(num2)

# Perform calculations
addition = number1 + number2
subtraction = number1 - number2
multiplication = number1 * number2
division = number1 / number2

# Display results
print(f"\n{number1} + {number2} = {addition}")
print(f"{number1} - {number2} = {subtraction}")
print(f"{number1} × {number2} = {multiplication}")
print(f"{number1} ÷ {number2} = {division}")


print("\n" + "="*50)
print("PROGRAM 3: AREA CALCULATOR")
print("="*50 + "\n")

# Calculate area of a rectangle
length = float(input("Enter length of rectangle: "))
width = float(input("Enter width of rectangle: "))

area = length * width
perimeter = 2 * (length + width)

print(f"\nArea of rectangle: {area}")
print(f"Perimeter of rectangle: {perimeter}")


# ============================================
# FORMATTED OUTPUT - Making output look nice
# ============================================

print("\n" + "="*50)
print("FORMATTED OUTPUT EXAMPLES")
print("="*50 + "\n")

# Aligning text
print(f"{'Item':<15} {'Price':>10}")  # <15 means left-align in 15 spaces
print(f"{'Apple':<15} {'$2.50':>10}")
print(f"{'Banana':<15} {'$1.25':>10}")
print(f"{'Orange':<15} {'$3.00':>10}")

# Formatting decimal numbers
pi = 3.14159265359
print(f"\nValue of Pi: {pi}")
print(f"Pi rounded to 2 decimals: {pi:.2f}")  # .2f means 2 decimal places

price = 19.5
print(f"Price: ${price:.2f}")  # Ensures two decimal places


# ============================================
# PRACTICE PROBLEMS
# ============================================

print("\n" + "="*50)
print("PRACTICE PROBLEMS")
print("="*50)

"""
Try these exercises:

1. Write a program that asks for your name and your friend's name,
   then prints "Hello [your name] and [friend's name]!"

2. Create a program that asks for two numbers and displays their sum,
   difference, product, and quotient.

3. Write a program that asks for your birth year and calculates your age
   (assuming current year is 2024).

4. Create a program that asks for temperature in Celsius and converts
   it to Fahrenheit using the formula: F = (C × 9/5) + 32

5. Write a program that asks for your name, favorite hobby, and how many
   hours you spend on it per week. Then print a nice summary message.

6. Create a simple shopping program that asks for item name, quantity,
   and price per item, then calculates and displays the total cost.
"""

print("\nTry solving the practice problems above!")
print("Create a new Python file and write your solutions there.")
