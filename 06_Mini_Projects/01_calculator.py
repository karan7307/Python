"""
MINI PROJECT 1: SIMPLE CALCULATOR
==================================

A calculator that can perform basic arithmetic operations.
This project uses functions to organize code better.
"""

def add(x, y):
    """Addition"""
    return x + y

def subtract(x, y):
    """Subtraction"""
    return x - y

def multiply(x, y):
    """Multiplication"""
    return x * y

def divide(x, y):
    """Division"""
    if y == 0:
        return "Error! Division by zero."
    return x / y

def display_menu():
    """Display calculator menu"""
    print("\n" + "=" * 50)
    print("SIMPLE CALCULATOR")
    print("=" * 50)
    print("\nOperations:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (×)")
    print("4. Division (÷)")
    print("5. Exit")
    print("=" * 50)

def calculator():
    """Main calculator function"""
    print("Welcome to Simple Calculator!")
    
    while True:
        display_menu()
        
        choice = input("\nEnter your choice (1-5): ")
        
        # Exit condition
        if choice == '5':
            print("\nThank you for using the calculator!")
            print("Goodbye! 👋")
            break
        
        # Check if choice is valid
        if choice not in ['1', '2', '3', '4']:
            print("\n❌ Invalid choice! Please select 1-5.")
            continue
        
        # Get numbers from user
        try:
            num1 = float(input("\nEnter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("\n❌ Invalid input! Please enter numbers only.")
            continue
        
        # Perform calculation based on choice
        if choice == '1':
            result = add(num1, num2)
            operation = "+"
        elif choice == '2':
            result = subtract(num1, num2)
            operation = "-"
        elif choice == '3':
            result = multiply(num1, num2)
            operation = "×"
        elif choice == '4':
            result = divide(num1, num2)
            operation = "÷"
        
        # Display result
        print("\n" + "-" * 50)
        print(f"Result: {num1} {operation} {num2} = {result}")
        print("-" * 50)
        
        # Ask if user wants to continue
        continue_calc = input("\nDo you want to perform another calculation? (yes/no): ")
        if continue_calc.lower() != 'yes':
            print("\nThank you for using the calculator!")
            print("Goodbye! 👋")
            break

# ============================================
# DEMONSTRATION MODE
# ============================================

def demo_calculator():
    """Demonstrates calculator with sample calculations"""
    print("\n" + "=" * 50)
    print("CALCULATOR DEMONSTRATION")
    print("=" * 50 + "\n")
    
    # Sample calculations
    calculations = [
        (10, 5, "Addition", add, "+"),
        (20, 8, "Subtraction", subtract, "-"),
        (6, 7, "Multiplication", multiply, "×"),
        (100, 4, "Division", divide, "÷"),
    ]
    
    for num1, num2, operation_name, operation_func, symbol in calculations:
        result = operation_func(num1, num2)
        print(f"{operation_name}: {num1} {symbol} {num2} = {result}")
    
    # Test division by zero
    print(f"\nDivision by zero test: {divide(10, 0)}")

# Run demonstration
demo_calculator()

# ============================================
# HOW TO USE THIS PROGRAM
# ============================================

print("\n" + "=" * 50)
print("HOW TO USE")
print("=" * 50)
print("""
To use the interactive calculator:

1. Uncomment the line below (remove the #):
   # calculator()

2. Run the program again

3. Follow the on-screen instructions:
   - Choose an operation (1-5)
   - Enter two numbers
   - View the result
   - Decide if you want to continue

Features:
✓ Handles division by zero
✓ Input validation
✓ User-friendly interface
✓ Option to exit anytime
""")

# Uncomment the line below to run the interactive calculator:
# calculator()

print("\n" + "=" * 50)
print("ENHANCEMENT IDEAS")
print("=" * 50)
print("""
Try adding these features:

1. More operations:
   - Square root
   - Power (x^y)
   - Modulus (remainder)
   - Percentage

2. Memory functions:
   - Store last result
   - Recall stored value

3. History:
   - Keep track of all calculations
   - Display calculation history

4. Advanced features:
   - Calculate expression: "5 + 3 * 2"
   - Scientific calculator functions
   - Unit conversions

5. Better interface:
   - Clear screen between operations
   - Colorful output
   - Save results to file
""")
