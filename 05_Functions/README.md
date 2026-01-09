# Functions in Python 🔧

## What are Functions?

Functions are reusable blocks of code that perform a specific task. They help organize code, avoid repetition, and make programs easier to understand and maintain.

## Why Use Functions?

1. **Code Reusability** - Write once, use many times
2. **Organization** - Break complex problems into smaller parts
3. **Readability** - Make code easier to understand
4. **Maintainability** - Update code in one place

## Function Basics

### Defining a Function
```python
def function_name():
    # code to execute
    print("Hello!")
```

### Calling a Function
```python
function_name()  # Call the function
```

### Parameters and Arguments
```python
def greet(name):        # 'name' is a parameter
    print(f"Hello, {name}!")

greet("Alice")          # "Alice" is an argument
```

### Return Values
```python
def add(a, b):
    return a + b

result = add(5, 3)      # result = 8
```

## Types of Arguments

1. **Positional Arguments** - Order matters
2. **Keyword Arguments** - Named arguments
3. **Default Arguments** - Pre-set values
4. **Variable-length Arguments** - `*args` and `**kwargs`

## Scope

- **Local Variables** - Defined inside function
- **Global Variables** - Defined outside function

## Examples in This Folder

1. **01_basic_functions.py** - Creating and calling functions
2. **02_parameters_arguments.py** - Working with function parameters
3. **03_return_values.py** - Returning values from functions
4. **04_scope.py** - Understanding variable scope
5. **05_practical_examples.py** - Real-world function applications

## Tips for Beginners

- Use descriptive function names (e.g., `calculate_area` not `func1`)
- Functions should do one thing well
- Use docstrings to document your functions
- Return values instead of printing when possible
- Test your functions with different inputs

## Practice

Try creating your own functions and combining them to solve problems!
