# Loops in Python 🔁

## What are Loops?

Loops allow you to repeat a block of code multiple times. Instead of writing the same code again and again, you can use loops to automate repetitive tasks.

## Types of Loops in Python

### 1. **for Loop**
Used when you know how many times you want to repeat something
```python
for i in range(5):
    print(i)
```

### 2. **while Loop**
Used when you want to repeat until a condition becomes False
```python
count = 0
while count < 5:
    print(count)
    count += 1
```

## Loop Control Statements

- **break**: Exit the loop immediately
- **continue**: Skip the current iteration and move to the next
- **pass**: Do nothing (placeholder)

## Common Loop Patterns

### Range Function
```python
range(5)        # 0, 1, 2, 3, 4
range(1, 6)     # 1, 2, 3, 4, 5
range(0, 10, 2) # 0, 2, 4, 6, 8
```

### Looping Through Collections
```python
# List
for item in [1, 2, 3]:
    print(item)

# String
for char in "hello":
    print(char)
```

## Examples in This Folder

1. **01_basic_for_loop.py** - Introduction to for loops
2. **02_range_function.py** - Using range() function
3. **03_while_loop.py** - Understanding while loops
4. **04_nested_loops.py** - Loops inside loops
5. **05_loop_control.py** - break, continue, pass statements
6. **06_practical_examples.py** - Real-world loop applications

## Tips for Beginners

- Use **for loops** when you know the number of iterations
- Use **while loops** when the number of iterations depends on a condition
- Always make sure while loops have a way to end (avoid infinite loops)
- Use meaningful variable names in loops (instead of just `i`)
- Remember proper indentation!

## Practice

Try modifying the loop ranges and conditions to see different outputs!
