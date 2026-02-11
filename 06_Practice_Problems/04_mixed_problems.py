"""
Mixed Problems - Combining Multiple Concepts
=============================================
These problems combine concepts from variables, conditions, loops, and functions.
"""

print("=" * 60)
print("PROBLEM 1: Temperature Statistics")
print("=" * 60)
print("Given a list of temperatures, find:")
print("- Average temperature")
print("- Number of days above average")
print("- Hottest and coldest days")
print()

# Solution:
def analyze_temperatures(temps):
    """Analyze temperature data"""
    if not temps:
        return None
    
    avg_temp = sum(temps) / len(temps)
    above_avg = sum(1 for temp in temps if temp > avg_temp)
    hottest = max(temps)
    coldest = min(temps)
    
    return {
        "average": avg_temp,
        "above_average_count": above_avg,
        "hottest": hottest,
        "coldest": coldest
    }

# Test
print("Solution:")
temperatures = [72, 68, 75, 70, 78, 65, 73]
results = analyze_temperatures(temperatures)
print(f"Temperatures: {temperatures}")
print(f"Average: {results['average']:.1f}°F")
print(f"Days above average: {results['above_average_count']}")
print(f"Hottest: {results['hottest']}°F")
print(f"Coldest: {results['coldest']}°F")

print("\n" + "=" * 60)
print("PROBLEM 2: Student Grade System")
print("=" * 60)
print("Calculate grades for multiple students and class statistics")
print()

# Solution:
def process_student_grades(students):
    """Process student grades"""
    results = []
    
    for name, scores in students:
        avg = sum(scores) / len(scores)
        
        if avg >= 90:
            grade = "A"
        elif avg >= 80:
            grade = "B"
        elif avg >= 70:
            grade = "C"
        elif avg >= 60:
            grade = "D"
        else:
            grade = "F"
        
        results.append({
            "name": name,
            "average": avg,
            "grade": grade,
            "status": "Pass" if avg >= 60 else "Fail"
        })
    
    return results

# Test
print("Solution:")
students = [
    ("Alice", [85, 90, 88]),
    ("Bob", [78, 82, 75]),
    ("Charlie", [92, 95, 98]),
    ("Diana", [55, 60, 58])
]

results = process_student_grades(students)
print(f"{'Name':<10} {'Average':<10} {'Grade':<8} {'Status'}")
print("-" * 40)
for student in results:
    print(f"{student['name']:<10} {student['average']:<10.2f} {student['grade']:<8} {student['status']}")

print("\n" + "=" * 60)
print("PROBLEM 3: Shopping Cart Calculator")
print("=" * 60)
print("Calculate total cost with discounts and tax")
print()

# Solution:
def calculate_shopping_cart(items, tax_rate=0.08, discount_threshold=100):
    """Calculate shopping cart total"""
    subtotal = sum(item["price"] * item["quantity"] for item in items)
    
    # Apply discount if subtotal exceeds threshold
    if subtotal >= discount_threshold:
        discount = subtotal * 0.1  # 10% discount
    else:
        discount = 0
    
    after_discount = subtotal - discount
    tax = after_discount * tax_rate
    total = after_discount + tax
    
    return {
        "subtotal": subtotal,
        "discount": discount,
        "after_discount": after_discount,
        "tax": tax,
        "total": total
    }

# Test
print("Solution:")
cart = [
    {"name": "Book", "price": 15.99, "quantity": 2},
    {"name": "Pen", "price": 2.50, "quantity": 5},
    {"name": "Notebook", "price": 8.99, "quantity": 3}
]

result = calculate_shopping_cart(cart)
print(f"Subtotal: ${result['subtotal']:.2f}")
print(f"Discount: -${result['discount']:.2f}")
print(f"After discount: ${result['after_discount']:.2f}")
print(f"Tax (8%): ${result['tax']:.2f}")
print(f"Total: ${result['total']:.2f}")

print("\n" + "=" * 60)
print("PROBLEM 4: Password Generator")
print("=" * 60)
print("Generate a random password with specific requirements")
print()

# Solution:
import random
random.seed(42)  # For consistent results

def generate_password(length=12, include_special=True):
    """Generate a random password"""
    lowercase = "abcdefghijklmnopqrstuvwxyz"
    uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    digits = "0123456789"
    special = "!@#$%^&*"
    
    # Ensure at least one of each type
    password = [
        random.choice(lowercase),
        random.choice(uppercase),
        random.choice(digits)
    ]
    
    if include_special:
        password.append(random.choice(special))
    
    # Fill remaining length
    all_chars = lowercase + uppercase + digits
    if include_special:
        all_chars += special
    
    while len(password) < length:
        password.append(random.choice(all_chars))
    
    # Shuffle the password
    random.shuffle(password)
    return "".join(password)

# Test
print("Solution:")
for i in range(3):
    pwd = generate_password(12)
    print(f"Password {i+1}: {pwd}")

print("\n" + "=" * 60)
print("PROBLEM 5: Word Frequency Analyzer")
print("=" * 60)
print("Analyze word frequency in a text")
print()

# Solution:
def analyze_word_frequency(text):
    """Analyze word frequency"""
    # Clean and split text
    words = text.lower().split()
    words = [word.strip(".,!?;:") for word in words]
    
    # Count frequencies
    freq = {}
    for word in words:
        if word:
            freq[word] = freq.get(word, 0) + 1
    
    # Find most common
    most_common = max(freq.items(), key=lambda x: x[1]) if freq else (None, 0)
    
    return {
        "total_words": len(words),
        "unique_words": len(freq),
        "frequency": freq,
        "most_common": most_common
    }

# Test
print("Solution:")
text = "Python is great. Python is powerful. I love Python programming!"
results = analyze_word_frequency(text)
print(f"Text: '{text}'")
print(f"Total words: {results['total_words']}")
print(f"Unique words: {results['unique_words']}")
print(f"Most common: '{results['most_common'][0]}' ({results['most_common'][1]} times)")
print("\nTop 5 words:")
sorted_freq = sorted(results['frequency'].items(), key=lambda x: x[1], reverse=True)
for word, count in sorted_freq[:5]:
    print(f"  '{word}': {count}")

print("\n" + "=" * 60)
print("PROBLEM 6: Number Pattern Generator")
print("=" * 60)
print("Generate various number patterns")
print()

# Solution:
def generate_pyramid(n):
    """Generate number pyramid"""
    print(f"Number Pyramid (n={n}):")
    for i in range(1, n + 1):
        # Print spaces
        print(" " * (n - i), end="")
        # Print numbers ascending
        for j in range(1, i + 1):
            print(j, end="")
        # Print numbers descending
        for j in range(i - 1, 0, -1):
            print(j, end="")
        print()

def generate_floyd_triangle(n):
    """Generate Floyd's triangle"""
    print(f"\nFloyd's Triangle (n={n}):")
    num = 1
    for i in range(1, n + 1):
        for j in range(i):
            print(num, end=" ")
            num += 1
        print()

# Test
print("Solution:")
generate_pyramid(5)
generate_floyd_triangle(5)

print("\n" + "=" * 60)
print("PROBLEM 7: Bank Account Simulator")
print("=" * 60)
print("Simulate basic banking operations")
print()

# Solution:
class BankAccount:
    """Simple bank account simulator"""
    def __init__(self, name, initial_balance=0):
        self.name = name
        self.balance = initial_balance
        self.transactions = []
    
    def deposit(self, amount):
        """Deposit money"""
        if amount > 0:
            self.balance += amount
            self.transactions.append(f"Deposit: +${amount:.2f}")
            return True
        return False
    
    def withdraw(self, amount):
        """Withdraw money"""
        if 0 < amount <= self.balance:
            self.balance -= amount
            self.transactions.append(f"Withdrawal: -${amount:.2f}")
            return True
        return False
    
    def get_balance(self):
        """Get current balance"""
        return self.balance
    
    def get_statement(self):
        """Get account statement"""
        return self.transactions

# Test
print("Solution:")
account = BankAccount("Alice", 1000)
print(f"Initial balance: ${account.get_balance():.2f}")

account.deposit(500)
print(f"After deposit: ${account.get_balance():.2f}")

account.withdraw(200)
print(f"After withdrawal: ${account.get_balance():.2f}")

print("\nTransaction History:")
for transaction in account.get_statement():
    print(f"  {transaction}")

print("\n" + "=" * 60)
print("PROBLEM 8: Calendar Helper")
print("=" * 60)
print("Determine day of the week for a given date")
print()

# Solution:
def is_leap_year(year):
    """Check if year is leap year"""
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

def days_in_month(month, year):
    """Get number of days in month"""
    days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if month == 2 and is_leap_year(year):
        return 29
    return days[month - 1]

def calculate_age(birth_year, current_year):
    """Calculate age"""
    return current_year - birth_year

# Test
print("Solution:")
print(f"2024 is leap year: {is_leap_year(2024)}")
print(f"2023 is leap year: {is_leap_year(2023)}")
print(f"Days in February 2024: {days_in_month(2, 2024)}")
print(f"Days in February 2023: {days_in_month(2, 2023)}")
print(f"Age if born in 2000 (current 2024): {calculate_age(2000, 2024)} years")
