"""
Practical Loop Examples
========================
This program contains real-world applications of loops.
"""

# Example 1: Grade Calculator for Multiple Students
print("=== GRADE CALCULATOR ===")
students = [
    {"name": "Alice", "marks": 85},
    {"name": "Bob", "marks": 92},
    {"name": "Charlie", "marks": 78},
    {"name": "Diana", "marks": 65},
    {"name": "Eve", "marks": 45}
]

print(f"{'Name':<12} {'Marks':<8} {'Grade':<8} {'Status'}")
print("-" * 40)

for student in students:
    marks = student["marks"]
    
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
    
    status = "Pass" if marks >= 50 else "Fail"
    print(f"{student['name']:<12} {marks:<8} {grade:<8} {status}")

# Example 2: Shopping Cart Total
print("\n=== SHOPPING CART ===")
cart = [
    {"item": "Laptop", "price": 899.99, "quantity": 1},
    {"item": "Mouse", "price": 25.50, "quantity": 2},
    {"item": "Keyboard", "price": 75.00, "quantity": 1},
    {"item": "USB Cable", "price": 10.99, "quantity": 3}
]

print(f"{'Item':<15} {'Price':<10} {'Qty':<5} {'Total'}")
print("-" * 40)

subtotal = 0
for item in cart:
    item_total = item["price"] * item["quantity"]
    subtotal += item_total
    print(f"{item['item']:<15} ${item['price']:<9.2f} {item['quantity']:<5} ${item_total:.2f}")

tax = subtotal * 0.08  # 8% tax
total = subtotal + tax

print("-" * 40)
print(f"{'Subtotal:':<30} ${subtotal:.2f}")
print(f"{'Tax (8%):':<30} ${tax:.2f}")
print(f"{'Total:':<30} ${total:.2f}")

# Example 3: Attendance Tracker
print("\n=== ATTENDANCE TRACKER ===")
attendance = {
    "Monday": True,
    "Tuesday": True,
    "Wednesday": False,
    "Thursday": True,
    "Friday": False
}

present_days = 0
total_days = 0

for day, status in attendance.items():
    total_days += 1
    if status:
        present_days += 1
        print(f"{day:<10} - Present ✓")
    else:
        print(f"{day:<10} - Absent ✗")

percentage = (present_days / total_days) * 100
print(f"\nAttendance: {present_days}/{total_days} days ({percentage:.1f}%)")

if percentage >= 75:
    print("Status: Good attendance! ✓")
else:
    print("Status: Low attendance! ✗")

# Example 4: Password Generator
print("\n=== SIMPLE PASSWORD GENERATOR ===")
import random
random.seed(42)  # For consistent output

lowercase = "abcdefghijklmnopqrstuvwxyz"
uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
digits = "0123456789"
symbols = "!@#$%^&*"

all_chars = lowercase + uppercase + digits + symbols
password_length = 12

password = ""
for i in range(password_length):
    password += random.choice(all_chars)

print(f"Generated password: {password}")

# Example 5: Prime Number Finder
print("\n=== PRIME NUMBERS (2-50) ===")
primes = []

for num in range(2, 51):
    is_prime = True
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        primes.append(num)

print("Prime numbers:", primes)
print(f"Count: {len(primes)}")

# Example 6: Word Frequency Counter
print("\n=== WORD FREQUENCY COUNTER ===")
text = "python is great and python is powerful python is easy"
words = text.split()
word_count = {}

for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

print("Word frequencies:")
for word, count in word_count.items():
    print(f"  '{word}': {count}")

# Example 7: Fibonacci Sequence Generator
print("\n=== FIBONACCI SEQUENCE (first 15 terms) ===")
n = 15
fib = [0, 1]

for i in range(2, n):
    next_num = fib[i-1] + fib[i-2]
    fib.append(next_num)

print("Fibonacci sequence:")
for i, num in enumerate(fib):
    print(f"F({i}) = {num}")

# Example 8: Temperature Converter
print("\n=== TEMPERATURE CONVERSION TABLE ===")
print(f"{'Celsius':>8} {'Fahrenheit':>12} {'Kelvin':>10}")
print("-" * 32)

for celsius in range(0, 101, 10):
    fahrenheit = (celsius * 9/5) + 32
    kelvin = celsius + 273.15
    print(f"{celsius:>8}°C {fahrenheit:>11.1f}°F {kelvin:>9.2f}K")

# Example 9: Pattern Matcher
print("\n=== EMAIL VALIDATOR ===")
emails = [
    "user@example.com",
    "invalid.email",
    "test@domain.org",
    "no-at-sign.com",
    "valid@test.co"
]

valid_count = 0
for email in emails:
    if "@" in email and "." in email.split("@")[1]:
        print(f"✓ {email} - Valid")
        valid_count += 1
    else:
        print(f"✗ {email} - Invalid")

print(f"\nValid emails: {valid_count}/{len(emails)}")

# Example 10: Sum and Average Calculator
print("\n=== STATISTICS CALCULATOR ===")
numbers = [45, 67, 23, 89, 12, 56, 78, 34, 91, 25]

total_sum = 0
count = 0
maximum = numbers[0]
minimum = numbers[0]

for num in numbers:
    total_sum += num
    count += 1
    if num > maximum:
        maximum = num
    if num < minimum:
        minimum = num

average = total_sum / count

print(f"Numbers: {numbers}")
print(f"Count: {count}")
print(f"Sum: {total_sum}")
print(f"Average: {average:.2f}")
print(f"Maximum: {maximum}")
print(f"Minimum: {minimum}")
print(f"Range: {maximum - minimum}")

# Example 11: Character Counter
print("\n=== CHARACTER STATISTICS ===")
text = "Hello, Python World!"
vowels = "aeiouAEIOU"
consonants = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"

vowel_count = 0
consonant_count = 0
digit_count = 0
space_count = 0
special_count = 0

for char in text:
    if char in vowels:
        vowel_count += 1
    elif char in consonants:
        consonant_count += 1
    elif char.isdigit():
        digit_count += 1
    elif char.isspace():
        space_count += 1
    else:
        special_count += 1

print(f"Text: '{text}'")
print(f"Vowels: {vowel_count}")
print(f"Consonants: {consonant_count}")
print(f"Digits: {digit_count}")
print(f"Spaces: {space_count}")
print(f"Special characters: {special_count}")
print(f"Total characters: {len(text)}")

# Example 12: Simple Progress Bar
print("\n=== PROGRESS BAR SIMULATION ===")
total_tasks = 20
for i in range(total_tasks + 1):
    percentage = (i / total_tasks) * 100
    filled = int(percentage / 5)
    bar = "█" * filled + "-" * (20 - filled)
    print(f"\rProgress: [{bar}] {percentage:.0f}%", end="")
    if i < total_tasks:
        import time
        time.sleep(0.05)  # Small delay for visualization
print("\nComplete!")
