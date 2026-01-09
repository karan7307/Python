"""
FUNCTIONS IN PYTHON
===================

Functions are reusable blocks of code that perform specific tasks.
They help organize code, avoid repetition, and make programs easier to read.

Basic Structure:
    def function_name(parameters):
        # code to execute
        return result  # optional
"""

# ============================================
# SIMPLE FUNCTIONS
# ============================================

print("=" * 50)
print("SIMPLE FUNCTIONS")
print("=" * 50 + "\n")

# Function without parameters
def greet():
    """Prints a greeting message"""
    print("Hello! Welcome to Python!")

# Call the function
greet()

print()

# Function with a simple task
def print_line():
    """Prints a decorative line"""
    print("-" * 40)

print_line()
print("This is between lines")
print_line()


# ============================================
# FUNCTIONS WITH PARAMETERS
# ============================================

print("\n" + "=" * 50)
print("FUNCTIONS WITH PARAMETERS")
print("=" * 50 + "\n")

# Function with one parameter
def greet_person(name):
    """Greets a person by name"""
    print(f"Hello, {name}! Welcome!")

greet_person("Alice")
greet_person("Bob")

print()

# Function with multiple parameters
def introduce(name, age, city):
    """Introduces a person with details"""
    print(f"My name is {name}.")
    print(f"I am {age} years old.")
    print(f"I live in {city}.")

print("Introduction 1:")
introduce("Sarah", 22, "New York")

print("\nIntroduction 2:")
introduce("John", 25, "London")


# ============================================
# FUNCTIONS WITH RETURN VALUES
# ============================================

print("\n" + "=" * 50)
print("FUNCTIONS WITH RETURN VALUES")
print("=" * 50 + "\n")

# Function that returns a value
def add_numbers(a, b):
    """Adds two numbers and returns the result"""
    result = a + b
    return result

# Use the returned value
sum1 = add_numbers(5, 3)
sum2 = add_numbers(10, 20)

print(f"5 + 3 = {sum1}")
print(f"10 + 20 = {sum2}")

print()

# Function with calculation
def calculate_area(length, width):
    """Calculates area of a rectangle"""
    area = length * width
    return area

rectangle_area = calculate_area(10, 5)
print(f"Area of rectangle (10 × 5): {rectangle_area}")


# ============================================
# FUNCTIONS WITH DEFAULT PARAMETERS
# ============================================

print("\n" + "=" * 50)
print("FUNCTIONS WITH DEFAULT PARAMETERS")
print("=" * 50 + "\n")

def greet_with_message(name, message="Good morning"):
    """Greets with a custom or default message"""
    print(f"{message}, {name}!")

# Using default parameter
greet_with_message("Alice")

# Overriding default parameter
greet_with_message("Bob", "Good evening")

print()

def calculate_power(base, exponent=2):
    """Calculates power with default exponent 2 (square)"""
    return base ** exponent

print(f"5 squared: {calculate_power(5)}")
print(f"2 to the power 3: {calculate_power(2, 3)}")


# ============================================
# FUNCTIONS WITH MULTIPLE RETURN VALUES
# ============================================

print("\n" + "=" * 50)
print("FUNCTIONS WITH MULTIPLE RETURN VALUES")
print("=" * 50 + "\n")

def calculate_rectangle(length, width):
    """Calculates both area and perimeter"""
    area = length * width
    perimeter = 2 * (length + width)
    return area, perimeter

# Unpack multiple return values
rect_area, rect_perimeter = calculate_rectangle(10, 5)
print(f"Rectangle (10 × 5):")
print(f"Area: {rect_area}")
print(f"Perimeter: {rect_perimeter}")

print()

def get_student_info():
    """Returns student information"""
    name = "Emma"
    grade = "A"
    score = 92
    return name, grade, score

student_name, student_grade, student_score = get_student_info()
print(f"Student: {student_name}")
print(f"Grade: {student_grade}")
print(f"Score: {student_score}")


# ============================================
# PRACTICAL FUNCTION EXAMPLES
# ============================================

print("\n" + "=" * 50)
print("PRACTICAL FUNCTION EXAMPLES")
print("=" * 50 + "\n")

# Example 1: Check if number is even
def is_even(number):
    """Returns True if number is even, False otherwise"""
    return number % 2 == 0

print("Is 10 even?", is_even(10))
print("Is 7 even?", is_even(7))

print()

# Example 2: Find maximum of three numbers
def find_max(a, b, c):
    """Returns the maximum of three numbers"""
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c

print(f"Maximum of 5, 12, 8: {find_max(5, 12, 8)}")
print(f"Maximum of 20, 15, 25: {find_max(20, 15, 25)}")

print()

# Example 3: Calculate discount
def calculate_discount(price, discount_percent):
    """Calculates final price after discount"""
    discount_amount = price * (discount_percent / 100)
    final_price = price - discount_amount
    return final_price

original_price = 100
discount = 20
final = calculate_discount(original_price, discount)
print(f"Original price: ${original_price}")
print(f"Discount: {discount}%")
print(f"Final price: ${final}")


# ============================================
# PROGRAM 1: TEMPERATURE CONVERTER
# ============================================

print("\n" + "=" * 50)
print("PROGRAM 1: TEMPERATURE CONVERTER")
print("=" * 50 + "\n")

def celsius_to_fahrenheit(celsius):
    """Converts Celsius to Fahrenheit"""
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

def fahrenheit_to_celsius(fahrenheit):
    """Converts Fahrenheit to Celsius"""
    celsius = (fahrenheit - 32) * 5/9
    return celsius

# Test the functions
temp_c = 25
temp_f = celsius_to_fahrenheit(temp_c)
print(f"{temp_c}°C = {temp_f}°F")

temp_f2 = 77
temp_c2 = fahrenheit_to_celsius(temp_f2)
print(f"{temp_f2}°F = {temp_c2:.1f}°C")


# ============================================
# PROGRAM 2: GRADE CALCULATOR
# ============================================

print("\n" + "=" * 50)
print("PROGRAM 2: GRADE CALCULATOR")
print("=" * 50 + "\n")

def calculate_grade(score):
    """Returns grade based on score"""
    if score >= 90:
        return "A+"
    elif score >= 80:
        return "A"
    elif score >= 70:
        return "B"
    elif score >= 60:
        return "C"
    elif score >= 50:
        return "D"
    else:
        return "F"

def calculate_average(scores):
    """Calculates average of a list of scores"""
    total = sum(scores)
    average = total / len(scores)
    return average

# Test the functions
student_scores = [85, 92, 78, 88, 95]
avg = calculate_average(student_scores)
grade = calculate_grade(avg)

print(f"Scores: {student_scores}")
print(f"Average: {avg:.2f}")
print(f"Grade: {grade}")


# ============================================
# PROGRAM 3: SIMPLE CALCULATOR
# ============================================

print("\n" + "=" * 50)
print("PROGRAM 3: SIMPLE CALCULATOR")
print("=" * 50 + "\n")

def add(a, b):
    """Returns sum of two numbers"""
    return a + b

def subtract(a, b):
    """Returns difference of two numbers"""
    return a - b

def multiply(a, b):
    """Returns product of two numbers"""
    return a * b

def divide(a, b):
    """Returns quotient of two numbers"""
    if b != 0:
        return a / b
    else:
        return "Error: Cannot divide by zero"

# Use the calculator functions
num1 = 20
num2 = 5

print(f"{num1} + {num2} = {add(num1, num2)}")
print(f"{num1} - {num2} = {subtract(num1, num2)}")
print(f"{num1} × {num2} = {multiply(num1, num2)}")
print(f"{num1} ÷ {num2} = {divide(num1, num2)}")


# ============================================
# PROGRAM 4: PASSWORD VALIDATOR
# ============================================

print("\n" + "=" * 50)
print("PROGRAM 4: PASSWORD VALIDATOR")
print("=" * 50 + "\n")

def is_strong_password(password):
    """Checks if password is strong"""
    # Check length
    if len(password) < 8:
        return False, "Password must be at least 8 characters"
    
    # Check for digit
    has_digit = False
    for char in password:
        if char.isdigit():
            has_digit = True
            break
    
    if not has_digit:
        return False, "Password must contain at least one number"
    
    # Check for uppercase
    has_upper = False
    for char in password:
        if char.isupper():
            has_upper = True
            break
    
    if not has_upper:
        return False, "Password must contain at least one uppercase letter"
    
    return True, "Password is strong!"

# Test passwords
test_passwords = ["weak", "Better123", "StrongPass1"]

for pwd in test_passwords:
    is_valid, message = is_strong_password(pwd)
    print(f"Password: '{pwd}'")
    print(f"Valid: {is_valid} - {message}\n")


# ============================================
# PRACTICE PROBLEMS
# ============================================

print("=" * 50)
print("PRACTICE PROBLEMS")
print("=" * 50)

"""
Try these exercises:

1. Write a function that checks if a number is prime.
   Return True if prime, False otherwise.

2. Create a function that reverses a string.
   Example: reverse("hello") should return "olleh"

3. Write a function that finds factorial of a number.

4. Create a function that checks if a string is a palindrome.
   (reads same forwards and backwards)

5. Write a function that calculates simple interest.
   Formula: (Principal × Rate × Time) / 100

6. Create a function that converts hours to seconds.

7. Write a function that finds the sum of digits in a number.
   Example: sum_digits(123) should return 6

8. Create a function that counts vowels in a string.

9. Write a function that generates the Fibonacci sequence up to n terms.
   Return the sequence as a list.

10. Create a function that checks if a year is a leap year.
    Return True if leap year, False otherwise.

11. Write a function that calculates BMI (Body Mass Index).
    BMI = weight(kg) / (height(m))²
    Return BMI and category (Underweight/Normal/Overweight/Obese)

12. Create a function that finds the largest and smallest number in a list.
    Return both values.
"""

print("\nTry solving the practice problems above!")
print("Functions make your code organized and reusable!")
