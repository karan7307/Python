"""
Working with Numbers in Python
===============================
This program demonstrates integer and float operations.
"""

# Integer examples
num1 = 10
num2 = 3

print("=== Integer Operations ===")
print("Number 1:", num1)
print("Number 2:", num2)
print("Addition:", num1 + num2)
print("Subtraction:", num1 - num2)
print("Multiplication:", num1 * num2)
print("Division:", num1 / num2)           # Returns float
print("Floor Division:", num1 // num2)    # Returns integer (rounds down)
print("Modulus (Remainder):", num1 % num2)
print("Power:", num1 ** num2)             # 10 to the power of 3

# Float examples
price1 = 19.99
price2 = 5.50

print("\n=== Float Operations ===")
print("Price 1: $", price1)
print("Price 2: $", price2)
print("Total Price: $", price1 + price2)
print("Average Price: $", (price1 + price2) / 2)

# Mixed operations (int and float)
quantity = 5                    # Integer
price_per_item = 12.50         # Float
total = quantity * price_per_item

print("\n=== Shopping Bill ===")
print("Quantity:", quantity)
print("Price per item: $", price_per_item)
print("Total amount: $", total)

# Useful number functions
number = -42.7

print("\n=== Number Functions ===")
print("Original number:", number)
print("Absolute value:", abs(number))      # Removes negative sign
print("Rounded value:", round(number))     # Rounds to nearest integer
print("Rounded to 1 decimal:", round(number, 1))

# Finding max and min
a, b, c = 15, 28, 9
print("\n=== Max and Min ===")
print("Numbers:", a, b, c)
print("Maximum:", max(a, b, c))
print("Minimum:", min(a, b, c))
