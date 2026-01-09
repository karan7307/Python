"""
NESTED CONDITIONS IN PYTHON
============================

Nested conditions means having if-else statements inside other if-else statements.
This is useful when you need to check multiple conditions in a hierarchical way.
"""

# ============================================
# BASIC NESTED IF EXAMPLE
# ============================================

print("=" * 50)
print("BASIC NESTED IF")
print("=" * 50 + "\n")

age = 25
has_ticket = True

if age >= 18:
    print("You are an adult.")
    if has_ticket:
        print("You can enter the movie theater! 🎬")
    else:
        print("Please buy a ticket first.")
else:
    print("You are under 18.")
    if has_ticket:
        print("You need parental guidance to enter.")
    else:
        print("You need a ticket and parental guidance.")


# ============================================
# SCHOOL GRADING SYSTEM WITH ATTENDANCE
# ============================================

print("\n" + "=" * 50)
print("PROGRAM 1: ADVANCED GRADING SYSTEM")
print("=" * 50 + "\n")

marks = 85
attendance = 82

print(f"Marks: {marks}")
print(f"Attendance: {attendance}%\n")

# First check attendance
if attendance >= 75:
    print("✓ Attendance requirement met")
    
    # Then check marks
    if marks >= 90:
        grade = "A+"
        print(f"Grade: {grade} - Outstanding!")
    elif marks >= 80:
        grade = "A"
        print(f"Grade: {grade} - Excellent!")
    elif marks >= 70:
        grade = "B"
        print(f"Grade: {grade} - Very Good!")
    elif marks >= 60:
        grade = "C"
        print(f"Grade: {grade} - Good")
    elif marks >= 50:
        grade = "D"
        print(f"Grade: {grade} - Pass")
    else:
        grade = "F"
        print(f"Grade: {grade} - Fail")
else:
    print("✗ Attendance requirement NOT met")
    print(f"You need at least 75% attendance, you have {attendance}%")
    print("Result: DETAINED (Cannot appear in exam)")


# ============================================
# LOAN ELIGIBILITY CHECKER
# ============================================

print("\n" + "=" * 50)
print("PROGRAM 2: LOAN ELIGIBILITY CHECKER")
print("=" * 50 + "\n")

age = 30
monthly_income = 50000
credit_score = 750
has_existing_loan = False

print(f"Age: {age}")
print(f"Monthly Income: ${monthly_income}")
print(f"Credit Score: {credit_score}")
print(f"Has Existing Loan: {has_existing_loan}\n")

# Check age eligibility
if age >= 21 and age <= 60:
    print("✓ Age requirement met")
    
    # Check income
    if monthly_income >= 30000:
        print("✓ Income requirement met")
        
        # Check credit score
        if credit_score >= 700:
            print("✓ Credit score is good")
            
            # Check existing loans
            if not has_existing_loan:
                print("✓ No existing loans\n")
                print("🎉 LOAN APPROVED!")
                print("You can borrow up to $500,000")
            else:
                print("⚠ You have an existing loan\n")
                print("LOAN APPROVED with conditions")
                print("You can borrow up to $200,000")
        else:
            print(f"✗ Credit score too low (need 700+, you have {credit_score})\n")
            print("LOAN REJECTED")
    else:
        print(f"✗ Income too low (need $30,000+, you have ${monthly_income})\n")
        print("LOAN REJECTED")
else:
    print(f"✗ Age must be between 21 and 60 (you are {age})\n")
    print("LOAN REJECTED")


# ============================================
# SHIPPING COST CALCULATOR
# ============================================

print("\n" + "=" * 50)
print("PROGRAM 3: SHIPPING COST CALCULATOR")
print("=" * 50 + "\n")

weight = 5  # in kg
distance = 150  # in km
is_express = False
is_fragile = True

print(f"Package Weight: {weight} kg")
print(f"Distance: {distance} km")
print(f"Express Delivery: {is_express}")
print(f"Fragile Item: {is_fragile}\n")

# Calculate base cost by weight
if weight <= 1:
    base_cost = 50
elif weight <= 5:
    base_cost = 100
elif weight <= 10:
    base_cost = 200
else:
    base_cost = 300

print(f"Base cost: ${base_cost}")

# Add distance charges
if distance > 100:
    distance_charge = 50
    print(f"Distance charge: ${distance_charge}")
else:
    distance_charge = 0
    print(f"Distance charge: ${distance_charge}")

# Calculate total
total_cost = base_cost + distance_charge

# Add express charges
if is_express:
    express_charge = total_cost * 0.5  # 50% extra
    print(f"Express delivery charge (50%): ${express_charge}")
    total_cost += express_charge

# Add fragile handling charges
if is_fragile:
    fragile_charge = 25
    print(f"Fragile handling charge: ${fragile_charge}")
    total_cost += fragile_charge

print(f"\nTOTAL SHIPPING COST: ${total_cost}")


# ============================================
# STUDENT SCHOLARSHIP PROGRAM
# ============================================

print("\n" + "=" * 50)
print("PROGRAM 4: SCHOLARSHIP ELIGIBILITY")
print("=" * 50 + "\n")

percentage = 92
family_income = 25000
sports_achievement = True
extra_curricular = True

print(f"Percentage: {percentage}%")
print(f"Family Income: ${family_income}")
print(f"Sports Achievement: {sports_achievement}")
print(f"Extra-Curricular Activities: {extra_curricular}\n")

scholarship_amount = 0

# Check academic performance
if percentage >= 90:
    print("✓ Excellent Academic Performance")
    scholarship_amount = 5000
    
    # Check family income
    if family_income < 50000:
        print("✓ Low family income - Additional support")
        scholarship_amount += 3000
    
    # Check sports
    if sports_achievement:
        print("✓ Sports Achievement Bonus")
        scholarship_amount += 2000
    
    # Check extra-curricular
    if extra_curricular:
        print("✓ Extra-Curricular Bonus")
        scholarship_amount += 1000

elif percentage >= 80:
    print("✓ Good Academic Performance")
    scholarship_amount = 3000
    
    if family_income < 50000:
        print("✓ Low family income - Additional support")
        scholarship_amount += 2000

elif percentage >= 70:
    print("✓ Average Academic Performance")
    scholarship_amount = 1000

else:
    print("✗ Does not meet academic requirements")

print(f"\nTOTAL SCHOLARSHIP AMOUNT: ${scholarship_amount}")


# ============================================
# PRACTICE PROBLEMS
# ============================================

print("\n" + "=" * 50)
print("PRACTICE PROBLEMS")
print("=" * 50)

"""
Try these exercises:

1. Create a water bill calculator:
   - First 100 units: $0.50 per unit
   - Next 100 units: $0.75 per unit
   - Above 200 units: $1.00 per unit
   - If bill > $150, add 10% tax
   - If bill > $200, add additional 5% surcharge

2. Write a college admission system that checks:
   - Entrance exam score (must be >= 70)
   - If qualified, check marks:
     * >= 90: Direct admission + $2000 scholarship
     * >= 80: Direct admission + $1000 scholarship
     * >= 70: Admission with interview
   - If not qualified, suggest improvement areas

3. Create a movie ticket booking system:
   - Check age for appropriate content rating
   - Check day (weekday/weekend for different prices)
   - Check showtime (matinee/evening/night)
   - Apply member discount if applicable
   - Calculate final price with all factors

4. Design a temperature alert system:
   - If temp > 35: Heat warning
     * If temp > 40: Severe heat warning
     * If temp > 45: Extreme heat danger
   - If temp < 10: Cold warning
     * If temp < 5: Severe cold warning
     * If temp < 0: Freezing danger
   - Else: Normal temperature

5. Build a restaurant bill calculator:
   - Different tax rates for dine-in (10%) and takeaway (5%)
   - Service charge (10%) only for dine-in
   - If bill > $100, give 10% discount
   - If customer is a member, give additional 5% discount
"""

print("\nTry solving the practice problems above!")
print("Nested conditions help solve complex real-world problems!")
