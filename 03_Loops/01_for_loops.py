"""
FOR LOOPS IN PYTHON
===================

A for loop is used to iterate over a sequence (like a list, string, or range).
It repeats a block of code for each item in the sequence.

Basic Structure:
    for variable in sequence:
        # code to repeat
"""

# ============================================
# BASIC FOR LOOP WITH RANGE
# ============================================

print("=" * 50)
print("BASIC FOR LOOP")
print("=" * 50 + "\n")

# Print numbers from 1 to 5
print("Numbers from 1 to 5:")
for i in range(1, 6):  # range(start, stop) - stop is not included
    print(i)

print()

# Print numbers from 0 to 4
print("Numbers from 0 to 4:")
for i in range(5):  # range(stop) starts from 0
    print(i)


# ============================================
# FOR LOOP WITH STEP
# ============================================

print("\n" + "=" * 50)
print("FOR LOOP WITH STEP")
print("=" * 50 + "\n")

# Print even numbers from 2 to 10
print("Even numbers from 2 to 10:")
for i in range(2, 11, 2):  # range(start, stop, step)
    print(i)

print()

# Count down from 10 to 1
print("Countdown from 10 to 1:")
for i in range(10, 0, -1):  # negative step for counting down
    print(i)
print("Blast off! 🚀")


# ============================================
# FOR LOOP WITH LISTS
# ============================================

print("\n" + "=" * 50)
print("FOR LOOP WITH LISTS")
print("=" * 50 + "\n")

# Loop through a list of fruits
fruits = ["apple", "banana", "orange", "mango", "grape"]

print("My favorite fruits:")
for fruit in fruits:
    print(f"- {fruit}")

print()

# Loop through a list of numbers
scores = [85, 92, 78, 90, 88]

print("Student scores:")
for score in scores:
    print(f"Score: {score}")


# ============================================
# FOR LOOP WITH STRINGS
# ============================================

print("\n" + "=" * 50)
print("FOR LOOP WITH STRINGS")
print("=" * 50 + "\n")

# Loop through each character in a string
word = "Python"

print(f"Letters in '{word}':")
for letter in word:
    print(letter)


# ============================================
# FOR LOOP WITH CALCULATIONS
# ============================================

print("\n" + "=" * 50)
print("CALCULATIONS WITH FOR LOOPS")
print("=" * 50 + "\n")

# Sum of numbers from 1 to 10
total = 0
for i in range(1, 11):
    total += i  # Add each number to total
print(f"Sum of numbers from 1 to 10: {total}")

print()

# Calculate factorial
number = 5
factorial = 1
for i in range(1, number + 1):
    factorial *= i
print(f"Factorial of {number}: {factorial}")

print()

# Calculate average of scores
scores = [85, 90, 78, 92, 88]
total = 0
for score in scores:
    total += score
average = total / len(scores)
print(f"Scores: {scores}")
print(f"Average score: {average}")


# ============================================
# NESTED FOR LOOPS
# ============================================

print("\n" + "=" * 50)
print("NESTED FOR LOOPS")
print("=" * 50 + "\n")

# Print a pattern
print("Pattern 1:")
for i in range(1, 6):
    for j in range(i):
        print("*", end=" ")
    print()  # New line after each row

print()

# Multiplication table
print("Multiplication Table (1-5):")
for i in range(1, 6):
    for j in range(1, 6):
        print(f"{i}×{j}={i*j:2d}", end="  ")
    print()  # New line after each row


# ============================================
# FOR LOOP WITH ENUMERATE
# ============================================

print("\n" + "=" * 50)
print("FOR LOOP WITH ENUMERATE")
print("=" * 50 + "\n")

# enumerate gives you both index and value
subjects = ["Math", "Science", "English", "History"]

print("My subjects:")
for index, subject in enumerate(subjects, start=1):
    print(f"{index}. {subject}")


# ============================================
# PRACTICAL PROGRAMS
# ============================================

print("\n" + "=" * 50)
print("PROGRAM 1: GRADE CALCULATOR")
print("=" * 50 + "\n")

students = ["Alice", "Bob", "Charlie", "Diana", "Eve"]
marks = [85, 92, 78, 88, 95]

print("STUDENT REPORT CARD")
print("-" * 50)

for i in range(len(students)):
    name = students[i]
    mark = marks[i]
    
    if mark >= 90:
        grade = "A+"
    elif mark >= 80:
        grade = "A"
    elif mark >= 70:
        grade = "B"
    else:
        grade = "C"
    
    print(f"{name:12} | Marks: {mark:3d} | Grade: {grade}")


print("\n" + "=" * 50)
print("PROGRAM 2: FIND MAXIMUM AND MINIMUM")
print("=" * 50 + "\n")

numbers = [45, 78, 23, 91, 34, 67, 89]

print(f"Numbers: {numbers}")

# Find maximum
maximum = numbers[0]
for num in numbers:
    if num > maximum:
        maximum = num

# Find minimum
minimum = numbers[0]
for num in numbers:
    if num < minimum:
        minimum = num

print(f"Maximum: {maximum}")
print(f"Minimum: {minimum}")


print("\n" + "=" * 50)
print("PROGRAM 3: SIMPLE MENU SYSTEM")
print("=" * 50 + "\n")

menu_items = ["Pizza", "Burger", "Pasta", "Salad", "Ice Cream"]
prices = [12.99, 8.99, 10.99, 6.99, 4.99]

print("RESTAURANT MENU")
print("-" * 50)

for i in range(len(menu_items)):
    print(f"{i+1}. {menu_items[i]:15} ${prices[i]:.2f}")


print("\n" + "=" * 50)
print("PROGRAM 4: COUNT VOWELS")
print("=" * 50 + "\n")

sentence = "Python is amazing"
vowels = "aeiouAEIOU"
vowel_count = 0

print(f"Sentence: {sentence}")

for char in sentence:
    if char in vowels:
        vowel_count += 1

print(f"Number of vowels: {vowel_count}")


print("\n" + "=" * 50)
print("PROGRAM 5: MULTIPLICATION TABLE")
print("=" * 50 + "\n")

number = 7

print(f"Multiplication Table of {number}")
print("-" * 30)

for i in range(1, 11):
    result = number * i
    print(f"{number} × {i:2d} = {result:3d}")


# ============================================
# PRACTICE PROBLEMS
# ============================================

print("\n" + "=" * 50)
print("PRACTICE PROBLEMS")
print("=" * 50)

"""
Try these exercises:

1. Write a program that prints all even numbers from 1 to 50.

2. Create a program that finds the sum of all odd numbers from 1 to 100.

3. Write a program that reverses a string using a for loop.
   Example: "hello" should become "olleh"

4. Create a program that counts how many times each vowel appears in a sentence.

5. Write a program that prints the Fibonacci sequence up to 10 terms.
   (0, 1, 1, 2, 3, 5, 8, 13, 21, 34...)

6. Create a program that checks if a number is prime using a for loop.

7. Write a program that creates a list of squares of numbers from 1 to 10.

8. Create a program that finds all numbers divisible by 3 and 5 between 1 and 100.

9. Write a program that prints the following pattern:
   1
   1 2
   1 2 3
   1 2 3 4
   1 2 3 4 5

10. Create a program that calculates compound interest for different years:
    Principal = $1000, Rate = 5%, Years = 1 to 10
"""

print("\nTry solving the practice problems above!")
print("The more you practice loops, the better you'll become!")
