"""
Return Values in Python Functions
==================================
This program demonstrates different ways functions can return values.
"""

# Simple return
print("=== Simple Return ===")
def square(number):
    """Returns the square of a number"""
    return number ** 2

result = square(5)
print(f"Square of 5: {result}")
print(f"Square of 8: {square(8)}")

# Return with conditional
print("\n=== Return with Conditional ===")
def absolute_value(number):
    """Returns absolute value of a number"""
    if number < 0:
        return -number
    return number

print(f"Absolute of -5: {absolute_value(-5)}")
print(f"Absolute of 10: {absolute_value(10)}")

# Multiple return statements
print("\n=== Multiple Returns ===")
def grade_to_points(grade):
    """Convert letter grade to points"""
    if grade == "A":
        return 4.0
    elif grade == "B":
        return 3.0
    elif grade == "C":
        return 2.0
    elif grade == "D":
        return 1.0
    else:
        return 0.0

print(f"Grade A: {grade_to_points('A')} points")
print(f"Grade B: {grade_to_points('B')} points")
print(f"Grade F: {grade_to_points('F')} points")

# Returning multiple values (tuple)
print("\n=== Returning Multiple Values ===")
def get_circle_properties(radius):
    """Returns area and circumference of a circle"""
    pi = 3.14159
    area = pi * radius ** 2
    circumference = 2 * pi * radius
    return area, circumference  # Returns a tuple

area, circumference = get_circle_properties(5)
print(f"Circle with radius 5:")
print(f"  Area: {area:.2f}")
print(f"  Circumference: {circumference:.2f}")

# Returning a list
print("\n=== Returning a List ===")
def get_multiples(number, count):
    """Returns first 'count' multiples of number"""
    multiples = []
    for i in range(1, count + 1):
        multiples.append(number * i)
    return multiples

result = get_multiples(5, 10)
print(f"First 10 multiples of 5: {result}")

# Returning a dictionary
print("\n=== Returning a Dictionary ===")
def get_student_info(name, age, grade):
    """Returns student information as a dictionary"""
    return {
        "name": name,
        "age": age,
        "grade": grade,
        "status": "Pass" if grade != "F" else "Fail"
    }

student = get_student_info("Alice", 20, "A")
print(f"Student: {student}")

# Return None (implicitly)
print("\n=== Return None ===")
def print_message(text):
    """Prints message but doesn't return anything"""
    print(f"Message: {text}")
    # No return statement means returns None

result = print_message("Hello")
print(f"Return value: {result}")

# Explicit return None
def check_positive(number):
    """Returns number if positive, None otherwise"""
    if number > 0:
        return number
    return None

print(f"Check 5: {check_positive(5)}")
print(f"Check -3: {check_positive(-3)}")

# Early return
print("\n=== Early Return ===")
def divide(a, b):
    """Divides a by b with error checking"""
    if b == 0:
        return "Error: Division by zero"
    return a / b

print(f"10 / 2 = {divide(10, 2)}")
print(f"10 / 0 = {divide(10, 0)}")

# Returning boolean
print("\n=== Returning Boolean ===")
def is_even(number):
    """Returns True if number is even"""
    return number % 2 == 0

def is_prime(n):
    """Returns True if number is prime"""
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

print(f"Is 10 even? {is_even(10)}")
print(f"Is 7 even? {is_even(7)}")
print(f"Is 17 prime? {is_prime(17)}")
print(f"Is 20 prime? {is_prime(20)}")

# Using return value in conditions
print("\n=== Using Return in Conditions ===")
def check_password(password):
    """Validates password strength"""
    if len(password) < 8:
        return False, "Too short"
    if not any(c.isdigit() for c in password):
        return False, "Needs a number"
    if not any(c.isupper() for c in password):
        return False, "Needs uppercase"
    return True, "Strong password"

passwords = ["short", "longpassword", "LongPassword1"]
for pwd in passwords:
    valid, message = check_password(pwd)
    status = "✓" if valid else "✗"
    print(f"{status} '{pwd}': {message}")

# Chaining function calls
print("\n=== Chaining Functions ===")
def double(x):
    return x * 2

def add_ten(x):
    return x + 10

number = 5
result = add_ten(double(number))  # double(5) = 10, then add_ten(10) = 20
print(f"double({number}) + 10 = {result}")

# Returning calculation results
print("\n=== Statistics Calculator ===")
def calculate_stats(numbers):
    """Returns multiple statistics"""
    total = sum(numbers)
    count = len(numbers)
    average = total / count if count > 0 else 0
    maximum = max(numbers) if numbers else None
    minimum = min(numbers) if numbers else None
    
    return {
        "sum": total,
        "count": count,
        "average": average,
        "max": maximum,
        "min": minimum
    }

nums = [45, 67, 23, 89, 12, 56]
stats = calculate_stats(nums)
print(f"Numbers: {nums}")
print(f"Statistics: {stats}")

# Practical: Grade calculator
print("\n=== Grade Calculator ===")
def calculate_final_grade(*scores):
    """Calculate average and assign letter grade"""
    if not scores:
        return None, "No scores"
    
    average = sum(scores) / len(scores)
    
    if average >= 90:
        letter = "A"
    elif average >= 80:
        letter = "B"
    elif average >= 70:
        letter = "C"
    elif average >= 60:
        letter = "D"
    else:
        letter = "F"
    
    return average, letter

avg, grade = calculate_final_grade(85, 90, 88, 92)
print(f"Average: {avg:.2f}, Grade: {grade}")

# Returning nested structures
print("\n=== Returning Nested Structures ===")
def analyze_text(text):
    """Analyzes text and returns detailed statistics"""
    words = text.split()
    return {
        "char_count": len(text),
        "word_count": len(words),
        "words": {
            "first": words[0] if words else None,
            "last": words[-1] if words else None,
            "longest": max(words, key=len) if words else None
        }
    }

text = "Python programming is fun and powerful"
analysis = analyze_text(text)
print(f"Text: '{text}'")
print(f"Analysis: {analysis}")

# Lambda with return
print("\n=== Lambda Functions (Inline Returns) ===")
square_lambda = lambda x: x ** 2
add_lambda = lambda a, b: a + b
max_lambda = lambda a, b: a if a > b else b

print(f"Square of 6: {square_lambda(6)}")
print(f"Add 3 + 7: {add_lambda(3, 7)}")
print(f"Max of 15, 10: {max_lambda(15, 10)}")
