"""
Variable Scope in Python
=========================
This program demonstrates local and global variable scope.
"""

# Global variable
global_var = "I am global"

print("=== Global Variable ===")
def show_global():
    """Access global variable"""
    print(f"Inside function: {global_var}")

print(f"Outside function: {global_var}")
show_global()

# Local variable
print("\n=== Local Variable ===")
def show_local():
    """Create and use local variable"""
    local_var = "I am local"
    print(f"Inside function: {local_var}")

show_local()
# print(local_var)  # Error: local_var not defined outside function

# Local vs Global with same name
print("\n=== Local vs Global with Same Name ===")
x = "global x"

def test_scope():
    x = "local x"  # This is a different variable
    print(f"Inside function: {x}")

print(f"Before function: {x}")
test_scope()
print(f"After function: {x}")  # Global x unchanged

# Using global keyword
print("\n=== Modifying Global Variable ===")
counter = 0

def increment():
    global counter  # Declare we want to use global variable
    counter += 1
    print(f"Counter inside: {counter}")

print(f"Initial counter: {counter}")
increment()
increment()
increment()
print(f"Final counter: {counter}")

# Multiple global variables
print("\n=== Multiple Global Variables ===")
name = "Alice"
age = 20

def update_info():
    global name, age
    name = "Bob"
    age = 25
    print(f"Updated: {name}, {age}")

print(f"Before: {name}, {age}")
update_info()
print(f"After: {name}, {age}")

# Function parameters are local
print("\n=== Parameters are Local ===")
def greet(name):
    """Parameter 'name' is local to this function"""
    name = name.upper()  # Modifies local copy
    print(f"Inside: {name}")

person = "alice"
print(f"Before: {person}")
greet(person)
print(f"After: {person}")  # Unchanged

# Nested function scope
print("\n=== Nested Function Scope ===")
def outer():
    outer_var = "I'm in outer"
    
    def inner():
        # Can access outer function's variables
        print(f"Inner accessing: {outer_var}")
    
    print(f"Outer: {outer_var}")
    inner()

outer()

# nonlocal keyword
print("\n=== Nonlocal Keyword ===")
def outer_function():
    count = 0
    
    def inner_function():
        nonlocal count  # Access outer function's variable
        count += 1
        print(f"Count: {count}")
    
    inner_function()
    inner_function()
    inner_function()
    print(f"Final count: {count}")

outer_function()

# Constants (convention: UPPERCASE)
print("\n=== Constants ===")
PI = 3.14159
MAX_SIZE = 100
APP_NAME = "MyApp"

def calculate_circle_area(radius):
    """Uses global constant PI"""
    return PI * radius ** 2

print(f"Circle area (r=5): {calculate_circle_area(5):.2f}")
print(f"Max size: {MAX_SIZE}")

# Scope resolution order
print("\n=== Scope Resolution (LEGB Rule) ===")
# LEGB: Local -> Enclosing -> Global -> Built-in

x = "global"

def outer():
    x = "enclosing"
    
    def inner():
        x = "local"
        print(f"Inner x: {x}")  # Local
    
    inner()
    print(f"Outer x: {x}")  # Enclosing

print(f"Global x: {x}")  # Global
outer()

# Built-in scope example
print("\n=== Built-in Scope ===")
# 'len' is a built-in function
my_list = [1, 2, 3, 4, 5]
print(f"Length: {len(my_list)}")

# Don't shadow built-ins!
def bad_example():
    len = 10  # Bad: shadows built-in function
    print(f"Local len: {len}")
    # print(len([1, 2, 3]))  # Error: len is now an integer

bad_example()
print(f"Global len still works: {len([1, 2, 3])}")

# Practical: Counter with closure
print("\n=== Practical: Counter ===")
def create_counter():
    """Creates a counter function using closure"""
    count = 0
    
    def increment():
        nonlocal count
        count += 1
        return count
    
    return increment

counter1 = create_counter()
counter2 = create_counter()

print(f"Counter 1: {counter1()}")  # 1
print(f"Counter 1: {counter1()}")  # 2
print(f"Counter 2: {counter2()}")  # 1 (separate counter)
print(f"Counter 1: {counter1()}")  # 3

# Practical: Configuration
print("\n=== Configuration Variables ===")
# Global configuration
DEBUG = True
MAX_RETRIES = 3

def process_data(data):
    """Uses global configuration"""
    if DEBUG:
        print(f"[DEBUG] Processing: {data}")
    
    retries = 0
    while retries < MAX_RETRIES:
        # Simulated processing
        if data:  # Success condition
            return f"Processed: {data}"
        retries += 1
    
    return "Failed after retries"

result = process_data("sample data")
print(result)

# Variable lifetime
print("\n=== Variable Lifetime ===")
def demonstrate_lifetime():
    """Local variables exist only during function execution"""
    temp = "I exist only during function call"
    print(temp)
    # 'temp' is destroyed when function ends

demonstrate_lifetime()
demonstrate_lifetime()  # New 'temp' created each time

# Global mutable objects
print("\n=== Global Mutable Objects ===")
scores = [85, 90, 78]

def add_score(score):
    """Can modify mutable global objects without 'global' keyword"""
    scores.append(score)  # Modifying list contents
    print(f"Scores: {scores}")

print(f"Initial: {scores}")
add_score(92)
add_score(88)
print(f"Final: {scores}")

# Best practices
print("\n=== Best Practices ===")
# Good: Pass values as parameters, return results
def calculate_total(items):
    """Pure function - doesn't depend on global state"""
    return sum(items)

# Good: Return value instead of modifying global
def add_item_good(items, new_item):
    """Returns new list instead of modifying global"""
    return items + [new_item]

numbers = [1, 2, 3]
total = calculate_total(numbers)
new_numbers = add_item_good(numbers, 4)

print(f"Total: {total}")
print(f"Original: {numbers}")
print(f"New list: {new_numbers}")
