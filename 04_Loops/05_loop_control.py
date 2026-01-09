"""
Loop Control Statements in Python
==================================
This program demonstrates break, continue, and pass statements.
"""

# break statement - exits the loop immediately
print("=== BREAK Statement ===")
print("Finding first number divisible by 7:")
for num in range(1, 20):
    if num % 7 == 0:
        print(f"Found: {num}")
        break  # Exit loop when found
    print(f"Checking: {num}")

# break in while loop
print("\n=== BREAK in While Loop ===")
count = 0
while True:  # Infinite loop
    count += 1
    print(f"Count: {count}")
    if count >= 5:
        print("Limit reached!")
        break  # Exit the infinite loop

# Search in a list
print("\n=== Searching in a List ===")
names = ["Alice", "Bob", "Charlie", "Diana", "Eve"]
search_name = "Charlie"

for name in names:
    if name == search_name:
        print(f"Found '{search_name}'!")
        break
else:
    # This runs only if break was NOT called
    print(f"'{search_name}' not found")

# continue statement - skips current iteration
print("\n=== CONTINUE Statement ===")
print("Printing odd numbers (1-10):")
for num in range(1, 11):
    if num % 2 == 0:
        continue  # Skip even numbers
    print(num, end=" ")
print()

# Skip specific values
print("\n=== Skipping Specific Values ===")
for i in range(1, 11):
    if i == 5:
        continue  # Skip 5
    print(i, end=" ")
print()

# Filtering with continue
print("\n=== Filtering Positive Numbers ===")
numbers = [12, -5, 8, -3, 15, -7, 20]
print(f"Original list: {numbers}")
print("Positive numbers:", end=" ")
for num in numbers:
    if num < 0:
        continue  # Skip negative numbers
    print(num, end=" ")
print()

# pass statement - does nothing (placeholder)
print("\n=== PASS Statement ===")
for i in range(5):
    if i == 2:
        pass  # Placeholder - do nothing special
    print(f"Number: {i}")

# Using pass in functions (placeholder for future code)
print("\n=== Pass in Function Definition ===")
def future_feature():
    pass  # Will implement later

future_feature()
print("Function with pass executed (did nothing)")

# Pass in exception handling
print("\n=== Pass in Exception Handling ===")
numbers = [1, 2, 0, 4, 5]
for num in numbers:
    try:
        result = 10 / num
        print(f"10 / {num} = {result}")
    except ZeroDivisionError:
        pass  # Ignore division by zero

# break with nested loops
print("\n=== Break in Nested Loops ===")
print("Finding first pair that multiplies to 20:")
found = False
for i in range(1, 10):
    for j in range(1, 10):
        if i * j == 20:
            print(f"Found: {i} × {j} = 20")
            found = True
            break
    if found:
        break  # Break outer loop too

# continue in nested loops
print("\n=== Continue in Nested Loops ===")
print("Multiplication table skipping multiples of 5:")
for i in range(1, 6):
    for j in range(1, 6):
        product = i * j
        if product % 5 == 0:
            continue  # Skip multiples of 5
        print(f"{i}×{j}={product}", end="  ")
    print()

# for-else and while-else
print("\n=== for-else Statement ===")
numbers = [2, 4, 6, 8, 10]
for num in numbers:
    if num % 2 != 0:
        print(f"Found odd number: {num}")
        break
else:
    # Executes only if loop completed without break
    print("All numbers are even!")

# while-else example
print("\n=== while-else Statement ===")
count = 0
while count < 5:
    print(count, end=" ")
    count += 1
else:
    # Executes when while condition becomes False
    print("\nLoop completed normally!")

# Practical: Password validator
print("\n=== Password Validator ===")
passwords = ["pass", "python123", "short", "validpass"]
min_length = 8

for password in passwords:
    if len(password) < min_length:
        print(f"'{password}' - Too short, skipped")
        continue
    if "admin" in password:
        print(f"'{password}' - Contains 'admin', rejected")
        break
    print(f"'{password}' - Valid!")

# Filtering and processing
print("\n=== Processing Scores ===")
scores = [45, 78, 92, 34, 88, 55, 67]
print(f"Original scores: {scores}")
print("\nProcessing:")
for score in scores:
    if score < 50:
        print(f"  {score} - Failed (skipping)")
        continue
    if score >= 90:
        print(f"  {score} - Excellent!")
    elif score >= 70:
        print(f"  {score} - Good")
    else:
        print(f"  {score} - Pass")

# Menu with break
print("\n=== Menu System (Simulated) ===")
menu_choices = [1, 2, 4, 3]  # Simulated inputs

for choice in menu_choices:
    print(f"\n--- Menu ---")
    print("1. View Profile")
    print("2. Edit Profile")
    print("3. Exit")
    print(f"Choice: {choice}")
    
    if choice == 1:
        print("Viewing profile...")
    elif choice == 2:
        print("Editing profile...")
    elif choice == 3:
        print("Exiting...")
        break
    else:
        print("Invalid choice, try again")
        continue

# Skip printing specific characters
print("\n=== Skipping Vowels ===")
text = "Hello World"
print(f"Original: {text}")
print("Without vowels: ", end="")
for char in text:
    if char.lower() in 'aeiou':
        continue
    print(char, end="")
print()

# Finding and stopping
print("\n=== Finding Negative Number ===")
numbers = [10, 20, -5, 30, 40]
for i, num in enumerate(numbers):
    if num < 0:
        print(f"First negative number at index {i}: {num}")
        break
else:
    print("No negative numbers found")
