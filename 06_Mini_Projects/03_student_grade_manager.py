"""
MINI PROJECT 3: STUDENT GRADE MANAGER
======================================

A simple system to manage student grades.
You can add students, view records, calculate averages, and more!
"""

# Store students in a list of dictionaries
students = []

def display_menu():
    """Display main menu"""
    print("\n" + "=" * 50)
    print("📚 STUDENT GRADE MANAGER 📚")
    print("=" * 50)
    print("\n1. Add New Student")
    print("2. View All Students")
    print("3. Search Student")
    print("4. Calculate Class Average")
    print("5. Find Top Performer")
    print("6. Display Grade Distribution")
    print("7. Exit")
    print("=" * 50)

def add_student():
    """Add a new student"""
    print("\n" + "-" * 50)
    print("ADD NEW STUDENT")
    print("-" * 50)
    
    name = input("Enter student name: ")
    
    try:
        math = float(input("Enter Math score (0-100): "))
        science = float(input("Enter Science score (0-100): "))
        english = float(input("Enter English score (0-100): "))
        
        # Validate scores
        if not all(0 <= score <= 100 for score in [math, science, english]):
            print("❌ Scores must be between 0 and 100!")
            return
        
        # Calculate average and grade
        average = (math + science + english) / 3
        grade = calculate_grade(average)
        
        # Create student record
        student = {
            'name': name,
            'math': math,
            'science': science,
            'english': english,
            'average': average,
            'grade': grade
        }
        
        students.append(student)
        print(f"\n✓ Student '{name}' added successfully!")
        print(f"  Average: {average:.2f}, Grade: {grade}")
        
    except ValueError:
        print("❌ Invalid input! Please enter numbers for scores.")

def calculate_grade(average):
    """Calculate letter grade from average"""
    if average >= 90:
        return "A+"
    elif average >= 80:
        return "A"
    elif average >= 70:
        return "B"
    elif average >= 60:
        return "C"
    elif average >= 50:
        return "D"
    else:
        return "F"

def view_all_students():
    """Display all student records"""
    if not students:
        print("\n❌ No students in the system yet!")
        return
    
    print("\n" + "=" * 80)
    print("ALL STUDENT RECORDS")
    print("=" * 80)
    print(f"{'Name':<20} {'Math':<8} {'Science':<8} {'English':<8} {'Average':<10} {'Grade':<8}")
    print("-" * 80)
    
    for student in students:
        print(f"{student['name']:<20} {student['math']:<8.1f} {student['science']:<8.1f} "
              f"{student['english']:<8.1f} {student['average']:<10.2f} {student['grade']:<8}")
    
    print("-" * 80)
    print(f"Total Students: {len(students)}")

def search_student():
    """Search for a student by name"""
    if not students:
        print("\n❌ No students in the system yet!")
        return
    
    name = input("\nEnter student name to search: ")
    
    found = False
    for student in students:
        if student['name'].lower() == name.lower():
            print("\n" + "-" * 50)
            print("STUDENT FOUND")
            print("-" * 50)
            print(f"Name: {student['name']}")
            print(f"Math: {student['math']:.1f}")
            print(f"Science: {student['science']:.1f}")
            print(f"English: {student['english']:.1f}")
            print(f"Average: {student['average']:.2f}")
            print(f"Grade: {student['grade']}")
            print("-" * 50)
            found = True
            break
    
    if not found:
        print(f"\n❌ Student '{name}' not found!")

def calculate_class_average():
    """Calculate and display class average"""
    if not students:
        print("\n❌ No students in the system yet!")
        return
    
    total_avg = sum(student['average'] for student in students)
    class_avg = total_avg / len(students)
    
    print("\n" + "-" * 50)
    print("CLASS STATISTICS")
    print("-" * 50)
    print(f"Total Students: {len(students)}")
    print(f"Class Average: {class_avg:.2f}")
    print(f"Class Grade: {calculate_grade(class_avg)}")
    print("-" * 50)

def find_top_performer():
    """Find and display the top performing student"""
    if not students:
        print("\n❌ No students in the system yet!")
        return
    
    top_student = max(students, key=lambda x: x['average'])
    
    print("\n" + "-" * 50)
    print("🏆 TOP PERFORMER 🏆")
    print("-" * 50)
    print(f"Name: {top_student['name']}")
    print(f"Average: {top_student['average']:.2f}")
    print(f"Grade: {top_student['grade']}")
    print("-" * 50)

def display_grade_distribution():
    """Show distribution of grades"""
    if not students:
        print("\n❌ No students in the system yet!")
        return
    
    # Count each grade
    grade_count = {}
    for student in students:
        grade = student['grade']
        grade_count[grade] = grade_count.get(grade, 0) + 1
    
    print("\n" + "-" * 50)
    print("GRADE DISTRIBUTION")
    print("-" * 50)
    
    for grade in ['A+', 'A', 'B', 'C', 'D', 'F']:
        count = grade_count.get(grade, 0)
        percentage = (count / len(students)) * 100 if students else 0
        bar = "█" * count
        print(f"{grade:<5} : {bar} ({count} students - {percentage:.1f}%)")
    
    print("-" * 50)

def main():
    """Main program function"""
    print("\n🎓 Welcome to Student Grade Manager! 🎓")
    
    while True:
        display_menu()
        
        choice = input("\nEnter your choice (1-7): ")
        
        if choice == '1':
            add_student()
        elif choice == '2':
            view_all_students()
        elif choice == '3':
            search_student()
        elif choice == '4':
            calculate_class_average()
        elif choice == '5':
            find_top_performer()
        elif choice == '6':
            display_grade_distribution()
        elif choice == '7':
            print("\n" + "=" * 50)
            print("Thank you for using Student Grade Manager!")
            print("Goodbye! 👋")
            print("=" * 50 + "\n")
            break
        else:
            print("\n❌ Invalid choice! Please select 1-7.")
        
        input("\nPress Enter to continue...")

# ============================================
# DEMONSTRATION MODE
# ============================================

def demo():
    """Demonstrate the system with sample data"""
    print("\n" + "=" * 50)
    print("DEMONSTRATION MODE")
    print("=" * 50 + "\n")
    
    # Add sample students
    sample_students = [
        {'name': 'Alice Johnson', 'math': 92, 'science': 88, 'english': 90},
        {'name': 'Bob Smith', 'math': 78, 'science': 82, 'english': 75},
        {'name': 'Charlie Brown', 'math': 95, 'science': 93, 'english': 91},
        {'name': 'Diana Prince', 'math': 85, 'science': 87, 'english': 89},
        {'name': 'Eve Wilson', 'math': 72, 'science': 70, 'english': 74},
    ]
    
    print("Adding sample students...\n")
    for student_data in sample_students:
        average = (student_data['math'] + student_data['science'] + student_data['english']) / 3
        grade = calculate_grade(average)
        
        student = {
            'name': student_data['name'],
            'math': student_data['math'],
            'science': student_data['science'],
            'english': student_data['english'],
            'average': average,
            'grade': grade
        }
        
        students.append(student)
        print(f"✓ Added: {student['name']}")
    
    # Show various features
    view_all_students()
    calculate_class_average()
    find_top_performer()
    display_grade_distribution()

# Run demonstration
demo()

# ============================================
# HOW TO USE
# ============================================

print("\n" + "=" * 50)
print("HOW TO USE")
print("=" * 50)
print("""
To use the interactive system:

1. Uncomment the line below (remove the #):
   # main()

2. Run the program again

3. Follow the menu options:
   - Add students with their scores
   - View all records
   - Search for specific students
   - See statistics and analytics

Note: Currently showing demonstration with sample data.
""")

# Uncomment the line below to run the interactive program:
# main()

# ============================================
# ENHANCEMENT IDEAS
# ============================================

print("\n" + "=" * 50)
print("ENHANCEMENT IDEAS")
print("=" * 50)
print("""
Try adding these features:

1. More Features:
   - Edit student records
   - Delete student records
   - Add more subjects
   - Calculate subject-wise averages

2. File Operations:
   - Save data to a file
   - Load data from a file
   - Export to CSV format
   - Import from CSV

3. Advanced Analytics:
   - Median and mode calculations
   - Standard deviation
   - Subject-wise rankings
   - Progress tracking over time

4. Better Interface:
   - Colored output
   - Sorting options (by name, grade, etc.)
   - Filter students by grade
   - Generate report cards

5. Validations:
   - Prevent duplicate student names
   - Confirm before deleting
   - Undo last operation
   - Data backup
""")
