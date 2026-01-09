# Conditional Statements in Python 🔀

## What are Conditional Statements?

Conditional statements allow your program to make decisions and execute different code based on conditions. They are like "if this happens, then do that" logic.

## Types of Conditional Statements

### 1. **if statement**
Executes code only if the condition is True
```python
if age >= 18:
    print("You are an adult")
```

### 2. **if-else statement**
Executes one block if True, another if False
```python
if age >= 18:
    print("You are an adult")
else:
    print("You are a minor")
```

### 3. **if-elif-else statement**
Tests multiple conditions
```python
if score >= 90:
    print("Grade A")
elif score >= 80:
    print("Grade B")
else:
    print("Grade C")
```

## Comparison Operators

- `==` : Equal to
- `!=` : Not equal to
- `>` : Greater than
- `<` : Less than
- `>=` : Greater than or equal to
- `<=` : Less than or equal to

## Logical Operators

- `and` : Both conditions must be True
- `or` : At least one condition must be True
- `not` : Reverses the condition

## Examples in This Folder

1. **01_basic_if_else.py** - Simple if-else conditions
2. **02_elif_statement.py** - Multiple conditions with elif
3. **03_nested_conditions.py** - Conditions inside conditions
4. **04_logical_operators.py** - Using and, or, not
5. **05_practical_examples.py** - Real-world applications

## Tips for Beginners

- Use proper indentation (4 spaces) - it's required in Python!
- Conditions must evaluate to True or False
- Use `==` for comparison, not `=` (which is for assignment)
- Test your conditions with different values

## Practice

Run each example and try modifying the conditions to see different outcomes!
