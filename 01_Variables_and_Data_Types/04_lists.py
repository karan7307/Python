"""
Working with Lists in Python
=============================
This program demonstrates list operations and methods.
Lists are ordered, mutable collections that can contain different data types.
"""

# Creating lists
fruits = ["apple", "banana", "orange"]
numbers = [1, 2, 3, 4, 5]
mixed = [1, "hello", 3.14, True]
empty_list = []

print("=== Creating Lists ===")
print("Fruits:", fruits)
print("Numbers:", numbers)
print("Mixed types:", mixed)
print("Empty list:", empty_list)

# Accessing list elements
print("\n=== Accessing Elements ===")
print("First fruit:", fruits[0])
print("Second fruit:", fruits[1])
print("Last fruit:", fruits[-1])

# List length
print("\n=== List Length ===")
print("Number of fruits:", len(fruits))

# Adding elements to list
fruits.append("grape")              # Add at the end
print("\n=== Adding Elements ===")
print("After append:", fruits)

fruits.insert(1, "mango")           # Insert at specific position
print("After insert at position 1:", fruits)

# Removing elements from list
fruits.remove("banana")             # Remove specific item
print("\n=== Removing Elements ===")
print("After removing banana:", fruits)

last_fruit = fruits.pop()           # Remove and return last item
print("Popped item:", last_fruit)
print("After pop:", fruits)

# List slicing
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print("\n=== List Slicing ===")
print("Original list:", numbers)
print("First 5 elements:", numbers[0:5])
print("Elements from index 5:", numbers[5:])
print("Last 3 elements:", numbers[-3:])
print("Every second element:", numbers[::2])

# List operations
list1 = [1, 2, 3]
list2 = [4, 5, 6]
print("\n=== List Operations ===")
print("List 1:", list1)
print("List 2:", list2)
print("Concatenation:", list1 + list2)
print("Repetition:", list1 * 3)

# Useful list methods
numbers = [3, 1, 4, 1, 5, 9, 2, 6]
print("\n=== List Methods ===")
print("Original list:", numbers)
print("Count of 1:", numbers.count(1))
print("Index of 4:", numbers.index(4))

numbers.sort()                      # Sort in ascending order
print("Sorted list:", numbers)

numbers.reverse()                   # Reverse the list
print("Reversed list:", numbers)

# Checking if item exists in list
shopping_list = ["milk", "bread", "eggs", "butter"]
print("\n=== Checking Items ===")
print("Shopping list:", shopping_list)
print("Is 'milk' in list?", "milk" in shopping_list)
print("Is 'cheese' in list?", "cheese" in shopping_list)

# List comprehension (advanced but useful)
squares = [x**2 for x in range(1, 6)]
print("\n=== List Comprehension ===")
print("Squares of 1-5:", squares)
