"""
Logical Operators in Python
============================
This program demonstrates using and, or, not operators in conditions.
"""

# AND operator - both conditions must be True
print("=== AND Operator ===")
age = 25
has_license = True

if age >= 18 and has_license:
    print("You can drive a car!")
else:
    print("You cannot drive")

# More AND examples
print("\n=== Login with AND ===")
username = "admin"
password = "1234"

if username == "admin" and password == "1234":
    print("Login successful!")
else:
    print("Invalid credentials")

# OR operator - at least one condition must be True
print("\n=== OR Operator ===")
day = "Sunday"

if day == "Saturday" or day == "Sunday":
    print("It's the weekend! 🎉")
else:
    print("It's a weekday 📚")

# More OR examples
print("\n=== Emergency Contact OR ===")
relationship = "parent"

if relationship == "parent" or relationship == "guardian" or relationship == "spouse":
    print("Valid emergency contact")
else:
    print("Please provide a close family member")

# NOT operator - reverses the condition
print("\n=== NOT Operator ===")
is_raining = False

if not is_raining:
    print("You don't need an umbrella")
else:
    print("Take an umbrella!")

# Combining AND, OR
print("\n=== Combining AND, OR ===")
age = 22
student = True
employed = False

if (age < 25 and student) or employed:
    print("Eligible for discount")
else:
    print("Not eligible for discount")

# Scholarship eligibility
print("\n=== Scholarship Eligibility ===")
marks = 85
income = 40000

if marks >= 80 and income < 50000:
    print("Eligible for scholarship!")
else:
    print("Not eligible for scholarship")

# Voting eligibility with logical operators
print("\n=== Voting Eligibility ===")
age = 20
is_citizen = True
has_criminal_record = False

if age >= 18 and is_citizen and not has_criminal_record:
    print("You are eligible to vote! ✓")
else:
    print("You are not eligible to vote")

# Weekend or holiday
print("\n=== Day Off Checker ===")
day = "Saturday"
is_holiday = False

if day == "Saturday" or day == "Sunday" or is_holiday:
    print("You have the day off! 😊")
else:
    print("It's a working day")

# Movie rating system
print("\n=== Movie Access Control ===")
age = 16
has_parent = True
movie_rating = "R"

if movie_rating == "G":
    print("Everyone can watch")
elif movie_rating == "PG" and (age >= 13 or has_parent):
    print("You can watch this movie")
elif movie_rating == "R" and age >= 18:
    print("You can watch this movie")
elif movie_rating == "R" and age >= 13 and has_parent:
    print("You can watch with parental guidance")
else:
    print("You cannot watch this movie")

# Exam pass conditions
print("\n=== Exam Pass Criteria ===")
theory = 65
practical = 70
attendance = 80

if (theory >= 50 and practical >= 50) and attendance >= 75:
    print("Result: PASS ✓")
    print("Congratulations!")
else:
    print("Result: FAIL ✗")
    if theory < 50:
        print("Failed in theory")
    if practical < 50:
        print("Failed in practical")
    if attendance < 75:
        print("Insufficient attendance")

# Login attempt validation
print("\n=== Login Validation ===")
username = "user123"
password = "pass456"
account_active = True
attempts_left = 3

if username == "user123" and password == "pass456":
    if account_active and attempts_left > 0:
        print("Login successful!")
    elif not account_active:
        print("Account is deactivated")
    else:
        print("Too many failed attempts")
else:
    print("Invalid username or password")

# Discount eligibility
print("\n=== Discount Eligibility ===")
purchase_amount = 1200
is_member = True
has_coupon = False

if purchase_amount >= 1000 or (is_member and purchase_amount >= 500):
    print("Base discount: 10%")
    if has_coupon:
        print("Additional coupon discount: 5%")
        print("Total discount: 15%")
    else:
        print("Total discount: 10%")
else:
    print("No discount available")

# Temperature comfort check
print("\n=== Temperature Comfort ===")
temperature = 24
humidity = 60

if (temperature >= 20 and temperature <= 26) and humidity < 70:
    print("Weather is comfortable! 😊")
elif temperature < 20:
    print("It's cold!")
elif temperature > 26:
    print("It's hot!")
else:
    print("High humidity makes it uncomfortable")

# Interactive example
print("\n=== Interactive Age & License Check ===")
user_age = int(input("Enter your age: "))
has_driving_license = input("Do you have a driving license? (yes/no): ").lower()

if user_age >= 18 and (has_driving_license == "yes" or has_driving_license == "y"):
    print("You are allowed to drive!")
elif user_age >= 18 and (has_driving_license == "no" or has_driving_license == "n"):
    print("You are old enough but need a license")
else:
    print("You are too young to drive")
