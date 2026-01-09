"""
Number Problems - Practice Exercises
=====================================
Try to solve these problems yourself before looking at the solutions!
"""

print("=" * 60)
print("PROBLEM 1: Even or Odd")
print("=" * 60)
print("Write a program that checks if a number is even or odd")
print()

# Your code here
# ...

# Solution:
def check_even_odd(number):
    """Check if number is even or odd"""
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"

# Test
print("Solution:")
test_numbers = [5, 10, 13, 20, 7]
for num in test_numbers:
    print(f"{num} is {check_even_odd(num)}")

print("\n" + "=" * 60)
print("PROBLEM 2: Sum of First N Natural Numbers")
print("=" * 60)
print("Calculate the sum of first n natural numbers (1 + 2 + 3 + ... + n)")
print()

# Your code here
# ...

# Solution:
def sum_natural_numbers(n):
    """Calculate sum of first n natural numbers"""
    total = 0
    for i in range(1, n + 1):
        total += i
    return total

# Alternative solution using formula
def sum_natural_formula(n):
    """Using mathematical formula: n * (n + 1) / 2"""
    return n * (n + 1) // 2

# Test
print("Solution:")
for n in [5, 10, 100]:
    print(f"Sum of 1 to {n} = {sum_natural_numbers(n)}")

print("\n" + "=" * 60)
print("PROBLEM 3: Factorial")
print("=" * 60)
print("Calculate factorial of a number (n! = n × (n-1) × ... × 2 × 1)")
print()

# Your code here
# ...

# Solution:
def factorial(n):
    """Calculate factorial of n"""
    if n < 0:
        return None
    if n == 0 or n == 1:
        return 1
    
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

# Test
print("Solution:")
for num in [0, 1, 5, 10]:
    print(f"{num}! = {factorial(num)}")

print("\n" + "=" * 60)
print("PROBLEM 4: Prime Number Checker")
print("=" * 60)
print("Check if a given number is prime")
print()

# Your code here
# ...

# Solution:
def is_prime(n):
    """Check if number is prime"""
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

# Test
print("Solution:")
test_numbers = [2, 4, 17, 20, 29, 30]
for num in test_numbers:
    result = "is" if is_prime(num) else "is not"
    print(f"{num} {result} prime")

print("\n" + "=" * 60)
print("PROBLEM 5: Reverse a Number")
print("=" * 60)
print("Reverse the digits of a number (e.g., 1234 → 4321)")
print()

# Your code here
# ...

# Solution:
def reverse_number(num):
    """Reverse digits of a number"""
    reversed_num = 0
    temp = abs(num)  # Handle negative numbers
    
    while temp > 0:
        digit = temp % 10
        reversed_num = reversed_num * 10 + digit
        temp //= 10
    
    return reversed_num if num >= 0 else -reversed_num

# Test
print("Solution:")
test_numbers = [1234, 9876, 100, 505]
for num in test_numbers:
    print(f"Reverse of {num} is {reverse_number(num)}")

print("\n" + "=" * 60)
print("PROBLEM 6: Sum of Digits")
print("=" * 60)
print("Find the sum of all digits in a number")
print()

# Your code here
# ...

# Solution:
def sum_of_digits(num):
    """Calculate sum of all digits"""
    total = 0
    temp = abs(num)
    
    while temp > 0:
        digit = temp % 10
        total += digit
        temp //= 10
    
    return total

# Test
print("Solution:")
test_numbers = [123, 9876, 505, 1111]
for num in test_numbers:
    print(f"Sum of digits in {num} = {sum_of_digits(num)}")

print("\n" + "=" * 60)
print("PROBLEM 7: Armstrong Number")
print("=" * 60)
print("Check if a number is an Armstrong number")
print("(e.g., 153 = 1³ + 5³ + 3³ = 1 + 125 + 27 = 153)")
print()

# Your code here
# ...

# Solution:
def is_armstrong(num):
    """Check if number is Armstrong number"""
    # Convert to string to count digits
    digits = [int(d) for d in str(num)]
    power = len(digits)
    
    total = sum(d ** power for d in digits)
    return total == num

# Test
print("Solution:")
test_numbers = [153, 370, 371, 407, 123, 9474]
for num in test_numbers:
    result = "is" if is_armstrong(num) else "is not"
    print(f"{num} {result} an Armstrong number")

print("\n" + "=" * 60)
print("PROBLEM 8: Fibonacci Sequence")
print("=" * 60)
print("Generate first n Fibonacci numbers (0, 1, 1, 2, 3, 5, 8, ...)")
print()

# Your code here
# ...

# Solution:
def fibonacci(n):
    """Generate first n Fibonacci numbers"""
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    
    fib = [0, 1]
    for i in range(2, n):
        fib.append(fib[i-1] + fib[i-2])
    return fib

# Test
print("Solution:")
for n in [5, 10]:
    print(f"First {n} Fibonacci numbers: {fibonacci(n)}")

print("\n" + "=" * 60)
print("PROBLEM 9: GCD (Greatest Common Divisor)")
print("=" * 60)
print("Find the GCD of two numbers")
print()

# Your code here
# ...

# Solution:
def gcd(a, b):
    """Calculate GCD using Euclidean algorithm"""
    while b:
        a, b = b, a % b
    return a

# Test
print("Solution:")
pairs = [(48, 18), (100, 50), (17, 19)]
for a, b in pairs:
    print(f"GCD of {a} and {b} = {gcd(a, b)}")

print("\n" + "=" * 60)
print("PROBLEM 10: Leap Year")
print("=" * 60)
print("Check if a year is a leap year")
print("Rules: Divisible by 4, but not by 100 (unless also by 400)")
print()

# Your code here
# ...

# Solution:
def is_leap_year(year):
    """Check if year is a leap year"""
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    return False

# Test
print("Solution:")
test_years = [2000, 2004, 2100, 2024, 1900]
for year in test_years:
    result = "is" if is_leap_year(year) else "is not"
    print(f"{year} {result} a leap year")

print("\n" + "=" * 60)
print("BONUS: Perfect Number")
print("=" * 60)
print("A perfect number equals the sum of its divisors (excluding itself)")
print("Example: 6 = 1 + 2 + 3")
print()

# Solution:
def is_perfect(n):
    """Check if number is perfect"""
    if n < 2:
        return False
    
    divisors_sum = 1  # 1 is always a divisor
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            divisors_sum += i
            if i != n // i:  # Add the other divisor
                divisors_sum += n // i
    
    return divisors_sum == n

# Test
print("Solution:")
test_numbers = [6, 28, 12, 496]
for num in test_numbers:
    result = "is" if is_perfect(num) else "is not"
    print(f"{num} {result} a perfect number")
