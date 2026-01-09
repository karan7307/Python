"""
Working with Strings in Python
===============================
This program demonstrates string operations and methods.
"""

# Creating strings
name = "Alice"
message = 'Hello World'
multiline = """This is a
multi-line
string"""

print("=== Basic Strings ===")
print("Name:", name)
print("Message:", message)
print("Multiline String:")
print(multiline)

# String concatenation (joining)
first_name = "John"
last_name = "Doe"
full_name = first_name + " " + last_name

print("\n=== String Concatenation ===")
print("First Name:", first_name)
print("Last Name:", last_name)
print("Full Name:", full_name)

# String repetition
laugh = "ha"
print("\n=== String Repetition ===")
print("Laugh:", laugh * 5)  # Prints "hahahahaha"

# String length
sentence = "Python is fun"
print("\n=== String Length ===")
print("Sentence:", sentence)
print("Length:", len(sentence))

# Accessing characters (indexing)
word = "Python"
print("\n=== String Indexing ===")
print("Word:", word)
print("First character:", word[0])    # P
print("Second character:", word[1])   # y
print("Last character:", word[-1])    # n
print("Second last:", word[-2])       # o

# String slicing
text = "Hello World"
print("\n=== String Slicing ===")
print("Original text:", text)
print("First 5 characters:", text[0:5])    # Hello
print("From index 6 to end:", text[6:])    # World
print("Last 5 characters:", text[-5:])     # World

# Useful string methods
sample = "  python programming  "
print("\n=== String Methods ===")
print("Original:", "[" + sample + "]")
print("Uppercase:", sample.upper())
print("Lowercase:", sample.lower())
print("Capitalized:", sample.capitalize())
print("Stripped (remove spaces):", "[" + sample.strip() + "]")
print("Replace:", sample.replace("python", "Python"))

# Checking string content
email = "student@example.com"
print("\n=== String Checks ===")
print("Email:", email)
print("Contains '@':", "@" in email)
print("Starts with 'student':", email.startswith("student"))
print("Ends with '.com':", email.endswith(".com"))

# String formatting
name = "Alice"
age = 20
print("\n=== String Formatting ===")
# Method 1: f-strings (recommended)
print(f"My name is {name} and I am {age} years old.")
# Method 2: format() method
print("My name is {} and I am {} years old.".format(name, age))
# Method 3: % operator (old style)
print("My name is %s and I am %d years old." % (name, age))
