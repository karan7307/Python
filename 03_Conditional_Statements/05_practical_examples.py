"""
Practical Examples of Conditional Statements
=============================================
This program contains real-world applications of if-else statements.
"""

# Example 1: Simple Calculator
print("=== SIMPLE CALCULATOR ===")
num1 = float(input("Enter first number: "))
operator = input("Enter operator (+, -, *, /): ")
num2 = float(input("Enter second number: "))

if operator == "+":
    result = num1 + num2
    print(f"{num1} + {num2} = {result}")
elif operator == "-":
    result = num1 - num2
    print(f"{num1} - {num2} = {result}")
elif operator == "*":
    result = num1 * num2
    print(f"{num1} * {num2} = {result}")
elif operator == "/":
    if num2 != 0:
        result = num1 / num2
        print(f"{num1} / {num2} = {result}")
    else:
        print("Error: Division by zero!")
else:
    print("Invalid operator!")

# Example 2: Grade Calculator
print("\n=== GRADE CALCULATOR ===")
marks = int(input("Enter your marks (0-100): "))

if marks > 100 or marks < 0:
    print("Invalid marks! Please enter between 0 and 100.")
else:
    if marks >= 90:
        grade = "A"
        remark = "Outstanding!"
    elif marks >= 80:
        grade = "B"
        remark = "Excellent!"
    elif marks >= 70:
        grade = "C"
        remark = "Good!"
    elif marks >= 60:
        grade = "D"
        remark = "Satisfactory"
    elif marks >= 50:
        grade = "E"
        remark = "Pass"
    else:
        grade = "F"
        remark = "Fail"
    
    print(f"Marks: {marks}")
    print(f"Grade: {grade}")
    print(f"Remark: {remark}")

# Example 3: Leap Year Checker
print("\n=== LEAP YEAR CHECKER ===")
year = int(input("Enter a year: "))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} is a leap year! 🎉")
else:
    print(f"{year} is not a leap year.")

# Example 4: Electricity Bill Calculator
print("\n=== ELECTRICITY BILL CALCULATOR ===")
units = int(input("Enter units consumed: "))

if units <= 100:
    bill = units * 0
    print("First 100 units are free!")
elif units <= 200:
    bill = (units - 100) * 2.50
elif units <= 300:
    bill = (100 * 2.50) + ((units - 200) * 4.00)
else:
    bill = (100 * 2.50) + (100 * 4.00) + ((units - 300) * 6.50)

print(f"Units consumed: {units}")
print(f"Total bill: ${bill:.2f}")

# Example 5: Triangle Type Checker
print("\n=== TRIANGLE TYPE CHECKER ===")
side1 = float(input("Enter first side: "))
side2 = float(input("Enter second side: "))
side3 = float(input("Enter third side: "))

if side1 + side2 > side3 and side2 + side3 > side1 and side1 + side3 > side2:
    print("Valid triangle!")
    if side1 == side2 == side3:
        print("Type: Equilateral Triangle")
    elif side1 == side2 or side2 == side3 or side1 == side3:
        print("Type: Isosceles Triangle")
    else:
        print("Type: Scalene Triangle")
else:
    print("Invalid triangle! Sum of any two sides must be greater than the third.")

# Example 6: Largest of Three Numbers
print("\n=== LARGEST OF THREE NUMBERS ===")
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if a >= b and a >= c:
    largest = a
elif b >= a and b >= c:
    largest = b
else:
    largest = c

print(f"The largest number is: {largest}")

# Example 7: Ticket Booking System
print("\n=== MOVIE TICKET BOOKING ===")
age = int(input("Enter your age: "))
movie_time = input("Enter show time (morning/afternoon/evening): ").lower()

# Calculate base price
if age < 3:
    base_price = 0
elif age < 12:
    base_price = 100
elif age < 60:
    base_price = 200
else:
    base_price = 150

# Apply time-based discount
if movie_time == "morning":
    discount = base_price * 0.20
    print("Morning show discount: 20%")
elif movie_time == "afternoon":
    discount = base_price * 0.10
    print("Afternoon show discount: 10%")
else:
    discount = 0
    print("No time discount for evening shows")

final_price = base_price - discount
print(f"\nBase price: ${base_price}")
print(f"Discount: ${discount}")
print(f"Final ticket price: ${final_price}")

# Example 8: Password Strength Checker
print("\n=== PASSWORD STRENGTH CHECKER ===")
password = input("Enter a password: ")
length = len(password)

has_upper = any(c.isupper() for c in password)
has_lower = any(c.islower() for c in password)
has_digit = any(c.isdigit() for c in password)

if length < 6:
    strength = "Very Weak"
    message = "Password is too short!"
elif length < 8:
    if has_upper and has_lower:
        strength = "Weak"
        message = "Add numbers for better security"
    else:
        strength = "Very Weak"
        message = "Use both uppercase and lowercase"
else:
    if has_upper and has_lower and has_digit:
        strength = "Strong"
        message = "Great password! ✓"
    elif (has_upper and has_lower) or (has_digit and (has_upper or has_lower)):
        strength = "Medium"
        message = "Consider adding more variety"
    else:
        strength = "Weak"
        message = "Use uppercase, lowercase, and numbers"

print(f"Password length: {length}")
print(f"Strength: {strength}")
print(f"Message: {message}")
