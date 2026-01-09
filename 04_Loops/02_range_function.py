"""
Range Function in Python
=========================
This program demonstrates different ways to use the range() function in loops.
"""

# Basic range - starts from 0
print("=== range(5) - Numbers 0 to 4 ===")
for i in range(5):
    print(i, end=" ")
print()

# Range with start and stop
print("\n=== range(1, 6) - Numbers 1 to 5 ===")
for i in range(1, 6):
    print(i, end=" ")
print()

# Range with step
print("\n=== range(0, 10, 2) - Even numbers ===")
for i in range(0, 10, 2):
    print(i, end=" ")
print()

# Odd numbers using range
print("\n=== Odd Numbers (1-20) ===")
for i in range(1, 21, 2):
    print(i, end=" ")
print()

# Counting backwards
print("\n=== Countdown from 10 ===")
for i in range(10, 0, -1):
    print(i, end=" ")
print("\nLiftoff! 🚀")

# Range with negative step
print("\n=== range(20, 0, -2) - Reverse even ===")
for i in range(20, 0, -2):
    print(i, end=" ")
print()

# Converting range to list
print("\n=== Range as List ===")
numbers = list(range(1, 11))
print(f"List: {numbers}")

# Sum of first n natural numbers
print("\n=== Sum of First 10 Natural Numbers ===")
n = 10
total = 0
for i in range(1, n + 1):
    total += i
print(f"Sum of 1 to {n} = {total}")

# Multiplication tables using range
print("\n=== Multiplication Table of 7 ===")
table_num = 7
for i in range(1, 11):
    result = table_num * i
    print(f"{table_num} × {i} = {result}")

# Printing multiples
print("\n=== Multiples of 3 (up to 30) ===")
for num in range(3, 31, 3):
    print(num, end=" ")
print()

# Squares using range
print("\n=== Squares of Numbers 1-10 ===")
for num in range(1, 11):
    print(f"{num}² = {num**2}")

# Powers of 2
print("\n=== Powers of 2 (2⁰ to 2¹⁰) ===")
for power in range(11):
    result = 2 ** power
    print(f"2^{power} = {result}")

# Accessing list elements using range
print("\n=== Accessing List with range ===")
fruits = ["apple", "banana", "orange", "grape", "mango"]
print("Fruits:")
for i in range(len(fruits)):
    print(f"  [{i}] {fruits[i]}")

# Reverse iteration through a list
print("\n=== Reverse List Iteration ===")
for i in range(len(fruits) - 1, -1, -1):
    print(fruits[i])

# Skipping elements
print("\n=== Every Third Element ===")
numbers = list(range(1, 21))
print(f"Original: {numbers}")
print("Every 3rd element:", end=" ")
for i in range(0, len(numbers), 3):
    print(numbers[i], end=" ")
print()

# Creating a number grid
print("\n=== Number Grid (5×5) ===")
for row in range(1, 6):
    for col in range(1, 6):
        print(f"{row * col:3}", end=" ")
    print()

# Alphabet using range
print("\n=== First 10 Letters of Alphabet ===")
for i in range(ord('A'), ord('A') + 10):
    print(chr(i), end=" ")
print()

# Factorial using range
print("\n=== Factorial of 5 ===")
num = 5
factorial = 1
for i in range(1, num + 1):
    factorial *= i
print(f"{num}! = {factorial}")

# Average of numbers
print("\n=== Average of 1 to 100 ===")
total = 0
count = 0
for num in range(1, 101):
    total += num
    count += 1
average = total / count
print(f"Sum: {total}")
print(f"Count: {count}")
print(f"Average: {average}")

# Nested range example
print("\n=== Nested Range - Right Triangle ===")
for i in range(1, 6):
    for j in range(i):
        print("*", end="")
    print()

# Temperature conversion table
print("\n=== Celsius to Fahrenheit Table ===")
print(f"{'Celsius':>8} {'Fahrenheit':>10}")
print("-" * 20)
for celsius in range(0, 101, 10):
    fahrenheit = (celsius * 9/5) + 32
    print(f"{celsius:>8}°C {fahrenheit:>10.1f}°F")

# Finding divisible numbers
print("\n=== Numbers Divisible by 5 (1-50) ===")
count = 0
for num in range(1, 51):
    if num % 5 == 0:
        print(num, end=" ")
        count += 1
print(f"\nTotal count: {count}")
