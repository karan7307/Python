"""
Basic if-else Statements in Python
===================================
This program demonstrates how to use if and else statements to make decisions.
"""

# Simple if statement
print("=== Simple if Statement ===")
age = 20

if age >= 18:
    print("You are an adult")
    print("You can vote!")

print("This line always executes\n")

# if-else statement
print("=== if-else Statement ===")
temperature = 25

if temperature > 30:
    print("It's hot outside!")
else:
    print("The weather is pleasant.")

# Checking even or odd
print("\n=== Even or Odd Checker ===")
number = 7

if number % 2 == 0:
    print(f"{number} is even")
else:
    print(f"{number} is odd")

# Comparison operators
print("\n=== Comparison Operators ===")
a = 10
b = 20

print(f"a = {a}, b = {b}")
print(f"a == b: {a == b}")   # Equal to
print(f"a != b: {a != b}")   # Not equal to
print(f"a > b: {a > b}")     # Greater than
print(f"a < b: {a < b}")     # Less than
print(f"a >= b: {a >= b}")   # Greater than or equal to
print(f"a <= b: {a <= b}")   # Less than or equal to

# Using comparisons in if statements
print("\n=== Grade Pass/Fail ===")
marks = 75

if marks >= 50:
    print(f"Marks: {marks}")
    print("Result: PASS ✓")
else:
    print(f"Marks: {marks}")
    print("Result: FAIL ✗")

# String comparison
print("\n=== String Comparison ===")
password = "python123"
user_input = "python123"

if user_input == password:
    print("Password correct! Access granted.")
else:
    print("Wrong password! Access denied.")

# Checking if a number is positive or negative
print("\n=== Positive/Negative Checker ===")
num = -5

if num >= 0:
    print(f"{num} is positive or zero")
else:
    print(f"{num} is negative")

# Age category checker
print("\n=== Age Category ===")
person_age = 15

if person_age >= 18:
    print("Category: Adult")
    print("Can drive, vote, and watch adult movies")
else:
    print("Category: Minor")
    print("Cannot drive or vote yet")

# Boolean variables in conditions
print("\n=== Boolean in Conditions ===")
is_raining = True

if is_raining:
    print("Take an umbrella!")
else:
    print("No need for an umbrella.")

# Discount eligibility
print("\n=== Discount Checker ===")
purchase_amount = 1500
minimum_for_discount = 1000

if purchase_amount >= minimum_for_discount:
    discount = purchase_amount * 0.1
    final_amount = purchase_amount - discount
    print(f"Purchase amount: ${purchase_amount}")
    print(f"Discount (10%): ${discount}")
    print(f"Final amount: ${final_amount}")
else:
    print(f"Purchase amount: ${purchase_amount}")
    print("No discount available")
    print(f"Final amount: ${purchase_amount}")

# Membership check
print("\n=== Membership Checker ===")
has_membership = False

if has_membership:
    print("Welcome back, member! Enjoy 20% off.")
else:
    print("Sign up for membership to get discounts!")

# Interactive example
print("\n=== Interactive Age Checker ===")
user_age = int(input("Enter your age: "))

if user_age >= 18:
    print("You are eligible to vote!")
else:
    years_left = 18 - user_age
    print(f"You need to wait {years_left} more year(s) to vote.")
