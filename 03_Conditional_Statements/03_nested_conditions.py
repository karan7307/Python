"""
Nested Conditional Statements in Python
========================================
This program demonstrates conditions inside conditions (nested if statements).
"""

# Basic nested if
print("=== Basic Nested if ===")
age = 25
has_license = True

if age >= 18:
    print("Age requirement met")
    if has_license:
        print("You can drive!")
    else:
        print("You need a driving license")
else:
    print("You are too young to drive")

# Nested if-else with multiple levels
print("\n=== Login System ===")
username = "admin"
password = "pass123"
user_input = "admin"
pass_input = "pass123"

if user_input == username:
    print("Username correct")
    if pass_input == password:
        print("Password correct")
        print("Login successful! ✓")
    else:
        print("Wrong password! ✗")
else:
    print("Username not found! ✗")

# Eligibility for scholarship
print("\n=== Scholarship Eligibility ===")
marks = 85
family_income = 30000
has_sports = True

if marks >= 80:
    print("Academic requirement met")
    if family_income < 50000:
        print("Income requirement met")
        if has_sports:
            print("Sports quota bonus!")
            print("Scholarship: $5000")
        else:
            print("Scholarship: $3000")
    else:
        print("Family income too high for scholarship")
else:
    print("Marks not sufficient for scholarship")

# Voting eligibility with detailed checks
print("\n=== Voting Eligibility Checker ===")
age = 20
is_citizen = True
has_id = True

if age >= 18:
    print("Age: Eligible")
    if is_citizen:
        print("Citizenship: Verified")
        if has_id:
            print("ID: Verified")
            print("\n✓ You can vote!")
        else:
            print("ID: Not found")
            print("\n✗ Please bring a valid ID to vote")
    else:
        print("Citizenship: Not verified")
        print("\n✗ Only citizens can vote")
else:
    years_left = 18 - age
    print(f"Age: Not eligible (wait {years_left} more years)")

# Admission process
print("\n=== College Admission System ===")
entrance_score = 450
interview_score = 85
has_recommendation = True

if entrance_score >= 400:
    print("Entrance exam: PASSED")
    if interview_score >= 80:
        print("Interview: PASSED")
        if has_recommendation:
            print("Recommendation letter: YES")
            print("\n🎓 Admission Status: ACCEPTED with Honors")
        else:
            print("Recommendation letter: NO")
            print("\n🎓 Admission Status: ACCEPTED")
    else:
        print("Interview: FAILED")
        print(f"Score: {interview_score}/100 (minimum required: 80)")
        print("\n❌ Admission Status: REJECTED")
else:
    print("Entrance exam: FAILED")
    print(f"Score: {entrance_score}/500 (minimum required: 400)")
    print("\n❌ Admission Status: REJECTED")

# Shopping discount with membership
print("\n=== Advanced Shopping Discount ===")
purchase_amount = 1500
is_member = True
first_time = False

if purchase_amount >= 1000:
    if is_member:
        if first_time:
            discount = purchase_amount * 0.25  # 25% for first time members
            print("Discount: 25% (Member + First Purchase)")
        else:
            discount = purchase_amount * 0.20  # 20% for regular members
            print("Discount: 20% (Regular Member)")
    else:
        discount = purchase_amount * 0.10  # 10% for non-members
        print("Discount: 10% (Non-member)")
else:
    if is_member:
        discount = purchase_amount * 0.05  # 5% for members on small purchases
        print("Discount: 5% (Member - small purchase)")
    else:
        discount = 0  # No discount
        print("No discount available")

final_amount = purchase_amount - discount
print(f"\nPurchase amount: ${purchase_amount}")
print(f"Discount amount: ${discount}")
print(f"Final amount: ${final_amount}")

# Exam result with detailed feedback
print("\n=== Exam Result System ===")
theory_marks = 75
practical_marks = 80
attendance = 85

if theory_marks >= 50:
    print("Theory: PASS")
    if practical_marks >= 50:
        print("Practical: PASS")
        if attendance >= 75:
            print("Attendance: Sufficient")
            average = (theory_marks + practical_marks) / 2
            print(f"\nOverall Average: {average}")
            
            if average >= 90:
                print("Result: DISTINCTION ⭐⭐⭐")
            elif average >= 75:
                print("Result: FIRST CLASS ⭐⭐")
            elif average >= 60:
                print("Result: SECOND CLASS ⭐")
            else:
                print("Result: PASS ✓")
        else:
            print("Attendance: Insufficient")
            print(f"Attendance: {attendance}% (minimum required: 75%)")
            print("\nResult: DETAINED")
    else:
        print("Practical: FAIL")
        print("\nResult: FAIL in Practical")
else:
    print("Theory: FAIL")
    print("\nResult: FAIL in Theory")
