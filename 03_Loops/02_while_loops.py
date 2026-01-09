"""
WHILE LOOPS IN PYTHON
=====================

A while loop repeats a block of code as long as a condition is True.
It's useful when you don't know in advance how many times to loop.

Basic Structure:
    while condition:
        # code to repeat
        # update condition to eventually become False
"""

# ============================================
# BASIC WHILE LOOP
# ============================================

print("=" * 50)
print("BASIC WHILE LOOP")
print("=" * 50 + "\n")

# Count from 1 to 5
count = 1
print("Counting from 1 to 5:")
while count <= 5:
    print(count)
    count += 1  # Important: update the variable!

print()

# Count down from 5 to 1
count = 5
print("Counting down from 5 to 1:")
while count > 0:
    print(count)
    count -= 1
print("Done!")


# ============================================
# WHILE LOOP WITH USER INPUT
# ============================================

print("\n" + "=" * 50)
print("WHILE LOOP WITH INPUT VALIDATION")
print("=" * 50 + "\n")

# Keep asking until valid input (simulated)
attempts = 0
max_attempts = 3
password = ""

print("Password must be at least 6 characters")
while attempts < max_attempts and len(password) < 6:
    password = "abc"  # Simulated input
    attempts += 1
    
    if len(password) < 6:
        print(f"Attempt {attempts}: Password too short! Try again.")
    else:
        print(f"Attempt {attempts}: Password accepted!")
        break

if len(password) < 6:
    print("Maximum attempts reached!")


# ============================================
# WHILE LOOP WITH CALCULATIONS
# ============================================

print("\n" + "=" * 50)
print("CALCULATIONS WITH WHILE LOOPS")
print("=" * 50 + "\n")

# Sum of numbers from 1 to 10
number = 1
total = 0

while number <= 10:
    total += number
    number += 1

print(f"Sum of numbers from 1 to 10: {total}")

print()

# Calculate factorial using while loop
n = 5
factorial = 1
i = 1

while i <= n:
    factorial *= i
    i += 1

print(f"Factorial of {n}: {factorial}")


# ============================================
# BREAK AND CONTINUE
# ============================================

print("\n" + "=" * 50)
print("BREAK AND CONTINUE STATEMENTS")
print("=" * 50 + "\n")

# BREAK - exits the loop immediately
print("Using BREAK:")
count = 1
while count <= 10:
    if count == 6:
        print("Breaking at 6!")
        break
    print(count)
    count += 1

print()

# CONTINUE - skips current iteration, continues with next
print("Using CONTINUE:")
count = 0
while count < 10:
    count += 1
    if count % 2 == 0:  # Skip even numbers
        continue
    print(count)


# ============================================
# INFINITE LOOP WITH BREAK
# ============================================

print("\n" + "=" * 50)
print("INFINITE LOOP WITH BREAK")
print("=" * 50 + "\n")

# Menu system (simulated)
print("Simple Calculator")
choice = 0

while True:  # Infinite loop
    choice += 1
    
    if choice == 1:
        print(f"Choice {choice}: Addition selected")
    elif choice == 2:
        print(f"Choice {choice}: Subtraction selected")
    elif choice == 3:
        print(f"Choice {choice}: Exit selected")
        print("Thank you for using the calculator!")
        break  # Exit the infinite loop
    
    if choice > 2:  # Safety break for simulation
        break


# ============================================
# NESTED WHILE LOOPS
# ============================================

print("\n" + "=" * 50)
print("NESTED WHILE LOOPS")
print("=" * 50 + "\n")

# Print a pattern
print("Pattern using nested while loops:")
i = 1
while i <= 5:
    j = 1
    while j <= i:
        print("*", end=" ")
        j += 1
    print()
    i += 1


# ============================================
# PRACTICAL PROGRAMS
# ============================================

print("\n" + "=" * 50)
print("PROGRAM 1: NUMBER GUESSING GAME")
print("=" * 50 + "\n")

secret_number = 7
guess = 0
attempts = 0
max_attempts = 5

print(f"Guess the number between 1 and 10!")
print(f"You have {max_attempts} attempts.\n")

while attempts < max_attempts and guess != secret_number:
    attempts += 1
    # Simulated guesses
    if attempts == 1:
        guess = 5
    elif attempts == 2:
        guess = 8
    elif attempts == 3:
        guess = 7
    
    print(f"Attempt {attempts}: Guessed {guess}")
    
    if guess == secret_number:
        print(f"🎉 Congratulations! You guessed it in {attempts} attempts!")
    elif guess < secret_number:
        print("Too low! Try a higher number.")
    else:
        print("Too high! Try a lower number.")

if guess != secret_number:
    print(f"\nGame Over! The secret number was {secret_number}")


print("\n" + "=" * 50)
print("PROGRAM 2: SUM OF DIGITS")
print("=" * 50 + "\n")

number = 12345
sum_digits = 0
temp = number

print(f"Number: {number}")

while temp > 0:
    digit = temp % 10  # Get last digit
    sum_digits += digit
    temp = temp // 10  # Remove last digit

print(f"Sum of digits: {sum_digits}")


print("\n" + "=" * 50)
print("PROGRAM 3: REVERSE A NUMBER")
print("=" * 50 + "\n")

number = 12345
reversed_number = 0
temp = number

while temp > 0:
    digit = temp % 10
    reversed_number = reversed_number * 10 + digit
    temp = temp // 10

print(f"Original number: {number}")
print(f"Reversed number: {reversed_number}")


print("\n" + "=" * 50)
print("PROGRAM 4: COMPOUND INTEREST CALCULATOR")
print("=" * 50 + "\n")

principal = 1000
rate = 5  # 5% per year
years = 0
target = 2000

print(f"Initial amount: ${principal}")
print(f"Interest rate: {rate}%")
print(f"Target amount: ${target}\n")

amount = principal
while amount < target:
    years += 1
    interest = amount * (rate / 100)
    amount += interest
    print(f"Year {years}: ${amount:.2f}")

print(f"\nIt takes {years} years to reach ${target}")


print("\n" + "=" * 50)
print("PROGRAM 5: COUNTDOWN TIMER")
print("=" * 50 + "\n")

seconds = 10
print(f"Countdown from {seconds} seconds:")

while seconds > 0:
    print(f"{seconds}...")
    seconds -= 1

print("Time's up! ⏰")


print("\n" + "=" * 50)
print("PROGRAM 6: FIND GCD (GREATEST COMMON DIVISOR)")
print("=" * 50 + "\n")

# Using Euclidean algorithm
num1 = 48
num2 = 18

print(f"Finding GCD of {num1} and {num2}\n")

a = num1
b = num2

while b != 0:
    temp = b
    b = a % b
    a = temp
    print(f"a = {a}, b = {b}")

print(f"\nGCD of {num1} and {num2} is: {a}")


# ============================================
# FOR vs WHILE - When to Use Which?
# ============================================

print("\n" + "=" * 50)
print("FOR vs WHILE LOOPS")
print("=" * 50 + "\n")

print("Use FOR loop when:")
print("- You know how many times to loop")
print("- You're iterating over a sequence (list, string, range)")
print("- Example: Print numbers 1 to 10")

print("\nUse WHILE loop when:")
print("- You don't know how many times to loop in advance")
print("- You loop until a condition becomes False")
print("- Example: Keep asking for input until valid")


# ============================================
# PRACTICE PROBLEMS
# ============================================

print("\n" + "=" * 50)
print("PRACTICE PROBLEMS")
print("=" * 50)

"""
Try these exercises:

1. Write a program that prints all numbers from 1 to 100 that are divisible by 7.

2. Create a program that finds the sum of all even numbers from 1 to 50.

3. Write a program to check if a number is a palindrome (reads same forwards and backwards).
   Example: 121, 12321 are palindromes

4. Create a program that finds the factorial of a number using a while loop.

5. Write a program that finds all prime numbers between 1 and 50.

6. Create a program that converts a decimal number to binary using a while loop.

7. Write a program that implements a simple ATM system:
   - Display menu (Check Balance, Withdraw, Deposit, Exit)
   - Keep running until user selects Exit
   - Validate withdrawal amount

8. Create a program that finds the nth Fibonacci number using a while loop.

9. Write a program that keeps asking for numbers and calculates their sum.
   Stop when the user enters 0.

10. Create a program that simulates a dice rolling game:
    - Roll until you get a 6
    - Count how many rolls it took
"""

print("\nTry solving the practice problems above!")
print("While loops are powerful for handling uncertain iterations!")
