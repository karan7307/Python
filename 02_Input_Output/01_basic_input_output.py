"""
Basic Input and Output in Python
=================================
This program demonstrates how to take input from users and display output.
"""

# Simple output using print()
print("=== Basic Output ===")
print("Hello, World!")
print("Welcome to Python programming!")

# Print multiple items
print("\n=== Multiple Items in Print ===")
print("My name is", "Alice", "and I am", 20, "years old")

# Print with different separators
print("\n=== Custom Separator ===")
print("apple", "banana", "orange", sep=" | ")
print("2024", "01", "15", sep="-")

# Print without newline (using end parameter)
print("\n=== Custom End Character ===")
print("Loading", end="...")
print("Done!")

# Taking simple input
print("\n=== Taking User Input ===")
name = input("What is your name? ")
print("Hello,", name, "! Nice to meet you!")

# Input comes as string by default
print("\n=== Input Type ===")
user_input = input("Enter something: ")
print("You entered:", user_input)
print("Type of input:", type(user_input))

# Creating interactive programs
print("\n=== Interactive Greeting Program ===")
user_name = input("Enter your name: ")
age = input("Enter your age: ")
city = input("Enter your city: ")

print("\n--- Your Information ---")
print("Name:", user_name)
print("Age:", age)
print("City:", city)

# Using input in strings
print("\n=== Using Input in Sentences ===")
favorite_color = input("What is your favorite color? ")
print("Wow!", favorite_color, "is a beautiful color!")

# Multiple print statements vs single print
print("\n=== Different Print Styles ===")
# Style 1: Multiple prints
print("First line")
print("Second line")
print("Third line")

# Style 2: Single print with \n (newline character)
print("\nFirst line\nSecond line\nThird line")

# Printing special characters
print("\n=== Special Characters ===")
print("This is a tab:\tSee the space?")
print("This is a quote: \"Hello\"")
print("This is a backslash: \\")
print("This prints on\ntwo lines")
