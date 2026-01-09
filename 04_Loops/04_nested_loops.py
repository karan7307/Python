"""
Nested Loops in Python
=======================
This program demonstrates loops inside loops (nested loops).
"""

# Basic nested loop
print("=== Basic Nested Loop ===")
for i in range(1, 4):
    for j in range(1, 4):
        print(f"i={i}, j={j}")
    print()

# Multiplication table
print("=== Multiplication Table (1-5) ===")
for i in range(1, 6):
    for j in range(1, 6):
        print(f"{i*j:3}", end=" ")
    print()

# Complete multiplication table
print("\n=== Complete Multiplication Table (1-10) ===")
print("   ", end="")
for i in range(1, 11):
    print(f"{i:4}", end="")
print()
print("   " + "-" * 40)

for i in range(1, 11):
    print(f"{i:2} |", end="")
    for j in range(1, 11):
        print(f"{i*j:4}", end="")
    print()

# Star patterns
print("\n=== Right Triangle Pattern ===")
for i in range(1, 6):
    for j in range(i):
        print("*", end=" ")
    print()

print("\n=== Inverted Right Triangle ===")
for i in range(5, 0, -1):
    for j in range(i):
        print("*", end=" ")
    print()

print("\n=== Pyramid Pattern ===")
n = 5
for i in range(1, n + 1):
    # Print spaces
    for j in range(n - i):
        print(" ", end="")
    # Print stars
    for j in range(2 * i - 1):
        print("*", end="")
    print()

print("\n=== Number Triangle ===")
for i in range(1, 6):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()

print("\n=== Number Pattern ===")
num = 1
for i in range(1, 5):
    for j in range(i):
        print(num, end=" ")
        num += 1
    print()

# Rectangle pattern
print("\n=== Rectangle Pattern (5×8) ===")
rows = 5
cols = 8
for i in range(rows):
    for j in range(cols):
        print("*", end=" ")
    print()

# Hollow rectangle
print("\n=== Hollow Rectangle (5×8) ===")
for i in range(rows):
    for j in range(cols):
        if i == 0 or i == rows - 1 or j == 0 or j == cols - 1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

# Diamond pattern
print("\n=== Diamond Pattern ===")
n = 5
# Upper half
for i in range(1, n + 1):
    for j in range(n - i):
        print(" ", end="")
    for j in range(2 * i - 1):
        print("*", end="")
    print()
# Lower half
for i in range(n - 1, 0, -1):
    for j in range(n - i):
        print(" ", end="")
    for j in range(2 * i - 1):
        print("*", end="")
    print()

# Nested loop with lists
print("\n=== Nested Lists Iteration ===")
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print("Matrix:")
for row in matrix:
    for element in row:
        print(f"{element:3}", end=" ")
    print()

# Sum of all elements in matrix
total = 0
for row in matrix:
    for element in row:
        total += element
print(f"Sum of all elements: {total}")

# Chess board pattern
print("\n=== Chess Board Pattern (8×8) ===")
for i in range(8):
    for j in range(8):
        if (i + j) % 2 == 0:
            print("■", end=" ")
        else:
            print("□", end=" ")
    print()

# Times table chart
print("\n=== Times Table Chart ===")
for num in range(1, 4):
    print(f"\nTable of {num}:")
    for i in range(1, 6):
        print(f"{num} × {i} = {num * i}")

# Finding all pairs
print("\n=== All Pairs from Two Lists ===")
list1 = [1, 2, 3]
list2 = ['A', 'B', 'C']

for num in list1:
    for char in list2:
        print(f"({num}, {char})", end=" ")
print()

# Matrix addition
print("\n=== Matrix Addition ===")
matrix1 = [[1, 2, 3], [4, 5, 6]]
matrix2 = [[7, 8, 9], [10, 11, 12]]
result = []

print("Matrix 1:")
for row in matrix1:
    print(row)

print("\nMatrix 2:")
for row in matrix2:
    print(row)

print("\nSum:")
for i in range(len(matrix1)):
    row_result = []
    for j in range(len(matrix1[0])):
        row_result.append(matrix1[i][j] + matrix2[i][j])
    result.append(row_result)
    print(row_result)

# Coordinate system
print("\n=== Coordinate Grid (5×5) ===")
for y in range(5, 0, -1):
    for x in range(1, 6):
        print(f"({x},{y})", end=" ")
    print()

# Nested while loops
print("\n=== Nested While Loops ===")
i = 1
while i <= 3:
    j = 1
    while j <= 3:
        print(f"{i}×{j}={i*j}", end="  ")
        j += 1
    print()
    i += 1

# Prime numbers up to n
print("\n=== Prime Numbers (2-30) ===")
for num in range(2, 31):
    is_prime = True
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        print(num, end=" ")
print()
