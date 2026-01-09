"""
Taking Numeric Input in Python
===============================
This program demonstrates how to take and use numeric input from users.
Remember: input() always returns a string, so we need to convert it!
"""

# Taking integer input
print("=== Taking Integer Input ===")
age = input("Enter your age: ")
print(f"You entered: {age} (type: {type(age)})")

# Convert string to integer
age = int(age)
print(f"After conversion: {age} (type: {type(age)})")

# Now we can do math with it
next_year_age = age + 1
print(f"Next year you will be {next_year_age} years old")

# Taking float input
print("\n=== Taking Float Input ===")
height = float(input("Enter your height in feet: "))
print(f"Your height is {height} feet")
height_in_inches = height * 12
print(f"That's {height_in_inches} inches!")

# Simple calculator
print("\n=== Simple Calculator ===")
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

print(f"\nResults:")
print(f"{num1} + {num2} = {num1 + num2}")
print(f"{num1} - {num2} = {num1 - num2}")
print(f"{num1} * {num2} = {num1 * num2}")
print(f"{num1} / {num2} = {num1 / num2}")

# Taking input and doing calculations
print("\n=== Rectangle Area Calculator ===")
length = float(input("Enter length of rectangle: "))
width = float(input("Enter width of rectangle: "))
area = length * width
perimeter = 2 * (length + width)

print(f"\nRectangle Properties:")
print(f"Length: {length}")
print(f"Width: {width}")
print(f"Area: {area}")
print(f"Perimeter: {perimeter}")

# Temperature converter
print("\n=== Temperature Converter (Celsius to Fahrenheit) ===")
celsius = float(input("Enter temperature in Celsius: "))
fahrenheit = (celsius * 9/5) + 32
print(f"{celsius}°C is equal to {fahrenheit}°F")

# Taking input with error handling
print("\n=== Safe Number Input ===")
try:
    number = int(input("Enter a whole number: "))
    print(f"You entered: {number}")
    print(f"Double of your number: {number * 2}")
except ValueError:
    print("Error: Please enter a valid whole number!")

# Shopping bill calculator
print("\n=== Shopping Bill Calculator ===")
item_name = input("Enter item name: ")
price = float(input("Enter price per item: $"))
quantity = int(input("Enter quantity: "))

total = price * quantity
tax = total * 0.1  # 10% tax
final_total = total + tax

print(f"\n--- Bill ---")
print(f"Item: {item_name}")
print(f"Price: ${price:.2f}")
print(f"Quantity: {quantity}")
print(f"Subtotal: ${total:.2f}")
print(f"Tax (10%): ${tax:.2f}")
print(f"Total: ${final_total:.2f}")

# Age calculator
print("\n=== Age Calculator ===")
current_year = 2024
birth_year = int(input("Enter your birth year: "))
age = current_year - birth_year
print(f"You are approximately {age} years old")

# BMI Calculator
print("\n=== BMI Calculator ===")
weight = float(input("Enter your weight in kg: "))
height_m = float(input("Enter your height in meters: "))
bmi = weight / (height_m ** 2)

print(f"\nYour BMI: {bmi:.2f}")
if bmi < 18.5:
    print("Category: Underweight")
elif bmi < 25:
    print("Category: Normal weight")
elif bmi < 30:
    print("Category: Overweight")
else:
    print("Category: Obese")
