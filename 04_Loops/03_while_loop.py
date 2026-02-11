"""
While Loop in Python
====================
This program demonstrates how to use while loops.
While loops continue until a condition becomes False.
"""

# Basic while loop
print("=== Basic While Loop ===")
count = 0
while count < 5:
    print(f"Count: {count}")
    count += 1

# Counting from 1 to 10
print("\n=== Counting 1 to 10 ===")
num = 1
while num <= 10:
    print(num, end=" ")
    num += 1
print()

# Countdown
print("\n=== Countdown from 5 ===")
countdown = 5
while countdown > 0:
    print(countdown)
    countdown -= 1
print("Blast off! 🚀")

# Sum of numbers until condition
print("\n=== Sum Until 100 ===")
total = 0
num = 1
while total < 100:
    total += num
    num += 1
print(f"Sum reached: {total}")
print(f"Last number added: {num - 1}")

# User input validation (simulated)
print("\n=== Password Attempt (Simulated) ===")
correct_password = "python123"
attempts = 0
max_attempts = 3

# Simulated user inputs
test_inputs = ["wrong1", "wrong2", "python123"]

while attempts < max_attempts:
    user_input = test_inputs[attempts] if attempts < len(test_inputs) else "wrong"
    print(f"Attempt {attempts + 1}: Trying password '{user_input}'")
    
    if user_input == correct_password:
        print("Access granted! ✓")
        break
    else:
        attempts += 1
        if attempts < max_attempts:
            print(f"Wrong password. {max_attempts - attempts} attempts remaining.")
        else:
            print("Access denied! Too many attempts.")

# While loop with condition
print("\n=== Doubling Until Limit ===")
number = 1
while number < 1000:
    print(number, end=" ")
    number *= 2
print()

# Menu-driven program (simulated)
print("\n=== Simple Menu (Simulated) ===")
running = True
iteration = 0
simulated_choices = [1, 2, 3]  # Simulated user choices

while running and iteration < len(simulated_choices):
    choice = simulated_choices[iteration]
    print(f"\n--- Menu ---")
    print("1. Say Hello")
    print("2. Show Date")
    print("3. Exit")
    print(f"Choice: {choice}")
    
    if choice == 1:
        print("Hello, User!")
    elif choice == 2:
        print("Today is a great day!")
    elif choice == 3:
        print("Goodbye!")
        running = False
    
    iteration += 1

# Finding first number divisible by 7
print("\n=== First Number Divisible by 7 ===")
num = 50
while num % 7 != 0:
    num += 1
print(f"First number >= 50 divisible by 7: {num}")

# Summing digits
print("\n=== Sum of Digits ===")
number = 12345
original = number
digit_sum = 0

while number > 0:
    digit = number % 10
    digit_sum += digit
    number //= 10

print(f"Number: {original}")
print(f"Sum of digits: {digit_sum}")

# Reverse a number
print("\n=== Reverse a Number ===")
number = 1234
original = number
reversed_num = 0

while number > 0:
    digit = number % 10
    reversed_num = reversed_num * 10 + digit
    number //= 10

print(f"Original: {original}")
print(f"Reversed: {reversed_num}")

# Guessing game (simulated)
print("\n=== Number Guessing Game (Simulated) ===")
secret_number = 7
guesses = [3, 5, 7]  # Simulated guesses
guess_count = 0
found = False

while guess_count < len(guesses) and not found:
    guess = guesses[guess_count]
    guess_count += 1
    print(f"Guess {guess_count}: {guess}")
    
    if guess == secret_number:
        print(f"Correct! You guessed it in {guess_count} attempts!")
        found = True
    elif guess < secret_number:
        print("Too low!")
    else:
        print("Too high!")

# Factorial using while loop
print("\n=== Factorial Using While ===")
num = 6
factorial = 1
temp = num

while temp > 0:
    factorial *= temp
    temp -= 1

print(f"{num}! = {factorial}")

# Fibonacci sequence
print("\n=== Fibonacci Sequence (up to 100) ===")
a, b = 0, 1
print(a, end=" ")
while b <= 100:
    print(b, end=" ")
    a, b = b, a + b
print()

# Collatz sequence
print("\n=== Collatz Sequence (starting from 10) ===")
num = 10
steps = 0
print(num, end=" ")

while num != 1:
    if num % 2 == 0:
        num = num // 2
    else:
        num = 3 * num + 1
    print(num, end=" ")
    steps += 1

print(f"\nReached 1 in {steps} steps")

# Bank balance simulation
print("\n=== Bank Balance Simulation ===")
balance = 1000
monthly_expense = 150
months = 0

print(f"Starting balance: ${balance}")
while balance >= monthly_expense:
    balance -= monthly_expense
    months += 1
    print(f"Month {months}: ${balance}")

print(f"Money lasted {months} months")

# Power of 2 until limit
print("\n=== Powers of 2 (until > 1000) ===")
power = 0
result = 1
while result <= 1000:
    print(f"2^{power} = {result}")
    power += 1
    result = 2 ** power
