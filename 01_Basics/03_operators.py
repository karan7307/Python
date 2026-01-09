"""
OPERATORS IN PYTHON
===================

Operators are special symbols that perform operations on variables and values.
Python has several types of operators:
1. Arithmetic Operators - For math operations
2. Comparison Operators - For comparing values
3. Logical Operators - For combining conditions
4. Assignment Operators - For assigning values
"""

# ============================================
# ARITHMETIC OPERATORS
# ============================================

print("=" * 50)
print("ARITHMETIC OPERATORS")
print("=" * 50 + "\n")

a = 15
b = 4

print(f"a = {a}, b = {b}\n")

# Addition
print(f"Addition: {a} + {b} = {a + b}")

# Subtraction
print(f"Subtraction: {a} - {b} = {a - b}")

# Multiplication
print(f"Multiplication: {a} × {b} = {a * b}")

# Division (always returns float)
print(f"Division: {a} ÷ {b} = {a / b}")

# Floor Division (returns integer, rounds down)
print(f"Floor Division: {a} ÷÷ {b} = {a // b}")

# Modulus (remainder after division)
print(f"Modulus: {a} % {b} = {a % b}")

# Exponentiation (power)
print(f"Exponentiation: {a} ^ {b} = {a ** b}")


# ============================================
# COMPARISON OPERATORS
# ============================================

print("\n" + "=" * 50)
print("COMPARISON OPERATORS")
print("=" * 50 + "\n")

x = 10
y = 20

print(f"x = {x}, y = {y}\n")

# Equal to
print(f"Is x equal to y? {x} == {y} : {x == y}")

# Not equal to
print(f"Is x not equal to y? {x} != {y} : {x != y}")

# Greater than
print(f"Is x greater than y? {x} > {y} : {x > y}")

# Less than
print(f"Is x less than y? {x} < {y} : {x < y}")

# Greater than or equal to
print(f"Is x greater than or equal to y? {x} >= {y} : {x >= y}")

# Less than or equal to
print(f"Is x less than or equal to y? {x} <= {y} : {x <= y}")


# ============================================
# LOGICAL OPERATORS
# ============================================

print("\n" + "=" * 50)
print("LOGICAL OPERATORS")
print("=" * 50 + "\n")

# Logical operators are used to combine conditions
age = 22
has_license = True
has_car = False

# AND - Both conditions must be True
print(f"Age: {age}, Has License: {has_license}, Has Car: {has_car}\n")
print(f"Can drive? (age >= 18 AND has_license): {age >= 18 and has_license}")
print(f"Can drive own car? (has_license AND has_car): {has_license and has_car}")

# OR - At least one condition must be True
is_weekend = True
is_holiday = False
print(f"\nIs Weekend: {is_weekend}, Is Holiday: {is_holiday}")
print(f"Can relax? (is_weekend OR is_holiday): {is_weekend or is_holiday}")

# NOT - Reverses the boolean value
is_raining = False
print(f"\nIs it raining? {is_raining}")
print(f"Is it NOT raining? {not is_raining}")


# ============================================
# ASSIGNMENT OPERATORS
# ============================================

print("\n" + "=" * 50)
print("ASSIGNMENT OPERATORS")
print("=" * 50 + "\n")

# Simple assignment
score = 50
print(f"Initial score: {score}")

# Add and assign
score += 10  # Same as: score = score + 10
print(f"After += 10: {score}")

# Subtract and assign
score -= 5  # Same as: score = score - 5
print(f"After -= 5: {score}")

# Multiply and assign
score *= 2  # Same as: score = score * 2
print(f"After *= 2: {score}")

# Divide and assign
score /= 4  # Same as: score = score / 4
print(f"After /= 4: {score}")


# ============================================
# PRACTICAL EXAMPLES
# ============================================

print("\n" + "=" * 50)
print("PRACTICAL EXAMPLES")
print("=" * 50 + "\n")

# Example 1: Calculate total bill with tip
bill_amount = 100
tip_percentage = 15
tip = bill_amount * (tip_percentage / 100)
total = bill_amount + tip

print("RESTAURANT BILL CALCULATOR")
print(f"Bill Amount: ${bill_amount}")
print(f"Tip ({tip_percentage}%): ${tip}")
print(f"Total to pay: ${total}")


# Example 2: Check if number is even or odd
number = 17
is_even = (number % 2 == 0)
print(f"\nIs {number} an even number? {is_even}")


# Example 3: Check eligibility for discount
print("\nDISCOUNT ELIGIBILITY CHECKER")
purchase_amount = 150
is_member = True
has_coupon = False

# Gets discount if purchase > 100 AND (is member OR has coupon)
eligible_for_discount = purchase_amount > 100 and (is_member or has_coupon)
print(f"Purchase Amount: ${purchase_amount}")
print(f"Is Member: {is_member}")
print(f"Has Coupon: {has_coupon}")
print(f"Eligible for discount: {eligible_for_discount}")


# Example 4: Temperature checker
print("\nTEMPERATURE CHECKER")
temperature = 28
is_hot = temperature > 30
is_cold = temperature < 15
is_comfortable = not is_hot and not is_cold

print(f"Temperature: {temperature}°C")
print(f"Is it hot? {is_hot}")
print(f"Is it cold? {is_cold}")
print(f"Is it comfortable? {is_comfortable}")


# ============================================
# PRACTICE PROBLEMS
# ============================================

print("\n" + "=" * 50)
print("PRACTICE PROBLEMS")
print("=" * 50)

"""
Try these exercises:

1. Write a program that takes two numbers and prints whether the first
   number is greater than, less than, or equal to the second number.

2. Create a program that calculates the area and perimeter of a circle
   given its radius. (Area = π × r², Perimeter = 2 × π × r)
   Use 3.14159 for π.

3. Write a program to check if a student passes an exam. A student passes if:
   - Score is >= 40 AND
   - Attendance is >= 75%

4. Create a simple program that converts kilometers to miles.
   (1 kilometer = 0.621371 miles)

5. Write a program that checks if a year is a leap year.
   A year is a leap year if:
   - It is divisible by 4 AND
   - (Not divisible by 100 OR divisible by 400)

6. Create a program that calculates the discount amount and final price.
   If purchase > $100, give 10% discount, otherwise 5% discount.
"""

print("\nTry solving the practice problems above!")
print("Practice makes perfect! Happy coding!")
