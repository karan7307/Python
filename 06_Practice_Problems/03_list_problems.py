"""
List Problems - Practice Exercises
===================================
Try to solve these problems yourself before looking at the solutions!
"""

print("=" * 60)
print("PROBLEM 1: Find Maximum and Minimum")
print("=" * 60)
print("Find the maximum and minimum elements in a list")
print()

# Your code here
# ...

# Solution:
def find_max_min(numbers):
    """Find max and min in list"""
    if not numbers:
        return None, None
    
    maximum = numbers[0]
    minimum = numbers[0]
    
    for num in numbers:
        if num > maximum:
            maximum = num
        if num < minimum:
            minimum = num
    
    return maximum, minimum

# Test
print("Solution:")
test_list = [45, 23, 67, 12, 89, 34]
max_val, min_val = find_max_min(test_list)
print(f"List: {test_list}")
print(f"Maximum: {max_val}, Minimum: {min_val}")

print("\n" + "=" * 60)
print("PROBLEM 2: Sum and Average")
print("=" * 60)
print("Calculate sum and average of numbers in a list")
print()

# Your code here
# ...

# Solution:
def calculate_sum_average(numbers):
    """Calculate sum and average"""
    if not numbers:
        return 0, 0
    
    total = sum(numbers)
    average = total / len(numbers)
    return total, average

# Test
print("Solution:")
test_list = [10, 20, 30, 40, 50]
total, avg = calculate_sum_average(test_list)
print(f"List: {test_list}")
print(f"Sum: {total}, Average: {avg}")

print("\n" + "=" * 60)
print("PROBLEM 3: Remove Duplicates")
print("=" * 60)
print("Remove duplicate elements from a list")
print()

# Your code here
# ...

# Solution:
def remove_duplicates(lst):
    """Remove duplicates preserving order"""
    unique = []
    seen = set()
    
    for item in lst:
        if item not in seen:
            unique.append(item)
            seen.add(item)
    
    return unique

# Test
print("Solution:")
test_list = [1, 2, 2, 3, 4, 4, 5, 1]
print(f"Original: {test_list}")
print(f"Without duplicates: {remove_duplicates(test_list)}")

print("\n" + "=" * 60)
print("PROBLEM 4: Find Second Largest")
print("=" * 60)
print("Find the second largest element in a list")
print()

# Your code here
# ...

# Solution:
def find_second_largest(numbers):
    """Find second largest element"""
    if len(numbers) < 2:
        return None
    
    # Remove duplicates and sort
    unique_numbers = list(set(numbers))
    unique_numbers.sort(reverse=True)
    
    if len(unique_numbers) < 2:
        return None
    
    return unique_numbers[1]

# Test
print("Solution:")
test_list = [45, 23, 67, 89, 34, 67]
print(f"List: {test_list}")
print(f"Second largest: {find_second_largest(test_list)}")

print("\n" + "=" * 60)
print("PROBLEM 5: Count Occurrences")
print("=" * 60)
print("Count how many times each element appears in a list")
print()

# Your code here
# ...

# Solution:
def count_occurrences(lst):
    """Count occurrences of each element"""
    freq = {}
    for item in lst:
        freq[item] = freq.get(item, 0) + 1
    return freq

# Test
print("Solution:")
test_list = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
freq = count_occurrences(test_list)
print(f"List: {test_list}")
print("Frequency:")
for item, count in sorted(freq.items()):
    print(f"  {item}: {count} times")

print("\n" + "=" * 60)
print("PROBLEM 6: Merge Two Sorted Lists")
print("=" * 60)
print("Merge two sorted lists into one sorted list")
print()

# Your code here
# ...

# Solution:
def merge_sorted_lists(list1, list2):
    """Merge two sorted lists"""
    merged = []
    i, j = 0, 0
    
    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            merged.append(list1[i])
            i += 1
        else:
            merged.append(list2[j])
            j += 1
    
    # Add remaining elements
    merged.extend(list1[i:])
    merged.extend(list2[j:])
    
    return merged

# Test
print("Solution:")
list1 = [1, 3, 5, 7]
list2 = [2, 4, 6, 8]
print(f"List 1: {list1}")
print(f"List 2: {list2}")
print(f"Merged: {merge_sorted_lists(list1, list2)}")

print("\n" + "=" * 60)
print("PROBLEM 7: Rotate List")
print("=" * 60)
print("Rotate list to the right by k positions")
print()

# Your code here
# ...

# Solution:
def rotate_list(lst, k):
    """Rotate list by k positions"""
    if not lst:
        return lst
    
    k = k % len(lst)  # Handle k larger than list length
    return lst[-k:] + lst[:-k]

# Test
print("Solution:")
test_list = [1, 2, 3, 4, 5]
for k in [1, 2, 3]:
    rotated = rotate_list(test_list, k)
    print(f"Rotate {test_list} by {k}: {rotated}")

print("\n" + "=" * 60)
print("PROBLEM 8: Find Common Elements")
print("=" * 60)
print("Find elements that appear in both lists")
print()

# Your code here
# ...

# Solution:
def find_common(list1, list2):
    """Find common elements"""
    return list(set(list1) & set(list2))

# Test
print("Solution:")
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]
print(f"List 1: {list1}")
print(f"List 2: {list2}")
print(f"Common elements: {find_common(list1, list2)}")

print("\n" + "=" * 60)
print("PROBLEM 9: Partition Even and Odd")
print("=" * 60)
print("Separate even and odd numbers into two lists")
print()

# Your code here
# ...

# Solution:
def partition_even_odd(numbers):
    """Partition into even and odd lists"""
    even = []
    odd = []
    
    for num in numbers:
        if num % 2 == 0:
            even.append(num)
        else:
            odd.append(num)
    
    return even, odd

# Test
print("Solution:")
test_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even, odd = partition_even_odd(test_list)
print(f"Original: {test_list}")
print(f"Even numbers: {even}")
print(f"Odd numbers: {odd}")

print("\n" + "=" * 60)
print("PROBLEM 10: Flatten Nested List")
print("=" * 60)
print("Convert a nested list into a flat list")
print()

# Your code here
# ...

# Solution:
def flatten_list(nested):
    """Flatten nested list"""
    flat = []
    for item in nested:
        if isinstance(item, list):
            flat.extend(flatten_list(item))  # Recursive call
        else:
            flat.append(item)
    return flat

# Test
print("Solution:")
nested_list = [1, [2, 3], [4, [5, 6]], 7]
print(f"Nested: {nested_list}")
print(f"Flattened: {flatten_list(nested_list)}")

print("\n" + "=" * 60)
print("BONUS: List Comprehension Examples")
print("=" * 60)

# Squares of numbers
numbers = [1, 2, 3, 4, 5]
squares = [x**2 for x in numbers]
print(f"Numbers: {numbers}")
print(f"Squares: {squares}")

# Filter even numbers
even_numbers = [x for x in numbers if x % 2 == 0]
print(f"Even numbers: {even_numbers}")

# Create pairs
pairs = [(x, y) for x in [1, 2] for y in [3, 4]]
print(f"Pairs: {pairs}")

# Convert to uppercase
words = ["hello", "world", "python"]
uppercase = [word.upper() for word in words]
print(f"Original: {words}")
print(f"Uppercase: {uppercase}")
