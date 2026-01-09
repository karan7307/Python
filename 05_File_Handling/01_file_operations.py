"""
FILE HANDLING IN PYTHON
========================

File handling allows you to work with files - read, write, and manipulate them.
Python makes file operations easy and straightforward.

Common File Operations:
1. Opening a file
2. Reading from a file
3. Writing to a file
4. Appending to a file
5. Closing a file

File Modes:
- 'r' : Read mode (default) - Opens file for reading
- 'w' : Write mode - Creates new file or overwrites existing
- 'a' : Append mode - Adds to the end of file
- 'r+': Read and Write mode
"""

import os

# ============================================
# WRITING TO A FILE
# ============================================

print("=" * 50)
print("WRITING TO A FILE")
print("=" * 50 + "\n")

# Create and write to a file
print("Creating a new file and writing to it...")

file = open("sample.txt", "w")  # Open in write mode
file.write("Hello, Python!\n")
file.write("This is a sample file.\n")
file.write("Learning file handling is fun!\n")
file.close()  # Always close the file

print("✓ File 'sample.txt' created and written successfully!")


# ============================================
# READING FROM A FILE
# ============================================

print("\n" + "=" * 50)
print("READING FROM A FILE")
print("=" * 50 + "\n")

# Read entire file
print("Reading the entire file:")
file = open("sample.txt", "r")  # Open in read mode
content = file.read()  # Read all content
print(content)
file.close()

print("-" * 50)

# Read line by line
print("Reading line by line:")
file = open("sample.txt", "r")
lines = file.readlines()  # Read all lines into a list
for line in lines:
    print(line.strip())  # strip() removes extra newline
file.close()


# ============================================
# USING 'WITH' STATEMENT (RECOMMENDED)
# ============================================

print("\n" + "=" * 50)
print("USING 'WITH' STATEMENT")
print("=" * 50 + "\n")

print("'with' automatically closes the file - safer and cleaner!\n")

# Writing with 'with' statement
with open("students.txt", "w") as file:
    file.write("Student List\n")
    file.write("=" * 30 + "\n")
    file.write("1. Alice - Grade A\n")
    file.write("2. Bob - Grade B\n")
    file.write("3. Charlie - Grade A\n")

print("✓ File 'students.txt' created!")

# Reading with 'with' statement
print("\nReading 'students.txt':")
with open("students.txt", "r") as file:
    content = file.read()
    print(content)


# ============================================
# APPENDING TO A FILE
# ============================================

print("=" * 50)
print("APPENDING TO A FILE")
print("=" * 50 + "\n")

# Append adds to the end without deleting existing content
print("Appending new students to the file...")

with open("students.txt", "a") as file:
    file.write("4. Diana - Grade A+\n")
    file.write("5. Eve - Grade B+\n")

print("✓ New students added!")

print("\nReading updated file:")
with open("students.txt", "r") as file:
    print(file.read())


# ============================================
# READING FILE LINE BY LINE
# ============================================

print("=" * 50)
print("READING LINE BY LINE")
print("=" * 50 + "\n")

print("Processing each line:")
with open("students.txt", "r") as file:
    line_number = 1
    for line in file:
        print(f"Line {line_number}: {line.strip()}")
        line_number += 1


# ============================================
# CHECKING IF FILE EXISTS
# ============================================

print("\n" + "=" * 50)
print("CHECKING IF FILE EXISTS")
print("=" * 50 + "\n")

if os.path.exists("students.txt"):
    print("✓ File 'students.txt' exists!")
else:
    print("✗ File 'students.txt' does not exist!")

if os.path.exists("nonexistent.txt"):
    print("✓ File 'nonexistent.txt' exists!")
else:
    print("✗ File 'nonexistent.txt' does not exist!")


# ============================================
# PROGRAM 1: SAVE STUDENT RECORDS
# ============================================

print("\n" + "=" * 50)
print("PROGRAM 1: STUDENT RECORDS SYSTEM")
print("=" * 50 + "\n")

def save_student_record(filename, name, roll_no, grade):
    """Saves student record to a file"""
    with open(filename, "a") as file:
        file.write(f"{roll_no},{name},{grade}\n")
    print(f"✓ Record saved: {name} (Roll: {roll_no}, Grade: {grade})")

def read_student_records(filename):
    """Reads and displays all student records"""
    if not os.path.exists(filename):
        print("No records found!")
        return
    
    print("\nSTUDENT RECORDS:")
    print("-" * 50)
    print(f"{'Roll No':<10} {'Name':<20} {'Grade':<10}")
    print("-" * 50)
    
    with open(filename, "r") as file:
        for line in file:
            parts = line.strip().split(",")
            if len(parts) == 3:
                roll, name, grade = parts
                print(f"{roll:<10} {name:<20} {grade:<10}")

# Save some student records
save_student_record("records.txt", "Alice Johnson", "101", "A")
save_student_record("records.txt", "Bob Smith", "102", "B+")
save_student_record("records.txt", "Charlie Brown", "103", "A-")

# Read and display records
read_student_records("records.txt")


# ============================================
# PROGRAM 2: WORD COUNTER
# ============================================

print("\n" + "=" * 50)
print("PROGRAM 2: WORD COUNTER")
print("=" * 50 + "\n")

def count_words_in_file(filename):
    """Counts words, lines, and characters in a file"""
    if not os.path.exists(filename):
        print(f"File '{filename}' not found!")
        return
    
    with open(filename, "r") as file:
        content = file.read()
        lines = content.split("\n")
        words = content.split()
        
        print(f"File: {filename}")
        print(f"Lines: {len(lines)}")
        print(f"Words: {len(words)}")
        print(f"Characters: {len(content)}")

# Create a sample file for counting
with open("essay.txt", "w") as file:
    file.write("Python is a powerful programming language.\n")
    file.write("It is easy to learn and widely used.\n")
    file.write("Many companies use Python for development.\n")

count_words_in_file("essay.txt")


# ============================================
# PROGRAM 3: TO-DO LIST
# ============================================

print("\n" + "=" * 50)
print("PROGRAM 3: TO-DO LIST MANAGER")
print("=" * 50 + "\n")

def add_task(task):
    """Adds a task to todo list"""
    with open("todo.txt", "a") as file:
        file.write(f"[ ] {task}\n")
    print(f"✓ Task added: {task}")

def show_tasks():
    """Displays all tasks"""
    if not os.path.exists("todo.txt"):
        print("No tasks yet!")
        return
    
    print("\nYOUR TO-DO LIST:")
    print("-" * 50)
    with open("todo.txt", "r") as file:
        tasks = file.readlines()
        if not tasks:
            print("No tasks yet!")
        else:
            for i, task in enumerate(tasks, 1):
                print(f"{i}. {task.strip()}")

# Add some tasks
add_task("Learn Python file handling")
add_task("Practice coding exercises")
add_task("Build a small project")

# Show all tasks
show_tasks()


# ============================================
# PROGRAM 4: SIMPLE DATABASE
# ============================================

print("\n" + "=" * 50)
print("PROGRAM 4: SIMPLE CONTACT DATABASE")
print("=" * 50 + "\n")

def add_contact(name, phone, email):
    """Adds a contact to the database"""
    with open("contacts.txt", "a") as file:
        file.write(f"{name}|{phone}|{email}\n")
    print(f"✓ Contact added: {name}")

def search_contact(name):
    """Searches for a contact by name"""
    if not os.path.exists("contacts.txt"):
        print("No contacts found!")
        return
    
    found = False
    with open("contacts.txt", "r") as file:
        for line in file:
            parts = line.strip().split("|")
            if len(parts) == 3 and parts[0].lower() == name.lower():
                print(f"\nContact Found:")
                print(f"Name: {parts[0]}")
                print(f"Phone: {parts[1]}")
                print(f"Email: {parts[2]}")
                found = True
                break
    
    if not found:
        print(f"Contact '{name}' not found!")

# Add contacts
add_contact("Alice", "123-456-7890", "alice@email.com")
add_contact("Bob", "098-765-4321", "bob@email.com")

# Search for a contact
search_contact("Alice")
search_contact("Charlie")


# ============================================
# CLEANUP (Delete sample files)
# ============================================

print("\n" + "=" * 50)
print("CLEANING UP SAMPLE FILES")
print("=" * 50 + "\n")

sample_files = ["sample.txt", "students.txt", "records.txt", "essay.txt", "todo.txt", "contacts.txt"]

for filename in sample_files:
    if os.path.exists(filename):
        os.remove(filename)
        print(f"✓ Deleted: {filename}")


# ============================================
# PRACTICE PROBLEMS
# ============================================

print("\n" + "=" * 50)
print("PRACTICE PROBLEMS")
print("=" * 50)

"""
Try these exercises:

1. Write a program that creates a file and writes your favorite quotes to it.
   Then read and display them.

2. Create a program that reads a file and counts how many times each vowel appears.

3. Write a program that copies the content of one file to another file.

4. Create a simple diary application that appends daily entries with timestamps.

5. Write a program that reads a file containing numbers (one per line) and 
   calculates their sum and average.

6. Create a grade book system that:
   - Saves student names and marks
   - Reads and displays all records
   - Calculates class average

7. Write a program that finds and replaces a word in a file.

8. Create a program that reads a file and counts the frequency of each word.

9. Write a program that merges two text files into a third file.

10. Create a simple inventory management system using file handling:
    - Add items (name, quantity, price)
    - Display all items
    - Update item quantity
    - Calculate total inventory value
"""

print("\nTry solving the practice problems above!")
print("File handling is essential for saving and managing data!")
