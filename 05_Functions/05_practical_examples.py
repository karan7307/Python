"""
Practical Function Examples
============================
This program contains real-world applications of functions.
"""

# Example 1: Temperature Converter
print("=== TEMPERATURE CONVERTER ===")
def celsius_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit"""
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    """Convert Fahrenheit to Celsius"""
    return (fahrenheit - 32) * 5/9

def celsius_to_kelvin(celsius):
    """Convert Celsius to Kelvin"""
    return celsius + 273.15

temp_c = 25
print(f"{temp_c}°C = {celsius_to_fahrenheit(temp_c):.1f}°F")
print(f"{temp_c}°C = {celsius_to_kelvin(temp_c):.2f}K")

# Example 2: Password Validator
print("\n=== PASSWORD VALIDATOR ===")
def validate_password(password):
    """Validate password strength"""
    if len(password) < 8:
        return False, "Password must be at least 8 characters"
    if not any(c.isupper() for c in password):
        return False, "Password must contain uppercase letter"
    if not any(c.islower() for c in password):
        return False, "Password must contain lowercase letter"
    if not any(c.isdigit() for c in password):
        return False, "Password must contain a number"
    return True, "Password is strong"

test_passwords = ["weak", "NoNumbers", "nonumbers1", "GoodPass123"]
for pwd in test_passwords:
    valid, message = validate_password(pwd)
    status = "✓" if valid else "✗"
    print(f"{status} '{pwd}': {message}")

# Example 3: Grade Calculator
print("\n=== GRADE CALCULATOR ===")
def calculate_grade(scores):
    """Calculate average and letter grade"""
    if not scores:
        return None, "N/A"
    
    average = sum(scores) / len(scores)
    
    if average >= 90:
        letter = "A"
    elif average >= 80:
        letter = "B"
    elif average >= 70:
        letter = "C"
    elif average >= 60:
        letter = "D"
    else:
        letter = "F"
    
    return average, letter

students = [
    ("Alice", [85, 90, 88, 92]),
    ("Bob", [78, 82, 75, 80]),
    ("Charlie", [92, 95, 98, 94])
]

print(f"{'Name':<10} {'Average':<10} {'Grade'}")
print("-" * 30)
for name, scores in students:
    avg, grade = calculate_grade(scores)
    print(f"{name:<10} {avg:<10.2f} {grade}")

# Example 4: Factorial Calculator
print("\n=== FACTORIAL CALCULATOR ===")
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

for num in [0, 1, 5, 10]:
    print(f"{num}! = {factorial(num)}")

# Example 5: Palindrome Checker
print("\n=== PALINDROME CHECKER ===")
def is_palindrome(text):
    """Check if text is a palindrome"""
    # Remove spaces and convert to lowercase
    cleaned = text.replace(" ", "").lower()
    return cleaned == cleaned[::-1]

words = ["racecar", "hello", "level", "python", "A man a plan a canal Panama"]
for word in words:
    result = "is" if is_palindrome(word) else "is not"
    print(f"'{word}' {result} a palindrome")

# Example 6: Prime Number Checker
print("\n=== PRIME NUMBER CHECKER ===")
def is_prime(n):
    """Check if number is prime"""
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def get_primes(start, end):
    """Get all prime numbers in range"""
    primes = []
    for num in range(start, end + 1):
        if is_prime(num):
            primes.append(num)
    return primes

primes = get_primes(1, 30)
print(f"Prime numbers (1-30): {primes}")

# Example 7: Shopping Cart
print("\n=== SHOPPING CART ===")
def calculate_total(items, tax_rate=0.08):
    """Calculate total with tax"""
    subtotal = sum(item['price'] * item['quantity'] for item in items)
    tax = subtotal * tax_rate
    total = subtotal + tax
    return subtotal, tax, total

cart = [
    {"name": "Book", "price": 15.99, "quantity": 2},
    {"name": "Pen", "price": 2.50, "quantity": 5},
    {"name": "Notebook", "price": 5.99, "quantity": 3}
]

subtotal, tax, total = calculate_total(cart)
print(f"Subtotal: ${subtotal:.2f}")
print(f"Tax (8%): ${tax:.2f}")
print(f"Total: ${total:.2f}")

# Example 8: List Statistics
print("\n=== LIST STATISTICS ===")
def get_statistics(numbers):
    """Calculate various statistics"""
    if not numbers:
        return None
    
    return {
        "count": len(numbers),
        "sum": sum(numbers),
        "average": sum(numbers) / len(numbers),
        "min": min(numbers),
        "max": max(numbers),
        "range": max(numbers) - min(numbers)
    }

data = [45, 67, 23, 89, 12, 56, 78]
stats = get_statistics(data)
print(f"Data: {data}")
for key, value in stats.items():
    if isinstance(value, float):
        print(f"{key.capitalize()}: {value:.2f}")
    else:
        print(f"{key.capitalize()}: {value}")

# Example 9: String Formatter
print("\n=== STRING FORMATTER ===")
def format_name(first, last, middle=None, title=None):
    """Format a person's name"""
    parts = []
    if title:
        parts.append(title)
    parts.append(first)
    if middle:
        parts.append(middle)
    parts.append(last)
    return " ".join(parts)

print(format_name("John", "Doe"))
print(format_name("John", "Doe", middle="Paul"))
print(format_name("John", "Doe", title="Dr."))
print(format_name("John", "Doe", middle="Paul", title="Prof."))

# Example 10: Fibonacci Generator
print("\n=== FIBONACCI SEQUENCE ===")
def generate_fibonacci(n):
    """Generate first n Fibonacci numbers"""
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    
    fib = [0, 1]
    for i in range(2, n):
        fib.append(fib[i-1] + fib[i-2])
    return fib

fib_sequence = generate_fibonacci(10)
print(f"First 10 Fibonacci numbers: {fib_sequence}")

# Example 11: Email Validator
print("\n=== EMAIL VALIDATOR ===")
def is_valid_email(email):
    """Basic email validation"""
    if "@" not in email:
        return False, "Missing @ symbol"
    
    parts = email.split("@")
    if len(parts) != 2:
        return False, "Invalid format"
    
    username, domain = parts
    if not username or not domain:
        return False, "Empty username or domain"
    
    if "." not in domain:
        return False, "Domain needs a period"
    
    return True, "Valid email"

emails = [
    "user@example.com",
    "invalid.email",
    "test@domain.co",
    "@nodomain.com",
    "noatsign.com"
]

for email in emails:
    valid, message = is_valid_email(email)
    status = "✓" if valid else "✗"
    print(f"{status} {email}: {message}")

# Example 12: Word Counter
print("\n=== WORD COUNTER ===")
def count_words(text):
    """Count word frequency"""
    words = text.lower().split()
    word_count = {}
    
    for word in words:
        # Remove punctuation
        word = word.strip(".,!?;:")
        if word:
            word_count[word] = word_count.get(word, 0) + 1
    
    return word_count

text = "Python is great. Python is powerful. I love Python!"
word_freq = count_words(text)
print(f"Text: '{text}'")
print("Word frequencies:")
for word, count in sorted(word_freq.items()):
    print(f"  {word}: {count}")

# Example 13: Distance Calculator
print("\n=== DISTANCE CALCULATOR ===")
def calculate_distance(x1, y1, x2, y2):
    """Calculate Euclidean distance between two points"""
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

point1 = (0, 0)
point2 = (3, 4)
distance = calculate_distance(*point1, *point2)
print(f"Distance between {point1} and {point2}: {distance:.2f}")
