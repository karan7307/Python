"""
elif (else-if) Statement in Python
===================================
This program demonstrates how to use elif for multiple conditions.
"""

# Basic elif example
print("=== Traffic Light System ===")
light = "yellow"

if light == "red":
    print("STOP")
elif light == "yellow":
    print("SLOW DOWN")
elif light == "green":
    print("GO")
else:
    print("Invalid light color")

# Grade calculator
print("\n=== Grade Calculator ===")
marks = 85

if marks >= 90:
    grade = "A"
elif marks >= 80:
    grade = "B"
elif marks >= 70:
    grade = "C"
elif marks >= 60:
    grade = "D"
elif marks >= 50:
    grade = "E"
else:
    grade = "F"

print(f"Marks: {marks}")
print(f"Grade: {grade}")

# Age category checker (more detailed)
print("\n=== Detailed Age Categories ===")
age = 25

if age < 0:
    print("Invalid age!")
elif age <= 2:
    print("Category: Infant")
elif age <= 12:
    print("Category: Child")
elif age <= 19:
    print("Category: Teenager")
elif age <= 59:
    print("Category: Adult")
else:
    print("Category: Senior Citizen")

# BMI category
print("\n=== BMI Category Calculator ===")
bmi = 23.5

if bmi < 18.5:
    category = "Underweight"
    suggestion = "You should eat more nutritious food"
elif bmi < 25:
    category = "Normal weight"
    suggestion = "Keep maintaining your healthy lifestyle!"
elif bmi < 30:
    category = "Overweight"
    suggestion = "Consider regular exercise and balanced diet"
else:
    category = "Obese"
    suggestion = "Please consult a doctor for health advice"

print(f"BMI: {bmi}")
print(f"Category: {category}")
print(f"Suggestion: {suggestion}")

# Temperature advisory
print("\n=== Temperature Advisory ===")
temp = 28

if temp < 0:
    print("Freezing! Stay indoors.")
elif temp < 15:
    print("Cold. Wear warm clothes.")
elif temp < 25:
    print("Pleasant weather. Enjoy!")
elif temp < 35:
    print("Warm. Stay hydrated.")
else:
    print("Very hot! Avoid going out.")

# Discount based on purchase amount
print("\n=== Discount Calculator ===")
amount = 2500

if amount >= 5000:
    discount_percent = 20
elif amount >= 3000:
    discount_percent = 15
elif amount >= 1000:
    discount_percent = 10
elif amount >= 500:
    discount_percent = 5
else:
    discount_percent = 0

discount = amount * discount_percent / 100
final_amount = amount - discount

print(f"Purchase amount: ${amount}")
print(f"Discount: {discount_percent}%")
print(f"Discount amount: ${discount}")
print(f"Final amount: ${final_amount}")

# Day of week
print("\n=== Day of Week ===")
day = 3

if day == 1:
    print("Monday - Start of the work week")
elif day == 2:
    print("Tuesday")
elif day == 3:
    print("Wednesday - Mid-week")
elif day == 4:
    print("Thursday")
elif day == 5:
    print("Friday - Last working day!")
elif day == 6:
    print("Saturday - Weekend!")
elif day == 7:
    print("Sunday - Weekend!")
else:
    print("Invalid day number!")

# Ticket pricing based on age
print("\n=== Movie Ticket Pricing ===")
visitor_age = 8

if visitor_age < 3:
    price = 0
    category = "Free (Infant)"
elif visitor_age < 12:
    price = 5
    category = "Child ticket"
elif visitor_age < 18:
    price = 8
    category = "Teen ticket"
elif visitor_age < 60:
    price = 12
    category = "Adult ticket"
else:
    price = 6
    category = "Senior citizen ticket"

print(f"Age: {visitor_age}")
print(f"Category: {category}")
print(f"Ticket price: ${price}")

# Interactive grade calculator
print("\n=== Interactive Grade Calculator ===")
score = int(input("Enter your marks (0-100): "))

if score > 100 or score < 0:
    print("Invalid marks! Please enter between 0 and 100.")
elif score >= 90:
    print("Grade: A - Excellent!")
elif score >= 80:
    print("Grade: B - Very Good!")
elif score >= 70:
    print("Grade: C - Good!")
elif score >= 60:
    print("Grade: D - Satisfactory")
elif score >= 50:
    print("Grade: E - Pass")
else:
    print("Grade: F - Fail")
