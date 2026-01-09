"""
IF-ELSE STATEMENTS IN PYTHON
=============================

Conditional statements allow your program to make decisions.
They execute different code based on whether conditions are True or False.

Basic Structure:
    if condition:
        # code to run if condition is True
    elif another_condition:
        # code to run if another_condition is True
    else:
        # code to run if all conditions are False
"""

# ============================================
# SIMPLE IF STATEMENT
# ============================================

print("=" * 50)
print("SIMPLE IF STATEMENT")
print("=" * 50 + "\n")

age = 18
if age >= 18:
    print("You are an adult!")
    print("You can vote!")

print()  # Empty line

# Another example
temperature = 35
if temperature > 30:
    print("It's hot outside! Drink plenty of water.")


# ============================================
# IF-ELSE STATEMENT
# ============================================

print("\n" + "=" * 50)
print("IF-ELSE STATEMENT")
print("=" * 50 + "\n")

score = 75

if score >= 50:
    print(f"Score: {score}")
    print("Result: PASS ✓")
else:
    print(f"Score: {score}")
    print("Result: FAIL ✗")


# Example 2: Check if number is even or odd
number = 17

if number % 2 == 0:
    print(f"\n{number} is an even number")
else:
    print(f"\n{number} is an odd number")


# ============================================
# IF-ELIF-ELSE STATEMENT
# ============================================

print("\n" + "=" * 50)
print("IF-ELIF-ELSE STATEMENT")
print("=" * 50 + "\n")

# Grade calculator
marks = 85

print(f"Marks: {marks}")

if marks >= 90:
    print("Grade: A+ (Excellent!)")
elif marks >= 80:
    print("Grade: A (Very Good!)")
elif marks >= 70:
    print("Grade: B (Good)")
elif marks >= 60:
    print("Grade: C (Average)")
elif marks >= 50:
    print("Grade: D (Pass)")
else:
    print("Grade: F (Fail)")


# Example 2: Traffic light system
print("\n")
traffic_light = "yellow"

if traffic_light == "red":
    print("STOP! 🔴")
elif traffic_light == "yellow":
    print("SLOW DOWN! 🟡")
elif traffic_light == "green":
    print("GO! 🟢")
else:
    print("Invalid traffic light color!")


# ============================================
# NESTED IF STATEMENTS
# ============================================

print("\n" + "=" * 50)
print("NESTED IF STATEMENTS")
print("=" * 50 + "\n")

# Movie ticket price calculator
age = 25
is_student = True

print(f"Age: {age}, Student: {is_student}")

if age < 12:
    price = 5
    print("Ticket Price: $5 (Child)")
elif age >= 60:
    price = 7
    print("Ticket Price: $7 (Senior)")
else:
    # Nested if for adult tickets
    if is_student:
        price = 8
        print("Ticket Price: $8 (Student)")
    else:
        price = 12
        print("Ticket Price: $12 (Adult)")


# ============================================
# MULTIPLE CONDITIONS (AND, OR)
# ============================================

print("\n" + "=" * 50)
print("MULTIPLE CONDITIONS")
print("=" * 50 + "\n")

# Example 1: Check if person can drive
age = 20
has_license = True

if age >= 18 and has_license:
    print("You can drive! ✓")
else:
    print("You cannot drive.")
    if age < 18:
        print("Reason: You are under 18")
    if not has_license:
        print("Reason: You don't have a license")


# Example 2: Weekend or Holiday checker
print()
day = "Sunday"
is_holiday = False

if day == "Saturday" or day == "Sunday" or is_holiday:
    print("Yay! It's time to relax! 🎉")
else:
    print("It's a working day. Stay productive! 💼")


# ============================================
# PRACTICAL PROGRAMS
# ============================================

print("\n" + "=" * 50)
print("PROGRAM 1: LOGIN SYSTEM")
print("=" * 50 + "\n")

# Simple login checker
correct_username = "admin"
correct_password = "python123"

username = "admin"
password = "python123"

if username == correct_username and password == correct_password:
    print("✓ Login successful! Welcome!")
else:
    print("✗ Login failed! Invalid credentials.")


print("\n" + "=" * 50)
print("PROGRAM 2: DISCOUNT CALCULATOR")
print("=" * 50 + "\n")

purchase_amount = 150
is_member = True

print(f"Purchase Amount: ${purchase_amount}")
print(f"Membership: {is_member}")

if purchase_amount >= 200:
    discount = 20
elif purchase_amount >= 100 and is_member:
    discount = 15
elif purchase_amount >= 100:
    discount = 10
elif purchase_amount >= 50:
    discount = 5
else:
    discount = 0

discount_amount = purchase_amount * (discount / 100)
final_price = purchase_amount - discount_amount

print(f"Discount: {discount}%")
print(f"Discount Amount: ${discount_amount}")
print(f"Final Price: ${final_price}")


print("\n" + "=" * 50)
print("PROGRAM 3: SIMPLE CALCULATOR")
print("=" * 50 + "\n")

num1 = 10
num2 = 5
operation = "+"

print(f"Number 1: {num1}")
print(f"Number 2: {num2}")
print(f"Operation: {operation}\n")

if operation == "+":
    result = num1 + num2
    print(f"Result: {num1} + {num2} = {result}")
elif operation == "-":
    result = num1 - num2
    print(f"Result: {num1} - {num2} = {result}")
elif operation == "*":
    result = num1 * num2
    print(f"Result: {num1} × {num2} = {result}")
elif operation == "/":
    if num2 != 0:
        result = num1 / num2
        print(f"Result: {num1} ÷ {num2} = {result}")
    else:
        print("Error: Cannot divide by zero!")
else:
    print("Error: Invalid operation!")


# ============================================
# PRACTICE PROBLEMS
# ============================================

print("\n" + "=" * 50)
print("PRACTICE PROBLEMS")
print("=" * 50)

"""
Try these exercises:

1. Write a program that checks if a number is positive, negative, or zero.

2. Create a program that takes a person's age and tells them which category
   they belong to:
   - 0-12: Child
   - 13-19: Teenager
   - 20-59: Adult
   - 60+: Senior

3. Write a program that checks if a triangle is valid. A triangle is valid if
   the sum of any two sides is greater than the third side.
   (Check for all three combinations)

4. Create a BMI calculator that categorizes the result:
   - BMI < 18.5: Underweight
   - BMI 18.5-24.9: Normal weight
   - BMI 25-29.9: Overweight
   - BMI >= 30: Obese
   Formula: BMI = weight(kg) / (height(m) × height(m))

5. Write a program that determines if a student gets admission to a college.
   Admission requirements:
   - Math score >= 80 AND
   - Science score >= 75 AND
   - English score >= 70

6. Create a simple menu system for a restaurant with at least 5 items.
   Based on the choice, display the item name and price.

7. Write a program to find the largest of three numbers.
"""

print("\nTry solving the practice problems above!")
print("Remember: Practice is the key to mastering programming!")
